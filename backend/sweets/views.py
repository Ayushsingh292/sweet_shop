from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Sweet
from .serializers import SweetSerializer
from auth_app.middleware import MongoJWTAuthentication



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sweets_list(request):
    """GET all sweets or POST new sweet"""
    try:
        if request.method == 'GET':
            sweets = Sweet.objects()  
            serializer = SweetSerializer(sweets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = SweetSerializer(data=request.data)
            if serializer.is_valid():
                Sweet(**serializer.validated_data).save()
                return Response({"message": "Sweet added successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_sweet(request):
    data = request.data
    if request.user.role != "admin":
        return Response({"error": "Only admin can add sweets"}, status=403)

    sweet = Sweet(
        name=data.get("name"),
        category=data.get("category"),
        price=float(data.get("price")),
        quantity=int(data.get("quantity"))
    )
    sweet.save()
    return Response({"message": "Sweet added successfully"}, status=201)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_sweets(request):
    name = request.GET.get("name")
    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    query = {}
    if name:
        query["name__icontains"] = name
    if category:
        query["category__icontains"] = category
    if min_price and max_price:
        query["price__gte"] = float(min_price)
        query["price__lte"] = float(max_price)

    sweets = Sweet.objects.filter(**query)
    return Response(SweetSerializer(sweets, many=True).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_sweet(request, id):
    try:
        sweet = Sweet.objects.get(id=id)
        if sweet.quantity <= 0:
            return Response({"detail": "Out of stock"}, status=400)
        sweet.quantity -= 1
        sweet.save()
        return Response({"message": "Sweet purchased successfully"})
    except Sweet.DoesNotExist:
        return Response({"detail": "Sweet not found"}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def restock_sweet(request, id):
    if request.user.role != "admin":
        return Response({"error": "Only admin can restock sweets"}, status=403)

    try:
        sweet = Sweet.objects.get(id=id)
        sweet.quantity += int(request.data.get("amount", 0))
        sweet.save()
        return Response({"message": f"{sweet.name} restocked successfully", "new_quantity": sweet.quantity})
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=404)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_sweet(request, id):
    if request.user.role != "admin":
        return Response({"error": "Only admin can update sweets"}, status=403)
    try:
        sweet = Sweet.objects.get(id=id)
        data = request.data
        sweet.name = data.get("name", sweet.name)
        sweet.category = data.get("category", sweet.category)
        sweet.price = float(data.get("price", sweet.price))
        sweet.quantity = int(data.get("quantity", sweet.quantity))
        sweet.save()
        return Response({"message": "Sweet updated successfully"})
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=404)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_sweet(request, id):
    if request.user.role != "admin":
        return Response({"error": "Only admin can delete sweets"}, status=403)
    try:
        Sweet.objects.get(id=id).delete()
        return Response({"message": "Sweet deleted successfully"})
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=404)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_sweets(request):
    """Search sweets by name/category/price range"""
    try:
        name = request.query_params.get('name', '')
        category = request.query_params.get('category', '')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        sweets = Sweet.objects()

        if name:
            sweets = sweets.filter(name__icontains=name)
        if category:
            sweets = sweets.filter(category__icontains=category)
        if min_price and max_price:
            sweets = sweets.filter(price__gte=float(min_price), price__lte=float(max_price))

        serializer = SweetSerializer(sweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def sweet_detail(request, id):
    """Update or Delete a sweet"""
    try:
        sweet = Sweet.objects.get(id=id)
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SweetSerializer(sweet, data=request.data, partial=True)
        if serializer.is_valid():
            sweet.update(**serializer.validated_data)
            return Response({"message": "Sweet updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role = getattr(request.user, 'role', 'user')
        if role != 'admin':
            return Response({"error": "Only admin can delete sweets"}, status=status.HTTP_403_FORBIDDEN)
        sweet.delete()
        return Response({"message": "Sweet deleted successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_sweet(request, id):
    """Purchase a sweet (decrease quantity by 1)"""
    try:
        sweet = Sweet.objects.get(id=id)
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=status.HTTP_404_NOT_FOUND)

    if sweet.quantity <= 0:
        return Response({"error": "Out of stock"}, status=status.HTTP_400_BAD_REQUEST)

    sweet.update(dec__quantity=1)
    return Response({"message": f"Purchased {sweet.name} successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def restock_sweet(request, id):
    """Restock a sweet (admin only)"""
    try:
        sweet = Sweet.objects.get(id=id)
    except Sweet.DoesNotExist:
        return Response({"error": "Sweet not found"}, status=status.HTTP_404_NOT_FOUND)

    role = getattr(request.user, 'role', 'user')
    if role != 'admin':
        return Response({"error": "Only admin can restock sweets"}, status=status.HTTP_403_FORBIDDEN)

    try:
        quantity = int(request.data.get('quantity', 0))
    except ValueError:
        return Response({"error": "Quantity must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

    if quantity <= 0:
        return Response({"error": "Quantity must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

    sweet.update(inc__quantity=quantity)
    return Response({"message": f"{sweet.name} restocked by {quantity}"}, status=status.HTTP_200_OK)


class SweetSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        name_query = request.GET.get('name', '')
        sweets = Sweet.objects.filter(name__icontains=name_query)
        serializer = SweetSerializer(sweets, many=True)
        return Response(serializer.data)

class SweetUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            sweet = Sweet.objects.get(id=id)
        except Sweet.DoesNotExist:
            return Response({"error": "Sweet not found"}, status=404)

        serializer = SweetSerializer(sweet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sweet updated successfully", "data": serializer.data})
        return Response(serializer.errors, status=400)




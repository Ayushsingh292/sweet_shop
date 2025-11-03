from django.urls import path
from . import views

urlpatterns = [
    path('', views.sweets_list),
    path('add/', views.add_sweet),
    path('search/', views.search_sweets),
    path('<str:id>/purchase/', views.purchase_sweet),
    path('<str:id>/restock/', views.restock_sweet),
    path('<str:id>/', views.update_sweet),
    path('<str:id>/delete/', views.delete_sweet),
    path('<str:id>/update/', views.SweetUpdateView.as_view(), name='update-sweet'),
    
]

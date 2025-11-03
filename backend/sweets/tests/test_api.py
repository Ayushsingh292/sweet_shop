
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class SweetFlowTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')       
        self.login_url = reverse('login')             
        self.sweets_url = reverse('sweet-list')       
        
        self.client.post(self.register_url, {
            "name": "Ayush",
            "email": "ayush@test.com",
            "password": "Ayush123!"
        }, format='json')
        
        res = self.client.post(self.login_url, {
            "email": "ayush@test.com", "password": "Ayush123!"
        }, format='json')
        self.token = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_and_list_sweets(self):
        create = self.client.post(self.sweets_url, {
            "name": "Rasgulla", "category": "Indian", "price": 20, "quantity": 10
        }, format='json')
        self.assertEqual(create.status_code, status.HTTP_201_CREATED)

        get_list = self.client.get(self.sweets_url)
        self.assertEqual(get_list.status_code, status.HTTP_200_OK)
        self.assertTrue(any(s['name'] == 'Rasgulla' for s in get_list.data))

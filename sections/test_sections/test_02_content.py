import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from rest_framework.test import APITestCase
from rest_framework import status

from sections.test_sections.utils import get_admin_user, get_member_user, get_test_section, get_test_content

class ContentTestAdmin(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.content = get_test_content()

    def test_08_content_create(self):
        data = {
            'section': self.content.section.id,
            'title': 'Test Content Title Create',
            'content': 'Test content create',
        }
        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Content Title Create')
        self.assertEqual(response.json().get('content'), 'Test content create')

    def test_09_content_detail(self): 
        response = self.client.get(f'/content/{self.content.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Title Content')
        self.assertEqual(response.json().get('content'), 'Test Content')

    def test_10_content_update(self):
        data = {
            'title': 'Test content title PATCH',
        }
        response = self.client.patch(f'/content/{self.content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test content title PATCH')

    def test_11_content_delete(self):
        response = self.client.delete(f'/content/{self.content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/content/{self.content.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_12_content_list(self): 
        response = self.client.get(f'/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], "Test Title Content")

class ContentTestMember(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.content = get_test_content()

        

if __name__ == '__main__':
    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    failures = TestRunner(verbosity=2).run_tests(['sections.test_sections.test_02_content'])
    sys.exit(bool(failures))


# from rest_framework.test import APITestCase
# from rest_framework import status

# from sections.test_sections.utils import get_admin_user, get_member_user, get_test_section

# class SectionTestsAdmin(APITestCase):
    
#     def setUp(self):
#         self.user = get_admin_user()
#         self.client.force_authenticate(user=self.user)
#         self.test_section = get_test_section()

#     def test_01_section_create(self):
#         data = {
#             'title': 'Test Section Create',
#             'description': 'Test Description Create',
#         }
#         response = self.client.post('/section/create/', data=data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_02_section_detail(self): 
#         response = self.client.get(f'/section/{self.test_section.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json().get('title'), "Test Section")
#         self.assertEqual(response.json().get('description'), "Test Description")

#     def test_03_section_update(self): 
#         data = {
#             'title': 'Test Section Update PUT',
#             'description': 'Test Description Update PUT',
#         }
#         response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json().get('title'), "Test Section Update PUT")
#         self.assertEqual(response.json().get('description'), "Test Description Update PUT")

#     def test_04_section_delete(self): 
#         response = self.client.delete(f'/section/{self.test_section.id}/delete/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         response = self.client.get(f'/sections/{self.test_section.id}/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_05_section_list(self):
#         response = self.client.get(f'/section/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json()['results'][0]['title'], "Test Section")

# class SectionTestMember(APITestCase):
#     def setUp(self): 
#         self.user = get_member_user()
#         self.client.force_authenticate(user=self.user)
#         self.test_section = get_test_section()
    
#     def test_06_section_create_forbidden(self): 
#         data = {
#             'title': 'Test Section Create Forbidden',
#             'description': 'Test Description Create Forbidden',
#         }
#         response = self.client.post('/section/create/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав')

#     def test_07_section_delete_forbidden(self): 
#         response = self.client.delete(f'/section/{self.test_section.id}/delete/')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self. assertEqual(response.json().get('detail'), 'У вас недостаточно прав')

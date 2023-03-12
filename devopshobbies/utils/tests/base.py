from faker import Faker
from django.test import TestCase
from devopshobbies.users.models import BaseUser
from rest_framework.test import APIRequestFactory , APIClient

class UserLoginTestCase(TestCase):
    factory = APIRequestFactory()
    
    # some setup here, explained later

    def test_correct_login(self):
        pass
       
    
    def test_if_password_incorrect_then_cant_login(self):
        pass
        
    
    def test_if_user_not_registered_cant_login(self):
        pass


class UserRegisterTestCase(TestCase):

    factory = APIRequestFactory()

    def test_correct_register(self):
        response = self.factory.post('/api/users/register/', {'ID': '3456765432' , 
            'email':'test@gmail.com',
            'first_name':'abolfazl' ,
            'last_name':'andalib' , 
            'bio':'only god !' , 
            'password':'abolfazl@123456',
            'password_confirm':'abolfazl@123456'} ,  format='json')
        
        
       

    def test_register_with_frequent_ID(self):
        response = self.factory.post('/api/users/register/', {'ID': '1234567890' , 
            'email':'test@gmail.com',
            'first_name':'abolfazl' ,
            'last_name':'andalib' , 
            'bio':'only god !' , 
            'password':'abolfazl@123456',
            'password_confirm':'abolfazl@123456'} ,  format='json')

    def test_register_with_weak_password(self):
        response = self.factory.post('/api/users/register/', {'ID': '1234567890' , 
            'email':'test@gmail.com',
            'first_name':'abolfazl' ,
            'last_name':'andalib' , 
            'bio':'only god !' , 
            'password':'123456',
            'password_confirm':'123456'} ,  format='json')




class AdminRegisterTestCase(TestCase):

    def test_correct_register(self):
        pass

    def test_register_with_frequent_ID(self):
        pass

    def test_register_with_weak_password(self):
        pass

    def test_register_by_non_admin_user(self):
        pass




        

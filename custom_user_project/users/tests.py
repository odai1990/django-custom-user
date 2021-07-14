from django.test import TestCase
from .models import CustomUser
from django.contrib.auth import get_user_model
# Create your tests here.
class movies_crud_test(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'odai',           
            email = 'admin@gmail.com',            
            password = 'odai1990'
        )       
                       
    def test_user_creation(self):
        self.assertEquals(self.user.__str__(),'odai')    

    def test_duplicates(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                username = 'odai',           
                email = 'admin@gmail.com',            
                password = 'odai1990'
            )           
        except:          
            print('Resgistration falied!')

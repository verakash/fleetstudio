from django.test import TestCase

# Create your tests here.


from .models import CustomerUser


class UserTestCase(TestCase):
    def setUp(self):
        CustomerUser.objects.create(email= "akash@gmail.com", password= "Akas#12")
        CustomerUser.objects.create(email= "max@gmail.com", password= "Max#21")

    def test_user_test(self):
        obj1= CustomerUser.objects.get(email= "akash@gmail.com" )
        obj2= CustomerUser.objects.get(email= "max@gmail.com" )
        self.assertEqual(obj1.email,"akash@gmail.com" )
        self.assertEqual(obj2.email, "max@gmail.com" )

from django.test import TestCase
from .models import Profile,Neighbourhood, Business,Post
from django.contrib.auth.models import User
# Create your tests here.





class ProfileTest(TestCase):
    def setUp(self):
        self.peris = User(username = 'Peris',email = 'peris@gmail.com')
        self.peris = Profile(user = Self.peris,user_id = 1,bio = 'my hood', email='test@gmail.com',profile_pic = 'image.jpg',location='Nairobi', neighbourhood='caren')

    def test_instance(self):
        self.assertTrue(isinstance(self.peris,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.peris.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_ neighborhood= Project(name ='caren',location = 'Nairobi',image = 'trial.jpg',description = 'I like your my hood',user = peris,hood_logo= 'logo.jpeg', emergency_contact= '911',occupants_count ='10')


    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.image.save_image()
        all_images = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)



class BusinessTestCase(TestCase):
    self.new_ neighborhood= Project(name = 'shop',user = 'Peris',email = 'test@gmail',neighborhood = 'Meru',descrption='This Hood')


    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.name.save_image()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_name()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_name = Business.get_one_name(self.food.id)
        self.assertTrue(one_name.name == self.name.name)



class PostTestCase(TestCase):
    self.new_ neighborhood= Project(title = 'hood',User = 'Peris',text = 'I like your my hood',,date_craeted='Oct,12.2020')
    def test_save_image(self):
        self.name.save_name()
        name = Business.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.name.save_name()
        self.name.delete_image()
        image_list = Business.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_image()
        all_names = Business.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_name = Business.get_one_name(self.food.id)
        self.assertTrue(one_name.name == self.name.name)

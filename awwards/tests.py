from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.gallery= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gallery,Project))

    # Testing Save Method
    def test_save_method(self):
        self.gallery.save_image()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)

        
       
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.gallery= Rating()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gallery,Rating))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.gallery= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gallery,Profile))

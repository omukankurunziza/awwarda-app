from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.indian= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.indian,Project))

    # Testing Save Method
    def test_save_method(self):
        self.indian.save_image()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.indian= Ratingt()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.indian,Rating))

  
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.DSC_76721.JPG= Image( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.DSC_76721.JPG,Image))

    # Testing Save Method
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs) 

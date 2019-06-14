from django.test import TestCase
from .models import Movie, Genre, Review
from .forms import GenreForm, MovieForm
import datetime
# Create your tests here.

class GenreTest(TestCase):
   def test_string(self):
       type=Genre(genre="SF")
       self.assertEqual(str(type), type.genre)

   def test_table(self):
       self.assertEqual(str(Genre._meta.db_table), 'genre')

class MovieTest(TestCase):
   #set up one time sample data
   def setup(self):
       genre = Genre(genre='Drama')
       movie=Movie(movietitle='movie1', movieduration='.99', moviedescription='drama')
       return movie

   def test_string(self):
       movi = self.setup()
       self.assertEqual(str(movi), movi.movietitle)
  
   #test the discount property
   def test_duration(self):
       movi=self.setup()
       self.assertEqual(movi.movieduration, '.99')

   def test_description(self):
       movi=self.setup()
       self.assertEqual(movi.moviedescription, 'drama')

   def test_table(self):
       self.assertEqual(str(Movie._meta.db_table), 'movie')

class Genre_Form_Test(TestCase):
    def test_genreform_is_valid(self):
        form=GenreForm(data={'genre': "Action", 'genredescription' : "fight"})
        self.assertTrue(form.is_valid())

class MovieFormTest(TestCase):
   def setUp(self):
      self.moviereleaseDate = datetime.date.today()

   def test_movieForm(self):
      data={
         'movieTitle' : 'testMeeting',
         'moviereleasedate' : self.moviereleaseDate,
         'movieduration' : '.99',
         'moviedescription' : 'Drama',
         
      }
      form = MovieForm(data=data)
      self.assertTrue(form.is_valid)
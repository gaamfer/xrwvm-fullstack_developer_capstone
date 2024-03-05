from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):

	COUNTRY_CHOICES = [
	('US', 'United States'),
	('UK','United KIngdom'),
	('DE', 'Germany'),
	('FR', 'France'),
	('ES', 'Spain'),
	('SWE', 'Sweden'),
	('CHN', 'China'),
	('JPN','Japan'),
	('KRN', 'South-Korea'),
	('IT','Italy'),
	]

	name = models.CharField(max_length=100)
	description = models.TextField()
	madeIncountry = models.CharField(max_length=3, choices=COUNTRY_CHOICES)

	def __str__(self):
		return self.name # Return the name as the string representation

class CarModel(models.Model): 
	
	TYPE_CHOICES = [
	('SEDAN','Sedan'),
	('SUV', 'SubUrban Vehicle'),
	('CABRIO', 'Cabriolet'),
	('SW', 'Station Wagon'),
	('COUPE', 'coupe'),
	('LIMO', 'Limousine'),
	]

	make = models.ForeignKey(CarMake, on_delete=models.CASCADE) #Many-to-one relationship
	dealerId = models.IntegerField()
	name = models.CharField(max_length=150)
	type = models.CharField(max_length=6, choices=TYPE_CHOICES)
	year = models.IntegerField(default=2024,
		validators=[
			MaxValueValidator(2024),
			MinValueValidator(1980)
		])

	def __srt__(self):
		return self.make, self.name

from django.db import models
from typing import List



# Create your models here.
class Root(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)  

    def __init__(self, i, name, url):
        self.id = i
        self.name = str(name)
        self.url = str(url)
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.url}"

class People(models.Model):
    name : str # The name of this person.
    birth_year : str # The birth year of the person, using the in-universe standard of BBY or ABY - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: str A New Hope.
    eye_color : str # The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
    gender : str # The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
    hair_color : str # The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
    height : str # The height of the person in centimeters.
    mass : str # The mass of the person in kilograms.
    skin_color : str # The skin color of this person.
    homeworld : str # The URL of a planet resource, a planet that this person was born on or inhabits.
    url : str # the hypermedia URL of this resource.
    created : str # the ISO 8601 date format of the time that this resource was created.
    edited : str # the ISO 8601 date format of the time that this resource was edited.

    films : List[str] # An array of film resource URLs that this person has been in.
    species : List[str] # An array of species resource URLs that this person belongs to.
    starships : List[str] # An array of starship resource URLs that this person has piloted.
    vehicles : List[str] # An array of vehicle resource URLs that this person has piloted.

    def __init__(self):
        self.name = name
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.gender = gender
        self.hair_color = hair_color
        self.height = height
        self. mass = mass
        self.skin_color = skin_color
        self.homeworld = homeworld
        self.url = url
        self.created = created
        self.edited = edited
    
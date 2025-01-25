from math import pi;
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

ramdom_planets = ch(planets)
radius = 0

if ramdom_planets == "Mercury":
    radius = 2440
elif ramdom_planets == "Venus":
    radius = 6052
elif ramdom_planets == "Earth":
    radius == 6371
elif ramdom_planets == "Mars":
    radius == 3390
else:
    print("Oops! Ocorreu um erro no console")

planet_area = 4 * pi * radius * radius

print(f"A area do {ramdom_planets}: {planet_area} ")







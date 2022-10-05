from random import *

a = randint(1,6)

x = int(input("name number between 1-6:"))

if a == x:
  print ("correct")
else: 
  print ("incorrect")
  print ("correct answer = ")
  print (a)
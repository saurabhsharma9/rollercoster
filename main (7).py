print("welcome to the rollercoster ride!")
height = int(input("What is your height in cm? "))
if height>=120:
  print("Yoy can ride rollercaster")
  age = int(input("What is your age?"))
  if(age<10):
    print("You have to pay $5")
  elif(age<=15):
   print("you have to pay $7")
  elif(age<=18):
   print("you have to pay $9") 
  else:
   print("you have to pay $12")
else:
 print("you can't ride rollercoster")

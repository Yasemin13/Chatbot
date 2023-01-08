import random
print("Welcome to the bank how may we help you today? ")
while True:
  print("\n\nTo check your account balance type 1")
  print("To transfer fundings type 2")
  print("To ask about additional services type 3")
  a= int(input(""))
  if a == 1:
    b= int(input("Alright, to check your account balance insert account number."))
    c= (input("Enter account pin for " + str(b) + "  "))
    d= random.randint(0, 1000000)
    print("Ÿour account balance is currently " + str(d/100))
  
  
  
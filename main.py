import random
print("Welcome to the bank how may we help you today? ")
#This chatbot is a bussness chatbot, its purpose is to help bank customers. They can check their balance, transfer funds, and ask some questions on a few things using this bot.

while True:
#This makes the user able to go back and go through a different area
  print("\n\nTo check your account balance type 1")
  print("To transfer fundings type 2")
  print("To ask about additional services type 3")
  a= int(input(""))
  if a == 1:
#When you choose option 1 you put in your account number and pin (you can put whaterver numbers you want)
#It will generate a random amout of money for you account and that will stay your amount unless you transfer from other accounts
    b= int(input("Alright, to check your account balance insert account number."))
    c= (input("Enter account pin for " + str(b) + "  "))
    d= random.randint(0, 1000000)
    print("Ÿour account balance is currently " + str(d/100))

  if a == 2:
    
    
  
  
  
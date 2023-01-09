import random
print("Welcome to the bank how may we help you today? ")
#This chatbot is a bussness chatbot, its purpose is to help bank customers. They can check their balance, transfer funds, and ask some questions on a few things using this bot.

while True:
#This makes the user able to go back and go through a different area
  print("\n\nTo check your account balance type 1")
  print("To transfer fundings type 2")
  print("To ask about additional services type 3")
  a= (input(""))

  while (a.isnumeric() != True):
    print("Please enter 1,2, or 3")
    print("\n\nTo check your account balance type 1")
    print("To transfer fundings type 2")
    print("To ask about additional services type 3")
    a= (input(""))



    

  a= int(a)
  if a == 1:
  #When you choose option 1 you put in your account number and pin   (you can put whaterver numbers you want)
  #It will generate a random amout of money for you account and that will stay your amount unless you transfer from other accounts
    b= (input("Alright, to check your account balance insert account number."))
    while (b.isnumeric() != True or len(b) != 7):
      b= (input("Please enter 7 digit account number"))

    c= (input("Enter account pin for " + str(b) + "  "))
    while (c.isnumeric() != True or len(c) != 4):
      c= (input("Please enter 4 digit account pin"))
    
    d= random.randint(0, 1000000)
    print("Your account balance is currently $" + str(d/100))


    

  elif a == 2:
#If you choose 2 you are asked a account number, an amount, and another account number to transfer the funds to. after this finishes it takes you back. 
    e= int(input("What is the account number you want to transfer money from? "))
          
    f= int(input("How much money would you like to transfer?"))
      
    g= int(input("What is the account number you want to transfer the $"+ str(f) +" to? "))
    print("$" + str(f) + " from " + str(e) + " has been transfered to " + str(g))




  
  elif a == 3:
#if you choose 3 it gives you a few things you can ask about and tells you a little information on them. After they give you a number to call to get more information.
    print("\nWhat are you curious about? ")
    print("If you would like to learn about how to open a checking account, enter 1 ")
    print("If you would like to learn about how to open a savings account, enter 2 ")
    print("If you would like to learn about how to open a credit deposit account, enter 3 ")
    print("To apply for a credit card, enter 4 ")
    print("To find a branch near you, enter 5")
    print("If you have any other questions, enter 6, and we will get you in contacts with a real person")
    h= int(input(""))
    if h == 1:
      print("We have 2 apptions of checking accounts.")
      print("Basic: $10 a month and addtional fees for services.")
      print("Advanced: $20 a month and free services")
      print("for more information or to sigh up call 810-555-5555")
    elif h == 2:
      print("Visit our website for currect the intrest rates we offer at www.randombank/savingaccount.com")
    elif h == 3:
      print("We offer 6 month 12 month 24 month and 60 month certificates all require a $1000 minumun balance. For current rates visit www.randombank/CD.com")
    elif h == 4:
      print("We have veriouse credit card for many needs, please visit www.randombank/creditcard.com")
    elif h == 5:
      i= int(input("Please enter your zip code so we can find a bank nearest to you"))
      
      j=(len(str(i)))
      if j != 5:
        print("A zip code must be 5 digits")
        i= int(input("Please enter your zip code so we can find a bank nearest to you"))
      print("The nearest bank to you based off of you zip code is 123 Main St " + str(i))
    else:
      print("Please contact 810-555-5555 for more information or visit www.randombank.com ")
  else:
    print("-please enter 1,2, or 3")
    print("\n\nTo check your account balance type 1")
    print("To transfer fundings type 2")
    print("To ask about additional services type 3")
    a= int(input("")) 
    

  
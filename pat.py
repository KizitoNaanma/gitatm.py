import pyfiglet
#design

print(pyfiglet.figlet_format("Welcome to Patty Bank"))

chances = 0
balance = 100.64
pin = int(input("please enter your four digit pin: "))

                                
                                
while chances < 3:
  if pin == 1234:
    break
  else:
    print("Wrong, Try Again!!")
    pin = int(input("please enter your four digit pin: "))
  chances = chances + 1
  
if chances == 3:
  print("Your card has been blocked")
  exit()


while True:
  option = int(input("what would you like to choose: \n 1 - Balance \t 2 - Withdraw \n\n 3 - Pay \t 4 - Transfer \n\n 5 - return card\n\n >>"))
  if option == 1:
    print (f"your balance is {balance}\n")
    restart = input("would you like to continue? ")

    if restart in ["n", "NO", "no", "N"]:
      print("Thank you for banking with us")

      break

    else:
      pass



  elif option == 2:
    withdrawal_option = float(input("How much do you want to withdraw? \n 1 - N10 \t 2 - N20 \n 3 - N50 \t 4 - N100 \n 5 - Other\n"))

    if withdrawal_option == 1:
      if balance > 10:
        balance -= 10
      else:
        print("Sorry you dont have sufficient fund to withdraw!")

    elif withdrawal_option == 2:
      if balance > 20:
        balance -= 20
      else:
        print("Sorry you dont have sufficient fund to withdraw!")

    elif withdrawal_option == 3:
      if balance > 50:
        balance -= 50
      else:
        print("Sorry you dont have sufficient fund to withdraw!")

    elif withdrawal_option == 4:
      if balance > 100:
        balance -= 100
      else:
        print("Sorry you dont have sufficient fund to withdraw!")

    elif withdrawal_option == 5:
      other_amount = int(input("How much do you want to withdraw? "))
      if balance > other_amount:
        balance -= other_amount
      else:
        print("Sorry you dont have sufficient fund to withdraw!")

    else:
      print("Option not valid!")

    print(f"Your balance is now N{balance}")

    restart = input("Would you like to continue? (y/n) ")
    if restart in ["n", "NO", "no", "N"]:
      print("Thank you for banking with us")
      break
    else:
      pass

  elif option == 3:
    pay_in = float(input("How much do you want to deposit? \n >>> "))
    balance += pay_in
    print("Successful!")

    restart = input("Would you like to continue? (y/n) ")
    if restart in ["n", "NO", "no", "N"]:
      print("Thank you for banking with us")
      break
    else:
      pass

  elif option == 4:
    transfer_account = input("Enter account number to transfer to \n >>>")
    transfer_amount = float(input("How much do you want to transfer? \n >>>"))

    if transfer_amount < balance:
      confirmation = input(f"Are you sure you want to transfer to {transfer_account} (y/n)")
      if confirmation == "y":
        balance -= transfer_amount
        print("Successful!")
      elif confirmation == "n":
        pass
      else:
        print("Invalid option")
        confirmation = input(f"Are you sure you want to transfer to {transfer_account} (y/n)")
    else:
      print("Sorry transfer wasn't Successful. Invalid funds")

    restart = input("Would you like to continue? (y/n) ")
    if restart in ["n", "NO", "no", "N"]:
      print("Thank you for banking with us")
      break
    else:
      pass

  elif option == 5:
    print("Thank you for banking with us")

    exit()

  else:
    print("Invalid option!")











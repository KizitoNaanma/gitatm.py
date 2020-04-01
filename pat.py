print("welcome to access bank")
restart=("Y")
chances = 3
balance = 100.64
while chances >=0:
    pin = int(input("please enter your four digit pin: "))
    if pin == (1234):
        print("pin accepted\n")
        while restart not in("n", "NO", "no", "N"):
            print("please press 1 for your balance\n")
            print("press 2 to make your withdrawal\n")
            print("press 3 to pay\n")
            print("press 4 to return card\n")
            option = int(input("what would you like to choose"))
            if option == 1:
                print (f"your balance is {balance}\n")
                restart = input("would you like to continue?")
                if restart in("n", "NO", "no", "N"):
                    print("thank you")
                    break
                elif option == 2:
                    option2 = ("Y")
                    withdrawal = float(input("how much would you like to withdraw?"))
                    if withdrawal in [10, 20, 40, 60, 80, 100]:
                        balance = balance - withdrawal
                        print("\nyour balance is now #", balance)
                        restart = input("would you like to continue?")
                        if restart in ("n", "NO", "no", "N"):
                            print("thank you")
                            break
                        elif withdrawal != [10, 20, 40, 60, 80, 100]:
                            print("invalid amount please retry\n")
                            restart = ("Y")
                            elif withdrawal == 1:
                                withdrawal = float(input("please enter desired amount: "))
                         elif option == 3:
                             pay_in = float(input("how much would you like to withdraw?"))
                             balance = balance + pay_in
                             print("\n your balance is now #", balance)
                             restart = input("would you like to go back?")
                             if restart in("n", "NO", "no", "N"):
                                 print("thank you")
                                 break
                          elif option == 4:
                              print("please wait while your card is been returned.....\n")
                              print("thank you for your service!")
                              break
                            else:
                                print("please enter a correct number. \n")
                                restart = ("Y")
        

              elif pin != (1234):
                  print("incorrect password")
                  chances = chances - 1
                  if chances == 0:
                      print("\n no more tries")
                      break
                                
                                













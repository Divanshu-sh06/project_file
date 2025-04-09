print("\t\t\t\tWELCOME TO OUR PVR\t\t\t\t")
while True:
    print("\t\t\t\t\t********----AVAILABE MOVIES----********")
    print("1. PUSHPA 2:THE RULE")
    print("2. BHOOL BHULAIYAA 3:")
    print("3. SINGHAM AGAIN:")
    print("4. VENOM:THE LAST DANCE")
    print("5. MOANA 2:")
    print("6. EXIT")
    
    mv = int(input("ENTER THE MOVIES YOU WANT TO WATCH"))
    if mv==6:
        print("THANKU VIST AGAIN")
        break
    elif mv not in [1,2,3,4,5]:
        print("INVAILD MOVIE")

    

def book():
    global totalbill ,ticketfare
    print("\nWHICH SEAT DO YOU PREFER")
    print("1. GOLD ----₹650/-")
    print("2. BALCONY ----₹780/-")
    print("3. LUXURY ----₹1235/-")
    print("4. ECONOMY ----₹260/-")
    
    seat = int(input("ENTER THE SEAT YOU WANT TO BOOK:"))
    s = int(input("HOW MANY SEAT YOU WANT TO BOOK"))
    if seat==1:
        ticketfare = 650*s
    elif seat==2:
        ticketfare = 780*s
    elif seat==3:
        ticketfare = 1235*s
    elif seat==4:
        ticketfare = 260*s
    else:
        print("INVALID SEAT CHOICE")
        return book()
    
    totalbill = ticketfare   

    wf = input("DO YOU WANT SOME NEED FOOD(YES/NO)")
    if wf=="yes":
        food()
    else:
        total()

def food():
    global totalbill,foodtotal
    while True:
        print("\n\n\t\t\t\t\t\t********** MENU **********")
        print("1. MARGHERITA PIZZA ₹470/-")
        print("2. POPCORN          ₹370/-")
        print("3. PATTIES          ₹100/-")
        print("4. PIZZA + PEPSI    ₹550/-")
        print("5. POPCORN + PEPSI  ₹385/-")
        print("6. WE DONT WANT SOME FOOD!")
        choice = int(input("ENTER THE FOOD NO. YOU WANT TO ORDER: "))
        if choice==6:
            break
        elif choice not in [1,2,3,4,5]:
            print("INVALID FOOD OREDR")
            food()
        else:
            x = int(input("HOW MANY MEALS YOU WANT TO ORDER: "))
        
            if choice == 1:
                foodtotal += 470 * x
            elif choice == 2:
                foodtotal += 370 * x
            elif choice == 3:
                foodtotal += 100 * x
            elif choice == 4:
                foodtotal += 550 * x
            elif choice == 5:
                foodtotal += 385 * x
        
            totalbill += foodtotal  # Add food cost to total bill
            a=input("You want reorder:(yes/no)")
            if a=="no":
                break

    return total()  # Return after updating food total

totalbill = 0
foodtotal = 0
ticketfare = 0 

from colorama import Fore,Back,Style

def total():
    name = input("ENTER YOUR NAME: ")
    print("\n\n\t\t\t\t\t\t-------- BILL ---------")
    print(Fore.LIGHTBLUE_EX + Back.MAGENTA + Style.DIM + "GST-18%")
    print(f"BILL NAMED BY {name}")
    print(f"TICKET TOTAL AMOUNT IS ₹{ticketfare}/-")
    print(f"FOOD TOTAL AMOUNT IS ₹{foodtotal}/-")
    ticketf=ticketfare*0.18
    print(f"TICKET AMOUNT AFTER GST IS {ticketf}")
    #print("TICKET AMOUNT IS AFTER GST:",ticketf+ticketfare)
    foodt = foodtotal*0.05
    print("FOOD TOTAL AMOUNT IS AFTER GST:{foodt}")
    total_amount = ticketf+ticketfare+ foodt+foodtotal
    print(f"TOTAL AMOUNT YOU HAVE TO PAY ₹{total_amount}/-")
    
 


    






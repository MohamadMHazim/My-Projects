import random
from tkinter import *
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t =============================================")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Welcome to our Restaurant Management System")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t =============================================")
print("VIP Lounge:\n===========\n- VIP Waiter in service.\n- Famous and classic musicians every Saturdays.\n- More comfortable and bigger rooms (with special view).\n- Special gaming lounge.")
print("Normal Lounge:\n==============\n- Affordable prices that suit all levels.\n\n\n")
price = 0
def gaming_lounge():
    import tkinter as t
    r = t.Tk()
    r.title('Gaming lounge Register Page')
    Label(r, text='First Name').grid(row=0)
    Label(r, text='Last Name').grid(row=1)
    Label(r, text='enter account username').grid(row=2)
    Label(r, text='enter account password').grid(row=3)
    e1 = Entry(r)
    e2 = Entry(r)
    e3 = Entry(r)
    e4 = Entry(r)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    r.geometry("200x100")
    button2 = t.Button(r, text='Register', width=80, command=r.destroy)
    button2.grid()
    r.mainloop()
    print("Welcome to our Mini-Gaming Lounge , we have two types of computers choose what is the best for you and have a good time.")
    print("PCS =>")
    GamingLounge=[]
    file=open("GamingLounge.txt","r")
    for i in file:
        high,end = i.split("|",6)
        GamingLounge1=[high,end]
        GamingLounge += GamingLounge1
    file.close()
    print(GamingLounge[0],GamingLounge[1],end="\n")
    print("Prices:")
    PRLCE = []
    file=open("PRICES.txt","r")
    for j in file:
        high,end=j.split("|",2)
        PRLCE1=[high,end]
        PRLCE += PRLCE1
    file.close()
    print(PRLCE[0],PRLCE[1])
    print("Bundles:")
    BUNDLES = []
    file=open("BUNDLES.txt","r")
    for z in file:
        high,end=z.split("|",2)
        BUNDLES1=[high,end]
        BUNDLES += BUNDLES1
    file.close()
    print(BUNDLES[0],BUNDLES1[1])
    pc_price = 0
    game_ans = int(input())
    if (game_ans) == 1:
        top_pc=int(input("Choose if you want our bundle(type 1) or recharge normally (type 2)"))
        if top_pc == 1:
            pc_price += 45
            print("The total cost is: ", pc_price,"$")
        elif top_pc == 2:
            hours = int(input("How many hours do you want to recharge?"))
            pc_price = 20 * hours
            print("The total cost is: ", pc_price,"$")
        else:
            print("Invalid Input")
            print("Choose if you want our bundle(type 1) or recharge normally (type 2).")
            game_ans = int(input())
            gaming_lounge()
    elif game_ans ==2:
        nor_pc = int(input("Choose if you want our bundle(type 1) or recharge normally (type 2)."))
        if nor_pc == 1:
            pc_price += 22
            print("The total cost is : ", pc_price, "$")
        elif nor_pc == 2:
            hours = int(input("How many hours do you want to recharge?"))
            pc_price += 10 * hours
            print("The total cost is: ", pc_price, "$")
        else:
            print("Invalid input , please try again.")
            gaming_lounge()
    elif game_ans == -1:
        exit()
    else:
        print("Invalid Input , please try again.")
        gaming_lounge()


def normal_rest():
    tot_price = 0
    print("Welcome to normal restaurant !")
    Normal_Menu1 = {"Fries": 5, "Baba Ghannouj": 4, "Hummus": 4, "Tabboule": 6, "Sambousek": 3, "Fatteh": 6,
                    "Mankoush": 2, "Kaak": 2, "Croissants": 5}
    a = 1
    print("Appetizers:")
    for items, price in Normal_Menu1.items():
        print("%d-" % (a), items, "=>", price, "$")
        a += 1
    print("\n")
    Normal_Menu2 = {"Water": 1.5, "Soft Drinks": 5, "Beer": 10, "Orange Juice": 5, "Apple Juice": 5, "Ice Tea": 6,
                    "Energy Drinks": 10, "Cofee": 4, "Milk Shake": 8, "Smoothy": 10}
    b = 1
    print("Drinks:")
    for items, price in Normal_Menu2.items():
        print("%d-" % (b), items, "=>", price, "$")
        b += 1
    print("\n")
    c = 1
    print("Main Plates:")
    Normal_Menu3 = {"Kebbeh": 15, "Masheweh": 30, "Fish": 35, "Farrouj": 25, "Sausages": 15, "Shawarma": 20,
                    "Fahita": 25, "Hamburger (with fries & coke)": 25, "Chickenburger (with fries & coke)": 25}
    for items, price in Normal_Menu3.items():
        print("%d-" % (c), items, "=>", price, "$")
        c += 1
    print("\n")
    nor_app = int(input(("Do you want to order some appetizers? type 0 for yes or type -1 for no (-1 to exit): ")))
    while nor_app != -1:
        if nor_app == 0:
            print("Choose your order")
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        if nor_app == 1:
            print("Successfully Added")
            tot_price += 5
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 2:
            print("Successfully Added")
            tot_price += 4
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 3:
            print("Successfully Added")
            tot_price += 4
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 4:
            print("Successfully Added")
            tot_price += 6
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 5:
            print("Successfully Added")
            tot_price += 3
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 6:
            print("Successfully Added")
            tot_price += 6
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 7:
            print("Successfully Added")
            tot_price += 2
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 8:
            print("Successfully Added")
            tot_price += 2
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app == 9:
            print("Successfully Added")
            tot_price += 5
            nor_app = int(input(("Choose your order (-1 to exit): ")))
        else:
            print("Invalid Input")
            nor_app = int(input(("Choose your order (-1 to exit): ")))
    print("The total price of your order till now is: ", tot_price, "$\n\n")

    nor_app_1 = int(input(("Do you want any drinks ? if yes type 0 & if no type -1")))
    while nor_app_1 != -1:
        if nor_app_1 == 0:
            print("Choose your order")
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        if nor_app_1 == 1:
            print("Successfully Added")
            tot_price += 1.5
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 2:
            print("Successfully Added")
            tot_price += 5
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 3:
            print("Successfully Added")
            tot_price += 10
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 4:
            print("Successfully Added")
            tot_price += 5
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 5:
            print("Successfully Added")
            tot_price += 5
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 6:
            print("Successfully Added")
            tot_price += 6
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 7:
            print("Successfully Added")
            tot_price += 10
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 8:
            print("Successfully Added")
            tot_price += 4
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 9:
            print("Successfully Added")
            tot_price += 8
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        elif nor_app_1 == 10:
            print("Successfully Added")
            tot_price += 10
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
        else:
            print("Invalid Input")
            nor_app_1 = int(input(("Choose your order (-1 to exit): ")))
    print("The total price of your order till now is: ", tot_price, "$\n\n")
    nor_app_2 = int(input("Do you want any main plats ? if yes type 0 & if no type -1."))
    while nor_app_2 != -1:
        if nor_app_2 == 0:
            nor_app_2 = int(input("Choose your order (-1 to exit): "))
            if nor_app_2 == 1:
                print("Succesfully Added")
                tot_price += 15
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 2:
                print("Succesfully Added")
                tot_price += 30
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 3:
                print("Succesfully Added")
                tot_price += 35
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 4:
                print("Succesfully Added")
                tot_price += 25
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 5:
                print("Succesfully Added")
                tot_price += 15
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 6:
                print("Succesfully Added")
                tot_price += 20
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 7:
                print("Succesfully Added")
                tot_price += 25
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 8:
                print("Succesfully Added")
                tot_price += 25
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            elif nor_app_2 == 9:
                print("Succesfully Added")
                tot_price += 25
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
            else:
                print("Invalid Input , please try again.")
                nor_app_2 = int(input(("Choose your order (-1 to exit): ")))
        print("The total price of your order till now is: ", tot_price, "$\n\n")
        print("Do you want to order more? if yes type 1 and if no type 2")
        nor_app = int(input())
        if nor_app ==1 :
            normal_rest()
        elif nor_app ==2:
            if (tot_price <= 20):
                print("Thank you ! Your order will take 10 minutes ... Please be patient and have a good time")
                exit()
            elif 20<tot_price<=40:
                print("Thank you ! Your order will take 22 minutes ... Please be patient and have a good time")
                exit()
            elif 40<tot_price<60:
                print("Thank you ! Your order will take 35 minutes ... Please be patient and have a good time")
                exit()
            elif tot_price>60:
                print("Thank you ! Your order will take up to 40 minutes ... Please be patient and have a good time")
                exit()
            else:
                print("Invalid Input , please try again ...")
                nor_app = int(input())



ans=int(input("Please choose your option: Type 1 for VIP Lounge & Type 2 for Normal Lounge(enter -1 to exit): "))
while ans != -1:
    if ans == 1:
        print("Welcome to our VIP Lounge , i hope you will have a great time.")
    elif ans == 2:
        print("Welcome to our Normal Lounge , i hope you will have a great time.")
    else:
        print("Invalid Input, please try again.")
        ans = int(input("Please choose your option: Type 1 for VIP Lounge & Type 2 for Normal Lounge(enter -1 to exit): "))
    if ans == 1 :
        print("1- Menu =>\n2- Vote for the Musician you want them to attend this week =>\n3- Go the gaming lounge =>\n")
        ans1=int(input())
        if ans1==1:
            print("What cuisine do you want to eat?\n1- Lebanese\n2- American.\n3- Italian\n4- French")
            ans2 = int(input())
            if ans2==1:
                lebanese=["1) Fattouch => 5$ ","2) Tabboule => 5$","3) Hummos => 4$","4) Kebbeh => 15$","5) Falafel => 7$","6) Masheweh => 35$","7) Sambousek => 6$"]
                for i in lebanese:
                    print(i)
                print("Type your orders by entering the number of the food(enter -1 to exit): ")
                answ=int(input())
                while answ != -1:
                    if answ == 1:
                        print("Type the amount of plates you want: ")
                        i = int(input())
                        price += 5 * i
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 2:
                        print("Type the amount of plates you want: ")
                        i1 = int(input())
                        price += 5 * i1
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 3:
                        print("Type the amount of plates you want: ")
                        i2 = int(input())
                        price += 4 * i2
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 4:
                        print("Type the amount of plates you want: ")
                        i3 = int(input())
                        price += 15 * i3
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 5:
                        print("Type the amount of plates you want: ")
                        i4 = int(input())
                        price += 7 * i4
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 6:
                        print("Type the amount of plates you want: ")
                        i5 = int(input())
                        price += 35 * i5
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    elif answ == 7:
                        print("Type the amount of plates you want: ")
                        i6 = int(input())
                        price += 6 * i6
                        print("Type your orders by entering the number of the food: ")
                        answ = int(input())
                    else:
                        print("Invalid Input. Please try again: ")
                        answ = int(input())
                print("The total cost of your order is: ", price , "$")
                print("Your order will be delivered within minutes , feel free to navigate through the Lounge.")
            elif ans2==2:
                American = ["1) Burger => 7$ ", "2) Hot Dogs => 8$", "3) french fries => 4$", "4) Bagels => 3$","5) apple pie => 7$", "6) chicken strips => 12$", "7) ice cream => 6$"]
                for i in American:
                    print(i)
                print("Type your orders by entering the number of the food(enter -1 to exit): ")
                answ1 = int(input())
                while (answ1 != -1):
                    if answ1 == 1:
                        print("Type the amount of plates you want: ")
                        p0 = int(input())
                        price += 7 * p0
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 2:
                        print("Type the amount of plates you want: ")
                        p1 = int(input())
                        price += 8 * p1
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 3:
                        print("Type the amount of plates you want: ")
                        p2 = int(input())
                        price += 4 * p2
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 4:
                        print("Type the amount of plates you want: ")
                        p3 = int(input())
                        price += 3 * p3
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 5:
                        print("Type the amount of plates you want: ")
                        p4 = int(input())
                        price += 12 * p4
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 6:
                        print("Type the amount of plates you want: ")
                        p5 = int(input())
                        price += 12 * p5
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    elif answ1 == 7:
                        print("Type the amount of plates you want: ")
                        p6 = int(input())
                        price += 6 * p6
                        print("Type your orders by entering the number of the food: ")
                        answ1 = int(input())
                    else:
                        print("Invalid Input. Please try again: ")
                        answ1 = int(input())
                print("The total cost of your order is: ", price, "$")
                print("Your order will be delivered within minutes , feel free to navigate through the Lounge.")

            elif ans2==3:
                Italian = ["1) Pizza => 10$ ", "2) Pasta => 12$", "3) Lasagna => 14$", "4) Tortellini => 13$","5) Cappuchino => 7$", "6) chickenella => 22$", "7) Hot chocolate => 6$"]
                for i in Italian:
                    print(i)
                print("Type your orders by entering the number of the food(enter -1 to exit): ")
                answ2 = int(input())
                while (answ2 != -1):
                    if answ2 == 1:
                        print("Type the amount of plates you want: ")
                        o0 = int(input())
                        price += 10 * o0
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 2:
                        print("Type the amount of plates you want: ")
                        o1 = int(input())
                        price += 12 * o1
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 3:
                        print("Type the amount of plates you want: ")
                        o2 = int(input())
                        price += 14 * o2
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 4:
                        print("Type the amount of plates you want: ")
                        o3 = int(input())
                        price += 13 * o3
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 5:
                        print("Type the amount of plates you want: ")
                        o4 = int(input())
                        price += 22 * o4
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 6:
                        print("Type the amount of plates you want: ")
                        o5 = int(input())
                        price += 7 * o5
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    elif answ2 == 7:
                        print("Type the amount of plates you want: ")
                        o6 = int(input())
                        price += 6 * o6
                        print("Type your orders by entering the number of the food: ")
                        answ2 = int(input())
                    else:
                        print("Invalid Input. Please try again: ")
                        answ2 = int(input())

                print("The total cost of your order is: ", price, "$")
                print("Your order will be delivered within minutes , feel free to navigate through the Lounge.")
            elif ans2==4:
                French = ["1) Croisants => 5$ ", "2) Macarons => 4$", "3) Frites => 6$", "4) café au lait => 3$","5) la dinde => 27$", "6) viande grillé => 32$", "7) le Poulet => 16$"]
                for i in French:
                    print(i)
                print("Type your orders by entering the number of the food(enter -1 to exit): ")
                answ3 = int(input())
                while (answ3 != -1):
                    if answ3 == 1:
                        print("Type the amount of plates you want: ")
                        z0 = int(input())
                        price += 5 * z0
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 2:
                        print("Type the amount of plates you want: ")
                        z1 = int(input())
                        price += 4 * z1
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 3:
                        print("Type the amount of plates you want: ")
                        z2 = int(input())
                        price += 6 * z2
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 4:
                        print("Type the amount of plates you want: ")
                        z3 = int(input())
                        price += 3 * z3
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 5:
                        print("Type the amount of plates you want: ")
                        z4 = int(input())
                        price += 27 * z4
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 6:
                        print("Type the amount of plates you want: ")
                        z5 = int(input())
                        price += 32 * z5
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    elif answ3 == 7:
                        print("Type the amount of plates you want: ")
                        z6 = int(input())
                        price += 16 * z6
                        print("Type your orders by entering the number of the food: ")
                        answ3 = int(input())
                    else:
                        print("Invalid Input. Please try again: ")
                        answ3 = int(input())

                print("The total cost of your order is: ", price, "$")
                print("Your order will be delivered within minutes , feel free to navigate through the Lounge.")
        if (ans1==2):
            Musicians = ("1) Ragheb Alameh", "2) Assi El Hellani", "3) Nancy Ajram")
            print("This week's musicians are:")
            for i in Musicians:
                print(i)
            a=random.randrange(0,1000)
            b=random.randrange(0,1000)
            c=random.randrange(0,1000)
            print("\nVote for the musician you want to attend this week(enter -1 to exit): ")
            answ2 = int(input())
            while answ2 != -1:
                if answ2 == 1:
                    print("You voted for the musician Ragheb Alemeh !\n")
                    break
                elif answ2 == 2:
                    print("You voted for the musician Assi El Hellani !")
                    break
                elif answ2 == 3:
                    print("You voted for the musician Nancy Ajram !")
                    break
                else:
                    print("Invalid Input. Please try again: ")
            print("The total votes of Ragheb Alameh is: ", a,"Votes")
            print("The total votes of Assi El Hellani is: ", b,"Votes")
            print("The total votes of Nancy Ajram is: ", c,"Votes")
            print("The total of people who voted are: ", a+b+c,"Votes")
            print("\n")
        if (ans1==3):
            gaming_lounge()
    elif ans == 2:
        normal_rest()
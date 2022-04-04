MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
turn_off_machine = False

''' Compare customer choice and see resources available or not'''
def does_resource_available(user_choice):
    if user_choice=='cappuccino':
        if resources["coffee"]<24:
            print(f"Sorry there is not enough coffee.") 
            return 0
        elif  resources["milk"]<100 :
            print(f"Sorry there is not enough milk.")   
            return 0
        elif resources["water"]<250:
            print(f"Sorry there is not enough water.") 
            return 0
        else:
            return MENU[user_choice]['cost'] 
            
       
    if user_choice=='latte':
        if resources["coffee"]<24:
            print(f"Sorry there is not enough coffee.") 
            return 0
        elif  resources["milk"]<150 :
            print(f"Sorry there is not enough milk.")  
            return 0
        elif resources["water"]<200:
            print(f"Sorry there is not enough water.")
            return 0
        else:
            return MENU[user_choice]['cost'] 


                 
    if user_choice=='espresso':
        if resources["coffee"]<18:
            print(f"Sorry there is not enough coffee.") 
            return 0
        elif resources["water"]<50:
            print(f"Sorry there is not enough water.")
            return 0
        else:
            return MENU[user_choice]['cost'] 



''' Show customer available resorces'''
def show_report():       
    water =resources["water"]
    milk =resources["milk"]
    coffee =resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}gm")
    print(f"Money: ${money}")
        


''' Accept money from customer and return change. if money insufficient return all'''
def ask_and_check_money(choice):
    print("Please insert coins.")
    quaters=int(input("how many quarters?:"))
    dimes =int(input("how many dimes?: "))
    nickles =int(input("how many nickles?: "))
    penny =int(input("how many penny?: "))
    user_total_money = quaters*0.25 + dimes*0.10 + nickles*0.05 + penny*0.01
    change=user_total_money - MENU[choice]['cost']
    if user_total_money<MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${round(change,2)} in change. \n Here is your {choice} ☕️. Enjoy!")  
        ''' update a resources '''  
        resources["water"] -= MENU[choice]['ingredients']['water']
        resources["coffee"] -= MENU[choice]['ingredients']['coffee']
        if choice != "espresso":
            resources["milk"] -= MENU[choice]['ingredients']['milk']

     

while not turn_off_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "report":
        show_report()
    elif user_choice == "off":
        turn_off_machine =True
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":     
        earn_money = does_resource_available(user_choice)
        if earn_money>1:
            ask_and_check_money(choice=user_choice)  
            money += earn_money
    else:
        print("Sorry We are not clear about what you want. Please Try Again")    

 
        

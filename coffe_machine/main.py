#create a funtion that ask the menu to the guest and do the prompt funtionalities
import data
from os import system
resources=list(data.resources.values())
water=resources[0]
milk=resources[1]
coffee=resources[2]
money=0
list_resources=[water,milk,coffee,money]
def data_item(item):
    """retorna los ingredientes del producto"""
    water=0
    milk =0
    coffee =0
    for i in data.MENU:
        if i == item:
            ingre=list(data.MENU[i]["ingredients"].keys())
            if "water" in ingre:
                water=data.MENU[i]["ingredients"]["water"]
            if "milk" in ingre:
                milk=data.MENU[i]["ingredients"]["milk"]
            if "coffee" in ingre:
                coffee=data.MENU[i]["ingredients"]["coffee"]
    return [water,milk,coffee,data.MENU[i]["cost"]]
def enough_resources(item):
    """verify if there is enought resources for the product"""
    list_r_item=data_item(item)
    count=0
    verificador=True
    while  not count>len(list_resources)-2:
        if list_resources[count]<list_r_item[count]:
            verificador=False
            print(f"Sorry there is not enough {list(data.resources.keys())[count]}")
            count=25
        count+=1
    return verificador
def check_transaction (product):
    """check the money_product the users insert is enough to purchase the product"""
    global  money
    verificador = True
    print("Insert the money_product")
    quarters = int(input("how many quarters? :"))
    dimes = int(input("how many dimes? :"))
    nickles = int(input("how many nickles? :"))
    pennies = int(input("how many pennies? :"))
    money_inserted=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    money_product=data_item(product)[3]
    if money_inserted<money_product:
        verificador = False
        print("Sorry that's not enough money_product. Money refunded")
    elif money_inserted>money_product:
        change_money=round(money_inserted-money_product,2)
        list_resources[3]=list_resources[3]+money_product
        print(f"Here is ${change_money} dollars in change.")
    else :
        list_resources[3]=list_resources[3]+money_product
    return verificador
def update_resources(product):
    """update the resources after a the user choice the product"""
    global list_resources
    lisr_resource=data_item(product)
    for i in range(len(list_resources)-1):
        list_resources[i]=list_resources[i]-lisr_resource[i]
def  promtp():
    system("cls")
    terminador=True
    #we created a loop while for the users choice a correct option
    while terminador:
        users_options = input("What would you like? (espresso/latte/cappuccino) :").lower()
        if users_options in ["espresso","latte","cappuccino","off","report"]:
            terminador=False
        else :
            print("you  chose  a wrong option")

    if users_options=="off":
        exit()
    elif users_options=="report":
        print(f"""
                        Water: {list_resources[0]}ml
                        Milk: {list_resources[1]}ml
                        Coffee: {list_resources[2]}g
                        Money: ${list_resources[3]}""")
        promtp()
    else:
        check1 = enough_resources(users_options)
        if check1 :
            check2 = check_transaction(users_options)
            if check2:
                update_resources(users_options)
                print(f"dispending a {users_options}")
                promtp()
            else:
                promtp()
        else:
            promtp()



promtp()

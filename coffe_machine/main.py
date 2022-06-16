#create a funtion that ask the menu to the guest and do the prompt funtionalities
import data
resources=list(data.resources.values())
water=resources[0]
milk=resources[1]
coffee=resources[2]
list_resources=[water,milk,coffee]
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
    return [water,milk,coffee]
def enough_resources(item):
    """verify if there is enought resources for the product"""
    list_r_item=data_item(item)
    count=0
    verificador=True
    while  not count>len(list_resources)-1:
        if list_resources[count]<list_r_item[count]:
            count=25
            verificador=False
        count+=1
    print("Sorry there is not enough water.")
def update_resources(product):
    """update the resources after a the user choice the product"""
    global list_resources
    lisr_resource=data_item(product)
    for i in range(len(list_resources)):
        list_resources[i]=list_resources[i]-lisr_resource[i]
def  promtp():
    terminador=True
    while terminador:
        users_options = input("What would you like? (espresso/latte/cappuccino) :").lower()
        if users_options in ["espresso","latte","cappuccino","off","report"]:
            terminador=False
            print(list_resources)
            update_resources(users_options)
            print(list_resources)
            print(data_item(users_options))
            enough_resources(users_options)
promtp()

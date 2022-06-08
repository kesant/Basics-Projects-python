
#calculator
import art

def add(n1,n2):
    """this funtion recieve two numbers and return the sum """
    return n1+n2
def subtract(n1,n2):
    """this funtion recieve two numbers and return the substract """
    return n1-n2
def multiply(n1,n2):
    """this funtion recieve two numbers and return the multiplication """
    return n1*n2
def divide (n1,n2):
    """this funtion recieve two numbers and return the divition """
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator ():
    print(art.logo)
    num1=float(input("What's the first number? :"))

    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input ("Pick an operation  :")
        num2=float(input("What's the next number? :"))
        calculation_funtion=operations[operation_symbol]
        answer=calculation_funtion(num1,num2)
        print(f"{num1}{operation_symbol}{num2} ={answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : ").lower()=="y":
            num1=answer
        else:
            should_continue=False
            calculator()


calculator()
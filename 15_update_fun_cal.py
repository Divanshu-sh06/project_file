def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

def cal():
    print("select the operations")
    print("1.add")
    print("2.sub")
    print("3.mul")

    choice = (input("select the number you want to pick"))
    if choice not in["1","2","3"]:
        print("invalid number please choose coorect")
        return
    elif choice in ["1","2","3"]:
        num1 = int(input("enter the first number"))
        num2 = int(input("enter the second number"))
        if choice=="1":
            print(f"the add of a and b is{add(num1,num2)}")
        elif choice=="2":
            print(f"the sum of a and b is:{sub(num1,num2)}")
        elif choice=="3":
            print(f"the mul of a and b is{mul(num1,num2)}")
        else:
            print("wrong operation")
cal()
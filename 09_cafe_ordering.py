class pythoncafeTalk:
    def __init__(self):
        print("\t\t\t\t\tDivansh cafe ")
        print("\t\t\t\t\tSince - 2018")
        print("\t\t\t\t\twww.cafeteria.com")
        print("\n\n\t\t\t\t\t\tMENU\t")

        x =["indian","German","korean","vietnamese"]
        for i in x:
            print("\n\n",i)
    def indian(self):
        x = ["misal pav","kosha mangsho","makki di roti & sarso da saag","dokhla","rogan josh","papaya khar","litti chowka","biryani","fish curry"]
        b = [80,200,350,120,200,150,250,400,500]
        Indian_={"indian types food ":x,"price":b}
        import pandas as pd
        df = pd.DataFrame(Indian_)
        print("\n\nINDIAN FOODS\n\n")
        print(df)
        d=[]
        while True:
            b=int(input("ENTER THE VALUE POSITION"))
            c=int(input("ENTER THE QUANTITY"))
            z=Indian_["price"][b]
            y=z*c
            d.append(y)
            x=input("DO YOU WANT TO REODER (YES/NO)")
            if x=="no":
                print('THANU YOU')
                break
        t =sum(d)
        m =(sum(d)*0.05)
        k = t+m
        from colorama import Fore,Back,Style
        print(Fore.BLACK+Back.RED+Style.BRIGHT+"service tax = 5%")
        print("TOTAL AMOUNT HAS TO PAY:",t,"RUPEES")
        print("TOTAL AMOUNT INCLUDING SERVICE TAX HAS TO PAY:",k,"RUPEES")

    def german(self):
        x = ["saverbraten-roas beef stew","schweinshaxe-pork kunckle","spatzle-egg noodles","himmel und erde","saumagen","spatzle"]
        b = [250,300,500,800,760,1000]
        german_={"GERMAN FOOD TYPES":x , "PRICE":b}
        import pandas as pd
        df = pd.DataFrame(german_)
        print("\n\nGERMAN FOODS\n\n")
        print(df)
        d = []
        while x:
            x=True
            a = int(input("ENTER THE VALUE POSITION"))
            b = int(input("ENTER THE QUANTITY"))
            z = german_["PRICE"][a]
            y = z*b
            d.append(y)
            x = input("DO YOU WANT TO REORDER (YES/NO)")
            if x == "no":
                print('thank you/n for coming our restaurent')
                break
        g = sum(d)
        h = (sum(d)*0.05)
        i = g+h
        from colorama import Fore,Back,Style
        print(Fore.BLACK+Back.GREEN+Style.BRIGHT+"service tax =5%")
        print("total amount",g,"rupees")
        print("total amount including service tax has to pay",i,"rupees")

    def korean(self):
        x = ["kimchi","bibimbap","bulgogi","jajangmyean","yukgaejang","ramyeon","mandu"]
        b = [200,100,350,400,670,900,1000]
        korean_={'KOREAN FOOD TYPES':x ,"PRICE":b}
        import pandas as pd 
        df = pd.DataFrame(korean_)
        print('\n\nKOREAN FOODS\n\n')
        print(df)
        d = []
        while x:
            x = True
            e = int(input("ENTER THE VALUE OF POSITION"))
            f = int(input("ENTER THE QUANTITY"))
            g = korean_["PRICE"][e]
            h = g*f
            d.append(h)
            x = input("DO YOU WANT TO REORDER (YES/NO)")
            if x == "no":
                print("thank you for coming our restaurent")
                break
        t = sum(d)
        j = (sum(d)*0.05)
        k = t+j
        from colorama import Fore,Back,Style
        print(Fore.GREEN+Back.YELLOW+Style.BRIGHT+"service tax = 5%")
        print("total amount",g,"rupees")
        print("total amount including service tax has to pay",k,"rupees")

    def vietnamese(self):
        x = ["pha","bhuncha","banhmi","banch cuan","gai cuan","cha gio","com tam","banh khoy"]
        b = [250,300,200,100,500,1200,670,2300]
        vietnamese_={'vietnamese food types':x,'price':b}
        import pandas as pd
        df = pd.DataFrame(vietnamese_)
        print("/n/nvietnamese food/n/n")
        print(df)
        d =[]
        while x:
            x = True
            b = int(input("enter the value of position"))
            c = int(input("enter the quantity"))
            z = vietnamese_["price"][b]
            k = z*c
            d.append(k)
            x = input("do you want to reoder (yes/no)")
            if x =="no":
                print("thank you for coming our restaurent")
                break
        t = sum(d)
        j = (sum(d)*0.05)
        k = t+j
        from colorama import Fore,Back,Style
        print(Fore.LIGHTBLUE_EX+Back.MAGENTA+Style.DIM+"service tax = 5%")
        print("total amount",t,"rupees")
        print("total amount including service tax has to pay",k,"rupees")

obj = pythoncafeTalk()

k = input("ENTER THE TYPE OF FOOD:")
if k=="indian":
    print(obj.indian())
elif k=="german":
    print(obj.german())
elif k=="korean":
    print(obj.korean())
elif k=="vietnamese":
    print(obj.vietnamese())
else:
    print("wrong option:\n please again choose the right option ") 
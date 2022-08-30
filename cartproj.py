d={"p1":100,"p2":200,"p3":300,"p4":400,"p5":500}
dc={}
tob=0
while True:
    print("p1 ---- 100\np2 ---- 200\np3 ---- 300\np4 ---- 400\np5 ---- 500\n")
    ch=int(input("press1: To buy product\npress2: to remove product\npress3: clear cart\npress4: print bill\npress5: exit\n"))
    
    if ch==1:
        name=input("enter product name\n")
        name=name.lower()
        if name in d and name not in dc:
                qt=int(input("enter quantity\n"))
                tob=tob+(qt*d[name])
                dc[name]=qt
        elif name in d and name  in dc:
                qt=int(input("enter quantity\n"))
                tob=tob+(qt*d[name])
                dc[name]+=qt
        else:
                print("invalid product")
    elif ch==2:
        name=input("enter product name\n")
        name=name.lower()
        while name not in dc:
            print("product not in your cart please enter correct name")
            name=input("enter product name\n")
        if  name  in dc:
                qt=int(input("enter quantity\n"))
                while  qt>dc[name]:
                    print("you have less quantity in cart,please enter again")
                    qt=int(input("enter quantity\n"))
                tob=tob-(qt*d[name])
                dc[name]-=qt
        else:
                ("product not found in cart")
    elif ch==3:
        dc.clear()
        tob=0
    elif ch==4:
        print(dc)
        print("your total bill is : ",tob)
    elif ch==5:
        break
					
				
				
				
				
				
		

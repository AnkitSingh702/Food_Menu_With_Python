print('welcome to food corner')
print('1=sunday \n2= monday \n3= tuesday \n4= wednesday \n5= thursday \n6= friday \n7= saturday ')

day = int(input ('enter day'))

if day==1 :
    print('1= breakfast\n 2= lunch\n 3= dinner')
    meal = int(input('enter what you want:'))
    if meal==1:
        print("1= sandwich,$40\n 2= chai, $ 30\n 3= burger,$80")
        choice =int(input('enter your choice'))
        if choice==1:
            print("1=veg sandwich $40\n 2=non veg sandwich $100")
            type = int(input("enter your choice"))
            if type==1:
                print("veg sandwich $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
                    print("stop")
            elif type==2:
                print("non veg sandwich $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif choice==2:
            print("1=simple chai $20\n 2=special chai $30")
            type = int(input('enter your choice'))
            if type==1:
                print("simple chai $20")
                bill= int(input("pay billing price"))
                if bill==20:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif type==2:
                print("special chai $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif choice==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            type = int(input("enter your choice :"))
            if type==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif type==2:
                print("non veg burger $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif meal ==2:
        print('1= daal chawal $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        choice=int(input('enter your choice'))
        if choice==1:
            print("1=half $30\n 2=full $60")
            type= int(input('enter your choice'))
            if type==1:
                print("half $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if choice==2:
            print('1=half $25\n 2=full $50')
            type= int(input('enter your choice'))
            if type==1:
                print("half $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if choice==3:
            print("1=half $40\n 2=full $80")
            type= int(input("enter your choice"))
            if type==1:
                print("half $40")
                bill= int(input("pay billing price"))
                if bill ==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            
    elif meal ==3:
        print("1= sahi paneer $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        choice=int(input('enter your choice'))
        if choice==1:
            print("1=half $100\n 2=full $200")
            type= int(input("enter your choice"))
            if type==1:
                print("half $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if choice==2:
            print('1= half $125\n 2= full $175')
            type= int(input("enter your choice"))
            if type==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if choice==3:
            print("1=half $185\n 2=full $225")
            type= int(input("enter your choice"))
            if type==1:
                print("half $185")
                billl=int(input("pay billing price"))
                if bill==185:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if type==2:
                print("full $225")
                bill=int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")

elif day==2 :
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= pohe,$40\n 2= chai, $ 30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=veg pohe $40\n 2=non veg pohe $100")
            z= int(input("enter your choice"))
            if z==1:
                print("veg pohe $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif z==2:
                print("non veg pohe  $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=simple chai $20\n 2=special chai $30")
            e= int(input('enter your choice'))
            if e==1:
                print("simple chai $20")
                bill= int(input("pay billing price"))
                if bill==20:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif e==2:
                print("special chai $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif choice==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            type= int(input("enter your choice :"))
            if type==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif type==2:
                print("non veg burger $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==2:
        print('1= daal chawal $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        type=int(input('enter your choice'))
        if type==1:
            print("1=half $30\n 2=full $60")
            g= int(input("enter your choice"))
            if g==1:
                print("half $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if g==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print('roti sabji $50')
            bill= int(input("pay billing price"))
            if bill==50:
                print("thankyou you can go now")
            else:
                print("stop")
        if type==3:
            print("1=half $40\n 2=full $80")
            g= int(input("enter your choice"))
            if g==1:
                print("half $50")
                bill= int(input("pay billing price"))
                if bill==50:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if g==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= sahi paneer $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice :'))

        if type==1:
            print("1=half $100\n 2=full $200")
            s=int(input("enter your choice"))
            if s==1:
                print("half $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if s==2:
                print("full $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print("1=half $125\n 2= full $175")
            d= int(input("enter your choice"))
            if d==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if d==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==3:
            print("1=half $150\n 2=full $225")
            d= int(input("enter your choice"))
            if d==1:
                print("half $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if d==2:
                print("full $225")
                bill= int(input("pay billing price"))
                if bill==225:
                    print("thankyou you can go now")
                else:
                    print("stop")  

elif day==3:
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= pohe,$40\n 2= chai, $ 30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=veg pohe $40\n 2=non veg pohe $100")
            z= int(input("enter your choice"))
            if z==1:
                print("veg pohe $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif z==2:
                print("non veg pohe  $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=simple chai $20\n 2=special chai $30")
            e= int(input('enter your choice'))
            if e==1:
                print("simple chai $20")
                bill= int(input("pay billing price"))
                if bill==20:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif e==2:
                print("special chai $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            f= int(input("enter your choice :"))
            if f==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif f==2:
                print("non veg burger $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==2:
        print('1= daal chawal $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        type=int(input('enter your choice'))
        if type==1:
            print("1=half $30\n 2=full $60")
            v= int(input("enter your choice"))
            if v==1:
                print("half $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if v==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==2:
            print('roti sabji $50')
            bill= int(input("pay billing price"))
            if bill==50:
                print("thankyou you can go now")
            else:
                print("stop")
        if type==3:
            print("1=half $40\n 2=full $80")
            v= int(input("enter your choice"))
            if v==1:
                print("half $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if v==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= aaloo paratha $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice'))
        if type==1:
            print("1= 2 parathe $100\n 2= 4 parathe $200\n")
            w= int(input("enter your choice"))
            if w==1:
                print("2 parathe $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if w==2:
                print("4 parathe $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print('half $125\n full $175')
            w= int(input("enter your choice"))
            if w==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if w==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==3:
            print("1=half $150\n 2=full $225")
            w= int(input("enter your choice"))
            if w==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if w==2:
                print("full $225")
                bill= int(input("pay billing price"))
                if bill==225:
                    print("thankyou you can go now")
                else:
                    print("stop")
elif day==4:
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= fried rice $40\n 2= chai, $ 30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=half $25\n 2=full $50")
            y= int(input("enter your choice)"))
            if y==1:
                print("half $25")
                bill= int(input("pay billing price"))
                if bill==25:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if y==2:
                print("full $50")
                bill= int(input("pay billing price"))
                if bill==50:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=simple chai $20\n 2=special chai $30")
            e= int(input('enter your choice'))
            if e==1:
                print("simple chai $20")
                bill= int(input("pay billing price"))
                if bill==20:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif e==2:
                print("special chai $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            p= int(input("enter your choice :"))
            if p==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif p==2:
                print("non veg burger $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==2:
        print('1= pizza $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        type=int(input('enter your choice'))
        if type==1:
            print("1=mini $30\n 2=large $60")
            q= int(input("enter your choice"))
            if q==1:
                print("mini $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if q==2:
                print("large $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==2:
            print('roti sabji $50')
            bill= int(input("pay billing price"))
            if bill==50:
                 print("thankyou you can go now")
            else:
                print("stop")
        if type==3:
            print("1=half $40\n 2=full $80")
            q= int(input("enter your choice"))
            if q==1:
                print("half $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")

            if q==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= aaloo paratha $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice'))
        if type==1:
            print("1= 2 parathe $100\n 2= 4 parathe $200\n")
            q= int(input("enter your choice"))
            if q==1:
                print("2 parathe $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if q==2:
                print("4 parathe $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==2:
            print('half $125\n full $175')
            q= int(input("enter your choice"))
            if q==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if q==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==3:
            print("1=half $150\n 2=full $225")
            r= int(input("enter your choice :"))
            if r==1:
                print("half $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if r==2:
             print("full $225")
             bill= int(input("pay billing price"))
             if bill==30:
                 print("thankyou you can go now")
             else:
                print("stop")


elif day==5:
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= pohe,$40\n 2= samoshe, $ 30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=veg pohe $40\n 2=non veg pohe $100")
            o= int(input("enter your choice"))
            if o==1:
                print("veg pohe $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if o==2:
                print("non veg pohe  $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=2amoshe $15\n 2=3samoshe $30")
            e= int(input('enter your choice'))
            if e==1:
                print("2 samoshe $15")
                bill= int(input("pay billing price"))
                if bill==15:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif e==2:
                print("3 samoshe $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            t= int(input("enter your choice :"))
            if t==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif t==2:
                    print("non veg burger $150")
    elif choice==2:
        print('1= daal chawal $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        type =int(input('enter your choice'))
        if type==1:
            print("1=half $30\n 2=full $60")
            i= int(input("enter your choice"))
            if i==1:
                print("half 30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print('roti sabji $50')
            bill= int(input("pay billing price"))
            if bill==50:
                print("thankyou you can go now")
            else:
                print("stop")
        if type==3:
            print("1=half $40\n 2=full $80")
            i= int(input("enter your choice"))
            if i==1:
                print("half 40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= aaloo paratha $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice'))
        if type==1:
            print("2 parathe $100\n 4 parathe $200\n")
            i= int(input("enter your choice"))
            if i==1:
                print("2 parathe $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("4 parathe $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==2:
            print('1=half $125\n 2=full $175')
            i= int(input("enter your choice"))
            if i==1:
                print("half 125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==3:
            print("1=half $150\n 2=full $225")
            i= int(input("enter your choice"))
            if i==1:
                print("half 150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $225")
                bill= int(input("pay billing price"))
                if bill==225:
                    print("thankyou you can go now")
                else:
                    print("stop")


elif day==6:
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= pohe,$40\n 2= samoshe, $ 30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=veg pohe $40\n 2=non veg pohe $100")
            z= int(input("enter your choice"))
            if z==1:
                print("veg pohe $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif z==2:
                print("non veg pohe  $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=2amoshe $15\n 2=3samoshe $30")
            e= int(input('enter your choice'))
            if e==1:
                print("2 samoshe $15")
                bill= int(input("pay billing price"))
                if bill==15:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif e==2:
                print("3 samoshe $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("1=veg burger $80\n 2=non veg burger $150")
            f= int(input("enter your choice :"))
            if f==1:
                print("veg burger $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif f==2:
                print("non veg burger $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==2:
        print('1= daal chawal $60\n 2= roti sabji $50\n 3= aaloo rajma $80')
        type=int(input('enter your choice'))
        if type==1:
            print("1=half $30\n 2=full $60")
            i= int(input("enter your choice"))
            if i==1:
                print("half 30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print('roti sabji $50')
        if type==3:
            print("1=half $40\n 2=full $80")
            i= int(input("enter your choice"))
            if i==1:
                print("half 40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= aaloo paratha $200\n 2= matar paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice'))
        if type==1:
            print("2 parathe $100\n 4 parathe $200\n")
            i= int(input("enter your choice"))
            if i==1:
                print("2 parathe $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("4 parathe $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==2:
            print('1=half $125\n 2=full $175')
            i= int(input("enter your choice"))
            if i==1:
                print("half 125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        if type==3:
            print("1=half $150\n 2=full $225")
            i= int(input("enter your choice"))
            if i==1:
                print("half 150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if i==2:
                print("full $225")
                bill= int(input("pay billing price"))
                if bill==225:
                    print("thankyou you can go now")
                else:
                    print("stop")
elif day==7:
    print('1= breakfast\n 2= lunch\n 3= dinner')
    choice= int(input('enter what you want:'))
    if choice==1:
        print("1= pohe,$40\n 2= chai, $30\n 3= burger,$80")
        type=int(input('enter your choice'))
        if type==1:
            print("1=veg pohe $40\n 2=non veg pohe $100")
            z= int(input("enter your choice"))
            if z==1:
                print("veg pohe $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif z==2:
                print("non veg pohe  $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print("1=simple chai $20\n 2=special chai $30")
            tea= int(input('enter your choice'))
            if tea==1:
                print("simple chai $20")
                bill= int(input("pay billing price"))
                if bill==20:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif tea==2:
                print("special chai $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("burger $80")
            bill= int(input("pay billing price"))
            if bill==80:
                print("thankyou you can go now")
            else:
                print("stop")
    elif choice==2:
        print('1= daal chawal $60\n 2= aaloo parwal $70\n 3= aaloo rajma $80')
        type=int(input('enter your choice'))
        if type==1:
            print("1=half $30\n 2=full $60")
            l= int(input("enter your choice"))
            if l==1:
                print("half $30")
                bill= int(input("pay billing price"))
                if bill==30:
                    print("thankyou you can go now")
                else:
                    print("stop")
            if l==2:
                print("full $60")
                bill= int(input("pay billing price"))
                if bill==60:
                    print("thankyou you can go now")
                else:
                    print("stop")

        if type==2:
            print('1 plate aaloo parwal $70')
        elif type==3:
            print("1=half $40\n 2=full $80")
            l= int(input("enter your choice"))
            if l==1:
                print("half $40")
                bill= int(input("pay billing price"))
                if bill==40:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif l==2:
                print("full $80")
                bill= int(input("pay billing price"))
                if bill==80:
                    print("thankyou you can go now")
                else:
                    print("stop")
    elif choice==3:
        print("1= aaloo paratha $200\n 2= kadhai paneer $175\n 3= palak paneer $225") 
        type=int(input('enter your choice'))
        if type==1:
            print("2 parathe $100\n 4 parathe $200\n")
            l= int(input("enter your choice"))
            if l==1:
                print("2 aaloo parathe $100")
                bill= int(input("pay billing price"))
                if bill==100:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif l==2:
                print("4 aaloo parathe $200")
                bill= int(input("pay billing price"))
                if bill==200:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==2:
            print('1=half $125\n 2=full $175')
            l= int(input("enter your choice"))
            if l==1:
                print("half $125")
                bill= int(input("pay billing price"))
                if bill==125:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif l==2:
                print("full $175")
                bill= int(input("pay billing price"))
                if bill==175:
                    print("thankyou you can go now")
                else:
                    print("stop")
        elif type==3:
            print("1=half $150\n 2=full $225")
            l= int(input("enter your choice"))
            if l==1:
                print("half $150")
                bill= int(input("pay billing price"))
                if bill==150:
                    print("thankyou you can go now")
                else:
                    print("stop")
            elif l==2:
                print("full $225")
                bill= int(input("pay billing price"))
                if bill==225:
                    print("thankyou you can go now")
                else:
                    print("stop")
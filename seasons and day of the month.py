monthNo= int(input("Enter The Number Of The Month:"))
if monthNo<1 or monthNo>12:
    print("Incorrect Entry")
else:
    if monthNo==2:
        print("This Month Has 28 Days")
        
    elif monthNo==4 or monthNo==6 or monthNo==9 or monthNo==11:
        print("This Month Has 30 Days")
    
    else:
        print("This Month Has 31 Days")

if monthNo in [12,1,2]:
    print("This Month is in Winter")
elif monthNo in [3,4,5]:
    print("This Month is in Spring")
elif monthNo in [6,7,8]:
    print("This Month is in Summer")
else:
    print("This Month is in Autumn")

side1= int(input("Enter lenght of first side of the triangle:"))
side2= int(input("Enter lenght of second side of the triangle:"))
side3= int(input("Enter lenght of last side of the triangle:"))
if not(abs(side2-side3)<side1<side2+side3 or abs(side1-side3)<side2<side1+side3 or  abs(side2-side1)<side3<side2+side1) :
    print("This is not a triangle")
    
else:
    
    if side1**2==side2**2+side3**2 or side2**2==side1**2+side3**2 or side3**2==side2**2+side1**2:
        print("This is Right Triangle")
    elif side1**2>side2**2+side3**2 or side2**2>side1**2+side3**2 or side3**2>side2**2+side1**2:
        print("This is Obtuse Triangle")
    else:
        print("This is Acute Triangle")
    
#kenarları istediğin sırada girecek şekilde ayarla

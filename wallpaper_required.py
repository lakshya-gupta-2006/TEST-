h = float(input("ENTER THE HEIGHTN OF ROOM(in sq feet): "))
w = float(input("ENTER THE WEIDTH OF ROOM(in sq feet): "))
l = float(input("ENTER THE LENGTH OF ROOM (in sq feet):"))
area =((l * h)*2 )+ ((w * h)*2 )
print("area of room =")
print(area)
print("wall rools required")
rolls_length = 9
rolls_required = area / rolls_length
print(rolls_required)

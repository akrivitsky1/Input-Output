length = int(input("Enter length:"))
width = int(input("Enter width:"))
area = length*width
number_pieces = (area / 9) + 1
print("You should order",int(number_pieces), "pieces.")

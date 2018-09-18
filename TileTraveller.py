x_start = 1
y_start = 1

victory = False
print("You can travel (N)orth. ")
direction = str(input("Direction: "))

if direction == "n" or direction == "N":
    x_start = x_start
    y_start += 1
    print("You can travel: (N)orth or (E)ast or (S)outh. ")
else:
    print("Not a valid direction")
    
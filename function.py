a1 = int(input("enter 1st Number:"))
a2 = int(input("enter 2nd Number:"))
a3 = int(input("enter 3rd Number:"))
def biggest(a1, a2, a3):
    if a1 > a2 and a1 > a3:
        highest = n1
    elif a2 > a1 and a2 > a3:
        highest = a2
    else:
        highest = a3
    return highest
print("The biggest number is", biggest(a1, a2, a3))


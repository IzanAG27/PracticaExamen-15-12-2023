isbn = [x for x in input("").split()]

calculo = (isbn[0]*1) + (isbn[1]*2) + (isbn[2]*3) + (isbn[3]*4) + (isbn[4]*5) + (isbn[5]*6) + (isbn[6]*7) + (isbn[7]*8) + (isbn[8]*9)
if calculo % 11 == 0:
    print("True")
elif calculo % 11 == 10:
    print(isbn.append("X"))
    print("True")
else:
    print("False")
print(calculo)
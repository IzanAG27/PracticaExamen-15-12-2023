any = int(input(""))

if any % 4 != 0:
    print("Any comú")
elif any % 100 != 0:
    print("Any de traspàs")
elif any % 400 != 0:
    print("Any comú")
else:
    print("Any de traspàs")
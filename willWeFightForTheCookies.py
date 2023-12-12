numPersonasGalletas = input("").split()

personas = int(numPersonasGalletas[0])
galletas = int(numPersonasGalletas[1])

if personas % galletas == 0:
    print("Let's Eat")
elif galletas % personas == 0:
    print("Let's Eat")
else:
    print("Let's Fight")
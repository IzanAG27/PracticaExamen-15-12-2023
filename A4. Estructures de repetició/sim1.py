nums = [int(num) for num in input().split()]
positivo = 0
noValido = []
for num in nums:
    if num > 0:
        positivo += num
    else:
        noValido += str(num)
print("Números positivos: ",positivo)
print("Carácteres no validos: ",noValido)
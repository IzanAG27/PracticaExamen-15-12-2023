
nums = [int(x) for x in input("").split()]

primerNumero = nums[0]
ultimoNumero = nums[-1]

nums[0] = ultimoNumero
nums[-1] = primerNumero

print(nums[:])
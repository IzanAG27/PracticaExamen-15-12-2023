"""
Programa que apartir de una lista de
números enteros calcula cual es el número máximo y cual el mínimo.
"""


def pedir_num():
    nums = [int(x) for x in input("").split()]
    return nums



def calcularMax(nums):
    maximum = nums[0]
    for y in nums:
        if y > maximum:
            maximum = y
    return maximum


def calcularMin(nums):
    minimum = nums[0]
    for y in nums:
        if y < minimum:
            minimum = y
    return minimum

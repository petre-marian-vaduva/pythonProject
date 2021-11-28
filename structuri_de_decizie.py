# # Să se scrie un program care determină maximul a două numere întregi citite de la tastatură.
# num1 = int(input())
# num2 = int(input())
# if num1 > num2:
#     print(f'Number {num1} is greater than {num2}')
# else:
#     print(f'Number {num2} is greater than {num1}')

# # Se dau trei numere naturale a b x. Să se verifice dacă numărul x aparține intervalului [a,b].
# Method 1
# a = int(input())
# b = int(input())
# x = int(input())
# if x > a and x < b or x < a and x > b:
#     print("X is in the interval a-b")
# else:
#     print("X doesn't belong to the interval a-b")
# Method 2
# a = int(input())
# b = int(input())
# x = int(input())
# if x in range(a, b):
#     print("Este")
# else:
#     print("Nu este")
# Method 3
# a = int(input())
# b = int(input())
# x = int(input())
# is_between = a <= x <= b
# print(is_between)

# Să se scrie un program care determină minimul a trei numere întregi.
# Method 1
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1 < num2 and num1 < num3:
#     print(f'{num1} is the smallest')
# elif num2 < num1 and num2 < num3:
#     print(f'{num2} is the smallest')
# else:
#     print(f'{num3} is the smallest')
# Method 2
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# smallest = min(num1, num2, num3)
# print(f'Smallest number is {smallest}')

# # Fiind date vârstele a doi copii afișați care dintre ei este cel mai mare și cu cât.
# child1 = int(input("Child1 age: "))
# child2 = int(input("Child2 age: "))
# if child1 < 0 or child2 < 0:
#     print("Introduce a real age")
# elif child1 > child2:
#     print(f'Child1 is older with {child1 - child2} years')
# else:
#     print(f'Child2 is older with {child2 - child1} years')

# # Se dau 10 numere distincte. Să se determine suma celor mai mari 5 dintre ele.
# num1 = int(input("Add a number: "))
# num2 = int(input("Add a number: "))
# num3 = int(input("Add a number: "))
# num4 = int(input("Add a number: "))
# num5 = int(input("Add a number: "))
# num6 = int(input("Add a number: "))
# num7 = int(input("Add a number: "))
# num8 = int(input("Add a number: "))
# num9 = int(input("Add a number: "))
# num10 = int(input("Add a number: "))
# list_elements = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
# set_elements = set(list_elements)
# if len(list_elements) != len(set_elements):
#     print("Numbers should be different")
# max_1 = 0
# max_2 = 0
# max_3 = 0
# max_4 = 0
# max_5 = 0
# for num in list_elements:
#     if num > max_1:
#         max_5 = max_4
#         max_4 = max_3
#         max_3 = max_2
#         max_2 = max_1
#         max_1 = num
#     elif num > max_2:
#         max_5 = max_4
#         max_4 = max_3
#         max_3 = max_2
#         max_2 = num
#     elif num > max_3:
#         max_5 = max_4
#         max_4 = max_3
#         max_3 = num
#     elif num > max_4:
#         max_5 = max_4
#         max_4 = num
#     elif num > max_5:
#         max_5 = num
# print(max_1, max_2, max_3, max_4, max_5)

# Să se scrie un program care citeşte de la tastatură trei numere naturale și determină diferenţa dintre cel mai mare şi cel mai mic.
# Method 1
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# smallest = 0
# biggest = 0
# if num1 > num2 and num1 > num3:
#     biggest = num1
# elif num2 > num1 and num2 > num3:
#     biggest = num2
# else:
#     biggest = num3
# if num1 < num2 and num1 < num3:
#     smallest = num1
# elif num2 < num1 and num2 < num3:
#     smallest = num2
# else:
#     smallest = num3
# print(biggest - smallest)
# Method 2
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# max_number = max(num1, num2, num3)
# min_number = min(num1, num2, num3)
# print(max_number - min_number)

# Se citește de la tastatură un număr natural de 3 cifre. Să se determine câte cifre impare conține.
# num = int(input())
# if num < 100:
#     print("Number is too small")
# elif num > 999:
#     print("Number is too big")
# count = 0
# while num > 0:
#     digit = num % 10
#     if digit % 2 != 0:
#         count += 1
#     num = num // 10
# print(f'The number has {count} odd digits')
# -----------------------------------
# Se citește de la tastatură un număr natural de 3 cifre. Să se stabilească dacă are toate cifrele egale.
# num = int(input())
# if num < 100:
#     print("Number is too small")
# elif num > 999:
#     print("Number is too big")
# arr = []
# while num > 0:
#     digit1 = num % 10
#     arr.append(digit1)
#     num = num // 10
# if arr[0] == arr[1] and arr[0] == arr[2]:
#     print("All digits are equals")
# else:
#     print("The digits are not equals")

# # Se dă un număr natural nenul n.
# # Să se determine cel mai mic număr natural, mai mare sau egal decât n, care are ultimele două cifre egale cu 0.
# num = int(input())
# while True:
#     num += 1
#     if num % 100 == 00:
#         print(num)
#         break

# # Să se scrie un program care citeşte de la tastatură un număr întreg şi determină semnul său.
# num = int(input())
# if num > 0:
#     print(f'{num} is positive')
# else:
#     print(f'{num} is negative')

# # Să se scrie un program care citeşte de la tastatură două numere întregi şi
# # verifică dacă cele doua numere au acelaşi semn.
# num1 = int(input())
# num2 = int(input())
# if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
#     print("Same sign")
# else:
#     print("Different sign")

# # # Se da un număr n. Calculați ultima cifră a lui 2 la puterea n.
# num = int(input())
# result = 1
# for digit in range(num):
#     result = result * 2
#     result = result % 10
# print(result)
# Method 2
# result = 2 ** num % 10
# print(result)

# # Să se scrie un program care verifică dacă un număr natural citit de la tastatură este pătrat perfect.
# import math
# num = int(input())
# square_root = int(math.sqrt(num))
# if num == square_root * square_root:
#     print("It's a square root")
# else:
#     print("It's not a square root")

# Se citește de la tastatură un număr natural de maxim 2 cifre. Să se afișeze pe ecran valori astfel:
# dacă numărul este mai mic sau egal cu 15 se va afișa pătratul valorii sale;
# dacă numărul este cuprins între 16 și 30 (inclusiv) se va afișa suma cifrelor sale;
# în caz contrar se va afișa produsul cifrelor sale.
# num = int(input())
# if num <= 15:
#     print(num * num)
# elif num > 16 and num <= 30:
#     sum = num % 10 + num // 10
#     print(sum)
# else:
#     print((num % 10) * (num // 10))

# Se dă un număr natural n. Să se determine cele mai mari două numere impare, mai mici decât n.
# num = int(input())
# arr = []
# while num > 0:
#     num -= 1
#     if num % 2 == 1:
#         arr.append(num)
#         if len(arr) == 2:
#             print(f'The odd numbers are: {arr}')
#             break
# # Se citește de la tastatură un număr natural de maxim 3 cifre. Să se determine câte cifre are.
# num = int(input())
# count = 0
# while num > 0:
#     count += 1
#     num //= 10
# print(f'The numbers has: {count} digits.')

# # Se citește de la tastatură un număr natural de 3 cifre. Să se afișeze pe ecran cea mai mare cifră a sa.
# num = int(input())
# max_digit = 0
# while num > 0:
#     num = num % 10
#     if num > max_digit:
#         max_digit = num
#         print(max_digit)
#     num = num // 10

# # Se citește de la tastatură un număr natural de 3 cifre, distincte. Să se afișeze pe ecran cifra din mijloc, ca valoare.
# num = int(input())
# num = num // 10 % 10
# print(num)
# num = int(input())
# middle_digit = num // 10 % 10
# print(middle_digit)
# num = int(input())
# max_1 = -99999999
# max_2 = -99999999
# max_3 = -99999999
# while num > 0:
#     aux = num % 10
#     if aux > max_1:
#        max_3 = max_2
#        max_2 = max_1
#        max_1 = aux
#     num = num // 10
#     print(max_1, max_2, max_3)

# Se citesc două numere naturale n m.  Să se decidă dacă cele două numere au cifre comune.
# num1 = int(input())
# num2 = int(input())
#
# num1_arr = []
# num2_arr = []
#
# while num1 > 0 and num2 > 0:
#     aux1 = num1 % 10
#     aux2 = num2 % 10
#     num1_arr.append(aux1)
#     num2_arr.append(aux2)
#     num1 = num1 // 10
#     num2 = num2 // 10
# common_digits = set(num1_arr).intersection(num2_arr)
# if len(common_digits) > 0:
#     print(common_digits)
# else:
#     print("There aren't")

# # Se citește de la tastatură un număr natural de 3 cifre. Să se afișeze cifrele sale în ordine crescătoare.
# num = int(input())
# max1 = -999999999999
# max2 = -999999999999
# max3 = -999999999999
# while num > 0:
#     digit = num % 10
#     if digit > max1:
#         max3 = max2
#         max2 = max1
#         max1 = digit
#     elif digit > max2:
#         max3 = max2
#         max2 = digit
#     elif digit > max3:
#         max3 = digit
#     num = num // 10
# print(max3, max2, max1)
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# Se citește de la tastatură un număr natural. Să se afișeze cifrele sale în ordine crescătoare.

# # ascending digits in an array
# num = int(input())
# arr = []
# while num > 0:
#     aux = num % 10
#     arr.append(aux)
#     num //= 10
# arr.sort()
# print(arr)
# # changed the digits to strings to concate then changed back to digits
# string_arr = []
# for i in arr:
#     aux = str(i)
#     string_arr.append(aux)
# separator = ""
# result = separator.join(string_arr)
# print(result)

# Se dă un număr natural n. Afișați în ordine descrescătoare numerele naturale impare mai mici sau egale cu n.
# arr = []
# num = int(input())
# for i in range(0, num+1):
#     if i % 2 != 0:
#         arr.append(i)
# print(sorted(arr, reverse=True))

# Se dă n. Să se afișeze 10n.

def outer():
    def inner():
        print('This is inner.')
    print('This is outer, returning inner.')
    return inner
i = outer()
i()




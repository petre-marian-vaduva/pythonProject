# # Să se scrie un program care citeşte de la tastatura două numere naturale şi determină suma lor.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# sum = num1 + num2
# print(sum)

# # Calculați ultima cifră a sumei a două numere naturale.
# num1 = int(input())
# num2 = int(input())
# last_digit = (abs(num1+num2)) % 10
# print(last_digit)

# # Fiind date două numere naturale x și y determinați valoarea care trebuie adunată la x pentru a obține triplul lui y.
# x = int(input())
# y = int(input())
# result = 3 * y -x
# print(result)

# Să se scrie un program care citeşte de la tastatură un număr natural cu cel puţin două cifre
# şi determină suma dintre cifra zecilor şi cifra unităţilor numărului citit.
# Answer
# num = int(input())
# if num < 10:
#     print("Number too small, try again!")
# elif num > 10:
#     sum = int(str(num)[0]) + int(str(num)[1])
#     print(sum)
# else:
#     print("Try again!")
# Right Answer
# num = int(input())
# last_digit = num % 10
# penultimate_digit = int(str(num)[-2])
# sum = last_digit + penultimate_digit
# print(sum)

# Scrieți un program care cere de la tastatură un număr a (de o cifră) și care afișează valoarea expresiei a16.
# num = int(input())
# print(num ** 16)

# # Se dă un număr. Să se afișeze rădăcina sa pătrată.
# import math
#
# num = int(input())
# print(math.sqrt(num))

# # Se dau două numere naturale nenule a și b, unde a≤b. Să se determine câte numere naturale divizibile cu 10 sunt în intervalul [a,b].
# a = int(input("Insert a number: "))
# b = int(input("Insert another number: "))
# arr = []
# if a > b:
#     print("a should be less than than b")
# else:
#     for i in range(a, b):
#         arr.append(i)
# print(arr)
# result = 0
# for last_digit in arr:
#     if last_digit % 10 == 0:
#         result += 1
# print(result)

# Să se scrie un program care citeşte de la tastatură un număr natural cu exact trei cifre și determină suma cifrelor sale.
# Method 1
# num = int(input())
# if num < 99:
#     print("Number too small")
# elif num > 999:
#     print("Number too big")
# sum = int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
# print(sum)
# Method 2
# num = int(input())
# if num < 99:
#     print("Number too small")
# elif num > 999:
#     print("Number too big")
# sum = 0
# for digit in range(len(str(num))):
#     sum += num % 10
#     num //= 10
# print(sum)

# Se dă un număr natural n cu exact trei cifre. Calculaţi produsul dintre cifra unităților și cifra sutelor.
# num = int(input())
# if num < 99:
#     print("Number too small")
# elif num > 999:
#     print("Number too big")
# last_digit = num % 10
# first_digit = num //100
# sum = first_digit + last_digit
# print(sum)
# num = int(input())
# if num < 99:
#     print("Number too small")
# elif num > 999:
#     print("Number too big")
# last_digit = num % 10
# while num > 0:
#     first_digit = num % 10
#     num = num // 10
# print(last_digit + first_digit)

# Se citește un număr natural impar n. Să se afișeze valoarea sumei 1+3+5+7+...n.
# Method 1
# num = int(input())
# if num % 2 == 0:
#     print("Insert an even number")
# sum = 0
# for i in range(1, num+1):
#     if i % 2 == 1:
#         sum = sum +i
# print(sum)
# Method 2
# num = int(input())
# sum = 0
# for i in range(1, num+1, 2):
#     sum += i
# print(sum)

# Să se scrie un program care citește o literă mică și afișează litera mare corespunzătoare.
# string = input()
# print(string.upper())

# Se dă un număr natural n. Afișați în ordine crescătoare numerele naturale pare nenule mai mici sau egale cu n.
# arr = [1, 8, 5, 2]
# new_arr = []
# aux = 0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             aux = arr[i]
#             arr[i] = arr[j]
#             arr[j] = aux
# print(arr)
# for odd in arr:
#     if odd % 2 == 1:
#         new_arr.append(odd)
# print(new_arr)

# Se dă n. Să se afișeze 10n.
import collections
import importlib.resources
import math

# num = int(input())
# aux = 1
# for i in range(1, num+1):
#     aux = aux * 10
# print(aux)
# exp = int(input())
# result = math.exp(num)
# print(pow(2, 3))

# Se dau numerele n și m. Să se determine exponentul la care se ridică n pentru a obține m.

# n = int(input())
# m = int(input())
# count = 0
# while n > 0:
#     count += 1
#     if n * n == m:
#         print(count)
#     break

# Se citesc 2 numere, n și p, afișați în ordine crescătoare toate puterile lui n care sunt mai mici sau egale cu p.
# n = int(input())
# p = int(input())
# count = 0
# result = 1
# while n>0:
#     result = result * n
#     print(result)
#     if result == p or result > p:
#         break

# count += 1
# print(f'The numbers in ascending order are: {count}')

# Se citesc numere de la tastatură până la apariția lui zero. Să se determine suma lor.
# num = int(input())
# sum = 0
# while num > 0:
#     curent_digit = num % 10
#     if curent_digit == 0:
#         break
#     sum += curent_digit
#     num = num // 10
# print(sum)


# Se citesc numere de la tastatură până când se introduc două numere consecutive egale.
# Să se determine suma tuturor numerelor citite.
# sum = 0
# while True:
#     num1 = int(input())
#     num2 = int(input())
#     sum += num1 + num2
#     if num1 == num2:
#         print("Both numbers are equal")
#         break
#     else:
#         continue
# print(sum)
# sum = 0
# aux = 0
# while True:
#     num = int(input())
#     # sum += num
#     if num == aux:
#         print(f'Numbers {num} and {num} are equal.')
#         break
#     aux = num
# print(num)

# Se dau n numere naturale.
# Să se determine primele două numere impare, nu neapărat distincte, dintre cele date.
# count = 0
# arr = []
# while True:
#     num = int(input())
#     if num % 2 == 1:
#         arr.append(num)
#         count += 1
#     if count == 2:
#         print(arr)
#         break

# Se dă un interval [l,r]. Aflaţi câte perechi de numere pare se pot forma alegând două numere din interval.
# l = int(input())
# r = int(input())
# arr= []
# for num in range(l, r+1):
#     if num % 2 == 0:
#         arr.append(num)
# print(arr)
# print(f'There are {len(arr) // 2} pairs of even numbers in the interval {l} - {r}')

# Se dau n numere naturale. Determinaţi câte cifre pare şi câte cifre impare se află în total în cele n numere.
# arr = []
# num1 = int(input())
# num2 = int(input())
# result = math.factorial(num1) / math.factorial(num1 - num2) * math.factorial(num2)
# print(result)

# Se citește n număr natural. Calculați suma numerelor naturale mai mici sau egale cu n.
# num = int(input())
# result = 1
# for i in range(num, 0, -1):
#     result = result * i
#     print(result)

# S=1*2+2*3+3*4...+n*(n+1)
# arr = []
# for i in range(0,5):
#     num = int(input())
#     arr.append(num)
#     min_num = arr[0]
#     for k in range(len(arr)):
#         if arr[k] < min_num:
#             min_num = arr[k]
#     print(min_num)

# Se citesc numere de la tastatură până la apariția lui zero. Să se determine maximul lor.
# total = 0
# while True:
#     num = int(input())
#     while True:
#         aux = num % 10
#         if aux == 0:
#             break
#         else:
#             total += aux
#             num = num // 10
#
#     print(total)

# Să se scrie un program care citește un șir de n numere naturale
# # şi determină numărul din șir care are prima cifră minimă.
# count = 0
# max_digit = -9999999
# arr = ['3123','52','33','33','52', '66']
# for i in range(0, len(arr)):
#     if int(arr[i][0]) > max_digit:
#         max_digit = int(arr[i][0])
#         count += 1
#         print(count)


# Să se scrie un program care citește un șir de n numere naturale şi determină cele mai mari două numere din şir.

#
# arr = [312,752,33333,33,89,66]
# max_1 = -9999
# max_2 = -9999
# for num in arr:
#     if num > max_1:
#         max_2 = max_1
#         max_1 = num
#     elif num > max_2:
#         max_2 = num
#     print(max_1, max_2)

# # Se dau n numere naturale. Determinați cel mai mare număr par introdus și numărul său de apariții.
# max_num = -99999
# max_num_even = -99999
# counter = 0
# arr = [2,5,5,3,5,6,4,6,6,6]
# for num in arr:
#     if num > max_num and num % 2 == 0:
#         max_num = num
# print(counter)

# Se citesc numere de la tastatură până la apariția lui zero. Să se determine maximul lor
# arr = []
# aux = 0
# while True:
#     num = int(input())
#     aux = num % 10
#     arr.append(num)
#     if aux == 0:
#         break
#     num = num // 10
#
# max_num = 0
# for num in arr:
#     if num > max_num:
#         max_num = num
# print(max_num)

# Să se scrie un program care citește un șir de n numere naturale şi determină cele mai mari două numere din şir.
#
# arr = []
# max_1 = -9999
# max_2 = -9999
# while len(arr) < 6:
#     number = int(input())
#     arr.append(number)
#     for num in arr:
#         if num > max_1:
#             max_2 = max_1
#             max_1 = num
#         elif num > max_2:
#             max_2 = num
#         print(arr, max_1, max_2)

# arr = [0]
# max_1 = -9999
# count = 0
# while True:
#     n = int(input())
#     arr.append(n)
#     for i in arr:
#         if i > max_1:
#             max_1 = i
#     for j in arr:
#         if j == max_1:
#             count += 1
# print(f'Number {max_1} appears {count} times.')


# arr = []
# frecventa = [0] * 10
# n = int(input())
# while n > 0:
#     num = int(input())
#     while num > 0:
#         last_digit = num % 10
#         frecventa[last_digit] = frecventa[last_digit] +1
#         num = num // 10
#     n = n -1
#
#     print(frecventa)
# frecventa = [0] * 9
# n = int(input())
# while n > 0:
#     num = int(input())
#     while num > 0:
#         last_digit = num % 10
#         frecventa[last_digit] = frecventa[last_digit] + 1
#         print(frecventa)
#         num = num // 10
#     n = n - 1
#

# # Să se scrie un program care citește un șir de n numere naturale şi determină de câte ori apare.
# n = int(input())
# frequencies = [0] * 999999
# max_num = 0
# while n > 0:
#     num = int(input())
#     frequencies[num] += 1
#     for i in reversed(range(0, len(frequencies))):
#         if frequencies[i] > 0:
#             if i > max_num:
#                 max_num = i
#             print(max_num, frequencies[max_num])
#     n = n-1

# Method 1
# for element in arr:
#     if element in frequencies:
#         frequencies[element] += 1
#     else:
#         frequencies[element] = 1
#     print(frequencies)
# Method 2
# frequencies_count = collections.Counter(arr)
# for key, value in frequencies_count.items():
#     print(f'{key}: {value}')

# n = int(input())
# frequency = [0] * 999999
# while n > 0:
#     frequency[int(input())] += 1
#     n -= 1
# for i in frequency
# n = int(input())
# max_num = -1
# counter = 0
# while n > 0:
#     num = int(input())
#     if num > max_num:
#         max_num = num
#         counter = 1
#     elif max_num == num:
#         counter += 1
#     n = n - 1
# print(max_num, counter)

# Să se scrie un program care citește un șir de n numere naturale şi determină cele mai mari două numere din şir.
# n = int(input('Insert a number:'))
# max_1 = -99999
# max_2 = -99999
# while n > 0:
#     num = int(input(f'Choose a number:'))
#     if num > max_1:
#         max_2 = max_1
#         max_1 = num
#     elif num > max_2:
#         max_2 = num
#     n = n - 1
# print(f'The greatest numbers are: {max_1} and {max_2}')

# Se dau n numere naturale. Determinați cel mai mare număr par introdus.
# n = int(input())
# max_num = -9999999
# while n > 0:
#     num = int(input())
#     if num > max_num and num % 2 == 0:
#         max_num = num
#     n -= 1
# print(max_num)

# Se dau n numere naturale. Determinați cele mai mici două numere dintre cele introduse care au ultimele două cifre egale.
# min_1 = 999999
# min_2 = 999999
# while True:
#     num = int(input())
#     if num < min_1:
#         min_2 = min_1
#         min_1 = num
#     elif num < min_2:
#         min_2 = num
#     if min_1 % 100 == min_2 % 100:
#         print(min_1, min_2)
#         break
#     else:
#         continue

# Se dau numerele naturale n și k, unde k este o cifră.
# Să se verifice dacă toate cifrele lui n sunt mai mici sau egale decât k.
# n = int(input())
# k = int(input())
# Ok = True
# while n > 0:
#     aux = n % 10
#     if aux > k:
#         Ok = False
#         break
#     n = n // 10
# if Ok == True:
#     print('DA')
# else:
#     print('NU')

# Se dă un număr natural n. Determinaţi câte cifre are suma cifrelor sale.
# n = int(input())
# total = 0
# count = 0
# while n > 0:
#     aux = n % 10
#     total += aux
#     n = n // 10
# print(len(str(total)))

# Se dau n numere naturale. Determinaţi câte cifre pare şi câte cifre impare se află în total în cele n numere.
# arr = []
# count_odd = 0
# count_even = 0
# n = int(input("How many numbers do you want to choose ?\n"))
# while n > 0:
#     num = int(input('Choose a number:\n'))
#     arr.append(num)
#     n -= 1
# for i in arr:
#     while i > 0:
#         aux = i % 10
#         if aux % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#         i = i // 10
# print(f'{count_even} even numbers and {count_odd} odd numbers.')

# Se dă n, număr natural nenul. Să se testeze dacă n are număr impar de divizori.
# n = int(input())
# count = 0
# for i in range(2, int(n/2)+1):
#     if n % i == 0:
#         count += 1
#         print(i)
# if count % 2 == 0:
#     print('even')
# elif count % 2 == 1:
#     print('odd')
# else:
#     print('no divisors')

# Se citește un număr natural n. Să se determine câți divizori pari are acest număr.
# n = int(input())
# count = 0
# for i in range(1, int(n/2)+1):
#     if n % i == 0 and i % 2 == 0:
#         count += 1
# print(count)

# Să se scrie un program care afișează divizorii comuni ai două numere naturale citite de la tastatură.
# num_1 = int(input())
# num_2 = int(input())
# if num_1 > num_2:
#     min_num = num_2
# elif num_2 > num_1:
#     min_num = num_1
# for i in range(1, min_num+1):
#     if num_1 % i == num_2 % i == 0:
#         print(i)

# Aici am aflat cel mai mare divizor comun.
# num_1 = int(input())
# num_2 = int(input())
# if num_1 > num_2:
#     min_num = num_2
# elif num_2 > num_1:
#     min_num = num_1
# for i in range(min_num, 1, -1):
#     if num_1 % i == num_2 % i == 0:
#         print(i)
#         break
# def gcd(a, b):
#    if a == 0 :
#       return b
#    return gcd(b%a, a)
# a = 11
# b = 15
# print(gcd(12,8))
# print(gcd(12,8))
# Euclideeeeee
# a = int(input())
# b = int(input())
# r = a % b
# while r:
#     a = b
#     b = r
#     r = a % b
#     print(b)

# Se citește un număr natural n. Să se determine numărul de divizori ai oglinditului lui n.
# n = int(input())
# new_num = 0
# count = 0
# while n > 0:
#     aux = n % 10
#     new_num = (new_num * 10) + aux
#     n = n // 10
# for i in range(1, new_num // 2 + 1):
#     if new_num % i == 0:
#         count += 1
#     elif count == 1:
#         print('1')
# print(count+1)

# Să se scrie un program care verifică dacă un număr natural citit de la tastatură este număr perfect.
# n = int(input())
# total = 0
# for i in range(1, (n // 2)+1):
#     if n % i == 0:
#         total += i
#         print(i)
# if total == n:
#     print('Perfect number')
# else:
#     print('Not perfect number')

# Să se scrie un program care să determine cel mai mare divizor comun a două numere naturale citite de la tastatură.
# n1 = int(input())
# n2 = int(input())
# min_num = 0
# if n1 > n2:
#     min_num = n2
# else:
#     min_num = n1
# for i in range(min_num, 0, -1):
#     if n1 % i == n2 % i == 0:
#         print(i)
#         break

# Să se scrie un program care citește un număr natural și verifică dacă este prim.
# n = int(input())
# is_num_prime = True
# for i in range(2, n//2 +1):
#     if n % i == 0:
#         is_num_prime = False
#         break
#     else:
#         is_num_prime = True
# print(is_num_prime)

# Se dă un număr natural n. Să se afişeze în ordine crescătoare, primii n termeni ai şirului lui Fibonacci.
# n = int(input('How many numbers ?'))
# count = 0
# n1 = 0
# n2 = 1
# if n <= 0:
#     print('Choose a positive number')
# else:
#     while count < n:
#         print(n1)
#         total = n1 + n2
#         n1 = n2
#         n2 = total
#         count += 1

# Se dau n numere naturale. Să se verifice despre fiecare dacă este termen al şirului lui Fibonacci.
# n = int(input())
# num1 = 0
# num2 = 1
# count = 0
# total = 0
# if n <= 0:
#     print('Enter a positive number')
# else:
#     while count < n:
#         print(num1)
#         total = num1 + num2
#         num1 = num2
#         num2 = total
#         count += 1


# Se citesc de la tastatură n numere naturale.
# Să se determine numarul de numere prime formate din primele 2 cifre ale fiecarui număr.

# n = int(input('How many numbers?\n'))
# while n > 0:
#     count = 0
#     num = int(input('Insert a number ?'))
#     for i in range(2, len(str(num))):
#         num = num // 10
#     for k in range(1, num // 2 + 1):
#         if num % k == 0:
#             count += 1
#             print(k)
#     print(f'Count is {count}')
# n -= 1
#
# Se citește un vector cu n elemente, numere naturale.
# Să se afișeze elementele din vector care sunt multipli ai ultimului element.
# n = int(input('Enter a number of elements: \n'))
# arr = []
# while n > 0:
#     num = int(input())
#     arr.append(num)
#     n -= 1
#
# last_element = arr[-1]
# for number in range(0, len(arr)-1):
#     if arr[number] % last_element == 0:
#         print(f'{arr[number]} is multiple of {last_element}')
#     else:
#         print('No multiples')

# Swap first and last element
# arr = [2,3,4,5]
# for num in arr:
#     first_element = arr[0]
#     last_element = arr[-1]
#     print(first_element, last_element)

# # Să se determine maximul şi minimul valorilor elementelor unui vector.
# arr = [22,31,4,5,6]
# # Method1
# min_number = arr[0]
# for num in arr:
#     if num < min_number:
#         min_number = num
# print(min_number)
#
# # Method 2
# arr.sort()
# print(arr[0])
#
# # Method 3
# print(min(arr))


# Se dă un vector x cu n elemente, numere naturale.
# Să se construiască un alt vector, y, care să conțină elementele prime din x, în ordine inversă.
# size = int(input('Number of elements:'))
# arr = []
# for i in range(0, size):
#     arr.append(int(input()))
# first = 0
# last = -1
# for k in range(0, len(arr)//2 +1):
#     temp = arr[first]
#     arr[first] = arr[last]
#     arr[last] = temp
#     first +=1
#     last -=1
#

# Se dă un vector x cu n elemente, numere naturale.
# Să se construiască un alt vector, y, care să conțină elementele prime din x, în ordine inversă.

# x = [1,4,5,8,9,11]
# new_x = []
# for i in range(len(x)-1, -1, -1):
#     new_x.append(x[i])
#     print(new_x)
# ---------------------------------


# Se dau n numere întregi. Determinaţi câte dintre numerele date apar o singură dată.

# arr = [7,3,3,4,5]
# count = [0] * len(arr)
# for i in range(0, len(arr)):
#     print(arr[i])

# # Să se scrie un program care citește un șir de n numere naturale şi determină de câte ori apare.
# n = int(input())
# frequencies = [0] * 999999
# max_num = 0
# while n > 0:
#     num = int(input())
#     frequencies[num] += 1
#     for i in reversed(range(0, len(frequencies))):
#         if frequencies[i] > 0:
#             if i > max_num:
#                 max_num = i
#             print(max_num, frequencies[max_num])
#     n = n-1

# Method 1
# for element in arr:
#     if element in frequencies:
#         frequencies[element] += 1
#     else:
#         frequencies[element] = 1
#     print(frequencies)
# Method 2
# frequencies_count = collections.Counter(arr)
# for key, value in frequencies_count.items():
#     print(f'{key}: {value}')

# n = int(input())
# frequency = [0] * 999999
# while n > 0:
#     frequency[int(input())] += 1
#     n -= 1
# for i in frequency
# n = int(input())
# max_num = -1
# counter = 0
# while n > 0:
#     num = int(input())
#     if num > max_num:
#         max_num = num
#         counter = 1
#     elif max_num == num:
#         counter += 1
#     n = n - 1
# print(max_num, counter)

# Se cere determinarea maximului şi minimului valorilor dintr-un sir.
# arr = [7,8,9,5]
# max_num = arr[0]
# min_num = arr[0]
# for k in arr:
#     if k > max_num:
#         max_num = k
#     elif k < min_num:
#         min_num = k
#     print(min_num, max_num)


# Se dă un șir cu n elemente numere naturale. Să se determine valoarea maximă din șir și de câte ori apare.
# FRECVENTAAAAAAAA
# arr = [2,2,4,5,6,6,8,3,3,3,7,7,1]
# freq = [0] * 999999
# max_num = -999999
# for i in arr:
#     freq[i] += 1
# for j in arr:
#     if freq[j] > 1:
#         if j > max_num:
#             max_num = j
# print(max_num)

# PROBLEMAAAAAAA
# arr = [1, 4, 5, 2, 20, 32, 6, 8, 15, 23, 24, 6]
# current = -999
# count = 0
# for i in arr:
#     if i > current:
#         current = i
#         count += 1
#         print(count)
#     elif current > i:
#         count = 1
#         current = -999999
#         print(count)
#         continue
# nums = [2,4,5,2,1,51]
# ans = anchor = 0
# for i in range(len(nums)):
#     if i and nums[i - 1] >= nums[i]: anchor = i
#     ans = max(ans, i - anchor + 1)
# print(ans)


# Să se șteargă dintr-un vector toate elementele care sunt numere prime.
# arr = [5,8,9,6,22,14]
# for i in arr:
#     prime = True
#     for k in range(3, i):
#         if i % k == 0:
#             prime = False
#     if prime:
#         print(i)
# print(arr)

# Se dă un vector cu n elemente numere naturale. Să se verifice dacă toate elementele vectorului sunt egale.
# arr = [1,1,2,1]
# equal = True
# new_arr = []
# for i in arr:
#     if arr[0] == i:
#         equal = True
#         continue
#     else:
#         equal = False
#         break
# if equal:
#     print('All equals')
# else:
#     print('NO')

# Se dă un vector cu n elemente numere naturale.
# Să se verifice dacă toate elementele vectorului sunt diferite două câte două.
# arr = [1,2,2,4,5,6,7,8]
# i = 0
# count = 1
# is_true = True
# while i < len(arr):
#     if arr[i] == arr[count]:
#         is_true = False
#     i += 2
#     count += 2
# if is_true:
#     print('sunt diferite')
# else:
#     print('nu sunt diferite')

# Se dă un vector cu n elemente numere naturale. Să se verifice dacă are elementele ordonate crescător.
# arr = [2,3,10,4,5,6]
# new_arr = sorted(arr)
# if arr == new_arr:
#     print('Da')
# else:
#     print('nu')

# Se dă un şir cu n elemente, numere naturale. Să se verifice dacă toate elementele şirului au număr par de cifre.
# arr = [25,45,898,20,2000,989809]
# count = 0
# is_even = True
# for i in range(0, len(arr)):
#     while arr[i] > 0:
#         count += 1
#         arr[i] = arr[i] // 10
#     if count % 2 == 1:
#         is_even = False
#         break
#     count = 0
# if is_even:
#     print('True')
# else:
#     print('False')

# Să se determine indicele maximului şi cel al minimului valorilor elementelor unui vector.
# arr = [22,4,632,24,3]
# min_num = 99999
# max_num = -99999
# for i in arr:
#     if i < min_num:
#         min_num = i
#     if i > max_num:
#         max_num = i
# print(min_num, max_num)

# Se dă un vector cu n numere naturale.
# Să se determine câte dintre elementele vectorului sunt prime cu ultimul element.
# arr = [12,11,7]
# for num in arr:
#     is_prime = True
#     for k in range(2, num // 2+1):
#         if num % k == 0:
#             is_prime = False
# print(is_prime)
#

# Se dau două şiruri cu elemente numere naturale.
# Determinaţi câte dintre elementele primului şir sunt mai mari decât toate elementele celui de-al doilea şir.
# count = 0
# arr = [102 ,4 ,14 ,22 ,30 ,223]
# arr_2 = [12 ,14 ,100 ,23 ,15]
# for num_1 in arr:
#     is_greater = True
#     for num_2 in arr_2:
#         if num_1 < num_2:
#             is_greater = False
#             break
#     if is_greater:
#         count += 1
# print(count)

# Să se șteargă dintr-un vector toate elementele care sunt numere prime.

# arr = [0,15,2,1,3,4,7,8,9,10,11]

# for i in arr:
#     if i == 0:
#         arr.pop()
#     for k in range(1, i//2 +1):
#         if i % k == 0:
#             break
#         else:
#             arr.remove(i)
#             break
# print(arr)

# Să se șteargă dintr-un vector toate elementele pare.

# arr = [3,4,4,5,6,7]
#
# for i in range(len(arr)-1, -1, -1):
#     if arr[i] % 2 == 0:
#         arr.pop(i)
# print(arr)

# Se citește un șir cu n elemente, numere întregi.
# Să se șteargă elementele care se repetă, păstrându-se doar primul de la stânga la dreapta.

# arr = [3,4,5,5,6,7]
# for i in range(len(arr)-1, -1, -1):
#     if arr[i] % 2 == 0:
#         arr.remove(arr[i])
# is_there = False
# set_elements = set()
# for element in arr:
#     if element in set_elements:
#         is_there = True
#     else:
#         set_elements.add(element)
# if is_there:
#     print('duplicate')
# else:
#     print('no duplicate')


# Se citește un șir cu n elemente, numere întregi.
# Să se șteargă elementele care se repetă, păstrându-se doar primul de la stânga la dreapta.
# arr = [3,4,5,6,7]
# new_arr = []
# for i in range(len(arr)-1, -1, -1):
#     if arr[i] in new_arr:
#         arr.pop(i)
#     else:
#         new_arr.append(arr[i])
# print(arr)

# # Să se insereze într-un șir după fiecare element par dublul său.
# arr = [3, 6, 5, 7, 4, 4]
# new_arr = []
# for i in range(len(arr)):
#     new_arr.append(arr[i])
#     if arr[i] % 2 == 0:
#         new_arr.append(arr[i] * 2)
# print(new_arr)

# for index,value in enumerate(arr):
#     new_arr.append(value)
#     if value % 2 == 0:
#         new_arr.append(value * 2)
# print(new_arr)

# arr = [3,4,5,6,8,7]
# new_arr = []
# for i in range(0, len(arr)):
#     new_arr.insert(i, arr[i])
#     if arr[i] % 2 == 0:
#         new_arr.insert(i+1, 99)
# print(new_arr)
# l = sorted(arr)
# print(l)


# Se dă un şir cu n elemente, numere naturale. Să se verifice dacă toate elementele şirului sunt pare.
# arr = [4,6,8]
# is_even = True
# for num in arr:
#     if num % 2 == 1:
#         is_even = False
# if is_even:
#     print('all even')
# else:
#     print('false')

# Se dă un vector cu n elemente numere naturale.
# Să se verifice dacă toate elementele vectorului sunt diferite două câte două.

# arr = [2,3,4,4,6,7,8,9]
# for i in range(0,len(arr),2):
#     if arr[i] == arr[i+1]:
#         print('DA')
#         print(arr[i],arr[i+1])
#     else:
#         print('NU')
#         print(arr[i], arr[i + 1])

# Se dă un vector cu n elemente numere naturale. Să se verifice dacă toate elementele vectorului sunt egale.
# arr = [4,4,4,4,5]
# is_equal = True
# first_number = arr[0]
# for item in range(1, len(arr)):
#     if first_number != arr[item]:
#         is_equal = False
#         break
# if is_equal:
#     print('equal')
# else:
#     print('not equal')

# Se dă un vector cu n elemente numere naturale.
# Să se verifice dacă toate elementele vectorului sunt diferite două câte două.
# arr = [2,3,4,6,6,7,8]
# is_different = True
# length = len(arr)
# # check if lenght is odd
# if length % 2 == 1:
#     length = length-1
# for i in range(0, length,2):
#     if arr[i] == arr[i+1]:
#         is_different = False
#         break
# if is_different:
#     print('Numbers are different')
# else:
#     print('Same')

# Se dă un vector cu n elemente numere naturale. Să se verifice dacă are elementele ordonate crescător.

# arr = [4,5,6,7,8]
# is_ascending = True
# max_number = arr[0]
# for i in range(1, len(arr)):
#     if max_number < arr[i]:
#         max_number = arr[i]
#     else:
#         is_ascending = False
# if is_ascending:
#     print('The numbers are in ascending order!')
# else:
#     print('False')

# Se dă un şir cu n elemente, numere naturale.
# Să se verifice dacă toate elementele şirului sunt multipli ai ultimului element din şir.
# arr = [6,12,0,6,2]
# is_multiple = True
#
# for num in range(0, len(arr)-1):
#     if arr[num] % arr[-1] != 0:
#         is_multiple = False
#         break
# if is_multiple:
#     print('true')
# else:
#     print('false')

# Given two lists a, b.
# Check if two lists have at least one element common in them.
# arr = [1,2,3,5,4]
# arr2 = [6,5,7,8]
#
# is_common = False
# for i in arr:
#     for k in arr2:
#         if i == k:
#             is_common = True
#             break
# if is_common:
#     print('is common number')
# else:
#     print('no common number')
import collections
# Method2
# arr = [1,2,3,5,4]
# arr2 = [6,5,7,8]
# set_a = set(arr)
# set_b = set(arr2)
# if len(set_a.intersection(set_b)) > 0:
#     print('common number')
# else:
#     print('no common numbers')

# Se dă un şir cu n elemente, numere naturale.
# Să se verifice dacă oglinditul primului element apare printre celelalte elemente ale șirului.
# arr = [14,2,3,5,41,4]
# number = arr[0]
# reversed_number = 0
# while number > 0:
#     last_digit = number % 10
#     reversed_number = reversed_number * 10 + last_digit
#     number = number // 10
# for num in range(1, len(arr)):
#     is_common = False
#     if arr[num] == reversed_number:
#         is_common = True
#         break
# if is_common:
#     print('common words')
# else:
#     print('no common words')

# while number > 0:
#     reversed_number = number[slice(0, len(str(number)), -1)]
#     number = number // 10
#     print(int(reversed_number))
#     number = number // 10

# arr = [5,4,3,6,7]
# new_arr = []
# min_number = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             new_arr.append(arr[i])
# print(new_arr)

# WHILE Ask a number loop
# n = 3
# max = int(input("Enter a number >> "))
# for i in range(n-1):
#     x = int(input("Enter a number >> "))
#     if x > max:
#         max = x
#         print("The largest value is", max)
# sum = 0
# num = 0
# more_data = 'y'
#
# while more_data == 'y':
#     num = int(input('Enter a number\n'))
#     sum += num
#     more_data = input('More data ? Yes or No ?')
# print(sum)

# nothing = int(input('Enter a number! ENTER to quit!\n'))
# sum = 0
# while nothing != '':
#     x = float(nothing)
#     sum += x
#     nothing = input('Enter a number! ENTER to quit!\n')
# print(sum)

# arr = [4,2,1,5,3,9]
#
# temp = 0
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             print(arr)
#
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp
#             print(arr)

# Se dau n numere naturale nenule. Ordonați descrescător cele n numere după numărul lor de divizori.
# arr = [2,1,41,456,4]
# temp = 0
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp
# print(arr)

# Se dau n numere naturale nenule. Ordonați descrescător cele n numere după numărul lor de divizori.
# count = 0
# arr = [8,9,12,7,4]
# new_arr = []
# for i in range(0, len(arr)):
#     count = 1
#     for j in range(1, arr[i] // 2 +1):
#         if arr[i] % j == 0:
#             count += 1
#     new_arr.append(count)
# print(new_arr)


# Se dă un vector cu n elemente, numere naturale distincte.
# Ordonați crescător elementele situate înaintea valorii maxime din vector
# și descrescător elementele situate după această valoare.
# arr = [6,2,12,7,1,5,49,4,9,7]
# max_num = arr[0]
# index_max_num = 0
# for i in range(len(arr)):
#     if max_num < arr[i]:
#         max_num = arr[i]
#         index_max_num = i
# temp = 0
# for i in range(0, index_max_num):
#     for j in range(i+1, index_max_num):
#         if arr[i] > arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
# temp = 0
# for i in range(index_max_num+1, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
# print(arr)

# insert sort algorithm !!!!!!!!!!!
# arr = [2,5,11,2,10]
# for i in range(1, len(arr)):
#     while arr[i-1] > arr[i]:
#         temp = arr[i-1]
#         arr[i-1] = arr[i]
#         arr[i] = temp
#         i = i - 1
# print(arr)


# sortedd = False
# while not sortedd:
#     sortedd = True
#     for i in arr:
#         sortedd = Falses
#         if i < 10:
#             print(i)

# arr = [5,9,11,3,10]
# for i in range(1, len(arr)):
#     while arr[i-1] > arr[i]:
#         temp = arr[i-1]
#         arr[i-1] = arr[i]
#         arr[i] = temp
#         i = i - 1
#         print(arr)

# Se citește de la tastură un număr natural n, apoi n numere naturale.
# Să se afişeze cel mai mic număr care poate fi scris folosind prima cifră a numerelor citite.
# arr = [1,99,5,42,10,7,33,50]
# first_digits = []
# for i in arr:
#     while i > 0:
#         first_digit = i % 10
#         i = i // 10
#     first_digits.append(first_digit)
#
# for i in range(0, len(first_digits)):
#     for j in range(i+1, len(first_digits)):
#         if first_digits[i] > first_digits[j]:
#             temp = first_digits[i]
#             first_digits[i] = first_digits[j]
#             first_digits[j] = temp
#
# concat_digits = int(''.join(map(str, first_digits)))
# print(concat_digits)
#
# x = [str(i) for i in first_digits]
# concat_digits = ''.join(x)
# print(concat_digits)

# Se dau două şiruri, cu n, respectiv m, elemente, numere naturale.
# Primul şir este ordonat crescător, iar al doilea element este ordonat descrescător.
# Să se afişeze, în ordine crescătoare, valorile pare din cele două şiruri.
# sortare
# a = [5,12,5,1,6]
# b = [75,32,8,2,75]
# for i in range(0, len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# sortate = False
# while not sortate:
#     sortate = True
#     for i in range(1, len(b)):
#         if b[i-1] > b[i]:
#             temp = b[i-1]
#             b[i-1] = b[i]
#             b[i] = temp
#             sortate = False
# print(b)
# even_values = []
# for i in a:
#     if i % 2 == 0:
#         even_values.append(i)
# for j in b:
#     if j % 2 == 0:
#         even_values.append(j)
#
# for k in range(1, len(even_values)):
#     while even_values[k-1] > even_values[k] and k > 0:
#         temp = even_values[k-1]
#         even_values[k-1] = even_values[k]
#         even_values[k] = temp
#         k = k - 1
# print(even_values)

# Se dă un șir de caractere. Să se determine câte vocale din șir sunt cuprinse între două consoane.
# arr = 'Am Venit sa colindam.'
# arr = arr.casefold()
# count = 0
# for char in arr:
#     if not char in 'aeiouAEIOU':
#         print(char)
#         count += 1
# print(count)

# Să se scrie un program care citeşte un şir de caractere format din litere mici ale
# alfabetului englez şi înlocuieşte fiecare vocală cu litera mare corespunzătoare.

# letters = 'Ce sa-i faci, n-ai ce sa-i faci'
# new_letters = ''
# for char in letters.casefold():
#     if char in 'aeiou':
#         char = char.upper()
#     new_letters += char
# print(new_letters)


# Reversed string
# letters = 'trebuie'
# new_letters = ''
# for i in range(1, len(letters)+1):
#     new_letters += letters[-i]
# print(new_letters)
#
# new_letters = ''.join(reversed(letters))
# print(new_letters)


# Să se scrie un program care citeşte de la tastatură o propoziţie formată din mai multe cuvinte separate prin spaţii
# şi transformă prima şi ultima literă a fiecărui cuvânt în literă mare.
# sentence = ',Rica nu stia sa zica rau, ratusca, ramurica.'
# new_sentence = sentence[0].upper()
#
# for i in range(1, len(sentence)-1):
#     if not sentence[i+1].isalpha() and sentence[i].isalpha():
#         new_sentence += sentence[i].upper()
#     elif not sentence[i-1].isalpha() and sentence[i].isalpha():
#         new_sentence += sentence[i].upper()
#     else:
#         new_sentence += sentence[i]
# new_sentence += sentence[-1]
# print(new_sentence)

# Să se înlocuiasca cu cifra 5 ultima literă a fiecărui cuvânt din text.
# letters = 'da trebuie'
# # new_letters = ' '
# # for i in range(0, len(letters)-1):
# #     if not letters[i+1].isalpha() and letters[i].isalpha():
# #         new_letters += '5'
# #     else:
# #         new_letters += letters[i]
# # if letters[-1].isalpha():
# #     new_letters += '5'
# # else:
# #     new_letters += letters[-1]
# # print(new_letters)

# Se dă o propoziție formată din litere mari și mici ale alfabetului englez, cifre, spații și semne de punctuație,
# în care literele mari și mici se consideră identice. Determinați vocala din șir cu număr maxim de apariții.
# letters = 'aax uiat'
# freq = {}
# for i in letters:
#     if i in 'aeiou':
#         if i not in freq:
#             freq[i] = 1
#         else:
#             freq[i] += 1
# max_num = -9999
# for j in freq:
#     if freq[j] > max_num:
#         max_num = freq[j]
#         name = j
# print(name, max_num)


# # Cate cuvinte / words apar in string.

# sentence = "Rica@ are o pisica, un ,caine, &o pisica, si un caine si un cal!"
# new_sentence = sentence.split()
# new_sentence = ''
# count = 0
# for i in sentence.split():
#     new_sentence += i.strip('!()-[]{};:\'"\,<>./?@#$%^&*_~') + ' '
#     count += 1
#
# print(f'original sentence: {sentence}')
# print(f'new sentence: {new_sentence}')
# print(f'number of words: {count}')
import pprint

# Să se scrie un program care citește un cuvânt și îl afișează după interschimbarea primei vocale cu ultima consoană.
# word = 'Alex Giulesti!!'.lower()
# for i in list(word):
#     if i in 'aeiou':
#         first_vowel = i
#         break
#
# for j in reversed(list(word)):
#     if j not in 'aeiou' and j.isalpha():
#         last_consonant = j
#         break
# result = word.replace(first_vowel, '_').replace(last_consonant, first_vowel).replace('_', last_consonant)
# print(result)


# Să se scrie un program care citește un text și inserează după fiecare vocală caracterul *.
# sentence = 'Ana are mere'.lower()
# new_sentence = ''
# for i in sentence:
#     new_sentence += i
#     if i in 'aeiou':
#         new_sentence += '*'
# print(new_sentence)

# Să se scrie un program care citește mai multe propoziții și determină propoziția cu cele mai multe vocale.
# sentence = 'I play tennis. I eat rice. I like red.'.lower().split('.')
# Method 1
# word = ''
# max_number_vowel = -1
# for i in sentence:
#     count = 0
#     for j in i:
#         if j in 'aeiou':
#             count += 1
#     if count > max_number_vowel:
#         max_number_vowel = count
#         word = i
# print(f'The sentence is: "{word}" with {max_number_vowel} vowels.')

# Method 2 with input - while
# arr = []
# while True:
#     sentence = input('Insert a sentence: (press \'s\' to stop)\n')
#     if sentence == 's':
#         break
#     arr.append(sentence)
#
# max_num_vowels = -1
# for i in arr:
#     count = 0
#     for j in i:
#         if j in 'aeiou':
#             count += 1
#     if count > max_num_vowels:
#         max_num_vowels = count
#         sentence_name = i
# print(arr)
# print(f'The sentence \'{sentence_name}\' has {max_num_vowels} vowels.')


# Să se scrie un program care citeşte un şir de caractere format
# din litere mici ale alfabetului englez şi elimină din șir toate vocalele.
#
# sentence = 'A long sentence'.lower()
# new_sentence = ''
# for i in sentence:
#     if i in 'aeiou':
#         continue
#     else:
#         new_sentence += i
# print(new_sentence)

# Să se scrie un program care citește un șir de caractere și afișează litera mică cel mai des întâlnită în șir.
# sentence = 'Alina este intr-un pom'.lower()
# freq = {}
# for i in sentence:
#     if i in freq:
#         freq[i] += 1
#     elif i not in freq and i.isalpha():
#         freq[i] = 1
# max_letter = -1
# for i in freq:
#     if freq[i] > max_letter:
#         max_letter = freq[i]
#         letter = i
# print(freq)
# print(letter, max_letter)


# ordonate in functie de lungimea cuvantului
# sentence = 'ana nu artaae m'
# new_sentence = ' '.join(sorted(sentence.split(' '), key=len))
# print(new_sentence)


import random

# secret_number = random.randint(1,40)
# print("I am thinking about a number between 1 and 40")
# for guess_taken in range(1,6):
#     print('Take a guess')
#     guess = int(input())
#     if guess == secret_number:
#         break
#     elif guess < secret_number:
#         print('Number too low')
#     elif guess > secret_number:
#         print('number too high')
# if guess == secret_number:
#     print(f'Congratz!!! This was the number that I was thinking of! You took {guess_taken} times to guess it')
# else:
#     print(f'zanen. Try again next time. The number was {secret_number}')


# Să se scrie o funcție C++ care să returneze pentru un număr
# natural n transmis ca parametru valoarea lui n!, adică 1•2•...•n.
# def multiply(num):
#     result = 1
#     for i in range(1, num+1):
#         result *= i
#     return result
# print(multiply(4))


# Să se scrie o funcție C++ care să returneze suma cifrelor unui număr natural transmis ca parametru.

# def sum(num):
#     result = 1
#     for i in num:
#         aux = num % 10

# def sum(number):
#     total = 0
#     for num in range(len(str(number))):
#         last_digit = number % 10
#         total += last_digit
#         number //= 10
#     return total
# print(sum(123))


# number = 2345
# total = 0
# for num in range(len(str(number))):
#     last_digit = number % 10
#     total += last_digit
#     number //= 10
# print(total)

# Se dau 2 șiruri de caractere. Sa se afișeze toate caracterele primului șir ce se găsesc și în al doilea.

# len1 = int(input('1st row numbers'))
# len2 = int(input('2st row numbers'))
# nums_1 = []
# nums_2 = []
# new_arr = []
#
# while len1 > 0:
#     nums_1.append(int(input('1st row')))
#     len1 -= 1
# while len2 > 0:
#     nums_2.append(int(input('2st row')))
#     len2 -= 1
# is_common = False
# for i in nums_1:
#     if i in nums_2:
#         is_common = True
#         if is_common:
#             print(i)

# Se dă un șir de caractere ce conține doar litere mici ale alfabetului englez. Să se afișeze cel mai lung subșir.

# arr = ['dan', 'repede', 'se stieweeee', 'sssss']
# max_num = -1
# for i in arr:
#     if len(i) > max_num:
#         max_num = len(i)
#         longest_row = i
# print(longest_row)

# Să se scrie un program care citeşte de la tastatură un număr natural cu exact
# trei cifre și determină suma cifrelor sale.
# def sum(num):
#     if num < 100:
#         return 'mic'
#     if num > 999:
#         return 'mare'
#     len_num = len(str(num))
#     sum = 0
#     while len_num > 0:
#         last_digit = num % 10
#         sum += last_digit
#         num //= 10
#         len_num -= 1
#     return sum
#
# print(sum(999))

# Se citesc de la tastatură n numere naturale.
# Să se determine numarul de numere prime formate din ultimele 2 cifre ale fiecarui număr.

# def is_prime_num(x):
#     is_prime = True
#     for i in range(2, x//2 + 1):
#         if x % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print('is a prime number')
#     else:
#         print('not a prime number')
#
# is_prime_num(13)


# Să se scrie un program care să determine suma cifrelor unui număr natural citit de la tastatură.
# def sum(num):
#     total = 0
#     while num > 0:
#         last_digit = num % 10
#         total += last_digit
#         num = num // 10
#     return total
#
# print(sum(234))


# Se citește un număr natural n. Să se determine suma divizorilor săi.
# def sum_divisibility(num):
#     total = 0
#     for i in range(1, num//2 +1):
#         if num % i == 0:
#             total += i
#     return total+num
#
# print(sum_divisibility(9))

# Se citesc de la tastatură n numere naturale.
# # Să se determine numarul de numere prime formate din ultimele 2 cifre ale fiecarui număr.
# def primes():
#     count = 0
#     is_prime = True
#     n = int(input('how many prime numbers ?'))
#     while n > 0:
#         num = int(input('enter a number:'))
#         last_two_digits = num % 100
#         for i in range(2, last_two_digits//2 + 1):
#             if last_two_digits % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             count += 1
#             print(count)
#         n = n - 1
#     return count
# primes()

# Se citește un vector cu n elemente, numere naturale.
# Să se afișeze elementele din vector care sunt multipli ai ultimului element.

# arr = []
# n = int(input('How many numbers ?'))
# while n > 0:
#     num = int(input('Enter a number:'))
#     arr.append(num)
#     n -= 1
# for i in range(0, len(arr)-1):
#     if arr[i] % arr[-1] == 0:
#         print(arr[i])


# Să se insereze într-un șir după fiecare element par dublul său.
# def double():
#     arr = [1,2,3,4,5,6]
#     new_arr = []
#     for num in arr:
#         if num % 2 == 0:
#             new_arr.append(num * 2)
#         else:
#             new_arr.append(num)
#     return new_arr
# print(double())

# Se dă un şir cu n elemente, numere naturale. Să se verifice dacă toate elementele şirului sunt pare.

# def all_even():
#     is_even = True
#     arr = []
#     int(input('Enter a number: (press \'Q\' to quit)\n'))
#     while True:
#         num = input('Enter a number: press \'Q\' to quit\n')
#         arr.append(num)
#         if num == 'Q' or num == 'q':
#             is_even = False
#             break
#     if is_even:
#         print('All even')
#     else:
#         print('Not even')
# all_even()


# Se citește un șir cu n elemente, numere întregi.
# Să se șteargă elementele care se repetă, păstrându-se doar primul de la stânga la dreapta.

# def no_repeat_numbers():
#     arr = []
#     while True:
#         num = input('Enter a number: (press \'q\' to quit.)\n')
#         if num == 'Q' or num == 'q':
#             break
#         if num in arr:
#             continue
#         else:
#             arr.append(num)
#     return arr
# print(no_repeat_numbers())


# Se dă un vector cu n elemente numere naturale. Să se verifice dacă toate elementele vectorului sunt egale.
# def check_if_equal():
#     arr = []
#     is_in_array = True
#     n = int(input('How many numbers ?\n'))
#     while n > 0:
#         num = int(input('Enter a number:\n'))
#         arr.append(num)
#         if num != arr[0]:
#             is_in_array = False
#             break
#         n -= 1
#     if is_in_array:
#         print('All numbers equal')
#     else:
#         print('Not equal')
# check_if_equal()

# Ascending numbers.
# def ascending():
#     arr = [3,5,2,1]
#     new_arr = []
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 temp = arr[j]
#                 arr[j] = arr[i]
#                 arr[i] = temp
#     return arr
# print(ascending())

# Să se scrie un program care citeşte un şir de caractere format din litere mici ale alfabetului englez şi
# înlocuieşte fiecare vocală cu litera mare corespunzătoare.

# sentence = input('Enter a sentence:\n').lower()
# # new_sentence = ''
# # for string in sentence:
# #     if string in 'aeiou':
# #         new_sentence += string.upper()
# #     else:
# #         new_sentence += string
# # print(new_sentence)

# Să se scrie un program care citeşte de la tastatură o propoziţie formată din mai multe cuvinte
# separate prin spaţii şi transformă prima şi ultima literă a fiecărui cuvânt în literă mare.

# word = input('Enter a sentence:\n').title()
# new_word = ''
# for i in range(len(word)-1):
#     if not word[i+1].isalpha() and word[i].isalpha():
#         new_word += word[i].upper()
#     else:
#         new_word += word[i]
# new_word += word[-1].upper()
# print(new_word)


# Se dă o propoziție formată din litere mari și mici ale alfabetului englez,
# cifre, spații și semne de punctuație, în care literele mari și mici se consideră identice.
# Determinați vocala din șir cu număr maxim de apariții.
# word = input('Insert a sentence: \n').lower()
# freq = {}
# for i in word:
#     if i in 'aeiou' or i in 'AEIOU':
#         if i in freq:
#             freq[i] += 1
#         elif i not in freq and i.isalpha():
#             freq[i] = 1
# max_num = -1
# for i in freq:
#     if freq[i] > max_num:
#         max_num = freq[i]
#         key = i
# print(key, max_num)


# Să se scrie un program care citește un cuvânt și îl afișează după interschimbarea primei vocale cu ultima consoană.
# word = 'malai'
# new_word = ''
# for i in word:
#     if i in 'aeiou':
#         vowel = i
#         break
# for i in reversed(range(len(word))):
#     if word[i] not in 'aeiou':
#         consonate = word[i]
#         break
# print(vowel, consonate)

# Să se scrie un program care citește un text și inserează după fiecare vocală caracterul *.
# def insert_after_vowel(word):
#     new_word = ''
#     for i in word:
#         new_word += i
#         if i in 'aeiou' or i in 'AEIOU':
#             new_word += '*'
#     return new_word
# print(insert_after_vowel('saorma'))

# Să se scrie un program care citește mai multe propoziții și determină propoziția cu cele mai multe vocale
# def vowels_number():
#     max_vowels = -1
#     while True:
#         count = 0
#         word = input('Enter a sentence: Press \'q\' to quit\n')
#         if word == 'q' or word == 'Q':
#             break
#         for i in word:
#             if i in 'aeiou' or i in 'AEIOU':
#                 count += 1
#                 if count > max_vowels:
#                     max_vowels = count
#                     current_sentence = word
#     return current_sentence, max_vowels
# print(vowels_number())

# Să se scrie un program care citeşte un şir de caractere format din litere mici ale alfabetului englez
# şi elimină din șir toate vocalele.

# def remove_vowels(word):
#     new_word = ''
#     for i in word.lower():
#         if i in 'aeiou':
#             continue
#         else:
#             new_word += i
#     return new_word
# print(remove_vowels('gigel'))

# ---------------------------------------------------------
# f = open(r'C:\Users\Admin\Desktop\nou.txt','w+')


# with open('project.txt','r') as f:
#     count = 0
#     for line in f.readlines():
#         count += 1
#         print(f'{count}. {line}')
# ----------------------------------------------------------

# Să se scrie o funcție C++ care să returneze oglinditul unui număr natural transmis ca parametru.
# def reverse_number(number):
#     reverse_number = 0
#     while number > 0:
#         last_digit = number % 10
#         reverse_number = reverse_number * 10 + last_digit
#         number = number // 10
#     return reverse_number
# print(reverse_number(12345))


# REPLACE MULTIPLE LETTERS IN A WORD WITH REPLACE------------------
# string = 'aabbccddee'
# not_allowed = 'ad'
# for i in not_allowed:
#     string = string.replace(i, '*')
#     print(string)
# ------------------------------------------------------------------

# Să se scrie o funcție C++ care să returneze cel mai mic număr care se poate scrie cu
# cifrele unui număr natural transmis ca parametru.
# n = 4214
# new_num = ''.join(sorted(str(n)))
# print(new_num)
#
# def read_document():
#     with open('input.txt', 'r') as f:
#         text = f.read()
#         return text
#
# def transform_in_list(text):
#     return text.split("\n")
#
#
# def join_function(text_list):
#     new_text = '%'.join(text_list)
#     return new_text
#
# #
# def write_in_document(text):
#     with open('myfile.txt', 'w') as f:
#         x = f.write(text)
#     return x
#
# def main():
#     read_result = read_document()
#     proccesed_text = join_function(transform_in_list(read_result))
#     write_in_document(proccesed_text)
#
# main()

# import random
#
#
#  def generate_random_number(start, stop):
#      num1 = random.randint(start, stop)
#      num2 = random.randint(start, stop)
#      return num1, num2

# a, b = generate_random_number(2, 10)
# print(a, b)

# 1. 2 numere random
# 2. verifica daca suma e buna 2 numere, 1 rezultat
# 3. main


# import random
# def random_numbers(start, stop):
#     num1 = random.randint(start, stop)
#     num2 = random.randint(start, stop)
#     return num1, num2
#
# def check_sum(start, stop):
#     num1,num2 = random_numbers(start,stop)
#     result = num1 + num2
#     guess = int(input(f'Enter the sum for {num1} + {num2}:\n'))
#     if guess == result:
#         print('You guessed the sum')
#     else:
#         print('You didn\'t guess the sum')
#         print(f'The Sum was: {result}')
#
# check_sum(1,20)

# Să se scrie o funcție C++ recursivă care returnează cel mai
# mare divizor comun a două numere transmise ca parametri.

# def highest_divisor(num1, num2):
#     if num1 > num2:
#         smallest = num2
#     else:
#         smallest = num1
#     for i in range(1, smallest+1):
#         if num1 % i == 0 and num2 % i == 0:
#             result = i
#     return result
# print(highest_divisor(8, 12))


# C++ recursivă care să returneze suma cifrelor unui număr natural transmis ca parametru.

#
# def sum(n):
# #     if n == 0:
# #         return 0
# #     return n % 10 + sum(n // 10)
# # print(sum(123))


# Să se scrie o funcție C++ recursivă care să returneze cifra maximă a unui număr natural transmis ca parametru.

# def highest_digit(x):
#     if x == 0:
#         return 0
#     return max(x % 10,highest_digit(x // 10))
#
# print(highest_digit(25241))

# Să se scrie o funcție C++ recursivă care să returneze numărul de cifre egale cu zero
# ale unui număr natural transmis ca parametru.

# def check_if_0(n, count = 0):
#     if n == 0:
#         return count
#     last_digit = n % 10
#     if last_digit == 0:
#         count += 1
#     return count, check_if_0(n // 10)
#
# print(check_if_0(209))

# def solution(string, ending):
#     if len(ending) > len(string):
#         return False
#     reversed_string = ''
#     for i in reversed(string):
#         reversed_string += i
#     for i in ending:
#         if i not in ending:
#             print(i)
#             return False
#     return True
# a = 'sumo'
# b = 'omo'
# is_True = True
# reversed_string = ''
# for i in reversed(a):
#     reversed_string += i
# for i in range(0, len(b)):
#     if b[i] != a[i]:
#         is_True = False
#         break
# if is_True:
#     print('true')
# else:
#     print('false')

# def vaporcode(s):
#     new_s = ''
#     for i in s.split():
#         print(i)
#     print(len(new_s))
#     return new_s
# print(vaporcode('mihai'))


# SORT SORTED BUBBLE JJJJ
# arr = [7,6,4,1,4]
# swapped = True
# while swapped:
#     swapped = False
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp
#             swapped = True


# def is_isogram(string):
#     for i in range(len(string)-1):
#         if string[i] == string[i+1]:
#             print(i)
#             return False
#     return True
#
# print(is_isogram('qfylmnvtnbvfaielzlqpukrsu'))
s = 'ALINA'
print(f'Hello {s.title()}')











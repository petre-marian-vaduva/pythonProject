# Create the function consecutive(arr) that takes an array of integers and
# return the minimum number of integers needed to make the contents of arr consecutive
# from the lowest number to the highest number.
# For example:
# If arr contains [4, 8, 6] then the output should be 2 because
# two numbers need to be added to the array (5 and 7) to make it a
# consecutive array of numbers from 4 to 8. Numbers in arr will be unique.

# def consecutive(arr):
#     if len(arr) <= 1:
#         return 0
#     count = 0
#     min_num = arr[0]
#     max_num = arr[0]
#     for i in arr:
#         if i > max_num:
#             max_num = i
#         if i < min_num:
#             min_num = i
#     new_arr = []
#     for i in range(min_num, max_num+1):
#         new_arr.append(i)
#     for i in new_arr:
#         if i not in arr:
#             count += 1
#     return count

# Challenge:
#
# Given a two-dimensional array, return a new array which carries over only those arrays from the original,
# which were not empty and whose items are all of the same type (i.e. homogenous).
# For simplicity, the arrays inside the array will only contain characters and integers.
# Example:
#
# Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].
#
# Please keep in mind that for this kata, we assume that empty arrays are not homogenous.
#
# The resultant arrays should be in the order they were originally in and should not have its values changed.

# No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.

# def filter_homogenous(arrays):
#     new_arr = []
#     for i in arrays:
#         if not i:
#             continue
#         else:
#             is_int = True
#             is_str = True
#             for j in i:
#                 if type(j) != int:
#                     is_int = False
#                 elif type(j) != str:
#                     is_str = False
#             if is_int or is_str:
#                 new_arr.append(i)
#     return new_arr

# Kate likes to count words in text blocks. By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:
#
# Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp. contains "words" ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']
#
# Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.
#
# Today Kate's too lazy and have decided to teach her computer to count "words" for her.
#
# Example Input 1
# Hello there, little user5453 374 ())$.
#
# Example Output 1
# 4
#
# Example Input 2
# I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.
#
# Example Output 2
# 112

# def word_count(s):
#     r = s.lower()
#     for c in r:
#         if c not in 'abcdefghijklmnopqrstuvwxyz': r=r.replace(c, ' ')
#     r = sum(bool(w) for w in r.split() if w not in  ["a", "the", "on", "at", "of", "upon", "in", "as"])
#     return r


# You are doing an excercise for chess class.
#
# Your job given a bishop's start position (pos1 / startPos) find if the end position (pos2 / endPos) given is possible within n moves.
#
# INPUT :
# startPos (1st param) ==> The position at which bishop is at
# endPos   (2nd param) ==> The position at which he is supposed to end at
# number   (3rd param) ==> The number of moves allowed to bishop to move to said position
# BOARD :
# 8 |_|#|_|#|_|#|_|#|
# 7 |#|_|#|_|#|_|#|_|
# 6 |_|#|_|#|_|#|_|#|
# 5 |#|_|#|_|#|_|#|_|
# 4 |_|#|_|#|_|#|_|#|
# 3 |#|_|#|_|#|_|#|_|
# 2 |_|#|_|#|_|#|_|#|
# 1 |#|_|#|_|#|_|#|_|
#    a b c d e f g h
# The board is a 8 x 8 board goes from a1 to h8
#
# BISHOP MOVEMENT :
# The bishop chess piece moves in any direction diagonally. Chess rules state that there is no limit to the number of squares a bishop can travel on the chessboard, as long as there is not another piece obstructing its path. Bishops capture opposing pieces by landing on the square occupied by an enemy piece.
#
# OUTPUT :
# Find out whether within n moves he can move from start pos to end pos. If he can return true, if not return false
#
# NOTES :
# Return true if start and end position are same; even if number of moves is 0
# Both start and end positions will always be valid (so within a1 ---> h8)
# Input positions will always follow this pattern : f1 (i.e : Char(representing one of a-h)Number(represnting one of 1-8) on chess board)
# The alphabet will always be lowercase followed immediately by number no space.
# For our purpose, chess board is always empty, i.e: the bishop is the only one that can be played.
# The number of moves n will always be whole number i.e : 0 or greater.
# Your bishop may only move using its predefined moment method (it may not act like a queen or knight).


# def bishop(p1, p2, move):
#     ChessRow = ["a", "b", "c", "d", "e", "f", "g", "h"]
#     ChessCol = ['1', '2', '3', '4', '5', '6', '7', '8']
#     x1 = 0
#     y1 = 0
#     result = []
#     nummove = 0
#     for pos in p1:
#         if pos in ChessRow:
#             x1 = ChessRow.index(pos) + 1
#         else:
#             y1 = ChessCol.index(pos) + 1
#     for pos in p2:
#         if pos in ChessRow:
#             x2 = ChessRow.index(pos) + 1
#         else:
#             y2 = ChessCol.index(pos) + 1
#     if move == 1:
#         nummove += 1
#         if x1 == y1 and x2 == y2:
#             nummove -= 1
#             if int(x1 + y1) % 2 == 0 and int(x2 + y2) % 2 == 0:
#                 if x1 + y1 != x2 + y2:
#                     if abs(x2 - x1) == 1:
#                         nummove -= 1
#                     else:
#                         pass
#                 else:
#                     pass
#         if int(x1 + y1) % 2 == 0 and int(x2 + y2) % 2 == 0:
#             if x1 + y1 != x2 + y2:
#                 nummove += 1
#             else:
#                 pass
#
#     if move > 0:
#         for r in range(move):
#             if x1 == y1 and x2 == y2:
#                 nummove -= 1
#             if x1 + y1 == x2 + y2:
#                 pass
#             if int(x1 + y1) % 2 == 0 and int(x2 + y2) % 2 == 0:
#                 if x1 + y1 != x2 + y2:
#                     nummove += 1
#                 else:
#                     pass
#             if int(x1 + y1) % 2 == 1 and int(x2 + y2) % 2 == 1:
#                 if x1 + y1 != x2 + y2:
#                     nummove += 1
#                 else:
#                     pass
#             if int((x1 + y1) - (x2 + y2)) % 2 != 0:
#                 nummove = int(move) + 1
#     elif move == 0:
#         if x1 == x2 and y1 == y2:
#             pass
#         else:
#             nummove = 100
#     return bool(nummove <= move)


# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y

#student name, age, grade
#get_grade
#Course name, max_students
#add_student student
# get_average_grade

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
# s1 = Student('Tim', 18, 80)
# s2 = Student('Bob', 18, 190)
# s3 = Student('Tech', 20, 40)
#
# course = Course('Geography', 2)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# print(course.get_average_grade())

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f'I am {self.name} and I am {self.age} years old')
#
#     def speak(self):
#         print('I don\'t know what to say')
#
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color


# arr = [i for i in range(10) if i % 2 == 1]
# arr2 = [(i, y) for i in range(10) for y in range(20)]
# arr3 = [['a' for i in range(10)] for i in range(10)]

#
# The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
#
# A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).
#
# We will write a function gap with parameters:
#
# g (integer >= 2) which indicates the gap we are looking for
#
# m (integer > 2) which gives the start of the search (m inclusive)
#
# n (integer >= m) which gives the end of the search (n inclusive)
#
# n won't go beyond 1100000.
#
# In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
#
# So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise `nil or null or None or Nothing (or ... depending on the language).
#
# In C++, Lua: return in such a case {0, 0}. In F#: return [||]. In Kotlin, Dart and Prolog: return []. In Pascal: return Type TGap (0, 0).
#
# Examples:
# gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}
#
# gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return []`
#
# gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}
#
# ([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)
#
# gap(6,100,110) --> nil or {0, 0} or ... : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.


# def gap(g, m, n):
#     """Returns first prime gap of gap g between m, n, if it exits, None otherwise."""
#     last_prime = n + 1
#     for i in range(m, n + 1):
#         if is_prime(i):
#             if i - last_prime == g:
#                 return [last_prime, i]
#             last_prime = i
#     return None
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0 and i < n:
#             return False
#     return True

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros

# def find_factor(p, n):
#     """Find how many times the prime number p divides n!"""
#     result, power = 0, p
#     while power < n:
#         result += n // power
#         power *= p
#     return result
#
# def zeros(n):
#     """Find the number of trailing zeroes in n!."""
#     return min(find_factor(p, n) for p in (2, 5))

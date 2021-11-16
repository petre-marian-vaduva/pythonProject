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


# Definition
# Balanced number is the number that * The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal*.
#
# Task
# Given a number, Find if it is Balanced or not .
#
# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0
#
# The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g 413023 is a balanced number because the left sum and right sum are both 5.
#
# Number passed is always Positive .
#
# Return the result as String

# first try
# def balanced_num(number):
#     number = [int(n) for n in str(number)]
#     left, right = 0, 0
#
#     while len(number) > 2:
#         left += number.pop(0)
#         right += number.pop(-1)
#
#     return "Balanced" if left == right else "Not Balanced"

# second try
# def balanced_num(n):
#     q = str(n)
#     m = (len(q)//2)
#     suml = 0
#     sumr = 0
#     if len(q)<=2:
#         return "Balanced"
#     else:
#         if len(q)%2 == 0:
#             l = q[:m-1]
#             r = q[m+1:]
#             for x in l:
#                 suml += int(x)
#             for x in r:
#                 sumr += int(x)
#             if suml == sumr:
#                 return "Balanced"
#             else:
#                 return "Not Balanced"
#         elif len(q)%2 != 0:
#             l = q[:m]
#             r = q[m+1:]
#             for x in l:
#                 suml += int(x)
#             for x in r:
#                 sumr += int(x)
#             if suml == sumr:
#                 return "Balanced"
#             else:
#                 return "Not Balanced"


# This
# kata
# concerns
# stochastic
# processes
# which
# often
# have
# to
# be
# repeated
# many
# times.We
# want
# to
# be
# able
# to
# randomly
# sample
# a
# long
# list
# of
# weighted
# outcomes
# quickly.
#
# For
# instance,
# with weights[
#     3, 1, 0, 1, 5], it's expected that index 4 occur 50% of the time, on average, and that index 2, with no weight, never occur.
#
# The
# issue is that
# the
# naive
# method
# for selecting an index randomly has time complexity on the order of O(n).If the number of weights is very large, this could be a bottleneck in simulation.
#
# The
# fastest
# method
# for this process is contant time, on order O(1), assuming random values are O(1) too.It involves making at most one comparison and two random calls in the sampling routine, as demonstrated below:
#
#
# class Distribution:  # preloaded
#
#     def __init__(self, weights):
#         self.weights = list(weights)
#         self.table = make_table(weights)
#
#     def sample(self):
#         index = random.randrange(len(self.weights))
#         probability, alias = self.table[index]
#         numerator, denominator = probability
#         chance = random.randrange(denominator)
#         if chance < numerator:
#             return index
#         else:
#             return alias
#
#
# def make_table(weights):  # solution
#     return [
#         ((1, 1), None),
#         ((1, 2), 4),
#         ((0, 1), 4),
#         ((1, 2), 0),
#         ((1, 1), None)
#     ]
#
#
# example = Distribution([3, 1, 0, 1, 5])  # test
# The
# solution
# above
# for the make_table pre-processing step is incomplete since it's hard-coded and entirely ignores its argument weights. You can verify that the hard-coded solution works for this one example, though.
#
# Your
# task is to
# implement
# this
# function
# make_table
# so
# that
# its
# return value
# respects
# the
# input and can
# be
# used
# by
# the
# Distribution
#
#
# class as written.To be clear, only revisions to make_table are within the scope of the problem.
#
#
# In
# other
# words, given
# a
# list
# of
# integer
# weights, create
# a
# table
# so
# that
# the
# odds
# of
# the
# sample
# method
# returning
# each
# index
# will
# correspond
# with the index's weight.
#
# Note
# how
# the
# sample
# method
# works
# with the example solution.With probability 0 / 1, it never allows index 2 to be returned, substituting alias 4 instead.4 is also substituted 1 / 2 the time index 1 is selected, and 0 is substituted 1 / 2 the time index 3 is selected.The overall odds align perfectly.
#
# When
# make_table is passed
# an
# arbitrary
# list
# of
# weights, can
# your
# code
# construct
# a
# similarly
# clever
# table? It
# should, and then
# the
# sample
# method is already
# written
# to
# be
# O(1) in randomly
# sampling
# it.
#
# To
# pass
# the
# largest
# tests
# with over a thousand weights, your solution should run in O(n) time for this pre-processing step.The result should be exact and also minimal ideally, meaning that probabilites from 0 to 1 are reduced to lowest terms.You're welcome to substitute any integer value for None, whose only purpose above is as an unused placeholder.

#
# def make_table(weights):
#     import math
#     s = sum(weights)
#     l = len(weights)
#     w = [l * x for x in weights]  # Now weights sum up to s*l
#     table = [None] * l
#
#     receivers = [x[0] for x in enumerate(w) if x[1] > s]
#     givers = [x[0] for x in enumerate(w) if x[1] <= s]
#     recweight = s
#
#     def receive(a):
#         nonlocal recweight
#         nonlocal receivers
#         nonlocal table
#         recweight += a
#         excess = recweight - w[receivers[-1]]
#
#         if excess == 0:
#             table[receivers[-1]] = ((1, 1), None)
#             recweight = s
#             _ = receivers.pop()
#         elif excess > 0:
#             gcd = math.gcd(s - excess, s)
#             table[receivers[-1]] = (((s - excess) // gcd, s // gcd), receivers[-2])
#             recweight = s
#             _ = receivers.pop()
#             receive(excess)
#
#     for giver in givers:
#         excess = s - w[giver]
#
#         if excess == 0:
#             table[giver] = ((1, 1), None)
#         elif excess > 0:
#             gcd = math.gcd(s - excess, s)
#             table[giver] = (((s - excess) // gcd, s // gcd), receivers[-1])
#             receive(excess)
#     return table

# We want to create a function that will add numbers together when called in succession.
#
# add(1)(2);
# // returns 3
# We also want to be able to continue to add numbers to our chain.
#
# add(1)(2)(3); // 6
# add(1)(2)(3)(4); // 10
# add(1)(2)(3)(4)(5); // 15
# and so on.
#
# A single call should return the number passed in.
#
# add(1); // 1
# We should be able to store the returned values and reuse them.
#
# var addTwo = add(2);
# addTwo; // 2
# addTwo + 5; // 7
# addTwo(3); // 5
# addTwo(3)(5); // 10
#
# def add(n):
#     return MyInt(n)
#
#
# class MyInt(object):
#     def __init__(self, n):
#         self.value = n
#
#     def __add__(self, n):
#         return MyInt(self.value + n)
#
#     def __sub__(self, n):
#         return MyInt(self.value - n)
#
#     def __call__(self, n):
#         return MyInt(self.value + n)
#
#     def __eq__(self, other):
#         if isinstance(other, MyInt):
#             return self.value == other.value
#         else:
#             return self.value == other

# You must organize contest, that contains two part, knockout and round-robin.
#
# Part 1
# Knockout part goes until we get an odd number of players. In each round players are paired up; each pair plays a game with the winning player advancing to the next round (no ties). This part continues as long as number of players is even. When we come to round with are an odd number of players we go to part 2.
#
# Part 1 will be skipped, if starting quantity of players is odd
# If Part 1 ends with 1 player then contest is considered over, we have a winner
# Part 2
# Round-robin. Each participant plays every other participant once. The player with the most points is the winner.
#
# How many players you must invite to participate in the contest for got N games to be played?
#
# Input/Output
# [input] integer n
#
# A positive number
#
# 1 ≤ n ≤ 10^9
#
# [output] array of Int
#
# Return array of all possible amounts of players. Array can be empty if requested number of games cannot be achieved by any one amount of players. Array must be sorted by ASC.
#
# If this kata is too easy, you can try much harder version.
#
# Examples
# 3 games
#
# We can invite 3 players. In this case part 1 will be skipped and contest start with part 2, where 3 games will played.
# Or we can invite 4 players, then part 1 will be made with 3 games. 2 semi-finals, final and we got a winner. Part 2 need no to be played, because we got 1 player only (winner of part 1).
# 12 games
#
# We must invite 12 players. Contest start with Part 1, where will be played 6 + 3 games, than 3 more games will be played in Part 2. So the got 6 + 3 + 3 = 12 games.



# import math
#
#
# def find_player_counts(n):
#     res = []
#     u = 1
#     while u * (u - 1) // 2 <= n:
#         v = n - u * (u - 1) // 2  # = u * (2 * x - 1)
#         if v % u == 0:
#             p = v // u + 1
#             x = math.log2(p)
#             if x == int(x):
#                 res.append(int(u * (2 ** x)))
#         u += 2
#     return sorted(res)

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter casing)

# def is_isogram(string):
#     string = string.lower()
#     for i in range(len(string)):
#         for j in range(i+1, len(string)):
#             if string[i] == string[j]:
#                 return False
#     return True

# Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.
#
# For example:
# solve("abc") = True, because it contains a,b,c
# solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
# solve("dabc") = True, because it contains a, b, c, d
# solve("abbc") = False, because b does not occur once.
# solve("v") = True

# from string import ascii_lowercase
# def solve(st):
#     return ''.join(sorted(st.lower())) in ascii_lowercase


# Move all exclamation marks to the end of the sentence
#
# Examples
# remove("Hi!") === "Hi!"
# remove("Hi! Hi!") === "Hi Hi!!"
# remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
# remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
# remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"

# def remove(s):
#     new_s = ''
#     count = 0
#     for char in s:
#         if char == '!':
#             count += 1
#             continue
#         else:
#             new_s += char
#     for i in range(count):
#         new_s += '!'
#     return new_s



# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
#
# Write a function which takes a list of strings and returns each line prepended by the correct number.
#
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
#
# Examples:
#
# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

# def number(lines):
#     lst = []
#     for i in range(len(lines)):
#         lst.append(f'{i+1}: {lines[i]}')
#     return lst

# Remove all exclamation marks from sentence except at the end.
#
# Examples
# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"
#
# def remove(s):
#     new_s = ''
#     for char in s:
#         if char != '!':
#             new_s += char
#         else:
#             continue
#     for char in reversed(s):
#         if char == '!':
#             new_s += char
#         else:
#             break
#     return new_s
#
# print(remove('!Hi'))


# Given an array of digitals numbers, return a new array of length number containing the last even numbers from the original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.
#
# For example:
#
# ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
# ([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
# ([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]
#
# def even_numbers(arr,n):
#     new_arr = []
#     for num in reversed(arr):
#         if num % 2 == 0:
#             new_arr.append(num)
#         if len(new_arr) == n:
#             break
#     return list(reversed(new_arr))

# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.
#
# def find_short(s):
#     l = 9999999
#     for word in s.split():
#         count = 0
#         for letter in word:
#             count += 1
#         if l > count:
#             l = count
#     return l





# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
#
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:
#
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

# def solve(s):
#     count_lower = 0
#     count_upper = 0
#     for char in s:
#         if char.islower():
#             count_lower += 1
#         else:
#             count_upper += 1
#     if count_lower > count_upper or count_lower == count_upper:
#         return s.lower()
#     elif count_upper > count_lower:
#         return s.upper()

# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

# def solve(s):
#     count = 0
#     max_vowels = -1
#     for char in s:
#         if char in 'aeiou':
#             count += 1
#         else:
#             count = 0
#         if count > max_vowels:
#             max_vowels = count
#     return max_vowels

# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.
#
# Example:
#
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

# def greet(name):
#     return f'Hello {name.title()}!'


# magine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.
#
# Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.
#
# // simple examples
# elevatorDistance([5,2,8]) = 9
# elevatorDistance([1,2,3]) = 2
# elevatorDistance([7,1,7,1]) = 18
#
# // if two consecutive floors are the same,
# //distance travelled between them is 0
# elevatorDistance([3,3]) = 0

# def elevator_distance(array):
#     total = 0
#     for i in range(len(array)-1):
#         total += abs(array[i] - array[i+1])
#     return total

# Factorials are often used in probability and are used as an introductory problem for looping constructs. In this kata you will be summing together multiple factorials.
#
# Here are a few examples of factorials:
#
# 4 Factorial = 4! = 4 * 3 * 2 * 1 = 24
#
# 6 Factorial = 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# In this kata you will be given a list of values that you must first find the factorial, and then return their sum.
#
# For example if you are passed the list [4, 6] the equivalent mathematical expression would be 4! + 6! which would equal 744.

# def sum_factorial(lst):
#     total = 0
#     for num in lst:
#         current_total = 1
#         for i in range(1, num +1):
#             current_total *= i
#         total += current_total
#     return total

# Determine if the poker hand is flush, meaning if the five cards are of the same suit.
#
# Your function will be passed a list/array of 5 strings, each representing a poker card in the format "5H" (5 of hearts), meaning the value of the card followed by the initial of its suit (Hearts, Spades, Diamonds or Clubs). No jokers included.
#
# Your function should return true if the hand is a flush, false otherwise.
#
# The possible card values are 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
#
# Examples
# ["AS", "3S", "9S", "KS", "4S"]  ==> true
#
# ["AD", "4S", "7H", "KS", "10S"] ==> false

# def is_flush(cards):
#     last_st = cards[0][-1]
#     for i in range(1, len(cards)):
#         if last_st != cards[i][-1]:
#             return False
#     return True


# Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
#
# Take a look on the test cases.
#
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.
#
# The second value in the first integer array is 0, since the bus is empty in the first bus stop.

# def number(bus_stops):
#     total = 0
#     for passengers in bus_stops:
#         total += passengers[0] - passengers[1]
#     return total

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
#
#
# def move_zeros(array):
#     newarr = []
#     zeroarr = []
#     for item in array:
#         if item != 0 or type(item) == bool:
#             newarr.append(item)
#         else:
#             zeroarr.append(item)
#
#     newarr.extend(zeroarr)
#     return (newarr)


# Description:
# Have a look at the following numbers.
#
#  n | score
# ---+-------
#  1 |  50
#  2 |  150
#  3 |  300
#  4 |  500
#  5 |  750
# Can you find a pattern in it? If so, then write a function getScore(n)/get_score(n)/GetScore(n) which returns the score for any positive number n:
#
# int getScore(1) = return 50;
# int getScore(2) = return 150;
# int getScore(3) = return 300;
# int getScore(4) = return 500;
# int getScore(5) = return 750;


# def get_score(n):
# #     return 50 if n == 1 else get_score(n-1) + 50 * n
#     sum = 0
#     for i in range(1, n + 1):
#         sum += 50 * i
#         print(sum)
#     return(sum)









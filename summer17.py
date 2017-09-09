# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 18:34:27 2017

@author: Asus
"""

#print({chr(65+i) for i in range(6)})

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
#print(mysum([1, 2, 3, 4, 5]))

def sumtree(L):
 tot = 0
 for x in L: # Обход элементов одного уровня
  print(L)
  if not isinstance(x, list):
   tot += x # Числа суммируются непосредственно
  else:
   tot += sumtree(x) # Списки обрабатываются рекурсивными вызовами
 return tot
L = [1, [2, [3,[0,[]], 4], 5], 6, [7, 8]] # Произвольная глубина вложения
#print(sumtree(L)) # Выведет 36
# Патологические случаи
#print(sumtree([1, [2, [3, [4, [5]]]]])) # Выведет 15 (центр тяжести справа)
#print(sumtree([[[[[1], 2], 3], 4], 5])) # Выведет 15 (центр тяжести слева)

def make(label): # Создает функцию, но не вызывает ее
 def echo(message):
  print(label + ':' + message)
 return echo

F = make('Spam') # Метка сохраняется во вложенной области видимости
#F('Ham!') # Вызов функции, созданной функцией make
#F('Eggs!')

from time import *
#print(asctime(gmtime(0))) # начало эпохи

def sum_n(L,n,k): # в степени k
    if not n:
        return 0
    else:
        L = list(range(1,n+1)) # генератор последовательности int
        s = 0
        for i in range(len(L)+1):
            s += i**k
            #print('n = ', i, ':', 's = ', s)
        return s
'''    
t1 = clock()
print(sum_n(L,int(1e+06),3))
t2 = clock()
n = 1e+06
t3 = clock()
print((n*(n+1)/2.)**2) # сумма кубов натурального ряда
t4 = clock()
print('time = ',t2-t1, 'sec')
print('time = ',t4-t3, 'sec')


L = [lambda x: x**2, # Встроенные определения функций
lambda x: x**3,
lambda x: x**4] # Список из трех функций
#for f in L:
# print(f(2)) # Выведет 4, 8, 16
#print(L[0](3)) # Выведет 9

n = int(1e+02)
print((n*(n+1)/2.)**2)
print(sum(map(lambda x, k = 3: x**k, list(range(1,n+1)))))
'''

#print(list(filter(lambda x: x > 0, list(range(-5, 5))))) 

'''
from functools import reduce
print(reduce((lambda x, y: x*y), [2, 2, 3, 4]))
print(reduce((lambda x, y: x**y), [2, 2, 3, 4]))


import operator, functools
# Оператор сложения в виде ф-ции
print(functools.reduce(operator.add, [2, 4, 6])) 


# Генераторы списков
print([x ** 2 for x in range(10)])
print(x ** 2 for x in range(10))
k = 3
n = 10
print(sum([x**k for x in range(1,n+1)]))
print(sum(x**k for x in range(n+1)))

print([x for x in range(5) if x % 2 == 0])
print([x + y for x in [0, 1, 2] for y in [100, 200, 300]])

print([(x, y) for x in range(5) if x % 2 == 0 
       for y in range(5) if y % 2 == 1])

M = [[1, 2, 3],
     [4, 5, 6],
    [7, 8, 9]]

#print([M[i][i] for i in range(len(M))])

N = [[2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]]

print([[M[row][col] * N[row][col] 
        for col in range(3)] for row in range(3)])

print([[M[row][col] * N[col][row] 
        for col in range(3)] for row in range(3)])
'''

data = [1,2,3]
sum1 = 0
for element in data:
    sum1 += element ** 2
#print(sum1)

#print(sum(map(lambda x : x**2, data)))

#print(len([5, 4/0., 3+2])) # not lazy?

'''
def func1():
    return 2, 5, 7

def func2(x,y,z):
    print(x+y+z)

func2(*func1()) # распаковка
'''

#C = (F - 32) / 1.8.
#F = 1.8*C + 32.
import scipy
from scipy.constants import F2C,  C2F
#print(F2C(np.array([-40, 40.0])))
#print(C2F(np.array([20, 40.0])))

from scipy.special import*
#print(scipy.special.binom(5, 3)) 

a = 555
b = 60
n = 110

power_bi = sum(a**(n-k)*b**k*scipy.special.binom(n, k)
                            for k in range(n+1)) 

eps_bi = (a + b)**n - power_bi 
int_eps_bi = int((a + b)**n)-int(power_bi)
#print(int(power_bi), ';' , int((a + b)**n), ';', eps_bi, ';', (555+60)**7, ';', (555+60)**7-int((a + b)**n)) 

#print(abs(int_eps_bi*100)/int((a + b)**n), '%')


# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

message = '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

#print(translated)

#print([translated + message[i] for i in range(len(message) - 1) and i >= 0])#?


# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
#import pyperclip
import copy
# the string to be encrypted/decrypted
#message = 'guv@ v@ z№ @rp$r! zr@@ntr C D1E' #'This is my secret message № 0.1'
message = 'Привет, мир!'
# the encryption/decryption key
key = 13
# tells the program to encrypt or decrypt
mode = 'encrypt' # set to 'encrypt' or 'decrypt'
# every possible symbol that can be encrypted ##?????
LETTERS = 'Ё ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.ёйцукенгшщзхъфывапролджэячсмитьбю,:;$@!&?*/№0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# stores the encrypted/decrypted form of the message
translated = ''
# capitalize the string in message
#message = message.upper()
# run the encryption/decryption code on each symbol in the message string
for symbol in message:
 if symbol in LETTERS:
# get the encrypted (or decrypted) number for this symbol
  num = LETTERS.find(symbol) # get the number of the symbol
  if mode == 'encrypt':
   num = num + key
  elif mode == 'decrypt':
   num = num - key
# handle the wrap-around if num is larger than the length of
# LETTERS or less than 0
  if num >= len(LETTERS):
   num = num - len(LETTERS)
  elif num < 0:
   num = num + len(LETTERS)
# add encrypted/decrypted number's symbol at the end of translated
  translated = translated + LETTERS[num]
 else:
# just add the symbol without encrypting/decrypting
  translated = translated + symbol
# print the encrypted/decrypted string to the screen
#print(translated)
# copy the encrypted/decrypted string to the clipboard
copy.deepcopy(translated)

'''
print('Hello world!'.upper(), '\n'
      'Hello world!'.lower(), '\n'
      'Hello world!'.upper().lower())
'''
#print('hello'.find('e'))


# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message2 = 'Ьб*ир/2Ф?*б7'
# loop through every possible key
for key2 in range(len(LETTERS)):
# It is important to set translated to the blank string so that the
# previous iteration's value for translated is cleared.
    translated2 = ''
# The rest of the program is the same as the original Caesar program:
# run the encryption/decryption code on each symbol in the message
    for symbol2 in message2:
        if symbol2 in LETTERS:
            num = LETTERS.find(symbol2) # get the number of the symbol
            num = num - key2
# handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
# add number's symbol at the end of translated
            translated2 = translated2 + LETTERS[num]
        else:
# just add the symbol without encrypting/decrypting
            ranslated2 = translated2 + symbol2
# display the current key being tested, along with its decryption
    #print('Key #%s: %s' % (key2, translated2))
# Key #13: Привет, мир!

'''
# Transposition Cipher Encryption
# http://inventwithpython.com/hacking (BSD Licensed)

def main():
    myMessage = 'Ещё в 1911 г. английский физик Эрнст Резерфорд высказал идею, что атом - это своего рода миниатюрная модель Солнечной системы'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)

# Print the encrypted string in ciphertext to the screen, with
# a | (called "pipe" character) after it in case there are spaces at
# the end of the encrypted message.
    print(ciphertext + '|')

# Copy the encrypted string in ciphertext to the clipboard.
    copy.deepcopy(ciphertext)

def encryptMessage(key, message):
# Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
# Loop through each column in ciphertext.
    for col in range(key):
        pointer = col
# Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
# Place the character at pointer in message at the end of the
# current column in the ciphertext list.
            ciphertext[col] += message[pointer]
# move pointer over
            pointer += key
# Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)
# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
'''





# Euclid’s GCD algorithm

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#print(gcd(21,46))


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# Primality Testing with the Rabin-Miller Algorithm
# http://inventwithpython.com/hacking (BSD Licensed)
import random

def rabinMiller(num):
# Returns True if num is a prime number.
    s = num - 1
    t = 0
    while s % 2 == 0:
# keep halving s until it is even (and use t
# to count how many times we halve s)
        s = s // 2
        t += 1
    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
    if v != 1: # this test does not apply if v is 1.
        i = 0
        while v != (num - 1):
            if i == t - 1:
                return False
            else:
                i = i + 1
                v = (v ** 2) % num
    return True


def isPrime(num):
# Return True if num is a prime number. This function does a quicker
# prime number check before calling rabinMiller().
    if (num < 2):
        return False # 0, 1, and negative numbers are not prime
# About 1/3 of the time we can quickly determine if num is not prime
# by dividing by the first few dozen prime numbers. This is quicker
# than rabinMiller(), but unlike rabinMiller() is not guaranteed to
# prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
# See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
# If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)


def generateLargePrime(keysize=1024):
# Return a random prime number of keysize bits in size.
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

#print(generateLargePrime())
#print(generateLargePrime(600))
#print(isPrime(90917069662819400398285269776121492945342646090395428367935696290427334511384743232820297913008401422470051982244663278012110935899661888734462911507903985360279430788953421000837928459728032280448956984449965185426001294918152019766169182897584937028921935544281248765235160875477030855926267546952137416989))
#print(isPrime(generateLargePrime()))


#print(pow(2, 8)==2**8)
#print(pow(2, 8, 10)==(2 ** 8) % 10)

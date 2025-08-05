# Function Problem Set 
"""
1. Function to Find Maximum of Three Numbers: Write a Python function that finds the maximum 
of three numbers. 
Sample Input: max_of_three(5, 10, 3)                
Expected Output: 10 
"""
def max_of_three(a,b,c):
    return max (a,b,c)
print(max_of_three(5,10,3))

#
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(5,10,3))
"""
2. Function to Sum Numbers in a List: Write a Python function that sums all the numbers in a list. 
Sample Input: sum_list([8, 2, 3, 0, 7])                
Expected Output: 20 
"""
def sum_list(list1):
    return sum(list1)

print(sum_list([8, 2, 3, 0, 7]))

"""
3. Function to Multiply Numbers in a List: Write a Python function that multiplies all the numbers 
in a list. 
Sample Input: multiply_list([8, 2, 3, -1, 7])               
Expected Output: -336 
"""
def multiply_list(mylist):
    count=1
    for num in mylist:
        count *= num
    return count

print(multiply_list([8, 2, 3, -1, 7]))

"""
4. Program to Reverse a String: Write a Python program that reverses a given string. 
Sample Input: "1234abcd"                
Expected Output: "dcba4321" 
"""
def reverse_string (text):
    result = text[::-1]
    return result
print(reverse_string("1234abcd"))

"""
5. Function  to  Calculate  Factorial:  Write  a  Python  function  to  calculate  the  factorial  of  a  non-
negative integer and return the factorial value. 
Sample Input: factorial(5)               
Expected Output: 120 
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
6. Function  to  Check  Number  within  Range:  Write  a  Python  function  that  checks  whether  a 
number falls within a given range. 
Sample Input: in_range(5, 1, 10)                
Expected Output: True 
"""


"""
7. Function  to  Count  Upper  and  Lower  Case  Characters:  Write  a  Python  function  that  accepts  a 
string and counts the number of upper and lower case letters. 
Sample Input: count_case('The quick Brow Fox')  
Expected Output: No. of Upper case characters: 3, No. of Lower case characters: 12 
"""


"""
8. Function  to Return  Unique  Elements  from  a List:  Write  a  Python  function  that  takes  a  list  and 
returns a new list with distinct elements from the first list. 
Sample Input: unique_elements([1, 2, 3, 3, 3, 3, 4, 5])                
Expected Output: [1, 2, 3, 4, 5] 
"""
              
"""
9. Function to Check Prime Number: Write a Python function that takes a number as a parameter 
and checks whether the number is prime or not. 
Sample Input: is_prime(7)                
Expected Output: True 
"""



"""10.  Program to Print Even Numbers from a List: Write a Python program to print the even numbers 
from a given list. 
Sample Input: even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])               
Expected Output: [2, 4, 6, 8] """


"""
11.  Function  to  Check  Perfect  Number:  Write  a  Python  function  to  check  whether  a  number  is 
"Perfect" or not. 
Sample Input: is_perfect(28)               
Expected Output: True 
"""


"""12.  Function to Check Palindrome: Write a Python function that checks whether a passed string is a 
palindrome or not. 
Sample Input: is_palindrome("madam")                
Expected Output: True  """





"""
Write  a  Python  function  that  takes  two  arguments:  a  sentence  and  a  substring.  The  function 
should count and return the number of words in the sentence that contain the given substring. 
Sample Input
sentence = "That object should not place at that direction.”
substring = "at" 

output
3
"""
def count_substring(sentence, substring):
    count = 0
    list_words = sentence.split()
    for word in list_words:
        if substring.lower() in word.lower():
            count += 1
    return count

sentence = "That object should not place at that direction."
substring = "at"
result = count_substring(sentence, substring)
print(result)








# Find the output of the following code: 
x = 10

def first_func():
    return x**2

def second_func(arg1, arg2, *arg):
    y = 20
    global x
    x = first_func()      # calls first_func(), which returns x**2
    print(x)
    x += arg1
    y += arg2
    for a in arg:
        print(a)
        x += a
    return y

result = second_func(5, 10, 15, 20)
print(x)
print(result)


# 1. Find the output of the following question : [10]

x = 10  

def func1(): 
    global x     
    x += 10     
    print(f"In func1: {x}") 

    if x % 2 == 0:         
        result = func2(x)         
        print(f"In func1 (if part): {result}")     
    else:         
        print(f"In func1 (else part): {x}")         
        x += 5 

def func2(val): 
    x = 10     
    print(f"In func2, x: {x}, value: {val}")          

    if val > 25: 
        x += 10 
        print(f"In func2 (if part): {x}")     
    else:         
        x += 5         
        print(f"In func2 (else part), x: {x}")     

    x += 1     
    return x  

def func3(val):     
    print("Hello func3".split())     
    print(f"In func3, value: {val}")  

print(f"Before func1 call: {x}") 
func1() 
print(f"After func1 call: {x}") 
func3(x)


# Find the output of the following question : [4]
def manipulate_string(s):
    s = s.lower()
    v = "aeiou"
    result = ""
    for char in s:
        if char not in v:
            result += char.upper()
    result = result[::-1]
    return result
string = manipulate_string("Hello,World!")
print(string)





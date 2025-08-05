# ********** String Method Practice Questions ************


"""
Question 1: 
Write a Python program that takes a sentence as input and prints the total number of words. 
Sample Input: 
Python is easy to learn 
Sample Output: 
5 
"""
#1
sentence = input("Enter a sentence: ")
words = sentence.split() # Convert the sentence into a list of words
word_count = len(words)
print(f"{word_count}")


"""
Question 2:  
Write a Python program that takes a sentence as input. Each word in the sentence represents 
a person's name. The program should capitalize each name and then return a list of all names 
that start with the letter 'S'. 
Sample Input: 
sarah fahim samia laboni sayem 
Sample Output: 
['Sarah', 'Samia', 'Sayem'] 
"""
#2
name = input("Enter sentence as input. Each word in the sentence represents a person's name: ")
s_name = []
name_list = name.split()
for person_name in name_list:
    capitalized = person_name.capitalize()
    if capitalized.startswith("S"):
        s_name.append(capitalized)
print(s_name)
        

"""
Question 3:  
Write  a  Python  program  that  takes  user  input  with  leading/trailing  spaces  and  special 
symbols  like  @,  and  print  a  cleaned  version  of  the  text  with  only  lowercase  letters  and  no 
symbols. 
Sample Input: 
@Hello@World!   
Sample Output: 
hello world 
"""
text = input("Enter text with symbols: ").lower()
text = text.split()
clean_text = ""
for char in text:
    if char.isalpha() or char == " ":
        clean_text += char
print(clean_text)       



"""
Question 4:  
Write a Python program that takes a string with words separated by dashes (-) and convert 
it into a normal sentence with spaces. 
Sample Input: 
data-science-is-cool 
Sample Output: 
data science is cool 
"""
sentence = input("Sentence: ")
print(sentence.replace("-", " "))

"""
Question 5:  
Write a Python program that takes a sentence as input and print the words in reverse order. 
[Hint: Use reversed() method. ] 
Sample Input: 
I love programming 
Sample Output: 
programming love I 
"""
text = input("Enter a sentence: ")

words = text.split()
reversed_words = list(reversed(words))
result = " ".join(reversed_words)
print(result)



# What will be the output of the following code? 
words = ["hello world", "good", "python programming!"]
result = []
for word in words:
    if len(word) % 2 != 0:
        result.append(word.upper().split())
    else:
        result.append(word.lower())
print(result)
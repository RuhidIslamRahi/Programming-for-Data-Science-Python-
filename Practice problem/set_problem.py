"""
(a) Write a Python program that takes two sentences as input. Your task is to find the common words between
these two sentences and determine the total number of unique words across both sentences. 

Sample Input 
Sentence 1: "The quick brown fox jumps over the
lazy dog"
Sentence 2: “A quick brown dog chases the fox”

Sample Output
Common Words: ["fox", "the", "dog", "quick", "brown"]
Total Number of Unique Words: 10
"""
def sentence_analisis (sen1, sen2):
    sentence1 = set(sen1.lower().split())
    sentence2 = set(sen2.lower().split())
    common_word = list(sentence1 & sentence2)
    print(f"Common Words: {common_word}")
    unique_word = len(sentence1 | sentence2)
    print(f"Total Number of Unique Words: {unique_word}")


sentence_1 = "The quick brown fox jumps over the lazy dog"
sentence_2 = "A quick brown dog chases the fox"
sentence_analisis(sentence_1, sentence_2)

#
def analyze_sentences(s1, s2):
    # Step 1: lowercase + split
    words1 = set(s1.lower().split())
    words2 = set(s2.lower().split())

    # Step 2: common words (intersection)
    common = list(words1 & words2)

    # Step 3: all unique words (union)
    total_unique = len(words1 | words2)

    return common, total_unique

s1 = "The quick brown fox jumps over the lazy dog"
s2 = "A quick brown dog chases the fox"

common, total_unique = analyze_sentences(s1, s2)
print("Common Words:", common)
print("Total Number of Unique Words:", total_unique)



"""
1. Write a Python program where for a given list of numbers, remove duplicates from 
the list and print the list without duplicates. 
Sample Input: [1, 2, 2, 3, 4, 4, 5] 
Sample Output: [1, 2, 3, 4, 5] 
"""
def sample_input (sen):
    sent = set (sen)
    return list(sent)

print(sample_input([1, 2, 2, 3, 4, 4, 5]))

"""
2. Write  a  Python  program  where  for  a  given  two  lists,  it  will  find  the  common 
elements. 
Sample Input: [1, 2, 3], [3, 4, 5] 
Sample Output: [3]
"""
def sentence_analysis (list1,list2):
    line1 = set(list1)
    line2 = set(list2)
    final = line1 & line2
    return list(final)

print(sentence_analysis([1, 2, 3], [3, 4, 5]))

"""
3.  Write a program that checks whether all elements in a list are unique. 
Sample Input: [1, 2, 3, 2] 
Sample Output: False 
"""
def elements_are_unique(lis):
    return len(lis) == len (set(lis))

print(elements_are_unique([1, 2, 3, 2]))

"""
4. Write  a  Python  program  where  for  a  given  list,  it  will  print  the  elements  that 
appear more than once. 
Sample Input: [1, 2, 2, 3, 4, 1] 
Sample Output: {1, 2} 
"""
def more_than_once (lst):
    return {x for x in lst if lst.count(x) > 1}


print(more_than_once([1, 2, 2, 3, 4, 1]))   

#
names = ["Rahi", "Amit", "Rahi", "Mitu"]
for name in names:
    if names.count(name) > 1:
        print(f"{name} is repeated")

"""
5. Write a Python program where for a given sentence, it will count the number of 
unique words. 
Sample Input: "the cat sat on the mat" 
Sample Output: 5
"""
def number_of_unique_words(sent):
    sentence_lower = sent.lower().split()
    unique_words_in_set = set(sentence_lower)
    return len(unique_words_in_set)
    
print(number_of_unique_words("the cat sat on the mat"))


"""
6. Write a Python program where for given two sets, it will print True if two sets have 
no common elements. 
Sample Input: {1, 2, 3}, {4, 5, 6} 
Sample Output: True 
"""
def are_disjoint(set1, set2):
    return len(set1 & set2) == 0

print(are_disjoint({1, 2, 3}, {4, 5, 6}))  # True
print(are_disjoint({1, 2, 3}, {2, 4, 5})) 

# Best way
def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)
print(are_disjoint({1, 2, 3}, {4, 5, 6}))  # True
print(are_disjoint({1, 2, 3}, {2, 4, 5}))  # False

"""
7. Write a Python program where for given two sets, it will print items in set A that 
are not in B. 
Sample Input: A = {1, 2, 3, 4}, B = {2, 4, 6} 
Sample Output: {1, 3}
"""
def items_in_a_not_in_b(a, b):
    return a - b

A = {1, 2, 3, 4}
B = {2, 4, 6}
print(items_in_a_not_in_b(A, B)) 

"""
8. Write a program to print all characters that appear only once in the given string. 
Sample Input: "banana" 
Sample Output: {'b'}
"""
def unique_char (text):
    return {chr for chr in text if text.count(chr)==1}
print(unique_char("banana"))

"""
9.  Given two sentences, print all words that are common in both. 
Sample Input: "I love Python", "Python is great" 
Sample Output: {'Python'}
"""
def common_words (text1,text2):
    sent1 = set(text1.split())
    sent2 = set(text2.split())
    common = sent1 & sent2
    return common

a = "I love Python"
b= "Python is great" 
print(common_words(a,b))

"""
10.  Print all repeated words from a sentence. 
Sample Input: "This is a test This test is simple" 
Sample Output: {'this', 'is', 'test'} 
"""
def repeated_word (text):
    split_words = text.lower().split()
    return{char for char in split_words if split_words.count(char) > 1}
print(repeated_word("This is a test This test is simple"))
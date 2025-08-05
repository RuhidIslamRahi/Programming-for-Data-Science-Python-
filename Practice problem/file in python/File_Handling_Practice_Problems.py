##



"""
Problem 2:
Write a program in Python that opens a file `story.txt` and count:
- Total number of lines
- Total number of words
- Total number of characters
Sample Input:

She learns Python.
Every day she practices.

Expected Output:

Lines: 2
Words: 7
Characters: 43
"""
with open("story.txt","r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    word_count += len(line.split())
    char_count += len(line)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")



"""
Problem 3:
Write a program in Python that takes input from the user line by line until they type `stop`.
Write each line to `output.txt`.
Sample Input:
I love Python.
It is easy to learn.
stop
Expected Output:
I love Python.
It is easy to learn.
"""


"""
Problem 4:
Write a program in Python that copies content from `source.txt` to `destination.txt`.
Sample Input (source.txt):
Hello World
Welcome to Python
Expected Output (destination.txt):
Hello World
Welcome to Python
"""

"""
Problem 5:
Write a program in Python that counts how many times the word "python" appears in the
file `data.txt` (case-insensitive).
Sample Input:
Python is powerful.
I love python.
PYTHON is easy.
Expected Output:
The word "python" appears 3 times.
"""

"""
Problem 6:
Write a program in Python that saves the following dictionary to `grades.txt` in `name:
grade` format.
Dictionary:
{"Arif": 85, "Nila": 92, "Sabbir": 78}
Expected Output (grades.txt):
Arif: 85
Nila: 92
Sabbir: 78
"""
grades = {"Arif": 85, "Nila": 92, "Sabbir": 78}
f = open("grades.txt","w")
for line in f:
    name,grade=line.strip().split(":")
f.close()

# Arif: 85
# Nila: 92
# Sabbir: 78


#
""""
grades.txt" te
Arif: 85
Nila: 92
Sabbir: 78
output:
{'Arif': 85, 'Nila': 92, 'Sabbir': 78}
"""
grades = {}
f = open("grades.txt","r")
for line in f:
    name,grade=line.strip().split(": ")
    grades[name] = int(grade)
f.close()
print(grades)

"""
Problem 7:
Write a program in Python that loads `grades.txt` content into a dictionary where name is
key and grade is value.
Sample Input:
Arif: 85
Nila: 92
Sabbir: 78
Expected Output:
{"Arif": 85, "Nila": 92, "Sabbir": 78}
"""


"""
Problem 8:
Write a program in Python that loads `contacts.txt` into a dictionary, take new name and
phone number as input, and append to the file.

Sample Input:
Sabbir: 12345
Sani: 67890
User Input:
Name: Saima
Number: 54321

Expected Output:
Sabbir: 12345
Sani: 67890
Saima: 54321
"""


"""
Problem 9:
Write a program in Python that stores the following nested dictionary into `employees.txt`
in comma-separated format.
Dictionary:
{"101": {"name": "Rahim", "department": "IT"}, "102": {"name": "Karim", "department":
"HR"}}
Expected Output:
101, Rahim, IT
102, Karim, HR
"""



"""
Problem 10:
Write a program in Python that reads 'employees.txt' and convert the contents into a nested
dictionary.
Sample Input:
101, Rahim, IT
102, Karim, HR
Expected Output:
{
"101": {"name": "Rahim", "department": "IT"}, "102": {"name": "Karim", "department": "HR"}
}
"""











# Final exam question

"""
1. (a) You are given a file named input.txt containing a list of student names and their corresponding scores in the
format: 

input.txt
Alice 95
Bob 87
Carol 92
David 78

Write a Python program to perform the following tasks:

i. Read the contents of input.txt and store the student names and scores in an appropriate data structure.

ii. Calculate the following statistics:
• The average score of all students.
• The highest score and the name of the student who achieved it.
• The lowest score and the name of the student who achieved it.

iii. Save the statistics in a new file named statistics.txt as shown below.

statistics.txt
Average score: 88.0
Highest score: 95 (Alice)
Lowest score: 78 (David)

"""
# 1
f = open("input.txt","w")
f.write("Alice 95\n")
f.write("Bob 87\n")
f.write("Carol 92\n")
f.write("David 78\n")
f.close()

#
students = []
with open("input.txt","r") as f:
    for line in f:
        name, score = line.strip().split()
        students.append((name, int(score)))
        #[('Alice', 95), ('Bob', 87), ('Carol', 92), ('David', 78)]

all_score = []
for student in students:
    all_score.append(student[1])
    average = sum(all_score)/ len(all_score)



highest_score = max(all_score)
highest_scorer_name = ""
for student in students:
    if student[1] == highest_score:
        highest_scorer_name = student [0]
        break

low_score = min(all_score)
low_scorer_name = ""
for student in students:
    if student[1] == low_score:
        low_scorer_name = student[0]
        break


with open("statistics.txt", "w") as f:
    f.write(f"Average score: {average:.1f}\n")
    f.write(f"Highest score: {highest_score} ({highest_scorer_name})\n")
    f.write(f"Lowest score: {low_score} ({low_scorer_name})\n")


# shortcut way
# Task i: Read the contents of input.txt and store the data
students = []
with open('input.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split()
        students.append((name, int(score)))

# Task ii: Calculate the statistics
scores = [score for name, score in students]
average = sum(scores) / len(scores)
highest_score = max(scores)
highest_student = [name for name, score in students if score == highest_score][0]
lowest_score = min(scores)
lowest_student = [name for name, score in students if score == lowest_score][0]

# Task iii: Save the statistics to statistics.txt
with open('statistics.txt', 'w') as file:
    file.write(f"Average score: {average:.1f}\n")
    file.write(f"Highest score: {highest_score} ({highest_student})\n")
    file.write(f"Lowest score: {lowest_score} ({lowest_student})\n")









    




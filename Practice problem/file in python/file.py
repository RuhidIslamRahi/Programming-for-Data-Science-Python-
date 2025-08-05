
# class 17 june 
# **** File I/O in Python *****

# Python can be used to perform operations on file.(read & write data)
# Python provides several ways to manipulate files.
"""
## Files are of two types.
--> Text of readable file: এর ভিতরে ডাটা character ফরম এ Store করা হয় 
.txt files, .py files, .docx, .log, etc
--> Binary or non-readable files:
.mp4, .mov, .png, jpeg, Images, Executables, etc

#### I this chapter I will learn 
--> How can I open a file
--> How can I read data from a file 
--> How can I write some data to a file
--> How can I close a file
--> How can I delete a file


Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for readung, 'w' for writing, or 'a' for appending. 

"""
"""
We can open a file in different modes.
Write ('w')): will create a file if the specified file does not exist
Append ('a')): will create a file if the specified file does not exist
Create ('x')): will create a file, returns an error if the file exist
Read ('r')): Returns an error if the file does not exist
"""
# Lets create a file using the simple open() method
f = open('sample.txt','w')
# This will create a file in the same directory the the python file is or in the current directory from where the comand is executed.


### Open, read & close File
# we have to open a file before reading or writing.

f = open('file_name','mode')

"""
'file_name' ---> sample.txt, demo.docx
'mode' ---> r: read mode , w: write mode
"""


"""
This will create a file in the same directory the the python file is or in the
current directory from where the comand is executed.



#------------------------------- File Write ------------------------------


--> Each time a file is opened in write mode, it will create a new file, thus
if a file existed, it will delete its content.
--> We get the handle of the file in the variable f
--> We can write strings in a file using the write() method.
"""
f = open('sample.txt','w')
f.write("Hello Python.\n")
f.write("I am writing in a file.\n")
f.close()
"""
sample.txt

Hello Python.
I am writing in a file.
"""


#----------------------------- File Append --------------------------


#--> If we run the code again, it will create the file afresh and write again to that new file.
#--> To append, we need to open in append mode.

f = open('sample.txt','a')
f.write("Hello Python.\n")
f.write("I am writing in a file.\n")
f.close()

# run this code output will be:
"""
Hello Python.
I am writing in a file.
Hello Python.
I am writing in a file.
"""

#--> It will appned next to the lines already existing.



#------------ File Read ----------- --> file এর মধ্যের ডাটা read করার জন্য 

#--> Lets consider a file where the following lines are written.

# Hello Python.
# I am writing in a file.
# Hello Python.
# I am writing in a file.

#--> Lets open this file and read its contents.

f = open("sample.txt","r")
print(f.read()) # this is read() Function . file এর সব ডাটা read করবে এবং string আকারে return করবে 
f.close()

# 
f = open("sample.txt","r")
data = f.read() # এইটা আমাদের ফাইল এর পুরা ডাটা return করে দিবে (String) e.
print(data)
print(type(data))
f.close()

#--> read() returns are contents as a string.
#--> If I want as a particaular character read 



#-------- Read a line -------


#--> readLine() returns the first line from the file.
#--> As the file is read sequentially, s subsequent call will return the second line.

f = open("sample.txt","r")
print(f.readline()) #return first line from the file. Hello Python., এই লাইনের পরে একটা নিউ লাইন প্রিন্ট করবে  
# এখন আমি যদি চাই যে আমি নিউ লাইন চাই না তাহলে নিচের লাইনের মতো করে লিখতে হবে 

f = open("sample.txt","r")
print(f.readline(),end="")
print(f.readline(),end="")
f.close()
# Hello Python.
# I am writing in a file.


# Alternative way (Using .Strip() function)
f = open("sample.txt","r")
line1 = f.readline()
line2 = f.readline()
f.close()

print(line1.strip())
print(line2.strip())


#------- Read all lines --------

#--> readLines() returns a list with all the lines in a file.
f = open('sample.txt','r')
print(f.readlines(),end="")
f.close()
# 
# ['Hello Python.\n', 'I am writing in a file.\n', 'Hello Python.\n', 'I am writing in a file.\n']
#
f = open("sample.txt","r")
list_line=f.readlines()
print(list_line) # list হিসাবে print করবে 
f.close()
# output: [['Hello Python.\n', 'I am writing in a file.\n', 'Hello Python.\n', 'I am writing in a file.\n']


# Reading File Content: The first step typically involves reading the content of a file into memory. This can be done line by line or by reading the entire file at once.

# Reading lines from a file
with open('sample.txt', 'r') as f:
    lines = f.readlines() 

print(lines)
# ['Hello Python.\n', 'I am writing in a file.\n', 'Hello Python.\n', 'I am writing in a file.\n']












# practice


"""
text file name : student_info
input:
Fahim 3.5
Sium 3.9
Rahi 4.0

output:
Fahim
3.5
Sium
3.9
Rahi
4.0
"""
f = open("student_info.txt", "r")
for line in f:
    name, cgpa = line.strip().split() #split function list return kore # name, cgpa একে বলা হয় লিস্ট unpacking , Unpacking--> আমরা যদি চাই একই লাইনে list এর যে item গুলো আছে সগুলো multiple variable এ store করে রাখতে চাই তাহলে আমরা এই স্টাইল এ করতে পারব .
    print(f"{name}")
    print(f"{cgpa}")

f.close()

##
"""
text file name : student_info1
Output:
Rahi
Mokles
কার কার Blood group B+
এইটা নামটা আমি নিচে নিচে প্রিন্ট করতে পারি, লিস্ট আকারে হক বা যেকোনো ভাবেই হক দেখাতে হবে """
f = open("student_info1.txt", "r")
for line in f:
    name,cgpa,blood_group = line.strip().split()
    if blood_group == "AB+":
        print(name)
f.close()


"""Problem 1:
Write a program in Python that reads a file named `notes.txt` and print its contents line by
line.
Sample Input:
Python is fun.
Files are useful.
Practice makes perfect.

Expected Output:
Python is fun.
Files are useful.
Practice makes perfect.
"""
f = open("notes.txt","r")
list_line = f.readlines()
for line in list_line:
    print(line.strip())

#
f = open("sample.txt","r")
list_line=f.readlines()
for line in list_line:
    print(line)
f.close()

# যদি new line না অ্যানতে চাই তাহলে 
f = open("sample.txt","r")
list_line=f.readlines()
for line in list_line:
    print(line.strip())
f.close()




# file write korno
f_read = open("sample.txt", "r")
f_write =open("output.txt", "w")
f_write.write("Hello World")
f_read.close()
f_write.close()
#--> file e dekhabe: Hello World


# file write korbo append mood e
f_read = open("sample.txt", "r")
f_write =open("output.txt", "a")
f_write.write("\nThis is my first first line")
f_read.close()
f_write.close()
#--> file e dekhabe:
# Hello World
# This is my first first line 
#
f_read = open("sample.txt", "r")
f_write =open("output.txt", "a")
f_write.write("\nHello World")
f_read.close()
f_write.close()
# 2 bar print korbo file e dekhabe:
# Hello World
# This is my first first line
# Hello World
# Hello World


# Previous year question
# student_info1.txt er data ke amra output1.txt file a run korbo.
f_read= open("student_info1.txt","r")
f_write=open("output1.txt","w")
#reading er kaj korte pari , ami e bar loop caliye korbo
for line in f_read:
     f_write.write(line)
f_read.close()
f_write.close()

# Output:
# Fahim 3.5 A+
# Sium 3.9 B+
# Rahi 4.0 AB+
# Mokles 2.0 AB+

#previpus year final question
f_read= open("student_info2.txt","r")
for line in f_read:
     f_write=open("output2.txt","w")
     f_write.write(line)
f_read.close()
f_write.close()
# Mokles 2.0 AB+

#blood group wise name list
f_read = open("student_info3.txt","r")
f_write = open("blood_group_wise_name.txt","a")
for line in f_read:
     name,cgpa,blood_group=line.strip().split(",")
     if blood_group=="AB+":
          f_write.write(f"{name}\n")
f_read.close()
f_write.close()
# Rahi
# Mokles


# dictionarty te store korte cassi as a key, value pair
grades={}
f = open("student.txt","r")
for line in f:
    name, cgpa, blood_group = line.strip().split()
    grades[name]=[ cgpa, blood_group ]
f.close()
print(grades)
#{'Fahim': ['3.9', 'O+'], 'Suhail': ['3.5', 'B+'], 'Zaima': ['3.95', 'O+']}

#
grades={}
f = open("student.txt","r")
for line in f:
    name, cgpa, blood_group = line.strip().split()
    grades[name]={"CGPA":float(cgpa),"Blood Group": blood_group}
f.close()
print(grades)
#{'Fahim': {'CGPA': 3.9, 'Blood Group': 'O+'}, 'Suhail': {'CGPA': 3.5, 'Blood Group': 'B+'}, 'Zaima': {'CGPA': 3.95, 'Blood Group': 'O+'}}


# student information as a list of dictionary
grades={}
grades_list = []
f = open("student.txt","r")
for line in f:
    name, cgpa, blood_group = line.strip().split()
    grades={"Name":name, "CGPA": cgpa, "Blood Group": blood_group}
    grades_list.append(grades)
f.close()
print(grades_list)
#[{'Name': 'Fahim', 'CGPA': '3.9', 'Blood Group': 'O+'}, {'Name': 'Suhail', 'CGPA': '3.5', 'Blood Group': 'B+'}, {'Name': 'Zaima', 'CGPA': '3.95', 'Blood Group': 'O+'}]


# dictionary te key hisebe jabe fahim, samin, sarah not name . amra nam tai as a key hisebe pathabo. tarpr tar value hisebe akta single value hobe. ebong value ta hobe ei 3 ta marks jog kore je avarage value asbe sei avarage value ta hobe ei dictionary key er value ,Output kind of 

grades = {}
f = open("student_info4.txt","r")
for line in f:
    line_list=line.strip().split()
    name = line_list[0]
    sum = 0
    for num in line_list[1:]:
        sum = sum +int(num)
    avg = round(sum/len(line_list[1:]),2)
    grades[name]= avg 

f.close()
print(grades)
# {'Fahim': 78.33, 'Samin': 92.33, 'Sarah': 90.0}



#built in function use kore 
grades = {}
with open("student_info4.txt", "r") as f:
    for line in f:
        line_list=line.strip().split() #["Fahim", "95", "85", "55"]
        name = line_list[0] # Fahim
        numbers = list(map(int,line_list[1:]))
        avg = round(sum(numbers)/len(numbers),2)  
        grades[name] = avg 
print(grades)
#{'Fahim': 78.33, 'Samin': 92.33, 'Sarah': 90.0}



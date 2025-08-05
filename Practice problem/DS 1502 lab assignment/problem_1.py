with open("employees.txt", "r") as f:
    employees = []
    for line in f:
        emp_id, name, department, salary = line.strip().split(",")
        emp_id = int(emp_id)
        salary = int(salary)
        employees.append({
        'id': emp_id,
        'name': name,
        'department': department,
        'salary': salary
        })

def count_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in name.lower():
        if letter in vowels:
            count += 1
    return count

two_vowel_names = []
for emp in employees:
    if count_vowels(emp['name']) == 2:
        two_vowel_names.append(emp['name'])

print("List of names containing exactly 2 vowels:",two_vowel_names)

#
total = 0
for emp in employees:
    total += emp['salary']
average = total / len(employees)
print("Average Salary of All Employees:", average)

#
dept_totals = {}
dept_counts = {}

for emp in employees:
    dept = emp['department']
    salary = emp['salary']
    
    if dept not in dept_totals:
        dept_totals[dept] = 0
        dept_counts[dept] = 0
    
    dept_totals[dept] += salary
    dept_counts[dept] += 1

dept_averages = {}
for dept in dept_totals:
    dept_averages[dept] = dept_totals[dept] / dept_counts[dept]

print("The dictionary of the average salaries of all the departments:", dept_averages)
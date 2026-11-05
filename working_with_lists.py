# 1. List of courses already taken at Walsh College 
courses = ["business algebra", "economics i", "english composition", "management i", "accounting", "business communication", "introduction to prograrmming",
           "statistical methods for business", "business communication strategies", "introduction to databases", "introduction to networking", "system analysis and design",
           "server virtualization and performance engineering", "networks and operating system", "database design and development", "principles of software engineering"]

# 2. Sort the list and print each course in uppercase
courses.sort()
for course in courses:
    course_upper = course.upper()
    print("I have taken " + course_upper + " at Walsh College")

# 3. Add upcoming courses and re-sort the list
upcoming_courses = ["introduction to security", "advanced programming", "ethical hacking & strategies tools", "fundamentals of cybersecurity"]
courses.extend (upcoming_courses)
courses.sort

print("\nThis is my course of study with upcoming course added:")
for course in courses:
    print(course)

# 4. Remove courses that was already taken and print it
courses_taken = ["business algebra", "economics i", "english composition", "management i", "accounting", "business communication", "introduction to prograrmming",
           "statistical methods for business", "business communication strategies", "introduction to databases", "introduction to networking", "system analysis and design",
           "server virtualization and performance engineering", "networks and operating system", "database design and development", "principles of software engineering"]

print("\nI do not have to take these course:")
for course in courses_taken:
    if course in courses:
        courses.remove(course)
        print(course)

# 5. Print remaining course to take next term
print("\nI plan to take the following courses next term:")
for course in courses:
    print(course)

# 6. A list of numbers from 1 to 1000 that are divisible by 6
numbers = []

for number in range(1,1001):
    if number % 6 == 0:
        numbers.append(number)

# 7. Print the first 20 numbers in the list
print("\nHere are twenty numbers divisble by 6:")
for number in numbers[:20]:
    print(number)

# 8. Calculate the maximum number of the original large list
max_number = max(numbers)

# 9. Print the maximum number
print("\nThe maximum value in the list is: " + str(max_number))

# 10. Calculate and print the sum of of the 10th through 50th values
sum_of_values = sum(numbers[9:50])

print("\nThe sum of values is: " + str(sum_of_values))

# 11. Overwrite the original courses variable with the numbers list
courses = numbers
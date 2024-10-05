#List
#Num1
courses = [
    "Data Structures and Algorithms", 
    "Psychology I", 
    "Macroeconomics", 
    "Linear Algebra", 
    "Introduction to Programming", 
    "Biology I", 
    "English Composition I", 
    "Calculus II", 
    "Chemistry I", 
    "Discrete Mathematics", 
    "Microeconomics", 
    "History I", 
    "Calculus I", 
    "Introduction to Philosophy", 
    "Physics I"
]

print("Original list:", courses)

#Num2
sorted_courses = sorted(courses)
print("Alphabetically sorted list:", sorted_courses)

sorted_courses_reverse = sorted(courses, reverse=True)
print("Reverse alphabetically sorted list:", sorted_courses_reverse)

#Num3
courses.reverse()
print("List after reverse():", courses)

courses.reverse()
print("List after second reverse():", courses)

#Num4
courses.sort()
print("List after sort() (alphabetically):", courses)

courses.sort(reverse=True)
print("List after sort() in reverse:", courses)

#List-Create Useable Coding
#Num1
# Original list of courses in non-alphabetical order
courses = [
    "Data Structures and Algorithms", 
    "Psychology I", 
    "Macroeconomics", 
    "Linear Algebra", 
    "Introduction to Programming", 
    "Biology I", 
    "English Composition I", 
    "Calculus II", 
    "Chemistry I", 
    "Discrete Mathematics", 
    "Microeconomics", 
    "History I", 
    "Calculus I", 
    "Introduction to Philosophy", 
    "Physics I"
]

sorted_courses = sorted(courses)
print("The following courses are available for expression of interest if the students meet the prerequisites:")
for course in sorted_courses:
    print(course)

#Num2
replaced_course = "Calculus I"
new_course = "Advanced Calculus"
courses[courses.index(replaced_course)] = new_course
print(f"\nThe course '{replaced_course}' has been withdrawn and replaced by '{new_course}'.")

#Num3
new_course1 = "Artificial Intelligence"  # To be inserted at the beginning
new_course2 = "Machine Learning"  # To be inserted in the middle
new_course3 = "Cloud Computing"  # To be added at the end

courses.insert(0, new_course1)

middle_index = len(courses) // 2
courses.insert(middle_index, new_course2)

courses.append(new_course3)
print("\nUpdated list of available courses:")
for course in courses:
    print(course)

#Num4
removed_courses = []
removed_courses.append(courses.pop(0))  # Remove the first course
removed_courses.append(courses.pop(middle_index))  # Remove the middle course
removed_courses.append(courses.pop(-1))  # Remove the last course
removed_courses.append(courses.pop(2))  # Remove a random course from near the start
print("\nThe following courses are no longer available due to technical and room availability issues:")
for course in removed_courses:
    print(course)

print("\nCourses still available:")
for course in courses:
    print(course)

#Create a list of tuples (course_id, course_name)
courses_tuple = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I")
]

#Create an empty list to store both course IDs and Names
courses_info = []

# Num 2: Loop through each tuple in the list
for course in courses_tuple:
    #Extract course ID and name from each tuple
    course_id, course_name = course
    
    #Add the course name to the empty list
    courses_info.append(f"Course ID: {course_id}, Course Name: {course_name}")

#Num 3 Print the course information from the new list
print("\nCourse Information:") 
for info in courses_info:
    print(info)

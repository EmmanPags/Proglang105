# Step 1: Create a list of tuples (course_id, course_name)
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

# Step 1.2: Create an empty list to store both course IDs and Names
courses_info = []

# Step 2: Loop through each tuple in the list
for course in courses_tuple:
    # Step 2.1: Extract course ID and name from each tuple
    course_id, course_name = course
    
    # Step 2.2: Add the course name to the empty list
    courses_info.append(f"Course ID: {course_id}, Course Name: {course_name}")

# Step 3: Print the course information from the new list
print("Course Information:")
for info in courses_info:
    print(info)

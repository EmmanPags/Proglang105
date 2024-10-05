# Full course list with course details: [course_id, course_name, department, prerequisites]
course_details = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

while True:
    user_input = input("Enter a course ID (1-15) or type 'quit' to exit: ")

    # Checking if user wants to quit
    if user_input.lower() == "quit" or user_input == "0":
        print(f"The value '{user_input}' has been used to exit.")
        break

    # Check if the input is a valid integer
    try:
        course_id = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the course_id is within range
    if 1 <= course_id <= 15:
        # Search for the course in the list
        course_found = False
        for course in course_details:
            if course[0] == course_id:
                print(f"Course ID {course_id}: {course[1]} is in the {course[2]} department.")
                print(f"Prerequisites: {course[3]}")
                course_found = True
                break
        
        if not course_found:
            print(f"Course ID {course_id} is not found.")
    else:
        print("Course ID is out of range (1-15), try again.")

# A. List of Departments: Create the list using course_id and department
courses = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

# B. Create an infinite while loop until the user enters 'quit' or '0'
while True:
    # Prompt the user for a course ID
    user_input = input("Enter a course ID (1-15) or type 'quit' to exit: ")

    # C. Conditional Statements to check the input
    # Check if the user wants to quit the loop
    if user_input.lower() == "quit" or user_input == "0":
        print(f"The value '{user_input}' has been used to exit.")
        break

    # Try to convert the input into an integer
    try:
        course_id = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # D. Search for department based on course_id
    if 1 <= course_id <= 15:  # Check if course_id is within range (1-15)
        course_found = False

        # Loop through the list of courses to find the matching course_id
        for course in courses:
            if course[0] == course_id:
                print(f"Course ID {course_id} is in the {course[1]} department.")
                course_found = True
                break

        if not course_found:
            print(f"Course ID {course_id} is not found.")
    else:
        print("Course ID is out of range (1-15), try again.")

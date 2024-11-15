from logic.exerciseOne import save_course

def design():
    course = input("Whats the course name? ")
    result = save_course(course)
    print(result)
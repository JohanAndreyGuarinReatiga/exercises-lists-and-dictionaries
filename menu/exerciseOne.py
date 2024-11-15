from logic.exerciseOne import save_course, search_currency

def designOneList():
    course = input("Whats the course name? ")
    result = save_course(course)
    print(result)
    
def designOneDict():
    currency = input("Whats the currency name? ")
    print(search_currency(currency))
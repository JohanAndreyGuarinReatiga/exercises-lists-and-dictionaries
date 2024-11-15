import json
def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        convertList = json.loads(data)
        return convertList
    
def write_file(data, path):
    with open(f"databases/{path}", "wb+") as file:
        convertJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertJson)
        file.close()
 
   
def save_course(course):
    data = read_file("exerciseOneList.json")
    data.append(course)
    write_file(data)
    return data
    
#Ejercicio 1 dict    
def search_currency(currency):
    data = read_file("exerciseOneDict.json")
    if (data.get(currency)):
        return data.get(currency)
    else:
        return "Currency not found"

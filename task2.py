import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19, 
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    name = input("Введите кличку питомца: ")
    pets[last+1] = {
        name: {
            "Вид питомца": input("Введите вид питомца: "),
            "Возраст питомца": int(input("Введите возраст питомца: ")),
            "Имя владельца": input("Введите имя владельца: ")  
        }
    }
    
def read(ID):
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        print(f"Это {pet[name]['Вид питомца'].lower()} по кличке \"{name}\".") 
        print(f"Возраст питомца: {pet[name]['Возраст питомца']} {get_suffix(pet[name]['Возраст питомца'])}")
        print(f"Имя владельца: {pet[name]['Имя владельца']}")
    else:
        print("Питомца с таким ID нет")
        
def update(ID):
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0] 
        pet[name]['Вид питомца'] = input("Введите новый вид питомца: ")
        pet[name]['Возраст питомца'] = int(input("Введите новый возраст питомца: "))
        pet[name]['Имя владельца'] = input("Введите новое имя владельца: ")
        print("Информация обновлена")
        
def delete(ID):
    if ID in pets:
        del pets[ID]
        print("Запись удалена")
    else:
        print("Питомца с таким ID нет")
        
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False
    
def get_suffix(age):
    if age % 10 == 1 and age != 11:
        return "год"
    elif 1 < age % 10 < 5 and not 11 < age < 15:
        return "года"
    else:
        return "лет"
        
def pets_list():
    for id, pet in pets.items():
        name = list(pet.keys())[0]
        print(f"ID: {id}, Кличка: {name}")

while True:
    command = input("Введите команду (create, read, update, delete, stop): ")
    if command == "stop":
        break
        
    if command == "create":
        create()
    elif command == "read":
        ID = int(input("Введите ID питомца: "))  
        read(ID)
    elif command == "update":
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == "delete":
        ID = int(input("Введите ID питомца: "))  
        delete(ID)
        
print("Работа программы завершена")

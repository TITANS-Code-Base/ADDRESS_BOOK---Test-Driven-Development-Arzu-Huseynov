from service import (
    create_person,
    get_db,
    save_to_db
)

texts = {
    "welcome" : "Welcome to Address Book. You can add/get/update/delete people from your terminal",
    "action_helper" : "Choose 1 for adding new person, 2 for searching, 3 for updating and 4 for deleting.",
    "action_create": "Cool! Now, you will add new person. Please follow the steps.",
    "action_create_success" : "Nice job! You have added new person.",
}

print(texts["welcome"])
print(texts["action_helper"])

action_type = input("Choose next step: ")

if action_type == "1":
    print(texts["action_create"])
    name = input("Add person name: ")
    surname = input("Add person surname: ")
    number = input("Add number: ")
    new_person = create_person(name,surname,number)
    saved, person = save_to_db(new_person)
    if saved:
        print(texts["action_create_success"])

elif action_type == "2":
    people=get_db()
    for person in people:
        print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')
        print("---")
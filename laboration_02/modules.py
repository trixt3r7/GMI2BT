import csv
import gui
import json
from person import Person


def check_num(input_string):
    try:
        input_string = int(input_string)
        return input_string
    except ValueError:
        print("Invalid input. Please try again.")


def file_exist(filename):
    try:
        file = open(filename)
        file.close()
        return True
    except IOError:
        # print("File not accessible")
        return False


def read_csv(filename, header=True):
    # Can switch if csv file has a header or not with header, default value 'True' will skip first line

    lines = []
    try:
        with open(filename, "r", encoding="utf-8") as file_obj:
            read_csv_file = csv.reader(file_obj, delimiter=";")
            for row in read_csv_file:
                if header:
                    header = False
                    continue
                person = Person(row[1].strip(), row[2].strip(), row[0].strip(), row[3].strip())
                lines.append(person.person_to_dict())
            print_table(lines)
        return lines
    except FileNotFoundError:
        print("File not found.")


def add_student(list_name):
    gui.add_header()
    while True:
        person = Person("", "", "", "")
        while not person.fname:
            person.fname = input("First name: ").strip()
        while not person.lname:
            person.lname = input("Last name: ").strip()
        while not person.username:
            person.username = input("Username: ").strip()
        while not person.email:
            person.email = input("E-mail: ").strip()
        student = person.person_to_dict()
        list_name.append(student)
        gui.add_menu()
        choice = input("Choose menu item: ")
        while choice != "1" and choice != "2":
            print("Menu item not available, please try again.")
            choice = input("Choose menu item: ")
        if choice == "2":
            break


def remove_student(list_name):
    list_student_names(list_name)
    gui.remove_menu()
    while True:
        student = input("Student to remove [number]: ")
        if student == "exit":
            break
        if student == "list":
            list_student_names(list_name)
            gui.remove_menu()
        elif check_num(student) and int(student) <= len(list_name):
            student = int(student) - 1
            print(f'{list_name[student]["fname"]} {list_name[student]["lname"]} removed!')
            list_name.pop(student)
        else:
            print("Not a valid item, try again.")


def list_student_names(list_name):
    i = 0
    # List all with index number)
    for student in list_name:
        i += 1
        print(f"{i}: {student['fname']} {student['lname']}")


def search_student(list_name):
    gui.search_header()
    while True:
        search = input("Search for student: ")
        search_list = search_result(search, list_name, "fname", "lname")
        if len(search_list) == 0:
            print(f"Your search on '{search}' gave no results!")
        else:
            gui.search_result()
        for result in search_list:
            print("{0:31}".format(f"{result['fname']} {result['lname']}"), end="")
            print(f"{result['email']}   {result['username']}")
        gui.search_menu()
        choice = input("Choose menu item: ")
        while not (choice == "1" or choice == "2"):
            print("Menu item not available, please try again.")
            choice = input("Choose menu item: ")
        if choice == "2":
            break


def search_result(search, list_item, key1, key2):
    return list(filter(lambda item: item[key1] == search or item[key2] == search, list_item))


def print_table(data):
    print("")
    print("{0:4}".format('Nr'), end="")
    print("{0:32}".format('Full Name'), end="")
    print("{0:12}".format('Username'), end="")
    print("E-mail")
    print("——————————————————————————————————————————————————————————————")
    i = 0
    for _ in data:
        print("{0:<4}".format(i + 1), end="")
        print("{0:32}".format(f"{data[i]['fname']} {data[i]['lname']}"), end="")
        print("{0:12}".format(data[i]['username']), end="")
        print(data[i]['email'])
        i += 1


def json_write_data(filename, data):
    # Save to json-file
    try:
        with open(filename, "w", encoding="utf-8") as file_obj:
            json.dump(data, file_obj, ensure_ascii=False)
    except FileNotFoundError as err:
        print(f"File not found {err}")


def json_read_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file_obj:
            content = json.load(file_obj)
            return content
    except FileNotFoundError:
        return False

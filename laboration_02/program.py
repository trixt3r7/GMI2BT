# Require labb2-personer.csv (not available in GitHub)
import gui
import modules
csv_file = 'labb2-personer.csv'
json_file = 'students.json'

if modules.json_read_data(json_file):
    json_list = modules.json_read_data(json_file)
else:
    json_list = []

while True:
    gui.logo()
    gui.print_menu()
    choice = input("Choose menu item: ")
    if choice == '1':
        # Read csv-file
        if modules.read_csv(csv_file):
            csv_read = modules.read_csv(csv_file)
        else:
            continue
        # Check if json data has been loaded and gives a different string depending on result
        file_exists = modules.file_exist(json_file)
        if file_exists:
            write_file_text = "overwrite"
        else:
            write_file_text = "write to"
        save_to_list = input(f"Do you want to {write_file_text} {json_file}? [yes/no]: ")
        if save_to_list == 'yes':
            modules.json_write_data(json_file, csv_read)
            json_list = modules.json_read_data(json_file)

    elif choice == '2' and modules.file_exist(json_file):
        modules.print_table(json_list)

    elif choice == '3' and json_list is not None:
        # Save to json-file
        modules.json_write_data(json_file, json_list)
        print("Data have been saved.")

    elif choice == '4':
        # Add person to json_list
        modules.add_student(json_list)

    elif choice == '5' and json_list is not None:
        # Remove person to json_list
        modules.remove_student(json_list)

    elif choice == '6' and json_list is not None:
        # search json_list
        modules.search_student(json_list)

    elif choice == '7':
        # Quit application
        break

    else:
        # Error messages
        if choice == '5':
            print("This menu item is not available as there isn't any data available to save.")
        elif choice == '2':
            print("JSON-data is empty.")
        elif choice == '6':
            print("This menu item is not available as there isn't any data available to search on.")
        elif json_list is None:
            print("JSON-data has not been loaded. This menu item is therefore not available.")
        else:
            print("Unknown error, please try again.")

import json, os
filename = "sample.json"
true_options = ('y', 'Y', 'yes', 'Yes', "YES", 'yep', 'Yep', 'YEP')
false_options = ("n", "N", "No", "no", "NO", "Nope", "nope", "NOPE")


if os.path.isfile(filename) and os.path.getsize(filename) == 0:
    print("No data found!")
    option = input("Do you want add to new data? (yes or no) ")

    if option in true_options:
       note_title = input("Enter note title: ")
       note_body = input("Enter not body: ")
       note = {'note_title' : note_title, 'note_body': note_body}

       with open(filename, 'w') as new_file:
           json.dump([note], new_file)
           print("New note created successfully!")
    elif option in false_options:
        print("Okay, The file still remains empty\nBye!")
    else:
        print("Invaid option!\nExiting application\nBye!")
else:
    with open(filename) as current_file:
        current_data = json.load(current_file)
    
    current_data_length = len(current_data)

    if current_data_length == 1:
        grammer = "is"
        data_word = "data"
    else:
        grammer = "are"
        data_word = "data's"

    print(f"There {grammer} {current_data_length} {data_word} available in the record")
    option = input("Do you want to add new data? (yes or no) ")

    if option in true_options:
        note_title = input("Enter note title: ")
        note_body = input("Enter not body: ")
        note = {'note_title' : note_title, 'note_body': note_body}

        current_data.append(note)

        with open(filename, 'w') as update_file:
            json.dump(current_data, update_file)
            print("New data added successfully")
    elif option in false_options:
        print("No new data added!")
        print(f"We still have {current_data_length} {data_word} available in the record")
    else:
        print("Invaid option!\nExiting application\nBye!")
        


       
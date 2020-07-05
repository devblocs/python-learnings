import os

def add_contents_to_file(file, filename: str):
    f = file
    old_contents = f.read()
    true_options = ("y" , "Y", "No", "yes", "YES", "Yep", "yep", "YEP")
    false_options = ("n", "N", "No", "no", "NO", "Nope", "nope", "NOPE")

    print("Do you want to add contents to the file?")
    option = input("Enter your decision: (yes or no) ")

    if option in true_options:
        print("Enter your contents: ")
        contents = input()
        new_contents = contents if os.path.isfile(filename) and os.path.getsize(filename) == 0 else old_contents + "\n" + contents

        f.write(str(new_contents))
    elif option in false_options:
        print("Okay! Closing the file from edit mode")
    else:
        print("Invalid input!")
        try_again = input("Do you want to try again? (yes or no) ")

        if try_again in true_options:
            add_contents_to_file(f, filename)
        elif try_again in false_options:
            print("Okay, Bye!")
        else:
            print("Invalid option!")
            print("Bye!")


filename = 'sample.txt'
with open(filename, 'r+') as f:
    file_content = f.read()

    if file_content == "":
        print("The file is empty!")
        
        add_contents_to_file(f, filename)
    else:
        print("Contents in the file are as follows: ")
        print(file_content)
        add_contents_to_file(f, filename)


with open(filename) as file:
    contents = file.read()

    print("\nPrinting new contents: ")
    print(contents)
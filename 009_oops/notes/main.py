from Classes.Note import Note

note_title = input("Enter note title: ")
note_body = input("Enter note body: ")

filename = "notes"

note = Note(note_title, note_body, filename)

note.check_data()
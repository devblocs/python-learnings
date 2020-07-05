import os, json
from Config import Config as config

class Note:
    __note_title = ""
    __note_body = ""
    __filename = ""

    def __init__(self, title: str, body: str, filename: str):
        self.__note_title = title
        self.__note_body = body
        self.__filename = filename
        self.__create_file_if_not_exists() #create empty file if doesn't exists
    
    def __file_path(self) -> str:
        filename = self.__filename + ".json"
        return os.path.join(config.output_path, filename)
    
    def __create_file_if_not_exists(self) -> None:
        if not os.path.isfile(self.__file_path()):
            # os.mknod(self.__file_path()) # not supported in windows OS
            open(self.__file_path(), 'a').close()

    
    def check_data(self):
        if os.path.isfile(self.__file_path()) and os.path.getsize(self.__file_path()) == 0:
            self.__create_note()
        else:
            self.__add_new_note()

    def __create_note(self):
        note = {
            'note_title': self.__note_title,
            'note_body': self.__note_body
        }

        with open(self.__file_path(), 'w') as new_file:
            json.dump([note],new_file)
    
    def __add_new_note(self):
        with open(self.__file_path(), 'r') as current_file:
            current_content =json.load(current_file)
        
        note = {
            'note_title': self.__note_title,
            'note_body': self.__note_body
        }

        current_content.append(note)

        with open(self.__file_path(), 'w') as update_file:
            json.dump(current_content, update_file)
import json
import os
from general_Character import general_Character


class CharacterManager:
    def save_load_menu(self, character=None):
        print("1. Save Character\n"
              "2. Load Character\n"
              "3. Display All Characters\n"
              "4. Delete Character\n"
              "5. Exit\n")
        choose = input("Choose: ")
        if choose == '1':
            if character is None:
                print("No character instance provided.")
                return
            file_path = character.atribute1 + ".json"
            self.save(character, file_path)
            self.save_load_menu()
        elif choose == '2':
            file_path = input("Write the name of the character you want to load: ")
            self.load(file_path + ".json")
            self.save_load_menu()
        elif choose == '3':
            directory = "C:/Users/cutas/PycharmProjects/pythonProject"
            self.display_all_files(directory)
            self.save_load_menu()
        elif choose == '4':
            append = ".json"
            file_path = input("Delete the name: ")
            self.delete(file_path + append)
            self.save_load_menu()

        elif choose == '5':
            return

    def save(self, character, file_path):
        parameters = {
            "name": character.atribute1,
            "age": character.atribute2,
            "skill": character.atribute3
        }
        try:
            with open(file_path, "w") as file:
                json.dump(parameters, file)
            print("Character saved successfully.")
        except IOError:
            print("Failed to save character.")

    def load(self, file_path):
        try:
            with open(file_path, "r") as file:
                parameters = json.load(file)
                character = general_Character(parameters["name"], parameters["age"], parameters["skill"])
                character.print_attributes()
                return character
        except FileNotFoundError:
            print("No saved character found.")
            return None

    def delete(self, file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("No file found.")

    def display_all_files(self, directory):
        json_files = [file for file in os.listdir(directory) if file.endswith(".json")]
        if json_files:
            print("Available JSON files:")
            for file in json_files:
                print(file)
        else:
            print("No JSON files found in the directory.")

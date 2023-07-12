from general_Character import general_Character

class Dialog:
    def __init__(self, character_instance):
        self.character1 = character_instance

    def talk(self):
        print("1. Character Introduction\n"
              "2. Character Age\n"
              "3. Character Skill\n"
              "4. Exit\n")
        number = input("Choose: ")
        if number == '1':
            self.introduction()
            self.talk()
        elif number == '2':
            self.whats_your_age()
            self.talk()
        elif number == '3':
            self.skill_prezentation()
            self.talk()
        elif number == '4':
            return
        else:
            print("Invalid choice\n")
            self.talk()




    def whats_your_age(self):
        if self.character1.atribute2 is not None:
            print(self.character1.atribute1 + " is " + self.character1.atribute2 + " years old \n")
        else:
            print("Fuck off \n")


    def skill_prezentation(self):
        if self.character1.atribute3 is not None:
            print(self.character1.atribute1 + " has the skill of " + self.character1.atribute3 + "\n")
        else:
            print("No skils to display\n")


    def introduction(self):
        if self.character1.atribute1 is not None:
            print("My name is", self.character1.atribute1 + "\n")
        else:
            print("Character name not set")

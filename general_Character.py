

class general_Character:
    def __init__(self, name = None, age = None, skill = None):
        self.atribute1 = name
        self.atribute2 = age
        self.atribute3 = skill


    def menu(self):
        print("1. Choose a name\n"
              "2. Set the age\n"
              "3. Add a skill\n"
              "4. Display character\n"
              "5. Display skill\n"
              "6. Exit\n")

        choose = input("Choose: ")
        if choose == '1':
            self.change_name()
            self.menu()
        elif choose == '2':
            self.change_age()
            self.menu()
        elif choose == '3':
            self.change_skill()
            self.menu()
        elif choose == '4':
            self.print_attributes()
            self.menu()
        elif choose == '5':
            self.print_skills()
            self.menu()
        elif choose == '6':
            return
        else:
            print("Invalid choice\n")
            self.menu()



    def change_name(self):
        self.atribute1 = input("Name: ")


    def change_age(self):
        self.atribute2 = input("Age: ")

    def change_skill(self):
        self.atribute3 = input("Skill: ")


    def print_attributes(self):
        print("Name: ", self.atribute1)
        print("Age: ", self.atribute2)
        print("Skill: ", self.atribute3)

    def print_skills(self):
        if self.atribute1 is None:
            print("\nYou must choose a name for your character in order to have a skill\n")
        elif self.atribute3 is None:
            print("\n" + self.atribute1 + " has no skills\n")
        else:
            print("\n" + self.atribute1 + " possesses the skill of " + self.atribute3 + "\n")
        self.menu()



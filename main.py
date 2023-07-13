from general_Character import general_Character
from dialog import Dialog
from save_load import CharacterManager



Dan = general_Character()
Dan.menu()
save = CharacterManager()
save.save_load_menu(Dan)
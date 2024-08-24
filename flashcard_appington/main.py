import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flashcard_appington.handlers import MenuHandler, IOHandler, PrintHandler
from flashcard_appington.models import CardSet, Settings

def main():
    settings = MenuHandler.display_settings(Settings.default_settings())
    file_path = MenuHandler.choose_file("flashcards/Swedish")
    card_set = CardSet(file_path).study(settings)
    MenuHandler.prompt_repeat(card_set.cards, file_path, settings)
    

if __name__ == "__main__":
    main()

from flashcard_appington.handlers import MenuHandler, IOHandler, PrintHandler
from flashcard_appington.models import CardSet, Settings
from flashcard_appington.helper import start_app

def main():
    # Initialize settings
    settings = Settings.default_settings()

    # Show settings menu and modify if needed
    settings = MenuHandler.display_settings(settings)

    # Choose a file to study
    file_path = MenuHandler.choose_file("flashcards/Swedish/flashcards")

    # Create a CardSet instance from the chosen file
    card_set = CardSet(file_path)
    
    # Start studying with the cards
    card_set.study(settings)

    # Repeat study session if needed
    MenuHandler.prompt_repeat(card_set.cards, file_path, settings)

    # Display welcome message
    PrintHandler.print_notice("Starting Flashcard Appington!")
    

if __name__ == "__main__":
    main()

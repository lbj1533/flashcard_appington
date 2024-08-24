from typing import List
from flashcard_appington.handlers import FileHandler, CardHandler

class CardSet:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.cards = self._load_cards()

    def _load_cards(self) -> List[List[str]]:
        """
        Load cards from the file specified by self.file_path.
        
        Returns:
            List[List[str]]: A list of card pairs.
        """
        content = FileHandler.open_file(self.file_path)
        return CardHandler.parse_cards(content)

    def study(self, settings):
        """
        Start studying the card set.
        
        Args:
            settings (list): A list of user settings.
        """
        CardHandler.display_cards(self.cards, 0, self.file_path, settings)


class Settings:
    @staticmethod
    def default_settings():
        """
        Returns a list of default settings.
        
        Returns:
            list: Default settings list.
        """
        return [["Language Mode", False], ["Shuffle Mode", True], ["Require Exact Answer", False]]

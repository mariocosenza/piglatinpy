from src.error import PigLatinError

VOWELS = "aeiou"

class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase
    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"
        elif self.phrase[0] in VOWELS:
            last_letter = self.phrase[-1]
            if last_letter == "y":
                return self.phrase + "nay"
            elif last_letter in VOWELS:
                return self.phrase + "yay"
            else:
                return self.phrase + "ay"

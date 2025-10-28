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
            return PigLatinTranslator.translate_word_starting_with_vowel(self.phrase)

    @staticmethod
    def translate_word_starting_with_vowel(word: str) -> str:
        last_letter = word[-1]
        if last_letter == "y":
            return word + "nay"
        elif last_letter in VOWELS:
            return word + "yay"
        else:
            return word + "ay"


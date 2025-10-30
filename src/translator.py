from src.error import PigLatinError

VOWELS = "aeiou"
CONSONANTS = "bcdfghjyklmnpqrstvwzx"

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

        words = self.phrase.split(sep=' ')
        translation = ""
        for word in words:
            composites = word.split(sep='-')
            if len(composites) > 1:
                for composite in composites:
                    translation += PigLatinTranslator.translate_helper(composite) + '-'
                translation = translation.rstrip('-')
            else:
                translation += PigLatinTranslator.translate_helper(word) + ' '

        return translation.rstrip()

    @staticmethod
    def translate_helper(word):
        first_letter = word[0]
        if first_letter in VOWELS:
            return PigLatinTranslator.translate_word_starting_with_vowel(word)
        elif first_letter in CONSONANTS:
            return PigLatinTranslator.translate_word_starting_with_consonant(word)

    @staticmethod
    def translate_word_starting_with_vowel(word: str) -> str:
        last_letter = word[-1]
        if last_letter == "y":
            return word + "nay"
        elif last_letter in VOWELS:
            return word + "yay"
        else:
            return word + "ay"


    @staticmethod
    def translate_word_starting_with_consonant(word: str) -> str:
        count = 0
        for letter in word:
            if letter in CONSONANTS:
                 count += 1
                 word += letter
            else:
                break
        substring = word[count:]
        return substring + "ay"
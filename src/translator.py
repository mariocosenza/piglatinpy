from src.error import PigLatinError

VOWELS = "aeiou"
CONSONANTS = "bcdfghjyklmnpqrstvwzx"
PUNCTUATION= ".,;?!:()"

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
                    if composite[-1] in PUNCTUATION:
                        split_composite = composite[:len(composite)-1]
                        translation += PigLatinTranslator.translate_helper(split_composite) + composite[-1] + '-'
                    else:
                        translation += PigLatinTranslator.translate_helper(composite) + '-'
                translation = translation.rstrip('-')
            else:
                translation += PigLatinTranslator.translate_helper(word)
            translation += ' '

        return translation.rstrip()

    @staticmethod
    def translate_helper(word):
        first_letter = word[0]
        if first_letter.lower() in VOWELS:
            return PigLatinTranslator.translate_word_starting_with_vowel(word)
        elif first_letter.lower() in CONSONANTS:
            return PigLatinTranslator.translate_word_starting_with_consonant(word)
        return None

    @staticmethod
    def translate_word_starting_with_vowel(word: str) -> str:
        last_letter = word[-1]
        temp_word = word
        if last_letter.lower() == "y":
            temp_word += "nay"
        elif last_letter.lower() in VOWELS:
            temp_word += "yay"
        else:
            temp_word += "ay"

        if PigLatinTranslator.is_all_upper_case(word):
            return temp_word.upper()

        return temp_word


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
        if PigLatinTranslator.is_all_upper_case(word):
            return substring + "AY"
        return substring + "ay"

    @staticmethod
    def is_all_upper_case(word: str) -> bool:
        return word == word.upper()

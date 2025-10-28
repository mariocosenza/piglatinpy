from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        phrase = "Hello world"
        translator = PigLatinTranslator(phrase)
        result = translator.get_phrase()
        self.assertEqual(result, phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_single_word_starting_with_vowel_a_and_ending_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_single_word_starting_with_vowel_e_and_ending_y(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_translate_single_word_starting_with_vowel_u_and_ending_with_vowel_a(self):
        translator = PigLatinTranslator("umbrella")
        translation = translator.translate()
        self.assertEqual("umbrellayay", translation)

    def test_translate_single_word_starting_with_vowel_i_and_ending_with_vowel_e(self):
        translator = PigLatinTranslator("intersubjective")
        translation = translator.translate()
        self.assertEqual("intersubjectiveyay", translation)
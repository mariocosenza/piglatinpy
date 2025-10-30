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

    def test_translate_single_word_starting_with_vowel_o_and_ending_with_consonant(self):
        translator = PigLatinTranslator("ok")
        translation = translator.translate()
        self.assertEqual("okay", translation)

    def test_translate_single_word_starting_with_vowel_a_and_ending_with_consonant(self):
        translator = PigLatinTranslator("and")
        translation = translator.translate()
        self.assertEqual("anday", translation)

    def test_translate_single_word_starting_with_consonant_h(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_single_word_starting_with_consonant_y(self):
        translator = PigLatinTranslator("yo")
        translation = translator.translate()
        self.assertEqual("oyay", translation)

    def test_translate_single_word_starting_with_consonants_kn(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_single_word_starting_with_consonants_spr(self):
        translator = PigLatinTranslator("spring")
        translation = translator.translate()
        self.assertEqual("ingspray", translation)

    def test_translate_single_word_starting_with_consonants_fly(self):
        translator = PigLatinTranslator("fly")
        translation = translator.translate()
        self.assertEqual("flyay", translation)

    def test_translate_more_words(self):
        translator = PigLatinTranslator("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation)

    def test_translate_composite_words(self):
        translator = PigLatinTranslator("well-being")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay", translation)

    def test_translate_composite_and_more_words(self):
        translator = PigLatinTranslator("well-being hello world")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay ellohay orldway", translation)

    def test_translate_composite_punctuation(self):
        translator = PigLatinTranslator("well-being!")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay!", translation)

    def test_translate_upper_case(self):
        translator = PigLatinTranslator("APPLE")
        translation = translator.translate()
        self.assertEqual("APPLEYAY", translation)

    def test_translate_title_cases(self):
        translator = PigLatinTranslator("Hello")
        translation = translator.translate()
        self.assertEqual("Ellohay", translation)

    def test_translate_title_cases_and_upper_case(self):
        translator = PigLatinTranslator("Hello APPLE")
        translation = translator.translate()
        self.assertEqual("Ellohay APPLEYAY", translation)
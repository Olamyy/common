import string
from alphabet_detector import AlphabetDetector
import re
ad = AlphabetDetector()


class Alphabets(str):
    def __init__(self):
        super(Alphabets, self).__init__()
        self.characters = string.ascii_letters
        self.punctuations = string.punctuation
        self.digits = string.digits
        self.oc_digits = string.octdigits

    def __repr__(self):
        return '<Alphabets characters:%s>' % self.characters

    def __next__(self):
        pass

    def __get__(self, instance, owner):
        pass

    def __iter__(self):
        pass


class Cases:
    def __init__(self):
        self.characters = string.ascii_letters

    def customCase(self):
        pass

    def capitalize(self, characters=None):
        """
        Capitalize characters
        :param characters:
        :return:
        """
        if not characters:
            characters = self.characters
            return characters.capitalize()
        else:
            return self.characters.capitalize()

    def titleCase(self, characters=None, sentence=False):
        """

        :param sentence:
        :param characters:
        :return:
        """
        if not characters and not sentence:
            characters = self.characters
            if characters.endswith("."):
                return characters.title().replace('.', '')
            else:
                return "{0}.".format(characters.title())
        else:
            return "{0}.".format(characters.title()) if not characters.endswith('.') else "{0}".format(characters.title())

    def lowerCase(self, characters=None):
        """

        :param characters:
        :return:
        """
        if not characters:
            characters = self.characters
            return characters.lower()
        else:
            return self.characters.lower()

    def sentenceCase(self, characters=None):
        if not characters:
            characters = self.characters
            if characters.endswith("."):
                return characters.capitalize()
            else:
                return "{0}.".format(characters.capitalize())

    def camelCase(self, characters=None):
        if not characters:
            characters = self.characters
            for word in characters.split():
                words = re.sub('[\s+]', '', characters)
                return word, words


test = Cases()
test.characters= "my nam   e is   adedeji"
print(test.camelCase())

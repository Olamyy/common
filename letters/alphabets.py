import string
from alphabet_detector import AlphabetDetector
import random

ad = AlphabetDetector()


class Cases():
    def __init__(self):
        self.characters = string.ascii_letters

    def getCase(self, case_string, characters):
        if case_string == "titleCase":
            return self.titleCase(characters)
        if case_string == "lowerCase":
            return self.lowerCase(characters)
        if case_string == "sentenceCase":
            return self.sentenceCase(characters)
        if case_string == "camelCase":
            return self.camelCase(characters)

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
            return "{0}.".format(characters.title()) if not characters.endswith('.') else "{0}".format(
                characters.title())

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
            return ''.join(word for word in characters.title() if not word.isspace())
        else:
            return ''.join(word for word in self.characters.title() if not word.isspace())


class Alphabets(str, Cases):
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

    def random(self, count, use_case=None):
        """
        Generate
        :return:
        """
        output = [random.choice(self.characters) for letter in range(count)]
        if not use_case:
            return output
        else:
            return self.getCase(use_case, "".join(output))


a = Alphabets()
print(a.random(count=5))

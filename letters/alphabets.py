import string
from alphabet_detector import AlphabetDetector

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

    def uppercase(self):
        """
        Return the characters in uppercase
        :return:
        """
        return self.characters.upper()


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

    def titlecase(self, characters=None):
        """

        :param characters:
        :return:
        """
        if not characters:
            characters = self.characters
            return characters.title()
        else:
            return self.characters.title()

    def lowercase(self, characters=None):
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
                return characters.replace(characters[0], characters[0].upper(), 1)
            else:
                return characters.replace(characters[0], characters[0].upper()).replace(characters[-1], (characters[-1]
                                                                                                         + '.'), 1)

test = Cases()
test.characters= "my name is adedeji"
print(test.sentenceCase())

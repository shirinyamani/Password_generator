import random
import string
from abc import ABC, abstractclassmethod

import nltk


class PasswordGenerator(ABC): #to not be abt to make obj from

    @abstractclassmethod
    def generate(self):
        pass


class Pincode(PasswordGenerator):
    def __init__(self, length):
        self.length = length
    
    def generate(self, length=8):
        return "".join([random.choice(string.digits) for _ in range(self.length)])
    

class RandomPass(PasswordGenerator):
    def __init__(self, length=8, include_symbol = False, include_num= False):
        self.length = length
        self.charactors = string.ascii_letters
        if include_num:
            self.charactors += string.digits
        if include_symbol:
            self.charactors += string.punctuation

    def generate(self):
        return "".join([random.choice(self.charactors) for _ in range(self.length)])
    

class MemoPassword(PasswordGenerator):
    def __init__(self, num_words=4, seperator='-', capitalize= False, vocab_list= None):
        if vocab_list is None:
            vocab_list = nltk.corpus.words.words()

        self.num_words = num_words
        self.seperator = seperator
        self.capitalize = capitalize
        self.vocab_list = vocab_list

    def generate(self):
        password_words = [random.choice(self.vocab_list) for _ in range(self.num_words)]
        if self.capitalize:
            password_words = [w.upper() if random.choice([True, False]) else w.lower() for w in password_words]
        return self.seperator.join(password_words)

if __name__ == "__main__":
    p_obj = RandomPass()
    print(p_obj.generate())



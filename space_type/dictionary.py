import arcade
import random

START_WORDS = 7

class Dictionary():
    """
    Main application class.
    """

    # MAX_WORDS = 7
    def __init__(self):
        self.word_list_size = START_WORDS
        self.word_list = self.load_word_list()
        # self.word_list.append('bacon')

    def lookup_word(self,word):
        # for i in range(0,len(self.word_list)):
        if word == self.word_list[len(self.word_list) - 1]:
            return True
        return False
        
    def load_word_list(self):
        self.word_list = []
        word_bank = open('assets/words.txt', 'r')
        Lines = word_bank.read().splitlines()
        words = len(Lines) - 1
        for i in range(0,self.word_list_size -1):
            self.word_list.append(Lines[random.randint(0, words)])
        self.word_list_size +=1

    def get_current_word(self):
        return self.word_list[len(self.word_list) - 1]

    def pop(self):
        self.word_list.pop()

    def is_empty(self):
        return len(self.word_list) == 0
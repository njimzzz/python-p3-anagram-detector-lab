# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_list):
        matches = []
        for word in word_list:
            if sorted(word.lower()) == sorted(self.word) and word.lower() != self.word:
                matches.append(word)
        return matches


     
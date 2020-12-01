
from collections import defaultdict

class Letter:
    def __init__(self, char):
        self.c = char
        self.suffixes = []

    def __repr__(self):
        return self.c

    def __iter__(self):
        yield from self.suffixes

    @property
    def character(self):
        return self.c
    
    def add_suffix(self, letter):
        if letter not in self.suffixes:
            self.suffixes.append(letter)


class LetterGraph:

    def __init__(self):
        self.letter_map = {}

    def __iter__(self):
        """Used to iterate over letters in the lettermap"""
        yield from self.letter_map.values()

    def add_letter(self, char):
        """
        If the letter hasn't been added yet, add it else return given letter
        """
        if char in self.letter_map:
            return self.letter_map[char]
        letter = Letter(char)
        self.letter_map[char] = letter
        return self.letter_map[char]

    def add_letter_suffix(self, letter_char, suffix_char):
        """
        Adds a known suffix for the given letter
        """
        letter = self.add_letter(letter_char)
        suffix = self.add_letter(suffix_char)
        letter.add_suffix(suffix)


    def find_suffix(self, letter, seen, order):
        """
        Recursive function to find the absolute depth of a letters suffix,
        then once we've hit the final char, add it to the order.
        """
        seen[letter] = True
        for suff in letter:
            if suff not in seen:
                self.find_suffix(suff, seen, order)
        order.append(letter.character)

    def find_letter_order(self):
        """
        Iterate over all the characters and if we haven't seen them, find their suffix
        Runs a DFS on the letter graph and builds an ordering from last char to first,
        then return the reversed order.
        """
        seen = {}
        order = []
        for letter in self:
            if letter not in seen:
                self.find_suffix(letter, seen, order)
        return order[::-1]


class Alphabet:



    @staticmethod
    def determine_suffix(s1, s2):
        """
        Given two equal length strings, find the first characters that do not match on the index
        
        > determine_suffix("ab", "bc")
        ("a", "b")
        > determine_suffix("aab", "aac")
        ("b", "c")
        """

        for ci in range(len(s1)):
            prefix_char = s1[ci]
            suffix_char = s2[ci]
            if prefix_char != suffix_char:
                return prefix_char, suffix_char
        return None, None

    @staticmethod
    def determine_alphabet(sorted_strings):
        """
        Given a list of sorted strings, return the alphabet used to create those words.
        
        Main function for the alphabet problem
        > determine_alphabet(["bca","aaa","acb"])
        ['b','a','c']
        """
        letter_graph = LetterGraph()

        # Iterate through all the letters and add them to the graph
        # A bit ineffcient but O(n) is generally fine
        [[letter_graph.add_letter(c) for c in s] for s in sorted_strings]                   


        # Goal - iterate through our strings and find the character suffixes 
        for wi in range(len(sorted_strings)-1):

            # Grab two words
            current_word = sorted_strings[wi]
            next_word = sorted_strings[wi + 1]
            
            # if two words are the same, just skip them
            if current_word == next_word:
                continue

            # Find the prefix -> suffix char from two strings
            prefix_char, suffix_char = Alphabet.determine_suffix(current_word, next_word)
            # If we cannot find a differentiating character, then we cannot make any assertions
            if not prefix_char or not suffix_char:
                continue

            # Add the prefix -> suffix vertex to the letter graph
            letter_graph.add_letter_suffix(prefix_char, suffix_char)


        # Once the letter graph has been populated, find the ordering
        sorted_alphabet = letter_graph.find_letter_order()
        return sorted_alphabet

# Export helper
determine_alphabet = Alphabet.determine_alphabet
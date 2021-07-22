from difflib import SequenceMatcher
import pytest
import sys

def minimum_word(words):
    min = 300
    min_word = ""

    for word in words:
        if (len(word) < min):
            min = len(word)
            min_word = word
    return min_word


def common_sequence(str):
    words = str.split(" ")
    min_word = minimum_word(words)
    match = SequenceMatcher(None, min_word, words[0]).find_longest_match(0, len(min_word), 0, len(words[0]))
    sequence = min_word[match.a: match.a + match.size]

    for word in words:
        match = SequenceMatcher(None, sequence, word).find_longest_match(0, len(sequence), 0, len(word))
        current_sequence = sequence[match.a: match.a + match.size]

        if current_sequence != sequence:
            sequence = current_sequence
    return sequence


if __name__ == "__main__":
    str = sys.argv[1]
    print(common_sequence(str))

def print_upper_words(words, must_start_with):
    """ Prints all words out in upper case letters """

    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
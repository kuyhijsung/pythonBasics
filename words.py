def print_upper_words(words, must_start_with):
    """Turns the input of type String into uppercase words."""

    for word in words:
        if word.startswith(must_start_with):
            print(word.upper())


print_upper_words(["hello", "elephant", "goodbye", "yo", "hey", "eggs"], "e")

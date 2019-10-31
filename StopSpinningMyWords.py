"""
6 kyu
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all five or
more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") =>
returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

"""


def spin_words2(sentence, length=5):
    words = sentence.split()
    return " ".join([word[::-1] if len(word) >= length else word for word in words])


def spin_words(sentence):
    words = sentence.split()
    res = []
    for word in words:
        if len(word) >= 5:
            res.append(word[::-1])
        else:
            res.append(word)

    return " ".join(res)


if __name__ == "__main__":
    print(spin_words("Welcome kind world and friends"))
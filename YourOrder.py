"""
Your task is to sort a given string. Each word in the string will contain a single number.
    This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.
"""


def order(sentence):
    if sentence == "":
        return sentence

    l_sentence = sentence.split(" ")
    n = len(l_sentence)

    l_ordered = [0] * n
    for word in l_sentence:
        for letter in word:
            if letter.isdigit():
                l_ordered[int(letter) - 1] = word
                break

    return " ".join(str(x) for x in l_ordered)

def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int("".join(filter(str.isdigit, x)))))


"""
The different test cases.
"""

@Test.describe("Basic tests")
def fixed_tests():
    Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
    Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    Test.assert_equals(order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"),
                       "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor")
    Test.assert_equals(order(""), "")
    Test.assert_equals(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")


@Test.describe("Random tests")
def random_tests():
    WORDS = "a able about after all an and as ask at bad be big but by call case child come company day different do early eye fact feel few find first for from get give go good government great group hand have he her high his I important in into it know large last leave life little long look make man my new next not number of old on one or other over own part person place point problem public right same say see seem she small take tell that the their there they thing think this time to try up use want way week will with woman work work world would year you young".split()

    from random import randint, sample, shuffle

    for _ in range(50):
        arr = sample(WORDS, randint(0, 9))
        arr2 = []
        for i, w in enumerate(arr):
            letters = list(w)
            letters.insert(randint(0, len(w)), str(i + 1))
            arr2.append("".join(letters))
        expected = " ".join(arr2)
        shuffle(arr2)
        test_str = " ".join(arr2)

        @Test.it('Testing: "%s"' % test_str)
        def single_test():
            Test.assert_equals(order(test_str), expected)
import re


def word_counter():
    sentence = input("Enter a sentence: ")
    print("The number of words in the sentence is: " + str(getWordCount(sentence)))


def getWordCount(sentence: str) -> int:
    return len(re.findall("[\\w-]+", sentence))


if __name__ == "__main__":
    word_counter()

#reverses the words in a sentence
def reverse_words(s):
    word=s.split(" ")
    sentence=" ".join(reversed(word))
    print(sentence)

sen="Solving Program Algorithm"
reverse_words(sen)
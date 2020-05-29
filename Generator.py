def Sentence(sentence):
    for word in sentence.split():
        yield word

words = Sentence('This is a test')
# for word in words:
#     print(word)
print(next(words))
print(next(words))

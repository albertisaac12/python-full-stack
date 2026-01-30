def mostWordsFound(sentences: list):
        l = []
        for sen in sentences:
            l.append(sen.count(" ")+1)
        return max(l)
print(mostWordsFound(["hello hi","meow meow"]))
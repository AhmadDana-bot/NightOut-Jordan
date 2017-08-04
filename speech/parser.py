import spacy
class NlpSingelton ():
    singletonCreated = False
    singletonObject = None

    def __init__(self):
        if self.singletonCreated:
            pass
        else:
            try:
                self.singletonObject = spacy.load('en_core_web_md')
                self.singletonCreated = True
            except Exception as exc1:
                self.singletonCreated = False
                print ("could not create singleton object "+str(exc1))

def parser (phrase):
    parsed = __nlpObject__.singletonObject(phrase)
    for word in parsed:
        print(word.text, word.lemma, word.lemma_, word.tag, word.tag_, word.pos, word.pos_)
if __name__ == "__main__":
    __nlpObject__ = NlpSingelton()
    user_input = input("Enter your sentence")
    parser(user_input)


# code to reverse words in the phrase

def rev(sentence):
    revSentence = ""
    for i in sentence:
        revSentence+= (i[::-1]+" ")
    return revSentence[0:len(revSentence)-1]

sentence =  input("Enter a Phrase : ").split()
print(f"The reversed phrase is : {rev(sentence)}")
import json
import os
from rapidfuzz import fuzz
from nltk.tokenize import RegexpTokenizer
import re
import sub
from langdetect import detect
from nltk.stem import PorterStemmer
import con
from gtts import gTTS
# import spacy
#
# from spacy import displacy
from timeit import timeit
# import textacy
with open('final.json','r',encoding='utf-8') as f:
    data = json.load(f)
with open('tamword.json','r',encoding='utf-8')as r:
    data1=json.load(r)
list2=[]
def tokening(list):
    tokenizer = RegexpTokenizer(r'\w+')
    list1=tokenizer.tokenize(list)
    ps = PorterStemmer()
    for w in list1:
        list2.append(ps.stem(w))
    return list2
def spliting(string):
    return string.split()
def eng_to_tam(s1):
    total = tokening(s1)
    total2 = sub.editreco(total)

    english = []

    for j in range(len(total2)):
        for i in data:
            ratio = fuzz.ratio(total2[j].lower(), str(i['eword']))
            if (ratio == 100):
                english.append(i)
                break


    corrected_words = []
    abonded = []
    for p in english:
        corrected_words.append(p['eword'])



    for t in range(len(total2)):
        try:
            if total2[t] != corrected_words[t]:
                abonded.append(total2[t])


        except IndexError:

            abonded.append(total2[t])

    abonded = list(set(total2).difference(set(corrected_words)))
    index = []
    for u in range(len(abonded)):
        for h in total2:
            if abonded[u] == h:
                index.append(total2.index(h))

    parts = []
    hwords = []
    new_word = []

    for l in abonded:
        n = 2
        parts.append([l[i:i + n] for i in range(0, len(l), n)])  # use for splitting words
        for i in parts:
            for t in i:
                for u in data1:
                    if fuzz.ratio(t, str(u['eword'])) == 100:
                        hwords.append(u['tword'])
    words = [hwords[i:i + 2] for i in range(0, len(hwords), 2)]
    for i in words:
        new_word.append("".join(i))


    final = []
    for tword in english:
        final.append(tword['tword'])
    for i in index:
        for k in new_word:
            final.insert(i, k)
            break
    return final

def tam_to_eng(s1):
    total1 = spliting(s1)
    hindi = []
    for j in range(len(total1)):
        for i in data:
            ratio = fuzz.ratio(total1[j], str(i['tword']))
            if (ratio == 100):
                hindi.append(i)
                break

    corrected_words = []
    abonded = []

    for p in hindi:
        corrected_words.append(p['tword'])

    for t in range(len(total1)):
        try:
            if total1[t] != corrected_words[t]:
                abonded.append(total1[t])


        except IndexError:

            abonded.append(total1[t])

    abonded = list(set(total1).difference(set(corrected_words)))
    index = []
    for u in range(len(abonded)):
        for h in total1:
            if abonded[u] == h:
                index.append(total1.index(h))
    new_word = con.call(abonded, 'ta', 'en')
    if len(new_word) != 0:
        final = []
        for tword in hindi:
            final.append(tword['eword'])
        for i in index:
            for k in new_word:
                final.insert(i, k)
                break
        return final
    else:
        parts = []
        hwords = []
        new_word = []

        for l in abonded:
            n = 2
            parts.append([l[i:i + n] for i in range(0, len(l), n)])  # use for splitting words

            for i in parts:
                for t in i:
                    for u in data1:
                        if fuzz.ratio(t, str(u['tword'])) == 100:
                            hwords.append(u['eword'])
        words = [hwords[i:i + 2] for i in range(0, len(hwords), 2)]

        for i in words:
            new_word.append("".join(i))

        final = []
        for tword in hindi:
            final.append(tword['eword'])
        for i in index:
            for k in new_word:
                final.insert(i, k)
                break
        #pos(final)
        return final
def tam_to_eng1(s1):
    final = []
    for i in data:
        if (fuzz.ratio(str(s1), str(i['tword'])) >= 90):
            result = (i['eword'])
            final = result.split()
    return final

def eng_to_tam1(s1):
    final = []

    for i in data:
        value = i['eword']
        if (fuzz.ratio(s1.lower(), str(value)) >= 95):
            result = ((i['tword']))
            final = result.split()
            result=''
    # print(final)

    return final
def ngraming_3(text,ngram=3):
    words = [word for word in text.split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans =([' '.join(ngram) for ngram in temp])
    return ans
def eng_to_tam_ngram3(s1):
    final=[]
    ngram2=ngraming_3(s1)
    for x in ngram2:
        for i in data:
            value = i['eword']
            if (fuzz.ratio(x.lower(), str(value)) >= 95):
                result = ((i['eword']))
                final.append( result)
    return final

def tam_to_eng_ngram3(s1):
    final=[]
    ngram2=ngraming_3(s1)
    for x in ngram2:
        for i in data:
            value = i['tword']
            if (fuzz.ratio(x.lower(), str(value)) >= 95):
                result = ((i['tword']))
                final.append( result)
    final=[*set(final)]
    return final

def NGRAM_eng_tam(word):
    ngram =(eng_to_tam_ngram3(word))
    # print(ngram)
    new_=word.split()
    new_ngram=[]
    for i in ngram:
        new_ngram.extend(i.split())
    for x in new_ngram:
        try:
            new_.remove(x)

        except ValueError:
            pass
    indices=[]
    end_word=[]

    for u in ngram:
        indices.append(word.find(u))
        end_word.append(eng_to_tam1(u))
    new_ =" ".join(new_)
    indices.sort()

    for i in indices:
        frnt=new_[:i]
        lst = new_[i:]
        break
    if frnt ==lst:
        lst=""
    frnt =eng_to_tam(frnt)
    lst = eng_to_tam(lst)

    if frnt == lst:
        lst[0]=""
    total_wor=[]
    total_wor.extend(" ".join(frnt)+" ")
    for i in end_word:
        total_wor.extend(" ".join(i)+" ")
    total_wor.extend(" ".join(lst)+" ")

    return total_wor


def NGRAM_tam_eng(word):
    ngram = (tam_to_eng_ngram3(word))

    new_ = word.split()
    new_ngram = []
    for i in ngram:
        new_ngram.extend(i.split())
    for x in new_ngram:
        try:
            new_.remove(x)

        except ValueError:
            pass

    indices = []
    end_word = []
    for u in ngram:
        indices.append(word.find(u))
        end_word.append(tam_to_eng1(u))
    new_ = " ".join(new_)



    for i in indices:
        frnt = new_[:i+1]
        lst = new_[i:]
        break

    frnt = tam_to_eng(frnt)
    lst = tam_to_eng(lst)
    # print(frnt)
    total_wor = []
    total_wor.extend(" ".join(frnt) + " ")
    for i in end_word:
        total_wor.extend(" ".join(i) + " ")
    total_wor.extend(" ".join(lst) + " ")

    return total_wor

# word ='ஜம்மு காஷ்மீரில் இன்று 2 முறை நிலநடுக்கம் ஏற்பட்டது. இதனால் பொது மக்கள் பீதியடைந்துள்ளனர். ஜம்மு காஷ்மீரில் ரெசி மாவட்டத்தில் உள்ள கட்ர பெல்ட்டில் இன்று அதிகாலை 3.28 மணிக்கு 3.4 என்கிற ரிக்டர் அளவிலும் மற்றொன்று டோடா மாவட்டத்தில் அதிகாலை.'
word = 'ஜம்மு காஷ்மீரில் இன்று 2 முறை நிலநடுக்கம் ஏற்பட்டது. இதனால் பொது மக்கள் பீதியடைந்துள்ளனர். ஜம்மு காஷ்மீரில் ரெசி மாவட்டத்தில் உள்ள கட்ர பெல்ட்டில் இன்று.'

try:
    result = "".join(NGRAM_tam_eng(word))
except UnboundLocalError:

    result=" ".join(tam_to_eng1(word))
    if len(result) == 0:
        result =" ".join(tam_to_eng(word))

print(result)
# lang = 'ta'
#
# object =gTTS(text=result,lang=lang,slow=False)
# object.save('output.mp3')
# os.system('output.mp3')
# eng_to_tam1("how are you")
# try:
#     def pos(list):
#         taken =" ".join(list)
#         nlp = spacy.load("en_core_web_sm")
#         doc = nlp(taken)
#         for token in doc:
#             print(token.text,"|",token.pos_)
#         pattern_n = [{"POS":"NOUN"}]
#         pattern_v = [{"POS": "VERB"}]
#         pattern_p = [{"POS": "PRON"}]
#
#         noun = textacy.corpus.extract.matches.token_matches(doc,patterns=pattern_n)
#         verb = textacy.corpus.extract.matches.token_matches(doc, patterns=pattern_v)
#         pronoun = textacy.corpus.extract.matches.token_matches(doc, patterns=pattern_p)
#
#         for i in noun:
#             print(i)
#         for j in verb:
#             print(j)
#         for k in pronoun:
#             print(k)
#

# html = displacy.render(doc,style='dep')
#
# with open('Data.html','w') as f:
#     f.write(html)

# except:
#     pass


# def ngraming_3(text,ngram=3):
#     words = [word for word in text.split(" ")]
#     temp = zip(*[words[i:] for i in range(0, ngram)])
#     ans =([' '.join(ngram) for ngram in temp])
#     return ans
# def tam_to_eng_ngram(s1):
#     final=[]
#     ngram2=ngraming_3(s1)
#     for x in ngram2:
#         for i in data:
#             value = i['tword']
#             if (fuzz.ratio(x.lower(), str(value)) >= 95):
#                 result = ((i['tword']))
#                 final.append( result)
#     return final
# def NGRAM_tam_to_(word):
#     ngram =(tam_to_eng_ngram(word))
#     new_=word.split()
#     new_ngram=[]
#     last =[]
#     for i in ngram:
#         new_ngram.extend(i.split())
#     for x in new_ngram:
#         new_.remove(x)
#     indices=[]
#     for u in ngram:
#         indices.append(word.find(u))
#         end_word=" ".join(tam_to_eng1(u))
#     new_ =" ".join(new_)
#
#
#     for i in indices:
#         frnt=new_[:i]
#         lst = new_[i:]
#
#     frnt =tam_to_eng(frnt)
#     lst = tam_to_eng(lst)
#     total_wor=" ".join(frnt)+" "+end_word+" "+" ".join(lst)
#     print(total_wor)
#
#
#
#
# word=""
# # print("Your word:" ,word)
# # result =" ".join( tam_to_eng(word))
# # print(result)
# NGRAM_tam_to_(word)
#
# print(eng_to_tam("hellow how are you"))
# नमस्ते मेरे दोस्त
# क्षेत्रीय अनुवादक
# मैं प्यार कारों
#print('Execution time: ',timeit(lambda :eng_to_tam('hello'),number=1))
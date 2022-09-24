import json
from rapidfuzz import fuzz
from nltk.tokenize import RegexpTokenizer
import sub
from nltk.stem import PorterStemmer
from langdetect import detect
import numpy as np
import con
from timeit import timeit
from gtts import gTTS
import os
import re
with open('final.json','r',encoding='utf-8') as f:
    data = json.load(f)

with open('hin-alphabets.json','r',encoding='utf-8') as d:
    data1=json.load(d)


list2=[]
def tokening(list):
    tokenizer = RegexpTokenizer(r'\w+')
    list1=tokenizer.tokenize(list)
    ps = PorterStemmer()
    for w in list1:
        list2.append(ps.stem(w))
    return list1

def spliting(string):
    return string.split()

def hin_to_eng1(s1):
    final=[]
    for i in data:
        if(fuzz.token_sort_ratio(str(s1),str(i['hword']))>= 90):
            result=(i['eword'])
            final=result.split()
    return (final)

def hin_to_eng(s1):
    total1=spliting(s1)
    # print(total1)
    hindi=[]
    for j in range(len(total1)):
        for i in data:
            ratio = fuzz.ratio(total1[j], str(i['hword']))
            if (ratio ==100):
                hindi.append(i)
                break

    corrected_words = []
    abonded = []

    for p in hindi:
        corrected_words.append(p['hword'])

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
    new_word = con.call(abonded, 'hi', 'en')
    if len(new_word) !=0:
        final = []
        for tword in hindi:
            final.append(tword['eword'])

        for i in index:
            for k in new_word:
                final.insert(i,k)
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
                        if fuzz.ratio(t, str(u['hword'])) ==100:
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
        return final

un_recog=[]
def eng_to_hin(s1):
    total=tokening(s1)
    total2=sub.editreco(total)


    english = []

    for j in range(len(total2)):
        for i in data:
            ratio =fuzz.ratio(total2[j].lower(), str(i['eword']))
            if ( ratio== 100):
                english.append(i)
                break

    corrected_words=[]
    abonded=[]
    for p in english:
        corrected_words.append(p['eword'])


    for t in range(len(total2)):
        try:
            if total2[t]!=corrected_words[t]:
                abonded.append(total2[t])


        except IndexError:

            abonded.append(total2[t])

    abonded=list(set(total2).difference(set(corrected_words)))
    index=[]
    for u in range(len(abonded)):
        for h in total2:
            if abonded[u]==h:
                index.append(total2.index(h))


    new_word=con.call(abonded,'en','hi')
    if len(new_word)!=0:
        final = []
        for tword in english:
            final.append(tword['hword'])
        for i in index:
            for k in new_word:
                final.insert(i,k)
            break
        return final
    else:
        new_word=[]
        parts=[]
        wordss=[]

        for l in abonded:
            n = 2
            parts.append([l[i:i + n] for i in range(0, len(l), n)])  # use for splitting words
            for i in parts:
                for t in i:
                    for u in data1:
                        if fuzz.ratio(t, str(u['eword'])) >=80:
                            wordss.append(u['hword'])
        words = [wordss[i:i + 2] for i in range(0, len(wordss), 2)]

        for i in words:
            new_word.append("".join(i))


        final = []
        for tword in english:
            final.append(tword['hword'])

        for i in index:
            for k in new_word:
                final.insert(i, k)
                break
        return final



def eng_to_hin1(s1):
    final=[]
    for i in data:
        value=i['eword']
        if (fuzz.ratio(s1.lower(),str(value))>=95):
            result=( (i['hword']))
            final=result.split()
    return final

def ngraming(text,ngram=1):
    words = [word for word in text.split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans =([' '.join(ngram) for ngram in temp])
    return ans


def ngraming_2(text,ngram=2):
    words = [word for word in text.split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans =([' '.join(ngram) for ngram in temp])
    return ans
def ngraming_3(text,ngram=3):
    words = [word for word in text.split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans =([' '.join(ngram) for ngram in temp])
    return ans

def eng_to_hin_ngram2(s1):
    final=[]
    ngram2=ngraming_2(s1)
    for x in ngram2:
        for i in data:
            value = i['eword']
            if (fuzz.ratio(x.lower(), str(value)) >= 95):
                result = ((i['hword']))
                final.append(result)
    return final


def eng_to_hin_ngram3(s1):
    final=[]
    ngram2=ngraming_3(s1)
    for x in ngram2:
        for i in data:
            value = i['eword']
            if (fuzz.ratio(x.lower(), str(value)) >= 95):
                result = ((i['eword']))
                final.append( result)
                break
    final=[*set(final)]

    return final

def hin_to_eng_ngram3(s1):
    final=[]
    ngram2=ngraming_3(s1)
    for x in ngram2:
        for i in data:
            value = i['hword']
            if (fuzz.ratio(x.lower(), str(value)) >= 95):
                result = ((i['hword']))
                final.append( result)
    final=[*set(final)]
    return final

def regex_finder(list_word):
    result=[]
    for i in list_word:
        first=i[0]
        last=i[-1]
        try:
            length =len(i)-2
        except IndexError:
            length = len(i)-2
        pattern = "%s.{}%s".format({length}) % (first, last)
        for i in data:
            final= (re.match(pattern,str(i['eword']) ))

            if final:
                result.append(final.group())
                break
    return result


# print(regex_finder(['சொர்க்கம்','சிறிய','நரகம்']))


word ="चार साल के लंबे अंतराल के बाद एक बार फिर एशिया कप का आयोजन किया जा रहा है।"

def NGRAM_eng_hin(word):
    ngram =(eng_to_hin_ngram3(word))
    print(word)
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
        end_word.append(eng_to_hin1(u))
    new_ =" ".join(new_)
    indices.sort()

    for i in indices:
        frnt=new_[:i]
        lst = new_[i:]
        break



    frnt =eng_to_hin(frnt)
    lst = eng_to_hin(lst)
    total_wor=[]
    total_wor.extend(" ".join(frnt)+" ")
    for i in end_word:
        total_wor.extend(" ".join(i)+" ")
    total_wor.extend(" ".join(lst)+" ")

    return total_wor

def NGRAM_hin_eng(word):
    ngram = (hin_to_eng_ngram3(word))

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
        end_word.append(hin_to_eng1(u))
    new_ = " ".join(new_)



    for i in indices:
        frnt = new_[:i+1]
        lst = new_[i:]
        break

    frnt = hin_to_eng(frnt)
    lst = hin_to_eng(lst)
    # print(frnt)
    total_wor = []
    total_wor.extend(" ".join(frnt) + " ")
    for i in end_word:
        total_wor.extend(" ".join(i) + " ")
    total_wor.extend(" ".join(lst) + " ")

    return total_wor


try:
    result = "".join(NGRAM_hin_eng(word))
except UnboundLocalError:

    result="".join(hin_to_eng1(word))
    if len(result) == 0:
        result =" ".join(hin_to_eng(word))

# result = hin_to_eng(word)

# try:
#     result = "".join(NGRAM_eng_hin(word))
# except UnboundLocalError:
#
#     result=" ".join(eng_to_hin1(word))
#     if len(result) == 0:
#         result =" ".join(eng_to_hin(word))


# result =eng_to_hin(word)
print(result)
#
# # result = eng_to_hin(word)
# print(word)
# print(result)
# lang = 'hi'
#
# object =gTTS(text=result,lang=lang,slow=False)
# object.save('output.mp3')
# os.system('output.mp3')
# print(eng_to_hin("hello my friend muralidhar"))
# print('Execution time: ',timeit(lambda :eng_to_hin('how are you'),number=1))
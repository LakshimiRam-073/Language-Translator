from tamil import *
from main import *

in_lang = "English"
out_lang = "Hindi"
word="hello how are you"


def fuc(in_lang,out_lang,word):

    if in_lang=="Tamil" and out_lang=="English":
        try:
            result = NGRAM_tam_eng(word)
        except UnboundLocalError:
            result = " ".join(tam_to_eng1(word))
            if (len(result) == 0):
                result = " ".join(tam_to_eng(word))
            print("Main " + result)
        return result
    elif in_lang=="English" and out_lang=="Tamil":
        try:
            result = NGRAM_eng_tam(word)
        except UnboundLocalError:
            result = " ".join(eng_to_tam1(word))
            if (len(result) == 0):
                result = " ".join(eng_to_tam(word))
            print("Main " + result)
        return result
    elif in_lang=='English' and out_lang=='Hindi':
        try:
            result=NGRAM_eng_hin(word)
        except UnboundLocalError:
            result = " ".join(eng_to_hin1(word))
            if (len(result) == 0):
                result = " ".join(eng_to_hin(word))
            print("Main " + result)
        return result
    elif in_lang=="Hindi" and out_lang == "English":
        try:
            result=NGRAM_hin_eng(word)
        except UnboundLocalError:
            result = " ".join(hin_to_eng1(word))
            if (len(result) == 0):
                result = " ".join(hin_to_eng(word))
            print("Main " + result)
        return result

    else:
        return word


# print(fuc(in_lang,out_lang,word))
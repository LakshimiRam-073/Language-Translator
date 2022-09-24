import json
import httpcore
from googletrans import Translator
lang=['en','ta','hi','te']

whole =[]
def trans(file):
    try:
        for lan in lang:
            t = Translator()
            translated = t.translate(file,dest=lan)
            for trans in translated:
                whole.append(trans.text)


        x=[]
        try:
            for i in range(0,len(whole),len(file)):
                x.append(list(whole[i:i+len(file)]))
        except ValueError:
            return


        eng = x[0]
        tam = x[1]
        hin = x[2]
        tel = x[3]
        result=[]
        for t in range(0, len(x)):
            for lent in range(len(eng)):
                result.append(
                    {"eword": str(eng[lent].lower()), "tword": str(tam[lent]), "hword": str(hin[lent]), "teword": str(tel[lent])})

        for res in result:
            with open('final.json', 'r+',encoding='utf-8') as f:
                data = json.load(f)
                data.append(res)
                f.seek(0)
                json.dump(data, f, indent=2)
                break

    except httpcore.ConnectError:
        return

'''def trans1(list):
    t = Translator()
    for lan in lang:
        trans =t.translate(list,dest=lan)
        whole.append(trans.text)'''


def ngraming_3(text,ngram=3):
    words = [word for word in text.split(" ")]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans =([' '.join(ngram) for ngram in temp])
    return ans

li ='''जिलेट ने कहा कि दक्षिण अफ्रीका में इसकी निरंतर उपस्थिति इसे दक्षिण अफ्रीकी समाज में अपने कर्मचारियों के जीवन और उन समुदायों के लिए सार्थक योगदान देने में सक्षम बनाती है जिनमें यह संचालित होता है।
उन्होंने कहा कि वह कुछ हफ्तों के भीतर एक सिफारिश करने की उम्मीद करते हैं कि क्या मिनीस्क्राइब को कंपनी के पूर्व अधिकारियों और निदेशकों के खिलाफ मुकदमा दायर करना चाहिए।
सरकार की बिक्री निश्चित रूप से चिंताओं को बढ़ाएगी कि जापानी कंपनियां अमेरिकी तकनीक खरीदेंगी और इसका उपयोग जैव प्रौद्योगिकी व्यापार और प्रतिस्पर्धा में ऊपरी हाथ प्राप्त करने के लिए करेंगी।
हाल के महीनों में कैलिफोर्निया का परिवहन विभाग सड़क और पुल डिजाइन में अनुभवी इंजीनियरों के लिए पेनसिल्वेनिया एरिजोना और टेक्सास में भर्ती कर रहा है।
श्री बेकर सीनेट के बहुमत वाले नेता जॉर्ज मिशेल की आलोचना से बचना चाहते हैं, लेकिन राज्य सचिव के रूप में उनके दर्शक पूरी स्वतंत्र दुनिया हैं, न कि केवल कांग्रेस।
'''
splited =[]
splited =li.split()
# print(splited)

def call(list,lang,des):
    nyll=trans(list)
    if des =='hi':
        de = 'hword'
    elif des == 'en':
        de= 'eword'
    elif des == 'te':
        de = 'teword'
    elif des == 'ta':
        de = 'tword'
    if lang =='hi':
        lang = 'hword'
    elif lang == 'en':
        lang= 'eword'
    elif lang == 'te':
        lang = 'teword'
    elif lang == 'ta':
        lang = 'tword'
    with open('final.json','r',encoding='utf-8') as f:
        data =json.load(f)
    total=[]
    for ele in list:
        for i in data:
            if ele == i[lang]:
                total.append(i[de])
                break


    return total

# call(splited,'en','ta')






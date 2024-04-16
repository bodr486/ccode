import nltk
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
nltk.download("punkt") 
import pymorphy2
import os
import pickle
import re
import json
import sklearn.ensemble
class TextProcessor:
    def __init__(self):
        with open("static/pickles/tfidf.pickle", 'rb') as file:
            self.tfidf = pickle.load(file=file)
        with open("static/pickles/model.pickle", 'rb') as file:
            self.model = pickle.load(file=file)
        with open("static/pickles/model_is_alive.pickle", "rb") as file:
            self.model_is_alive = pickle.load(file=file)
        with open("static/pickles/model_subprediction.pickle", 'rb') as file:
            self.model_subprediction = pickle.load(file=file)
        self.stopwords = nltk.corpus.stopwords.words('russian')
        self.stopwords.extend([
            'что', "это", "так", "вот", "быть", "как", "в", "к", "на", 'наш', "нас", 'подписка',
            'подпишись', 'предложка', "также", "нами", "нашим", "телеграм", "который", "всё",
            "ещё", "подписаться"
        ])
        
    def message_processing(self, text: str) -> dict:
        regex = re.compile('[^А-я\s]')
        text = text.lower()        
        text = regex.sub('', text)
        text = text.replace('[%s]', '')
        text = text.replace('http', '')
        words = word_tokenize(text)
        morph = pymorphy2.MorphAnalyzer()
        lemmatized_words = [morph.parse(word)[0].normal_form for word in words]
        filtered_words = [word for word in lemmatized_words if word not in self.stopwords]
        text = ' '.join(filtered_words)
        vectorized_text = self.tfidf.transform([text])
        prediction = self.model.predict(vectorized_text.toarray())[0]
        if prediction == 'svo':
            is_alive = self.model_is_alive.predict(vectorized_text.toarray())[0]
            subprediction = self.model_is_alive.predict(vectorized_text.toarray())[0]
        else:
            is_alive, subprediction = None, None
        proba = self.model.predict_proba(vectorized_text.toarray())[0]
        result =  {
            "deanon": proba[0], 
            "descriditation_vsrf": proba[1],
            "internation_discord": proba[2],
            "lendlease": proba[3],
            "offtop": proba[4],
            "svo": proba[5],
            "is_alive": is_alive,
            "subprediction": subprediction,
            "vsrf_offensive": proba[6],
            "vsu_offensive": proba[7],
        }
        result_ru = {
            "Деанонимизация граждан РФ": proba[0], 
            "Дискредитация ВС РФ": proba[1],
            "Разжигание межнациональной розни": proba[2],
            "Военная помощь Украине": proba[3],
            "Сво": proba[5],
            "Успехи ВС РФ": proba[6],
            "Успехи ВСУ": proba[7],
        }
        return result_ru


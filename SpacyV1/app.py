from urllib.request import Request
from flask import Flask, render_template, request
from crypt import methods
from unittest import result
import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language
import nltk
from spacy.cli.download import download
download(model="es_core_news_md")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def get_lang_detector(nlp, name):
    return LanguageDetector()

def obtenerEntidades(texto):
    nlp = spacy.load("es_core_news_md")

    # Se pasa la funcion que nos permitira saber que idioma detecta
    Language.factory("language_detector", func=get_lang_detector)
    nlp.add_pipe('language_detector', last=True)

    doc = nlp(texto)

    # Si el texto esta en ingles se vuelve a procesar el texto con el modelo en ingles
    if doc._.language['language'] == 'en':
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(texto)

    # Obtenemos todas las entidades
    entidades = [(ent.label_, ent.text) for ent in doc.ents]

    return entidades, doc._.language['language']



@app.route("/process", methods = ['POST'])
def procces_text():
    if request.method == 'POST':
        opciones = request.form['taskoption']
        entidades, language = obtenerEntidades(request.form['rawtext'])
        
        if opciones == "organization":
            entidad = "ORG"
        elif opciones == "location":
            entidad = "LOC"
        elif opciones == "person":
            if language == 'en':
                entidad = "PERSON"
            else:
                entidad = "PER"

        cantidad_resultados = [ent for ent in entidades if ent[0] == entidad]
    

    return render_template("index.html", num_of_results=len(cantidad_resultados), results=cantidad_resultados)

if __name__ ==  '__main__':
    app.run(debug = True)
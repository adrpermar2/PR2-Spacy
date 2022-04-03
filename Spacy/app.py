# from crypt import methods
# from flask import Flask, render_template, request
# import spacy
# from spacy.tokens import Span


# app = Flask(__name__)



# @app.route("/", methods=["GET"])
# def home():
#     data = request.form.get("rawtext")
#     return render_template("index.html", data=data)
    
# @app.route("/process",methods=["POST"])
# def process():
#     nlp = spacy.load("es_core_news_sm")

#     doc = nlp(request.form.get("rawtext"))
#     for ent in doc.ents:
#         # Imprime en pantalla el texto y la URL de Wikipedia de la entidad
#         lista = ""
#         lista = lista + ent.text

        
#         lista = lista.split(" ")
        

#     return render_template("process.html", lista=lista)


# if __name__ == "__main__":
#     app.run(debug = True)

from crypt import methods
from flask import Flask, render_template, request
import spacy
from spacy.tokens import Span


app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    data = request.form.get("rawtext")
    return render_template("index.html", data=data)
    
@app.route("/process",methods=["POST"])
def process():
    nlp = spacy.load("es_core_news_sm")

    doc = nlp(request.form.get("rawtext"))
    for ent in doc.ents:
        # Imprime en pantalla el texto y la URL de Wikipedia de la entidad
        lista = ""
        lista = lista + ent.text

        
        lista = lista.split(" ")

        tipo = ""
        tipo = tipo + ent.label_
        tipo = tipo.split(" ")
        

    return render_template("process.html", lista=lista, tipo=tipo)


if __name__ == "__main__":
    app.run(debug = True)
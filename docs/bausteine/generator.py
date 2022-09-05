 
import random

import json

import markdownify

from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

postbeginn = "---<br>title: <br>weight: 2<br>---<br>"

ai = aitextgen(model_folder="trained_model",
                tokenizer_file="aitextgen.tokenizer.json")

def generiere (x):
    generierung = ai.generate_one(prompt=x, temperature=0.5)
    return generierung

def generiereformatiert(wort, strophen):
    ergebnis = ""
    for stelle in range(strophen):
        ergebnis = ergebnis + "## " + generiere(wort).replace(",", "</p><p>").replace(".", "</p><p>").replace("!", "</p><p>").replace("?", "</p><p>").rsplit("<p>", 1)[0]
    return ergebnis

def generierepost(wort, strophen):
    ergebnis = markdownify.markdownify(((postbeginn[:14] + wort + postbeginn[14:]) + generiereformatiert(wort, strophen)), heading_style="ATX")
    return ergebnis

#print(generierepost("Gold ", 4))

def Zufallwort():
    with open("kombinatorikliste.json", "r") as f:
        score = json.load(f)
    i = random.randint(0, 1238769 )
    ergebnis = score[i].capitalize()
    return ergebnis

def generierepost(wort, strophen):

    ergebnis = markdownify.markdownify(((postbeginn[:14] + wort + postbeginn[14:]) + generiereformatiert(wort, strophen)), heading_style="ATX")
    buchstabe = str(wort[0].capitalize())
    print(buchstabe)
    pfad = "/" + buchstabe + "/"
    zuschaff = "/home/simon/draupnirkombinatorik/content/docs/Bausteine/" + pfad + wort + ".md"
    datei = open(zuschaff, "w")
    datei.writelines(ergebnis)
    return ergebnis

def generieremehrereposts(anzahl, strophen):
    for x in range(anzahl):
        wort = Zufallwort()
        ergebnis = markdownify.markdownify(((postbeginn[:14] + wort + postbeginn[14:]) + generiereformatiert(wort, strophen)), heading_style="ATX")
        buchstabe = str(wort[0].capitalize())
        pfad = "/" + buchstabe + "/"
        zuschaff = "/home/simon/draupnirkombinatorik/content/docs/Bausteine/" + pfad + wort + ".md"
        datei = open(zuschaff, "w")
        datei.writelines(ergebnis)
        print(buchstabe)
        print(wort)


generieremehrereposts(1000, 10)

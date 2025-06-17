import json
import csv
import openpyxl
from openpyxl import Workbook
wb = Workbook()

sheet1 = wb.active
sheet1.title = "possibles derivated"
sheet1["A1"] = "derivated"
sheet1["B1"] = "possible base"


with open("dict.json", encoding="utf-8") as f:
    data = json.load(f)
with open("russian_nouns.txt", encoding="utf-8") as f:
    allnouns = [line.strip() for line in f if line.strip()] #all nouns in Russian Language

nouns_set = {lemma["text"] for lemma in data["lemmas"]} #noanimated nouns from operncorpora

nouns = [] #nouns from the ruscorpora, RNC

with open("ruscorpora_content.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        word = row["word_0"]
        if word in nouns_set:
            nouns.append(word)

cells = 2
for each in nouns:
    no_suffix = each[:-2]
    combinations = [no_suffix+"а",no_suffix]
    if no_suffix.endswith("он"):
        combinations.append(no_suffix[:-2]+"я")
    for c in combinations:
        if c in allnouns:
            sheet1["A"+str(cells)] = each
            sheet1["B"+str(cells)] = c
            cells+=1

wb.save("data.xlsx")
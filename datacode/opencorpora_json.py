from lxml import etree
import json

xml_file = "dict.opcorpora.xml"
tree = etree.parse(xml_file)
root = tree.getroot()
lemmas = []

for lemma in root.findall(".//lemma"):
    base_form = lemma.find("l").get("t")
    grammemes = set()
    for g in lemma.find("l").findall("g"):
        grammemes.add(g.get("v"))
    if "NOUN" in grammemes and "anim" in grammemes:
        lemmas.append({
            "text": base_form,
            "grammemes": list(grammemes)
        })
with open("dict.json", "w", encoding="utf-8") as f:
    json.dump({"lemmas": lemmas}, f, ensure_ascii=False, indent=2)


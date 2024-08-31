from index import *
from functions import *

Katakana_vowel = ["uni30A1", "uni30A2", "uni30A3", "uni30A4", "uni30A5",
                  "uni30A6", "uni30A7", "uni30A8", "uni30A9", "uni30AA"]


def geneXMLInfo():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(JP_Katakana, "Katakana")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(10):
        oo = str(hex(ord(Latin_vowel[o])))
        XMLAppend(xml_elements, oo, Katakana_vowel[o])
    for o in range(42):
        oo = str(hex(ord(Latin_conso[o])))
        XMLAppend(xml_elements, oo, JP_Katakana[o])

    for o in JP:
        JP_name = f"uni{o[2:].upper()}"
        XMLAppend(xml_elements, o, JP_name)

    counter = 0
    for o in CJK:
        index = counter % 86
        XMLAppend(xml_elements, o, JP_Hiragana[index])
        counter = counter + 1
        if counter % 86 == 0:
            random.shuffle(JP_Hiragana)

    return xml_elements


if __name__ == "__main__":
    START("JP", geneXMLInfo())

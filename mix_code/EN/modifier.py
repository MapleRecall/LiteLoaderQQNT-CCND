from index import *
from functions import *


def geneXMLInfo():
    xml_elements = []
    Latin_Cap_mirror = COPY(Latin_Cap)
    DeepShufferList(Number, "Number")
    DeepShufferList(Latin_Cap, "Latin Cap")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Cap[o])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Latin_Cap_mirror, weights=Latin_weight)[0]
            XMLAppend(xml_elements, o, selectedLetter)

    return xml_elements


def StartEN():
    START("EN", geneXMLInfo())

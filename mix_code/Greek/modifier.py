import unicodedata
from index import *
from functions import *


def RemoveAccents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def GetWeight():
    weight = []
    letter = []
    with open(".\\sample.txt") as f:
        greek = f.read()

    greek = greek.lower()
    greek = RemoveAccents(greek)
    for o in greek:
        if o not in letter:
            letter.append(o)
            weight.append(1)
        else:
            index = letter.index(o)
            weight[index] += 1
    print(letter, len(letter))
    print(weight, len(weight))


def geneXMLInfo():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(Greek_Cap, "Greek Cap")

    Greek_Cap_mirror = COPY(Greek_Cap)
    Greek_Cap_mirror.insert(16, 'Ξ')
    Greek_Cap_mirror.insert(25, 'Ψ')

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        oo = Greek_Sml.index(Greek_Cap_mirror[o].lower())
        XMLAppend(xml_elements, hex(0x41 + o), Greek_Cap_name[oo])
    for o in range(26):
        oo = Greek_Sml.index(Greek_Cap_mirror[o].lower())
        XMLAppend(xml_elements, hex(0x61 + o), Greek_Sml_name[oo])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Greek_Sml, weights=Greek_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = selectedLetter.upper()
                selectedLetter = Greek_Cap_name[Greek_Cap.index(selectedLetter)]
            else:
                selectedLetter = Greek_Sml_name[Greek_Sml.index(selectedLetter)]
            XMLAppend(xml_elements, o, selectedLetter)
            
    return xml_elements


def StartGreek():
    START("Greek", geneXMLInfo())

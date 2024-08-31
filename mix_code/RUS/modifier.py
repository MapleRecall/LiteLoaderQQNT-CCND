from index import *
from functions import *


def geneXMLInfo():
    xml_elements = []
    DeepShufferList(Number, "Number")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])

    random.shuffle(Russia_Cap_name)
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Russia_Cap_name[o])
    for o in range(26):
        oo = Russia_Sml_name.index(f"uni0{str(hex(int(Russia_Cap_name[o][-3:], 16) + 32))[-3:].upper()}")
        XMLAppend(xml_elements, hex(0x61 + o), Russia_Sml_name[oo])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Russia_Sml, weights=Russia_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = str(hex(int(selectedLetter, 16) - 0x20))
                selectedLetter = Russia_Cap_name[Russia_Cap.index(selectedLetter)]
            else:
                selectedLetter = Russia_Sml_name[Russia_Sml.index(selectedLetter)]
            XMLAppend(xml_elements, o, selectedLetter)

    return xml_elements


if __name__ == "__main__":
    START("RUS", geneXMLInfo())

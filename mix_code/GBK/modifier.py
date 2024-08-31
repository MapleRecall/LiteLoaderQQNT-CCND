from index import *
from functions import *

GBK = COMMON[0:7]


def geneXMLInfo():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(Latin_Cap, "Latin Cap")

    Latin_Sml_mirror = COPY(Latin_Cap)
    for index in range(len(Latin_Sml_mirror)):
        Latin_Sml_mirror[index] = Latin_Sml_mirror[index].lower()

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Sml_mirror[o])
        
    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 7
            XMLAppend(xml_elements, o, GBK[index])
            counter = counter + 1
            
    return xml_elements


if __name__ == "__main__":
    START("GBK", geneXMLInfo())


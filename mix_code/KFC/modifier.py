from index import *
from functions import *

KFC = COMMON


def geneXMLInfo():
    xml_elements = []

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Sml[o])
    
    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 12
            XMLAppend(xml_elements, o, KFC[index])
            counter = counter + 1

    return xml_elements


def StartKFC():
    START("KFC", geneXMLInfo())

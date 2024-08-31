import os
import random
import subprocess
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import compress


declaration = '<?xml version="1.0" encoding="UTF-8"?>'


def getXML(name):
    o_font = TTFont(fr".\output\{name}.TTF")
    o_font.saveXML(fr".\output\{name}.ttx")


def COPY(item):
    temp = []
    for o in item:
        temp.append(o)
    return temp


def DeepShufferList(item, name):
    counter = 0
    temp = COPY(item)

    while True:
        random.shuffle(item)
        tag_stop = True
        for o in range(len(item)):
            if temp[o] == item[o]:
                tag_stop = False
                break
        counter += 1

        if tag_stop:
            print(f"Finished shuffling \"{name}\", tried {counter} time(s).")
            break


def XMLModifier(name: str, info: list[ET.Element]):
    XML = ET.parse(f"./output/{name}.raw.ttx")
    root = XML.getroot()

    cmap = root.find('cmap')
    cmap_f = cmap.findall('cmap_format_4')

    for sub in cmap_f:
        temp = sub.attrib
        sub.clear()
        sub.extend(info)
        sub.attrib = temp

    XML.write(f"./output/{name}.ttx", xml_declaration=True, encoding='utf-8')


def XMLAppend(self, index, name):
    new_element = ET.Element("map")
    new_element.attrib = {"code": f"{index}", "name": f"{name}"}
    self.append(new_element)


def START(namespace, info, keep_procedure=False):
    getXML(f"{namespace}.raw")
    XMLModifier(namespace, info)
    subprocess.run(f'ttx -o "output\\{namespace}.ttf" "output\\{namespace}.ttx"')
    compress(f"output\\{namespace}.ttf", f"output\\{namespace}.woff2")

    if not keep_procedure:
        os.remove(f"output\\{namespace}.raw.ttx")
        os.remove(f"output\\{namespace}.ttf")
        os.remove(f"output\\{namespace}.ttx")


if __name__ == "__main__":
    pass

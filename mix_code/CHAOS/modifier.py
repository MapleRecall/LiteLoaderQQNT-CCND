import random
from index import COPY
from chao import *


def shuffleCJK():
    for lst in ("jp_name", "gb2312_name", "gb2312_add_name"):
        nn = 0
        while True:
            random.shuffle(eval(lst))
            tag_stop = True
            for o in range(len(eval(lst))):
                if eval(lst[:-5])[o].upper() == eval(lst)[o][3:]:
                    tag_stop = False
                    break

            nn += 1
            if tag_stop:
                print(f"Finished shuffling \"{lst}\", tried {nn} time(s).")
                break


def shuffleLatin():
    for lst in ("greek_name", "latin_name"):
        nn = 0
        temp = COPY(eval(lst))
        while True:
            random.shuffle(eval(lst))
            tag_stop = True
            for o in range(len(eval(lst))):
                if temp[o] == eval(lst)[o]:
                    tag_stop = False
                    break

            nn += 1
            if tag_stop:
                print(f"Finished shuffling \"{lst}\", tried {nn} time(s).")
                break


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    f.write("<!--jp-->" + '\n')
    for o in range(len(jp)):
        xml = f'      <map code="0x{jp[o]}" name="{jp_name[o]}"/>'
        f.write(xml + '\n')

    f.write("<!--gb2312-->" + '\n')
    for o in range(len(gb2312)):
        xml = f'      <map code="0x{gb2312[o]}" name="{gb2312_name[o]}"/>'
        f.write(xml + '\n')

    f.write("<!--gb2312+-->" + '\n')
    for o in range(len(gb2312_add)):
        xml = f'      <map code="0x{gb2312_add[o]}" name="{gb2312_add_name[o]}"/>'
        f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


def writeLatinInfo():
    f = open("log_latin.xml", 'w')
    f.write("<cmap>\n")

    f.write("<!--latin-->" + '\n')
    for o in range(len(latin)):
        xml = f'      <map code="{latin[o]}" name="{latin_name[o]}"/>'
        f.write(xml + '\n')

    f.write("<!--greek-->" + '\n')
    for o in range(len(greek)):
        xml = f'      <map code="{greek[o]}" name="{greek_name[o]}"/>'
        f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass

#!/usr/bin/env python
#Lars Backer

import sys
import xml.etree.ElementTree as ET

def main(argv):
    tree = ET.parse(argv[1])
    root = tree.getroot()
	
    for POINT in root.findall("POINT"):
        top = float(POINT.find("TOP_HZ").text)
        bottom = float(POINT.find("BOTTOM_HZ").text)
        start = float(POINT.find("F0_START").text)
        end = float(POINT.find("F0_END").text)
        if end < bottom or start > top or end > top or start < bottom:
            root.remove(POINT)
    tree.write(argv[2])



if __name__ == "__main__":
    main(sys.argv)

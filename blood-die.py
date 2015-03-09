#!/usr/bin/python3
#Lars Backer

import json
from collections import namedtuple


def main():
	openFile = json.load(open("blood-die.json"))
	results = []
	element = namedtuple("language","language, lclass, blood, die")
	
	for i in openFile:
		language = i[0].strip().split()
		lclass = i[1].strip().split()
		blood = i[2].strip().split()
		die = i[3].strip().split()
		
		for blooditem in blood:
			for dieitem in die:
				if(blooditem == dieitem):
					results.append(element(language,lclass,blood,die))
	print(results)


if __name__ == "__main__":
    main()

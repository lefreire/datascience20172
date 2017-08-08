import pandas as pd
import numpy as np
import math
#for graphic
import matplotlib.pyplot as plt

#Name, Allegiances, Death Year, Book of Death, Death Chapter, Book Intro Chapter, Gender, Nobility, GoT, CoK, SoS, FfC, D99wD
data = pd.read_csv("character-deaths.csv")

max_chapters = [999,999,999,999,999]

#taking the first appearance of each character
chapter_intro = []
for no_intro in data["Book Intro Chapter"]:
	if math.isnan(no_intro):
		chapter_intro = chapter_intro + [0]
	else:
		chapter_intro = chapter_intro + [int(no_intro)]

#taking the death of each character
book_death = []
for no_death in data["Book of Death"]:
	if math.isnan(no_death):
		book_death = book_death + [0]
	else:
		book_death = book_death + [int(no_death)]

#taking the chapter each character died
death_chapter = []
for chap_death in data["Death Chapter"]:
	if math.isnan(chap_death):
		death_chapter = death_chapter + [0]
	else:
		death_chapter = death_chapter + [int(chap_death)]

#taking the books each character is in
books_appearance = []
for i in range(0, len(data["GoT"])):
	temp = [[data["GoT"][i]] + [data["CoK"][i]] + [data["GoT"][i]] + [data["SoS"][i]] + [data["FfC"][i]] + [data["DwD"][i]]]
	books_appearance = books_appearance + temp

print chapter_intro
print book_death
print death_chapter
print books_appearance
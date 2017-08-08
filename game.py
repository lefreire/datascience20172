import pandas as pd
import numpy as np
import math
#for graphic
import matplotlib.pyplot as plt

#Name, Allegiances, Death Year, Book of Death, Death Chapter, Book Intro Chapter, Gender, Nobility, GoT, CoK, SoS, FfC, D99wD
data = pd.read_csv("character-deaths.csv")

max_chapters = [-1,-1,-1,-1,-1]

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
	temp = [[data["GoT"][i]] + [data["CoK"][i]] + [data["SoS"][i]] + [data["FfC"][i]] + [data["DwD"][i]]]
	books_appearance = books_appearance + temp

#taking the books each character is introduced
book_intro = []
for i in range(0, len(books_appearance)):
	for j in range(0, len(books_appearance[i])):
		if books_appearance[i][j]:
			book_intro = book_intro + [1 + j]
			break

#calculating number of chapters in each book based on chapters characters are introduced or die
#assuming at least one character is introduced or dies in the last chapter of each book
#even if it doesnt occour, this is still a good estimation 
for i in range(0, len(books_appearance)):
	max_chapters[book_intro[i] -1] = max(max_chapters[book_intro[i] -1], chapter_intro[i])
	if book_death[i]:
		max_chapters[book_death[i] -1] = max(max_chapters[book_death[i] -1], death_chapter[i])

#checking if is ok
print "chapter_intro"
print chapter_intro
print "book_death"
print book_death
print "death_chapter"
print death_chapter
print "books_appearance"
print books_appearance
print "book_intro"
print book_intro
print max_chapters

print data.head()

#calculating the life time of each character
life_time = []
#see every character in the data
for character in range(0, len(books_appearance)):
	#if the character died, it is calculated differently
	if book_death[character]:
		print data["Name"][character]
		print max_chapters[book_intro[character] -1]
		print max_chapters[book_death[character] -1]
		print chapter_intro[character]/max_chapters[book_intro[character] -1]
		print chap_death[character]/max_chapters[book_death[character] - 1]
		life_time = life_time + [1 - chapter_intro[character]/max_chapters[book_intro[character] -1] + chap_death[character]/max_chapters[book_death[character] 	 -1] + book_death[character] - book_intro[character] -1]
	else:
		life_time = life_time + [chapter_intro[character]/max_chapters[book_intro[character] -1] + 5 - book_intro[character]]

	# for book in range(0, len(books_appearance[character])):
	#calculating his life time
	#if the character appears in the first book, it needs to be older than the character that appears in the last book
	#because of this, each book has weight, the first book has weight 5 and the last, 1
	#the first appearance of each character has value depending on the book weight
	# 	#taking the first appearance of each character
	# 	if books_appearance[character][book] == 1:
	# 		first_appearance = True
			
	# 		try:
	# 			temp_a = chapter_intro[character]/max_chapters[]
	# 		except Exception:
	# 			temp_a = 
	# 		life_time = life_time + [(5 - book) + (chapter_intro[character]/max_chapters[] + chap_death[character]/max_chapters[book_death[character]]]
	# 		break

print life_time

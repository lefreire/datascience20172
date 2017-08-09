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
print "chapter_intro: ", chapter_intro
print "book_death: ", book_death
print "death_chapter: ", death_chapter
print "books_appearance: ", books_appearance
print "book_intro: ", book_intro
print "max_chapters: ", max_chapters

print "data.head(): ", data.head()

cont_deaths = 0
#calculating the life time of each character
life_time = [format(1.00, '.2f') for x in range(0, len(death_chapter))]
#see every character in the data
for character in range(0, len(books_appearance)):
	#if the character died, it is calculated differently
	if book_death[character]:
		cont_deaths += 1
		#calculating the life and death time of each character
		life_percentage = chapter_intro[character]/float(max_chapters[book_intro[character] -1])
		death_percentage = death_chapter[character]/float(max_chapters[book_death[character] -1])
		book_difference = book_death[character] - book_intro[character]
		temp = 1 - life_percentage + death_percentage + book_difference -1
		#"age" of each character in death
		total = book_death[character] -1 + death_percentage
		try:
			temp = temp/total
		except:
			print data["Name"][character]
			print data["Book of Death"][character]
			print data["Death Chapter"][character]
			print data["Book Intro Chapter"][character]
			temp = 0	
		life_time[character] = temp
    #if character is still alive
	else:
		temp = float(chapter_intro[character])/max_chapters[book_intro[character] -1] + 5 - book_intro[character]
		life_time[character] = temp

# print life_time

#building the graph
#life: the closer to 1, the earlier the character was introduced in the series
#chapter: the closer to 1, the later the character died in the book 
# axisx = [format(1.00, '.2f') for x in range(0, len(death_chapter))]
# axisy = [format(1.00, '.2f') for x in range(0, len(death_chapter))]
axisx = [1.00 for x in range(0, len(death_chapter))]
axisy = [1.00 for x in range(0, len(death_chapter))]
for i in xrange(0, len(life_time)):
	if book_death[i]:
		axisx[i] = life_time[i]
		if life_time[i] > 0.9:
			print "life"
			print data["Name"][i]
		axisy[i] = float(death_chapter[i])/max_chapters[book_death[i] -1]
		if axisy[i] > 0.9:
			print "chapter"
			print data["Name"][i]
print "X"
print axisx
print "Y"
print axisy

heatmap, xedges, yedges = np.histogram2d(axisx, axisy)
im = plt.imshow(heatmap, cmap = 'pink', interpolation = 'nearest')
plt.gca().invert_yaxis()
plt.colorbar(im)

plt.xlabel('~insert here something about x axis~')
plt.ylabel('~insert here something about y axis~')
plt.title('Game of Thrones something', bbox={'facecolor': '0.8', 'pad': 5})

plt.show()

# plt.scatter(axisx, axisy, s=80, facecolors = 'none', edgecolors = 'r')
# plt.show()
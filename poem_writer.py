#__author__ = "Lai Wei"
#__copyright__ = "Copyright 2017, Poem Generator"

import os
import nltk 
import pickle
from statistics import mode
from nltk.tokenize import word_tokenize
import random

def training():
	nouns = ["I", "she", "he", "we", "they"]
	verbs = ["am", "is", "are"]
	adverb = []
	poems = open("training/poems.txt","r", encoding='utf-8', errors='replace').read()
	for sentence in poems.split("\n"):
		words = word_tokenize(sentence)
		form = nltk.pos_tag(words)
		for word in form:
			if word[1] == 'NN':
				nouns.append(word[0])
			elif word[1] =='VB' or word[1] == 'VBD' or word[1] == 'VBG':
				verbs.append(word[0])
			elif word[1] =='RB':
				adverb.append(word[0])
	stat_noun = nltk.FreqDist(nouns)
	nouns = list(stat_noun.keys())[:150]
	stat_verb = nltk.FreqDist(verbs)
	verbs = list(stat_verb.keys())[:150]
	stat_adv = nltk.FreqDist(adverb)
	adverb = list(stat_adv.keys())[:150]
	poem_writer = poem_generator(nouns, verbs, adverb)
	open_file=open("model/writer.pickle", "wb")
	pickle.dump(poem_writer,open_file)
	open_file.close()
class poem_generator:
	def __init__(self, nouns=None, verbs=None, adverb=None):
		self.nouns = nouns
		self.verbs = verbs
		self.adverb = adverb
	def generate(self, lines = 5):
		if self.nouns == None:
			return "please initialized a trained poem_generator"

		line = 0
		while line < lines:
			line_words = random.randint(4, 8)
			if line_words % 2 == 1:
				line_words += 1
			sentence = ""
			for i in range(line_words):
				n_random = random.randint(0, 149)
				sentence += self.nouns[n_random] + " "
				if i % 3 == 1:
					adverb_random = random.randint(0, 149)
					sentence += self.adverb[adverb_random] + " "
				if i % 3 == 2:
					v = random.randint(0, 149)
					sentence += self.verbs[v] + " "
			print (sentence + "\n")
			line += 1
def write_poem(train = False, lines = 5):
	if train:
		training()
	open_file = open("model/writer.pickle", "rb")
	writer = pickle.load(open_file)
	open_file.close()
	writer.generate(lines)

write_poem(True, 10)



# -*- coding: utf-8 -*-
from collections import OrderedDict

dataset = OrderedDict({})

output = []

def check(queries, search, d):

	numberOfMatches = 0

	for query in queries:

		query = query.replace("\n", "")

		if query.upper() in str(search).upper():

			numberOfMatches+=1

			if numberOfMatches == len(queries):

				return d

	return 0

def executeQuery(command):

		text = command.replace("QUERY", "")
		text = text[1:]
		position = text.find(" ")
		numberOfResults = int(text[:position])
		originalQuery = text[position:]
		originalQuery = originalQuery[1:]

		cont = 0
		control = True

		queries = originalQuery.split(" ")

		output = []
		numberOfIterations = 0

		if numberOfResults > 0:

			keys = dataset.keys()

			while control and numberOfIterations < len(dataset):

					d = keys[numberOfIterations]

					score, search = dataset[d]
					search = str(search).replace("\n", "")
					result = check(queries, search, d)

					if result != 0:

						output.append(result)
						cont+=1

						if cont == numberOfResults:

							control = False
					numberOfIterations+=1

		print output

def extractor(command):

	if command.startswith("ADD"):

		begin = command.find(" ",4)
		end = command.find(" ",begin+1)
		#print "Begin: ", begin
		#print "End: ", end
		uid = command[begin:end]
		uid = uid[1:]
		text = command[end+1:]
		score = text[:text.find(" ")]
		#print score
		text = text.replace(score, "")
		text = text[1:]
		#print text
		data = (score, text)
		dataset[uid] = data

	elif command.startswith("DEL"):

		uid = command.replace("DEL", "")
		uid = uid[1:]
		uid = uid.replace("\n", "")
		del dataset[uid]

	elif command.startswith("QUERY"):

		executeQuery(command)

with open("dataset2") as lines:
	for line in lines:

		extractor(line)

"""print "FINAL"
for d in dataset:

	print d + " ---- " + str(dataset[d])"""
import sys
import re
#random number generate import
from random import randrange

MissedList = list()
tmpList = list()
lineUsed = "n"
tmpFile = open('MissedConnections_List.txt', 'rw')
tmpFile2 = open('tmpFile.txt', 'rw')

for line in open('MissedConnections.txt'):
	line = line.strip()
	tempEmbeddedList = list()
	tempEmbeddedList.append(line)
	tempEmbeddedList.append(lineUsed)
	MissedList.append(tempEmbeddedList)
	#enumerate is not working. Attempting to add a unique identifier to each quote
	enumerate(tempEmbeddedList)
	# attempting to remove blank lines from document, but failing so did manually
	# if re.search(r"^ \n", line):
	# 	MissedList.remove(line)

#generate random number the length of the MissedList list
NumRandom = randrange(len(MissedList))

#print embedded list element syntax
#print MissedList[1][0]

def print_random_quote():
	#generate random number the length of the MissedList list
	NumRandom = randrange(len(MissedList))
	#grab a random quote out of embedded list
	quoteUsed = MissedList[NumRandom][1]
	#if the quote variable isn't used then
	if quoteUsed == "n":
		# print str(NumRandom) + ': ' + MissedList[1][0]
		#print "Quote#: Quote"
		print str(NumRandom) + ': ' + MissedList[NumRandom][0]
		#change quoteUsed variable to "y"
		MissedList[NumRandom][1] = "y"
		#print "quote # used?: y"
		print "quote " + str(NumRandom) + " now used?: " + MissedList[NumRandom][1]
	else:
		#print Quote# is used?: y Running again.
		print str(NumRandom) + " is used?: " + quoteUsed + " Running again." 
		#generate a new random number
		NumRandom = randrange(len(MissedList))
		#run through function again
		print_random_quote()

def overwrite_List(tmpList):
	tmpFile = open('MissedConnections_List.txt', 'rw')
	tmpFile2 = open('tmpFile.txt', 'rw')
	for line in tmpFile2:
		# tmpList = str(MissedList)
		#overwrite the whole list with new variable inserted into embedded list
		tmpFile2.write(tmpList)
		# tmpFile.close()
		#print tmpList


def print_random_quote_fromFile():
	tmpFile = open('MissedConnections_List.txt', 'rw')
	#tmpFile2 = open('tmpFile.txt', 'rw')
	for line in tmpFile:
		#generate random number the length of the MissedList list
		NumRandom = randrange(len(MissedList))
		#grab a random quote out of embedded list
		quoteUsed = MissedList[NumRandom][1]
		if quoteUsed == "n":
			# print str(NumRandom) + ': ' + MissedList[1][0]
			#print "Quote#: Quote"
			print str(NumRandom) + ': ' + MissedList[NumRandom][0]
			#change quoteUsed variable to "y"
			MissedList[NumRandom][1] = "y"
			#print "quote # used?: y"
			print "quote " + str(NumRandom) + " now used?: " + MissedList[NumRandom][1]
			tmpList = str(MissedList)
			print tmpList
			return tmpList
			overwrite_List(tmpList)

			# tmpFile.close()
			# for line in tmpFile2:
			# 	tmpFile2.write(tmpList)
			# 	tmpFile2.close()
		else:
			#print Quote# is used?: y Running again.
			print str(NumRandom) + " is used?: " + quoteUsed + " Running again." 
			#generate a new random number
			NumRandom = randrange(len(MissedList))
			#run through function again
			print_random_quote_fromFile()
	



def print_MissedList ():
	print MissedList


#print_random_quote()
#print_MissedList()
print_random_quote_fromFile()
tmpFile2.close()

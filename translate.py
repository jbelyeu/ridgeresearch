#! /usr/bin/env python

from Bio.Seq import Seq
import sys

#usage function
def usage():
	if len(sys.argv) != 3:
		print("Failed execution. Expected parameters are:\nInput file of values to translate\nOutput file (will be overwritten)")
		print("Parameters given: " )
		for arg in sys.argv:
			print (arg)
		sys.exit()
	return


#create entry class to store each lump of data from the files. 
'''Should have:
	tax_id
	ID for nucleotide data (from GFF3)
	nucleotide string
	ID for peptide data (from PFAM)
	peptide string
'''
class Entry:
	taxID = ""
	nucID = ""
	nucStr = ""
	pepID = ""
	pepStr = ""
	
	#class function to translate nucleotide string into peptide string. Return translated object
	def translate(self):
		return

	#class function for entry to write the data back out 
	def write(self, outfile):
		return
	#prints object	
	def show(self):
		print("\nTaxID: " + self.taxID)
		print("Nucleotide ID: " + self.nucID)
		print("Nucleotide Sequence: " + self.nucStr)
		print("Peptide ID: " + self.pepID)
		print("Peptide Sequence: " + self.pepStr + "\n")
		return
	def validate(self):
		if (self.taxID == "" or self.nucID == "" or self.nucStr == "" or
			self.pepID == "" or self.pepStr ==""):
			print("Error validating entry: ")
			self.show()
			return False
		else:
			return True




#main should verify args, open the file passed as param 1, begin parsing
#should read the file by first creating the Entry object with empty string, then setting the fields with each of the lines read until the endo the entry is reached
#when Entry is fully ready, call the translate function, which returns the entry with the nuc string translated to peptide
#main then calls the write method to write the whole thing back out to the output file
usage()

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

line = infile.readline().strip()
while line != "":
	entry = Entry()
	entry.taxID = line
	entry.nucID = infile.readline().strip()
	entry.nucStr = infile.readline().strip()
	entry.pepID = infile.readline().strip()
	entry.pepStr = infile.readline().strip()
	delimiter = infile.readline().strip()
	
	entry.show()
	if not (isinstance(delimiter, str)) :
		print("Error: offset in parsing. Delimiter found is: ")
		print(delimiter)

	elif (len(delimiter) <= 0 ) or (delimiter[0] != "#"):
		print("Error: offset in parsing. Delimiter found is: ")
		print(delimiter)

	if (entry.validate()):
		entry.translate()
		entry.write(outfile)
	line = infile.readline().strip()




	

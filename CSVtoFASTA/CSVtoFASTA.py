#!/usr/bin/env python3

##########################################################################################################
############### CSV to FASTA :: file format converter ####################################################
##########################################################################################################
#
# Andreas Novotny, 2018-02-15
# andreas.novotny@su.se
#
##########################################################################################################
#
# Usage is bash:
# python3 CSVtoFASTA.py input_file.csv output_file.fa
#
##########################################################################################################

def CSV_to_fasta (input_file, output_file):
	counter = 0
	with open (input_file, 'r') as input_file, open (output_file, 'w') as output_file:
		for row in input_file:
			if counter == 0:
				counter += 1
			else:
				row_list=row.split(',')
				sequence=row_list[1]
				sequence=sequence.replace('\"','')
				x = ''.join(['>', sequence])
				output_file.write(x)
				output_file.write(sequence)
				output_file.write('\n')

if __name__ == '__main__':

    import sys
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	CSV_to_fasta(input_file, output_file)


##########################################################################################################
##########################################################################################################
#### EXPLANATIONS:

# Converts a CSV file containing a list of sequences (as obtained by the get.sequences() in dada2),
# and converts it to a handy FASTA format, where the sequence is its own name:
# >ATGTGTAAA
# ATGTAAAA
#
# >ATGTGCAAA
# ATGCAAAA
#
# ect...

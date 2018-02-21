#!/usr/bin/env python3

##########################################################################################################
############### FastViewer :: FASTQ sequence overwiev ####################################################
##########################################################################################################
#
# Andreas Novotny, 2018-02-21
# https://github.com/andreasnovotny/QuickTools
#
##########################################################################################################
#
# Usage in bash:
# python3 FastViewer.py input_file.fastq output_file.txt
#
##########################################################################################################

def FastViewer (input_file, output_file):
	counter = 0
	alternator =0
	rownumber = 0
	headings=0
	quality=0
	with open (input_file, 'r') as input_file, open (output_file, 'w') as output_file:
		for row in input_file:
			if alternator==0:
				alternator+=1
				continue
			if alternator==1:
				output_file.write(row)
				counter+=1
				alternator+=1
				continue
			if alternator==2:
				alternator+=1
				continue
			if alternator==3:
				alternator=0
				continue

	print('FastWiew found ',counter,' sequences')

if __name__ == '__main__':

	import sys
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	FastViewer(input_file, output_file)

##########################################################################################################

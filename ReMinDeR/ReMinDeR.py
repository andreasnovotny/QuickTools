#!/usr/bin/env python3

##########################################################################################################
############### ReMinDeR ::Rmarkdown - Rscript converter #################################################
##########################################################################################################

# Andreas Novotny, 2018-02-07
# andreas.novotny@su.se

##########################################################################################################

# Usage is bash:
# python3 ReMinDeR.py Rmd_file R_file input_format=Rmd

def Rmd_to_R (file_Rmd, file_R):
	Alternator = 0
	Counter = 0
	with open (file_Rmd, 'r') as input_file, open (file_R, 'w') as output_file:
		for row in input_file:
			if Alternator == 0:
				if row.startswith("```"):
					Alternator = 1
					Counter += 1
					output_file.write("\n")
					
				else:
					output_file.write(''.join(['# ', row]))
				
				continue
			
			if Alternator == 1:
				if row.startswith("```"):
					Alternator = 0
				
				else:
					output_file.write(row)
	
	print("Combined", Counter, "R-code chunks in", file_R)


def R_to_Rmd (file_R, file_Rmd):
	Counter = 0
	Alternator = 0
	with open (file_R, 'r') as input_file, open (file_Rmd, 'w') as output_file:
		for row in input_file:
			if Alternator == 0:
				if row.startswith('#'):
					output_file.write(row.lstrip('#'))
					continue
				
				if row.startswith(' ') or row.startswith('\n'):
					output_file.write(row)
					continue
				else:
					Alternator = 1
					output_file.write("```{R}\n")
					Counter += 1
					output_file.write(row)
					continue

			if Alternator == 1:
				if row.startswith("#"):
					Alternator = 0
					output_file.write("```\n")
					output_file.write(row.lstrip('#'))
					continue
				else:
					output_file.write(row)

	print("Created", Counter, "R-code chunks in", file_Rmd)

def ReMinDeR (file_Rmd, file_R, input_format = 'Rmd'):
	print (input_format)
	if input_format == 'Rmd':
		Rmd_to_R(file_Rmd, file_R)
	
	if input_format == 'R':
		R_to_Rmd(file_R, file_Rmd)


if __name__ == '__main__':

	import sys
	ReMinDeR(sys.argv[1], sys.argv[2], sys.argv[3])


##########################################################################################################
##########################################################################################################
#### EXPLANATIONS:

# Elegant convertion of R markdown files to R scripts
# Rough converstion
# -*- coding: utf-8 -*-

import codecs,os,sys,re

ruleFile = open('normalize.rules', 'r')
rules = ruleFile.readlines()
ruleFile.close()


def normalize(line):

	for rule in rules:
		rule = rule.split('\t')
		
		if ( '#' or "" ) in rule[0] or len(rule) < 2 :
			continue
#		print rule
#		print list(line)
		#print rule[0], rule[1]	
		#line = line.replace(rule[0],rule[1])
		line = re.sub(rule[0].decode('utf-8'),rule[1].decode('utf-8'),line,)
#		print list(line)
#		line = line.replace(rule[0],rule[1])
#		print list(line)

	
	return line



if __name__ == '__main__':

	if len(sys.argv) < 2 :
		print "Usage: python normalize.py <infile> <outfile>"

	with codecs.open(sys.argv[1],'r','utf-8') as inpfile:
		with codecs.open(sys.argv[2],'w','utf-8') as outfile:
			for line in inpfile:
				normalized_line = normalize(line)
#				print list(normalized_line)
				outfile.write(normalized_line)
		

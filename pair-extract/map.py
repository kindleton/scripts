from Levenshtein import distance
import sys
from collections import defaultdict


def norm_dist(str1, str2):
	dist = distance(str1,str2)
	max_len = max(len(str1),len(str2))
	norm = dist/float(max_len)
	return norm

map_file = open(sys.argv[1],'r+')

mappings = defaultdict()

for line in map_file:
	line = line.decode('utf-8').split('\t')
	#assuming col1 = ARB and col2=DEV
	mappings[line[1].strip()] = line[0]
map_file.close()

#print line[1] , mappings[line[1]]


def modify_to_snd(str1,maps):
	#assuming: maps is a dict, key = hin(unicodes) , val = arb(unicodes)
	for pair in maps.items():
		str1 = str1.replace(pair[0],pair[1])
	return str1


pair_file = open(sys.argv[2],'r+')

for pair in pair_file:
	hin , snd = pair.decode('utf-8').split()
	hin_modified = modify_to_snd(hin,mappings)
	dist = norm_dist(hin_modified,snd)

#	print dist, hin.encode('utf-8'), hin_modified.encode('utf-8'), snd.encode('utf-8')
	print str(dist)+'\t'+hin.encode('utf-8')+'\t\t'+snd.encode('utf-8')
#print mappings

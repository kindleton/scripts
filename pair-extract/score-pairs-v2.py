from Levenshtein import distance
import os,sys
from collections import defaultdict


def norm_dist(str1, str2):
	dist = distance(str1,str2)
	max_len = max(len(str1),len(str2))
	norm = dist/float(max_len)
	return norm,dist

map_file = open(sys.argv[1],'r+')
map_rev_file = open(sys.argv[2],'r+')

#map devnagari to intermediate
map_d2i = defaultdict()
#map arabic to intermediate
map_s2i = defaultdict()

for line in map_file:
	line = line.decode('utf-8').split('\t')
	#assuming col1 = ARB and col2=DEV
	map_d2i[line[1].strip()] = line[0]
map_file.close()

for line in map_rev_file:
	line = line.decode('utf-8').split('\t')
	#assuming col1 = ARB and col2=INTERIM
	map_s2i[line[0]] = line[1].strip()
map_rev_file.close()


def modify_to_int(str1,maps):
	#assuming: maps is a dict, key = to-be-replaced(unicodes) , val = intermediate(unicodes)
	for pair in maps.items():
		str1 = str1.replace(pair[0],pair[1])
	return str1

pair_file = open(sys.argv[3],'r+')
file_size = os.stat(sys.argv[3]).st_size
cnt = 0
for pair in pair_file:
	cnt += len(pair)
	percentage_completion = (cnt * 100.0) / file_size
	sys.stderr.write("\r %f %% processed"%(percentage_completion))

	try :
		hin , snd = pair.split()
		hin = hin.decode('utf-8')
		snd = snd.decode('utf-8')
	except :
		sys.stderr.write(pair)
		continue

	# a randonm threshold for cleaning out pairs with huge length difference 
	#( equivalent to a cleaning step in MOSES)
	if abs(len(hin)-len(snd)) > 3 :
		continue

	hin_modified = modify_to_int(hin,map_d2i)
	snd_modified = modify_to_int(snd,map_s2i)

	norm , dist = norm_dist(hin_modified,snd_modified)

	if dist > 2 : #assuming maps.txt had dev-matras to NULL mappings
		continue

	print dist, hin.encode('utf-8'), hin_modified.encode('utf-8'), snd.encode('utf-8')
	print str(norm)+'\t'+hin.encode('utf-8')+'\t'+snd.encode('utf-8')
#print mappings

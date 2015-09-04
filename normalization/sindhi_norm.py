# -*- encoding: utf-8 -*-

import sys,re
f1 = open(sys.argv[1],'r')

for line in f1:
	if u'\u0952'.encode('utf-8') in line:
		lineObject = line.decode('utf-8')
		flag = 0
		line2 = ''
		for letter in lineObject[::-1]:
			if u'\u0952' in letter:
				flag = 1
				#print 'found'
				continue

			if flag:
				if letter == u'\u0921':
					letter = re.sub(u'\u0921',u'\u097e',letter)
					flag = 0
					#print 'found'
				elif letter == u'\u0917':
					letter = re.sub(u'\u0917',u'\u097b',letter)
					flag = 0
				elif letter == u'\u091c':
					letter = re.sub(u'\u091c',u'\u097c',letter)
					flag = 0
				elif letter == u'\u092c':
					letter = re.sub(u'\u092c',u'\u097f',letter)
					flag = 0
			line2 += letter
		line2 = line2[::-1]
		#print ''.join(reversed(line2)),
		print line2.encode('utf-8'),

	else:
		print line,
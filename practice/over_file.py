primeslist = []
with open('primenumbers.txt') as primesfile:
	line = primesfile.readline()
	while line:
		primeslist.append(int(line))
		line = primesfile.readline()

happieslist = []
with open('happynumbers.txt') as happiesfile:
	line = happiesfile.readline()
	while line:
		happieslist.append(int(line))
		line = happiesfile.readline()

overlaplist = []
for elem in primeslist:
	if elem in happieslist:
		overlaplist.append(elem)
		
print(overlaplist)

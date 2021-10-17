# Singular integer right triangles

'''

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, 
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, 
and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

'''

import eulerlib, fractions


def compute():
	LIMIT = 1500000
	# 
	# Pythagorean triples theorem:
	#   Every primitive Pythagorean triple with a odd and b even can be expressed as
	#   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
	# 
	triples = set()
	for s in range(3, eulerlib.sqrt(LIMIT) + 1, 2):
		for t in range(s - 2, 0, -2):
			if fractions.gcd(s, t) == 1:
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a + b + c <= LIMIT:
					triples.add((a, b, c))
	
	ways = [0] * (LIMIT + 1)
	for triple in triples:
		sigma = sum(triple)
		for i in range(sigma, len(ways), sigma):
			ways[i] += 1
	
	ans = ways.count(1)
	return str(ans)


if __name__ == "__main__":

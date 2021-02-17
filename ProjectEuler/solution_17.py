'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

'''

# the final list that holds the string lengths
addList = [] 

# dictionary holding integer:corresponding word pairs
numbersDict = { 
0:"zero",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety"
}

### There has to be an easier way to do all this below ###

def numberLetters(num):

    letters = ""

    if 0 < num <= 20:
        letters += numbersDict[num]

    if 21 <= num <= 99:
        a,b = divmod(num, 10)
        if b == 0:
            letters += numbersDict[a*10]
        else:
            letters += numbersDict[a*10] + numbersDict[b]

    if 100 <= num <= 999:
        if num % 100 == 0:
            letters += numbersDict[int(num / 100)] + "hundred"
        else:
            digit = int(num / 100)
            num = num - digit * 100
            if 0 < num <= 20:
                letters += numbersDict[digit] + "hundredand" + numbersDict[num]
            if 21 <= num <= 99:
                a,b = divmod(num, 10)
                if b == 0:
                    letters += numbersDict[digit] + "hundredand" + numbersDict[a*10]
                else:
                    letters += numbersDict[digit] + "hundredand" + numbersDict[a*10] + numbersDict[b]
    if num == 1000:
        letters += "onethousand"

    return letters

for i in range(1,1001):
    addList.append(len(numberLetters(i)))
print(sum(addList))

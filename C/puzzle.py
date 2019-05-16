import weel


def findspace(p):
	for i in range(15,-1,-1):
			if (puzzle[i] == " "):
				return i
al = [[" ",None],["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],["g",7],["h",8],["i",9],["j",10],["k",11],["l",12],["m",13],["n",14],["o",15],["p",16],["q",17],["r",18],["s",19],["t",20],["u",21], ["v",22],["w",23],["x",24],["y",25],["z",26]]
def stringtolist(string):
    lis = [] #this exists because strings don't support assignment
    for i in range(len(string)):
        lis.append(string[i])
    return lis
def convert_to_puzz(puzzle,al):
	if (len(puzzle) <= 16):
		str1 = puzzle
		str1 += " " * (16-len(str1))
		str2 = " "*16
		str3 = " "*16
		str4 = " "*16
	elif(len(puzzle) > 16 and len(puzzle) <=32):
		if (puzzle[16] == " "):
			str1 = puzzle[0:15]
			str2 = puzzle[17:]
			str3 = " "*16
			str4 = " "*16
		else:
			findspace(p)
			str1 = puzzle[0:i]
			str1 += " " * (16-len(str1))
			if(len(puzzle[i+1:]) <= 16):
				str2 = puzzle[i+1:]
				str3 = " "*16
				str4 = " "*16
			else:

				str2 = puzzle[i+1:]

	encodedpuzzle = stringtolist(puzzle.lower())
    for i in range(len(puzzle)): #this function will be the basis for how encoded puzzles can be displayed while keeping the original intact
        for j in range(len(al)):
            if (encodedpuzzle[i] == al[j][0]):
                encodedpuzzle[i] = al[j][1]
                break
    return encodedpuzzle
def listoletters():
    return ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def listoconsonants():
    return ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def listovowels():
    return ['a','e','i','o','u']
def checkforints(ep):
    anyints = False
    for i in range(len(ep)):
        if (type(ep[i]) == int):
            anyints = True
            break
    return anyints
def guessL():
    guess = input("please guess a consonant")
    guess = guess[0]
    jeff = []
    jeff.append(guess)
    if ((jeff[0] in listoconsonants()) == 0):
        guessL()
    return jeff[0]
def reveal(g,ep,p):
    changes = False
    for i in range(len(ep)):
        print g[0], p[i]
        if (g[0] == p[i]):
            
            ep[i] = p[i]
            changes = True
    return ep, changes
def solve(p, ep):
    guess = input("please guess a phrase")
    if (guess == p):
      ep = p
    


    
    
    


        


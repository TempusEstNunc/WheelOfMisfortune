import Tkinter as tk
from random import randint as R
from weel import *
import speech_recognition as sr
import pyttsx3
from time import sleep, time
import Adafruit_ADS1x15
from buttons import *
global BEBEG
BEBEG = True

adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1


al = [[" ",None],["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],["g",7],["h",8],["i",9],["j",10],["k",11],["l",12],["m",13],["n",14],["o",15],["p",16],["q",17],["r",18],["s",19],["t",20],["u",21], ["v",22],["w",23],["x",24],["y",25],["z",26]]

class player(object):
        """docstring for ClassName"""
        def __init__(self, pn):
                self.pn = pn
                self.score = 0
                self.totalscore = 0



                
class Game(Toplevel1):
        """docstring for ClassName"""
        def __init__(self, top):
                Toplevel1.__init__(self,top)
                self.changes = False
                self.revealed = 0
                self.rounds = 3
                self.rn = 1
                self.l2p = {
                        " " : "space.gif",
                        "a" : "a.gif",
                        "b" : "b.gif",
                        "c" : "c.gif",
                        "d" : "d.gif",
                        "e" : "e.gif",
                        "f" : "f.gif",
                        "g" : "g.gif",
                        "h" : "h.gif",
                        "i" : "i.gif",
                        "j" : "j.gif",
                        "k" : "k.gif",
                        "l" : "l.gif",
                        "m" : "m.gif",
                        "n" : "n.gif",
                        "o" : "o.gif",
                        "p" : "p.gif",
                        "q" : "q.gif",
                        "r" : "r.gif",
                        "s" : "s.gif",
                        "t" : "t.gif",
                        "u" : "u.gif",
                        "v" : "v.gif",
                        "w" : "w.gif",
                        "x" : "x.gif",
                        "y" : "y.gif",
                        "z" : "z.gif",
                        "int": "blank.gif"  
                
                }
                self.wedges = ["lose","bankrupt","lose","bankrupt",250,300,350,400,450,500,550,600,700,800]
                self.jeff = [["it is literally right there bro","F3"],["a bird in the hand is worth two in the bush","Saying"],["spill the beans","Saying"],["until the cows come home","Saying"],\
                             ["sweet dreams are made of these","Song Titles"],["fly me to the moon","Song Titles"],["the sound of silence","Song Titles"],["everybody wants to rule the world","Song Titles"],\
                             ["open sesame street","Before & After"],["deep purple rain","Before & After"],["stained glass windows vista","Before & After"], ["monty python and the holy grail", "Movie Titles"], ["the empire strikes back", "Movie Titles"]]
                self.p1 = player(1)
                self.p2 = player(2)
                self.p3 = player(3)
                self.currentplayer = self.p3
                self.al = [[" ",None],["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],["g",7],["h",8],["i",9],["j",10],["k",11],["l",12],["m",13],["n",14],["o",15],["p",16],["q",17],["r",18],["s",19],["t",20],["u",21], ["v",22],["w",23],["x",24],["y",25],["z",26]]
                
                self.Button1.configure(command =lambda: self.go())
                

        def listoconsonants(self):
                return ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        def listovowels(self):
                return ['a','e','i','o','u']
        def go(self):
                self.Button1.destroy()
                self.puzzlestart()
                self.play()

                
        def puzzlestart(self):
                self.p1.score = 0
                self.p2.score = 0
                self.p3.score = 0
                self.solved = False
                self.remaining_consonants = self.listoconsonants()
                self.remaining_vowels = self.listovowels()
                self.utpuzzle,self.category = self.getpuzzle()
                self.puzzle = self.makepuzzle(self.utpuzzle)
                self.encodedpuzzle = self.convert_to_puzz()
                self.Label221.configure(text='Category: {}'.format(self.category))
                self.puzzleupdate()
                self.texToSpeech("And the Category is {}".format(self.category))
                
                


        def getpuzzle(self):
                
                pn = R(0,len(self.jeff)-1)
                jeff = self.jeff[pn][0]
                james = self.jeff[pn][1]
                self.jeff.remove(self.jeff[pn])
                return jeff,james


        def makepuzzle(self,puzzle):
                puzzle += " " * (64- len(puzzle))
                if (puzzle[16] == " "):
                        str1 = puzzle[0:16]
                        puzzle = puzzle[17:]
                else: 
                        for i in range(15,-1,-1):
                                if (puzzle[i]== " "):
                                        break
                        str1 = puzzle[0:i]
                        str1 += (16-len(str1)) * " " 
                        puzzle = puzzle[i+1:]
                if (puzzle[16] == " "):
                        str2 = puzzle[0:16]
                        puzzle = puzzle[17:]
                else: 
                        for i in range(15,-1,-1):
                                if (puzzle[i]== " "):
                                        break
                        str2 = puzzle[0:i]
                        str2 += (16-len(str2)) * " " 
                        puzzle = puzzle[i+1:]
                if (puzzle[16] == " "):
                        str3 = puzzle[0:16]
                        puzzle = puzzle[17:]
                else:

                        for i in range(15,-1,-1):
                                if (puzzle[i]== " "):
                                        break
                        str3 = puzzle[0:i]
                        str3 += (16-len(str3)) * " " 
                        puzzle = puzzle[i+1:]
                str4 = puzzle[0:16]
                str4 += (16-len(str4)) * " "

                return str1+str2+str3+str4

        def puzzleupdate(self):
                

                self.text = "Round Cash: $"+ str(self.p3.score)+"\nTotal Cash: $"+str(self.p3.totalscore)
                self.Label3_76.configure(text=self.text)
                self.Label3_76.text = self.text
                self.text = "Round Cash: $"+ str(self.p2.score)+"\nTotal Cash: $"+str(self.p2.totalscore)
                self.Label3_75.configure(text=self.text)
                self.Label3_75.text = self.text
                self.text = "Round Cash: $"+ str(self.p1.score)+"\nTotal Cash: $"+str(self.p1.totalscore)
                self.Label3.configure(text=self.text)
                self.Label3.text = self.text
                self.text = ""
                for i in range(len(self.remaining_consonants)):
                        self.text+= self.remaining_consonants[i] + ", "
                self.text = self.text[0:-2]
                self.text += "\n"
                for i in range(len(self.remaining_vowels)):
                        self.text+= self.remaining_vowels[i] + ", "
                self.text = self.text[0:-2]
                self.text = self.text.upper()
                self.Label0.configure(text=self.text)
                self.Label0.text = self.text
                




                if (type(self.encodedpuzzle[0])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[0]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[0]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_1.configure(image=self.image)
                self.panel_1.image = self.image
                
                if (type(self.encodedpuzzle[1])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[1]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[1]]
                self.image = tk.PhotoImage(file=phrase)


                self.panel_2.configure(image=self.image)

                self.panel_2.image = self.image
                

                if (type(self.encodedpuzzle[2])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[2]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[2]]
                self.image = tk.PhotoImage(file=phrase)


                self.panel_3.configure(image=self.image)

                self.panel_3.image = self.image
                

                if (type(self.encodedpuzzle[3])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[3]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[3]]
                self.image = tk.PhotoImage(file=phrase)


                self.panel_4.configure(image=self.image)

                self.panel_4.image = self.image
                

                if (type(self.encodedpuzzle[4])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[4]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[4]]
                self.image = tk.PhotoImage(file=phrase)


                self.panel_5.configure(image=self.image)

                self.panel_5.image = self.image
                

                if (type(self.encodedpuzzle[5])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[5]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[5]]
                self.image = tk.PhotoImage(file=phrase)

                
                self.panel_6.configure(image=self.image)

                self.panel_6.image = self.image
                

                if (type(self.encodedpuzzle[6])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[6]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[6]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_7.configure(image=self.image)

                self.panel_7.image = self.image
                

                if (type(self.encodedpuzzle[7])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[7]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[7]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_8.configure(image=self.image)

                self.panel_8.image = self.image
                

                if (type(self.encodedpuzzle[8])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[8]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[8]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_9.configure(image=self.image)

                self.panel_9.image = self.image
                

                if (type(self.encodedpuzzle[9])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[9]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[9]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_10.configure(image=self.image)

                self.panel_10.image = self.image
                

                if (type(self.encodedpuzzle[10])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[10]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[10]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_11.configure(image=self.image)

                self.panel_11.image = self.image
                
                if (type(self.encodedpuzzle[11])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[11]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[11]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_12.configure(image=self.image)
                self.panel_12.image = self.image
                
                if (type(self.encodedpuzzle[12])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[12]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[12]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_13.configure(image=self.image)

                self.panel_13.image = self.image
                

                if (type(self.encodedpuzzle[13])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[13]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[13]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_14.configure(image=self.image)

                self.panel_14.image = self.image
                

                if (type(self.encodedpuzzle[14])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[14]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[14]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_15.configure(image=self.image)

                self.panel_15.image = self.image
                
                if (type(self.encodedpuzzle[15])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[15]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[15]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_16.configure(image=self.image)

                self.panel_16.image = self.image

                if (type(self.encodedpuzzle[16])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[16]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[16]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_17.configure(image=self.image)

                self.panel_17.image = self.image
                
                if (type(self.encodedpuzzle[17])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[17]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[17]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_18.configure(image=self.image)

                self.panel_18.image = self.image
                
                if (type(self.encodedpuzzle[18])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[18]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[18]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_19.configure(image=self.image)

                self.panel_19.image = self.image
                
                if (type(self.encodedpuzzle[19])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[19]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[19]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_20.configure(image=self.image)

                self.panel_20.image = self.image
                
                if (type(self.encodedpuzzle[20])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[20]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[20]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_21.configure(image=self.image)

                self.panel_21.image = self.image
                
                if (type(self.encodedpuzzle[21])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[21]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[21]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_22.configure(image=self.image)

                self.panel_22.image = self.image
                
                if (type(self.encodedpuzzle[22])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[22]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[22]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_23.configure(image=self.image)

                self.panel_23.image = self.image
                
                if (type(self.encodedpuzzle[23])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[23]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[23]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_24.configure(image=self.image)

                self.panel_24.image = self.image
                
                if (type(self.encodedpuzzle[24])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[24]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[24]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_25.configure(image=self.image)

                self.panel_25.image = self.image
                
                if (type(self.encodedpuzzle[25])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[25]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[25]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_26.configure(image=self.image)

                self.panel_26.image = self.image
                
                if (type(self.encodedpuzzle[26])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[26]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[26]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_27.configure(image=self.image)

                self.panel_27.image = self.image
                
                if (type(self.encodedpuzzle[27])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[27]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[27]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_28.configure(image=self.image)

                self.panel_28.image = self.image
                
                if (type(self.encodedpuzzle[28])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[28]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[28]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_29.configure(image=self.image)

                self.panel_29.image = self.image
                
                if (type(self.encodedpuzzle[29])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[29]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[29]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_30.configure(image=self.image)

                self.panel_30.image = self.image
                
                if (type(self.encodedpuzzle[30])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[30]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[30]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_31.configure(image=self.image)

                self.panel_31.image = self.image
                
                if (type(self.encodedpuzzle[31])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[31]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[31]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_32.configure(image=self.image)

                self.panel_32.image = self.image
                
                if (type(self.encodedpuzzle[32])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[32]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[32]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_33.configure(image=self.image)

                self.panel_33.image = self.image
                
                if (type(self.encodedpuzzle[33])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[33]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[33]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_34.configure(image=self.image)

                self.panel_34.image = self.image
                
                if (type(self.encodedpuzzle[34])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[34]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[34]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_35.configure(image=self.image)

                self.panel_35.image = self.image
                
                if (type(self.encodedpuzzle[35])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[35]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[35]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_36.configure(image=self.image)

                self.panel_36.image = self.image
                
                if (type(self.encodedpuzzle[36])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[36]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[36]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_37.configure(image=self.image)

                self.panel_37.image = self.image
                
                if (type(self.encodedpuzzle[37])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[37]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[37]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_38.configure(image=self.image)

                self.panel_38.image = self.image
                
                if (type(self.encodedpuzzle[38])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[38]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[38]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_39.configure(image=self.image)

                self.panel_39.image = self.image
                
                if (type(self.encodedpuzzle[39])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[39]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[39]]
                self.image = tk.PhotoImage(file=phrase)      
                self.panel_40.configure(image=self.image)

                self.panel_40.image = self.image
                
                if (type(self.encodedpuzzle[40])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[40]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[40]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_41.configure(image=self.image)
                self.panel_41.image = self.image



                if (type(self.encodedpuzzle[41])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[41]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[41]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_42.configure(image=self.image)
                self.panel_42.image = self.image


                if (type(self.encodedpuzzle[42])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[42]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[42]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_43.configure(image=self.image)
                self.panel_43.image = self.image


                if (type(self.encodedpuzzle[43])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[43]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[43]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_44.configure(image=self.image)
                self.panel_44.image = self.image


                if (type(self.encodedpuzzle[44])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[44]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[44]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_45.configure(image=self.image)
                self.panel_45.image = self.image


                if (type(self.encodedpuzzle[45])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[45]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[45]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_46.configure(image=self.image)
                self.panel_46.image = self.image


                if (type(self.encodedpuzzle[46])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[46]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[46]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_47.configure(image=self.image)
                self.panel_47.image = self.image


                if (type(self.encodedpuzzle[47])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[47]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[47]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_48.configure(image=self.image)
                self.panel_48.image = self.image


                if (type(self.encodedpuzzle[48])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[48]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[48]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_49.configure(image=self.image)
                self.panel_49.image = self.image


                if (type(self.encodedpuzzle[49])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[49]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[49]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_50.configure(image=self.image)
                self.panel_50.image = self.image


                if (type(self.encodedpuzzle[50])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[50]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[50]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_51.configure(image=self.image)
                self.panel_51.image = self.image


                if (type(self.encodedpuzzle[51])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[51]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[51]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_52.configure(image=self.image)
                self.panel_52.image = self.image


                if (type(self.encodedpuzzle[52])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[52]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[52]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_53.configure(image=self.image)
                self.panel_53.image = self.image


                if (type(self.encodedpuzzle[53])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[53]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[53]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_54.configure(image=self.image)
                self.panel_54.image = self.image


                if (type(self.encodedpuzzle[54])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[54]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[54]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_55.configure(image=self.image)
                self.panel_55.image = self.image

                if (type(self.encodedpuzzle[55])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[55]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[55]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_56.configure(image=self.image)
                self.panel_56.image = self.image


                if (type(self.encodedpuzzle[56])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[56]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[56]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_57.configure(image=self.image)
                self.panel_57.image = self.image

                if (type(self.encodedpuzzle[57])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[57]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[57]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_58.configure(image=self.image)
                self.panel_58.image = self.image


                if (type(self.encodedpuzzle[58])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[58]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[58]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_59.configure(image=self.image)
                self.panel_59.image = self.image


                if (type(self.encodedpuzzle[59])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[59]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[59]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_60.configure(image=self.image)
                self.panel_60.image = self.image


                if (type(self.encodedpuzzle[60])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[60]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[60]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_61.configure(image=self.image)
                self.panel_61.image = self.image


                if (type(self.encodedpuzzle[61])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[61]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[61]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_62.configure(image=self.image)
                self.panel_62.image = self.image


                if (type(self.encodedpuzzle[62])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[62]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[62]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_63.configure(image=self.image)
                self.panel_63.image = self.image


                if (type(self.encodedpuzzle[63])== int):
                        phrase = self.l2p['int']
                elif (self.encodedpuzzle[63]== None):
                        phrase = self.l2p[' ']
                else:
                        phrase = self.l2p[self.encodedpuzzle[63]]
                self.image = tk.PhotoImage(file=phrase)

                self.panel_64.configure(image=self.image)
                self.panel_64.image = self.image
                root.update()

        def spin(self):
                wedge = R(0,30)
                
                adc.start_adc(0, gain = GAIN)
                print('Reading ADS1x15 channel 0 for 5 seconds...')
                start = time()
                while((time() - start) <= 5.0):
                        value = adc.get_last_result()
                        print('Channel 0: {0}'.format(value))
                        sleep(0.5)
                adc.stop_adc
                if (ButtonPressed()):
                        self.rn = 4
                        self.solved = True
                wedge += value
                wedge %= len(self.wedges)
                wedge1 = self.wedges[wedge]
                if (type(wedge1) == int): 
                        self.text = "$"+ str(wedge1)
                elif(wedge1 == "lose"):
                        self.text = "Lose a Turn."
                else:
                        self.text = "Bankrupt!"
                self.Label22.configure(text=self.text)
                self.Label22.text = self.text
                root.update()
                if (type(wedge1) == str):
                        if (wedge1 == "lose"):
                                self.texToSpeech("Lose a Turn.")
                                
                        else:
                                self.texToSpeech("Bankrupt. Oof")
                                self.currentplayer.score = 0
                else:
                        self.texToSpeech("{} dollars".format(wedge1))
                        self.currentplayer.score += wedge1 * self.reveal()

        def reveal(self):
                while (True):
                        guess = self.speechInitiate(2)
                        if(guess!=None):
                                checkstring = "Did you want the letter "+guess
                                self.texToSpeech(checkstring)
                                h = self.speechInitiate(5)
                                if(h=="yes"):
                                        break
                        elif(guess==None):
                                pass


                self.changes = False
                revealed = 0
                if ((guess in self.remaining_consonants) == 1):
                        self.remaining_consonants.remove(guess)
                        for i in range(len(self.encodedpuzzle)):
                        
                                if (guess == self.puzzle[i]):
                                        self.encodedpuzzle[i] = self.puzzle[i]
                                        self.changes = True
                                        revealed += 1
                if (revealed == 1):
                        self.text = "there is {} {}".format(revealed,guess)
                else:
                        self.text = "there are {} {}'s".format(revealed,guess)
                
                self.texToSpeech(self.text)
                self.Label22.configure(text=self.text)
                self.Label22.text = self.text
                
                return revealed
        def solve(self):
                guess = self.speechInitiate(3)
                while True:
                        if(guess==None):
                                guess = self.speechInitiate(3)
                        else:
                                break
                if (guess == self.utpuzzle):
                        self.encodedpuzzle = self.puzzle
                        self.puzzleupdate()
                        self.solved = True
                        if (self.currentplayer.score > 1000):
                                self.currentplayer.totalscore += self.currentplayer.score
                        else:
                                self.currentplayer.score = 1000
                                self.currentplayer.totalscore += self.currentplayer.score
                        self.text = "Congratulations, Player {}, you solved the puzzle and earned {} dollars.".format(self.currentplayer.pn, self.currentplayer.score)
                        self.texToSpeech(self.text)
                        self.Label22.configure(text=self.text)
                        self.Label22.text = self.text
                        
                else:
                        self.text = "I'm sorry, that's incorrect."
                        self.texToSpeech(self.text)
                        self.Label22.configure(text=self.text)
                        self.Label22.text = self.text
                        

                        
        def buyvowel(self):
                while (True):
                        guess = self.speechInitiate(1)
                        if(guess!=None):
                                checkstring = "Did you want the letter "+guess
                                self.texToSpeech(checkstring)
                                h = self.speechInitiate(5)
                                if(h=="yes"):
                                        break
                        elif(guess==None):
                                pass
                if ((guess in self.remaining_vowels) == 1):
                        self.remaining_vowels.remove(guess)
                        revealed = 0
                        for i in range(len(self.encodedpuzzle)):
                        
                                if (guess == self.puzzle[i]):
                                        self.encodedpuzzle[i] = self.puzzle[i]
                                        self.changes = True
                                        revealed += 1
                
                if (revealed == 1):
                        self.text = "there is {} {}".format(revealed,guess)
                else:
                        self.text = "there are {} {}'s".format(revealed,guess)
                
                self.texToSpeech(self.text)
                self.Label22.configure(text=self.text)
                self.Label22.text = self.text
                

                if (self.changes == True):
                        self.puzzleupdate()
        def play(self):
                
                self.nextplayer()
                self.turn()
                
                if (self.solved == False):
                        self.play()
                elif(self.rn < self.rounds):
                        self.rn +=1

                        self.texToSpeech("Alright, onto the next round")
                        self.puzzlestart()
                        self.play()
                else:
                        one = False
                        two = False
                        three = False
                        if (self.p1.totalscore > self.p2.totalscore and self.p1.totalscore> self.p3.totalscore):
                                self.text = "Congratulations Player 1, you won with {} dollars".format(self.p1.totalscore)
                                one = True
                        elif (self.p2.totalscore > self.p1.totalscore and self.p2.totalscore> self.p3.totalscore):
                                self.text = "Congratulations Player 2, you won with {} dollars".format(self.p2.totalscore)
                                two = True
                        elif (self.p3.totalscore > self.p1.totalscore and self.p3.totalscore> self.p2.totalscore):
                                self.text = "Congratulations Player 3, you won with {} dollars".format(self.p3.totalscore)
                                three = True
                        elif (self.p2.totalscore == self.p1.totalscore and self.p2.totalscore> self.p3.totalscore):
                                self.text = "Congratulations Players 1 and 2, you tied for first with {} dollars".format(self.p1.totalscore)
                                one = True
                                two = True
                        elif (self.p2.totalscore == self.p3.totalscore and self.p2.totalscore> self.p1.totalscore):
                                self.text = "Congratulations Players 2 and 3, you tied for first with {} dollars".format(self.p2.totalscore)
                                two = True
                                three = True
                        elif (self.p3.totalscore == self.p1.totalscore and self.p2.totalscore< self.p3.totalscore):
                                self.text = "Congratulations Players 1 and 3, you tied for first with {} dollars".format(self.p1.totalscore)
                                one = True
                                three = True
                                
                        elif (self.p3.totalscore == self.p1.totalscore and self.p3.totalscore == self.p2.totalscore):
                                self.text = "Wow, did you rig the system? You all tied for first with {} dollars".format(self.p1.totalscore)
                                one = True
                                two = True
                                three = True
                        self.texToSpeech(self.text)
                        self.Label22.configure(text = self.text)
                        self.Label22.text = self.text
                        while (True):
                                if (one == True):
                                        self.Label3.configure(background = "#a00000")                                    
                                if (two == True):
                                        self.Label3_75.configure(background = "#a0a000")
                                if (three == True):
                                        self.Label3_76.configure(background = "#0000a0")
                                root.update()
                                sleep(.5)
                                if (one == True):
                                        self.Label3.configure(background = "#ff0000")                                    
                                if (two == True):
                                        self.Label3_75.configure(background = "#f0f000")
                                if (three == True):
                                        self.Label3_76.configure(background = "#0000ff")
                                root.update()
                                sleep(.5)
                                
                                
                                        
                              

        def turn(self):
                
                self.changes= False
                turnOnButton()
                while(ButtonPressed() == 0):
                        sleep(.5)
                turnOffButton()
                while(True):
                        j =self.speechInitiate(4)
                        if(j!=None):
                                
                                checkstring = "Did you want to"+j
                                self.texToSpeech(checkstring)
                                h = self.speechInitiate(5)
                                if(h=="yes"):
                                        break
                                elif(h=="no"):
                                        self.texToSpeech("hey, What do you want to do?")
                        elif(j==None):
                                pass
                if (j == "spin" or j == "i want to spin"):
                        self.texToSpeech('Time to spin the wheel.')
                        self.spin()
                elif(j == "solve"or j == "i want to solve"):
                        self.texToSpeech('Time to solve the puzzle. One guess.')
                        self.solve()
                elif((j == "buy vowel" or j == "buy a vowel") and self.currentplayer.score > 249):
                        self.texToSpeech('So you are buying a vowel?')
                        self.currentplayer.score -= 250
                        self.buyvowel()
                elif(j=="buy vowel" or j== "buy a vowel"):
                        self.texToSpeech('You cannot afford a vowel.')
                self.puzzleupdate()
                if (self.changes == True):
                        self.turn()
                        
        def nextplayer(self):
                if (self.currentplayer.pn == 1):
                        
                        self.currentplayer = self.p2
                        
                        
                elif(self.currentplayer.pn == 2):
                        self.currentplayer = self.p3
                elif(self.currentplayer.pn == 3):
                        self.currentplayer = self.p1
                self.text =  "Alright Player {}, it's your turn.".format(self.currentplayer.pn)
                self.texToSpeech(self.text)
                self.Label22.configure(text=self.text)
                self.Label22.text = self.text

        def speechInitiate(self, src):
                recog = sr.Recognizer()

                if (src == 1):
                        grammar = "WheelOText1.fsg"
                if (src == 2):
                        grammar = "WheelOText2.fsg"
                if (src == 3):
                        grammar = "WheelOText3.fsg"
                if (src == 4):
                        grammar = "WheelOText4.fsg"
                if(src == 5):
                        grammar = "WheelOText5.fsg"

                with sr.Microphone() as source:
                        
                        recog.adjust_for_ambient_noise(source)
                        self.texToSpeech('Hey, Speak.')
                        print "Speak, my child."
                        audio = recog.listen(source)         
                print src
                counter = 0
                while (counter < 3) :
                        jeff = self.speechRecognize(recog, audio, grammar)
                        print "aaaaah"
                        if(jeff == "Couldn't recognize text. Try again."):
                                sleep(.5)
                                return None
                        else:
                                return jeff
                        counter+=1

        def speechRecognize(self, recog, audio, grammar):
                try:
                        if (BEBEG):
                                print str(recog.recognize_sphinx(audio, show_all = False, grammar=grammar))
                        resultyea = str(recog.recognize_sphinx(audio, show_all = False, grammar=grammar))
                        #print('Using grammar: ' +resultyea)
                        return resultyea
                except sr.UnknownValueError:
                        self.text =  "Did not understand audio. Try again."
                        self.texToSpeech(self.text)
                        self.Label22.configure(text=self.text)
                        self.Label22.text = self.text
                        
                        return "Couldn't recognize text. Try again."

        def texToSpeech(self, feed):
                engine = pyttsx3.init()
                engine.setProperty('volume',2.0)
                engine.setProperty('rate',140)
                #engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                engine.say(feed)
                engine.runAndWait()
                sleep(0.1)
        
        def convert_to_puzz(self):
                encodedpuzzle = stringtolist(self.puzzle.lower())
                for i in range(len(puzzle)):
                                for j in range(len(self.al)):
                                        if (encodedpuzzle[i] == self.al[j][0]):
                                                encodedpuzzle[i] = self.al[j][1]
                                                break
                return encodedpuzzle
        def stringtolist(self,string):
                lis = [] #this exists because strings don't support assignment
                for i in range(len(string)):
                        lis.append(string[i])
                return lis


        def convert_to_puzz(self):
                encodedpuzzle = self.stringtolist(self.puzzle.lower())
                for i in range(len(self.puzzle)):
                                for j in range(len(al)):
                                        if (encodedpuzzle[i] == al[j][0]):
                                                encodedpuzzle[i] = al[j][1]
                                                break
                return encodedpuzzle


###main



global root 
root = tk.Tk()
top = Game(root)
weel_support.init(root, top)
#if (BEBEG == 0):
root.attributes("-fullscreen", True)
root.title("fortunate wheel")

root.mainloop()
closingTime()

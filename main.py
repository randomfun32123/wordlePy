import random

import os

clear = lambda: os.system("clear")

allowedFile = open("allowed-guesses.txt", "r")
answersFile = open("answers-alphabetical.txt", "r")


allowed = []

answers = []

answer = ""

skipTry = 0

errored = 0

tries = 6 # DON'T CHANGE THIS!


# Colors
class bColors:
  correct = '\033[92m'
  other = '\033[93m'
  endc = '\033[0m'


for line in allowedFile:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  allowed.append(line_list)


allowedFile.close()


for line in answersFile:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  answers.append(line_list)


answersFile.close()

answer = str(random.choice(answers))

answer = answer.replace("[", "").replace("]", "").replace("'", "").upper()

#print(answer)

ansSplit = list(answer)

aLetter1 = " "
aLetter2 = " "
aLetter3 = " "
aLetter4 = " "
aLetter5 = " "

bLetter1 = " "
bLetter2 = " "
bLetter3 = " "
bLetter4 = " "
bLetter5 = " "

cLetter1 = " "
cLetter2 = " "
cLetter3 = " "
cLetter4 = " "
cLetter5 = " "

dLetter1 = " "
dLetter2 = " "
dLetter3 = " "
dLetter4 = " "
dLetter5 = " "

eLetter1 = " "
eLetter2 = " "
eLetter3 = " "
eLetter4 = " "
eLetter5 = " "

fLetter1 = " "
fLetter2 = " "
fLetter3 = " "
fLetter4 = " "
fLetter5 = " "

aInd = "->"
bInd = "  "
cInd = "  "
dInd = "  "
eInd = "  "
fInd = "  "


topBoard = "      _____________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      ---------------------"

midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      ---------------------"
midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      ---------------------"
midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      ---------------------"
midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      ---------------------"
midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      ---------------------"

while tries != 0:
  clear()
  print(topBoard)
  print(midBoard1)
  print(midBoard2)
  print(midBoard3)
  print(midBoard4)
  print(midBoard5)
  x = str(input("WoRDlE -> ")).lower()
  x2 = "['" + x.capitalize() + "']"
  if len(x) == 5:
    #if x2 in allowed:
      if aLetter1 == " ":
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          aLetter1 = bColors.correct + xSplit[0] + bColors.endc
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          aLetter1 = bColors.other + xSplit[0] + bColors.endc
        if xSplit[1] == ansSplit[1]:
          aLetter2 = bColors.correct + xSplit[1] + bColors.endc
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          aLetter2 = bColors.other + xSplit[1] + bColors.endc
        if xSplit[2] == ansSplit[2]:
          aLetter3 = bColors.correct + xSplit[2] + bColors.endc
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          aLetter3 = bColors.other + xSplit[2] + bColors.endc
        if xSplit[3] == ansSplit[3]:
          aLetter4 = bColors.correct + xSplit[3] + bColors.endc
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          aLetter4 = bColors.other + xSplit[3] + bColors.endc
        if xSplit[4] == ansSplit[4]:
          aLetter5 = bColors.correct + xSplit[4] + bColors.endc
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          aLetter5 = bColors.other + xSplit[4] + bColors.endc
        aInd = "  "
        bInd = "->"
      elif bLetter1 == " ":
        xSplit = list(x)
        bLetter1 = xSplit[0]
        bLetter2 = xSplit[1]
        bLetter3 = xSplit[2]
        bLetter4 = xSplit[3]
        bLetter5 = xSplit[4]
        bInd = "  "
        cInd = "->"
      elif cLetter1 == " ":
        xSplit = list(x)
        cLetter1 = xSplit[0]
        cLetter2 = xSplit[1]
        cLetter3 = xSplit[2]
        cLetter4 = xSplit[3]
        cLetter5 = xSplit[4]
        cInd = "  "
        dInd = "->"
      elif dLetter1 == " ":
        xSplit = list(x)
        dLetter1 = xSplit[0]
        dLetter2 = xSplit[1]
        dLetter3 = xSplit[2]
        dLetter4 = xSplit[3]
        dLetter5 = xSplit[4]
        dInd = "  "
        eInd = "->"
      elif eLetter1 == " ":
        xSplit = list(x)
        eLetter1 = xSplit[0]
        eLetter2 = xSplit[1]
        eLetter3 = xSplit[2]
        eLetter4 = xSplit[3]
        eLetter5 = xSplit[4]
        eInd = "  "
        fInd = "->"
      elif fLetter1 == " ":
        xSplit = list(x)
        fLetter1 = xSplit[0]
        fLetter2 = xSplit[1]
        fLetter3 = xSplit[2]
        fLetter4 = xSplit[3]
        fLetter5 = xSplit[4]
        fInd = "  "
    #else:
      #print("Not in Dictionary")
      #errored = 1
      #skipTry = 1
  else:
    print("Too Long")
    errored = 2
    skipTry = 1

  if skipTry == 0:
    topBoard = "      _____________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      ---------------------"

    midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      ---------------------"
    midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      ---------------------"
    midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      ---------------------"
    midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      ---------------------"
    midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      ---------------------"

    tries -= 1
  else:
    input("Countinue? ")
    skipTry = 0
    errored = 0

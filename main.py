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

finish = 0

tries = 6 # DON'T CHANGE THIS!

def printHelp():
  print("WoRDlE")
  print("")
  print(" * - Correct")
  print("")
  print(" ? - Other Position")
  print("")
  print(" ! - Incorrect")
  print("")
  print("")
  print("Have Fun!")
  print("")

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

answer = answer.replace("[", "").replace("]", "").replace("'", "").lower()

#print(answer)

ansSplit = list(answer)

aLetter1 = "  "
aLetter2 = "  "
aLetter3 = "  "
aLetter4 = "  "
aLetter5 = "  "

bLetter1 = "  "
bLetter2 = "  "
bLetter3 = "  "
bLetter4 = "  "
bLetter5 = "  "

cLetter1 = "  "
cLetter2 = "  "
cLetter3 = "  "
cLetter4 = "  "
cLetter5 = "  "

dLetter1 = "  "
dLetter2 = "  "
dLetter3 = "  "
dLetter4 = "  "
dLetter5 = "  "

eLetter1 = "  "
eLetter2 = "  "
eLetter3 = "  "
eLetter4 = "  "
eLetter5 = "  "

fLetter1 = "  "
fLetter2 = "  "
fLetter3 = "  "
fLetter4 = "  "
fLetter5 = "  "

aInd = "->"
bInd = "  "
cInd = "  "
dInd = "  "
eInd = "  "
fInd = "  "

printHelp()

topBoard = "      __________________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      --------------------------"

midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      --------------------------"
midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      --------------------------"
midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      --------------------------"
midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      --------------------------"
midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      --------------------------"

#print(answer)

while True:
  clear()
  print(topBoard)
  print(midBoard1)
  print(midBoard2)
  print(midBoard3)
  print(midBoard4)
  print(midBoard5)

  if finish == 1:
    exit()

  x = str(input("WoRDlE -> ")).lower()
  x2 = "['" + x.capitalize() + "']"
  if len(x) == 5:
    #if x2 in allowed:
      if aLetter1 == "  ":
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          aLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          aLetter1 = xSplit[0] + "?"
        else:
          aLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          aLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          aLetter2 = xSplit[1] + "?"
        else:
          aLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          aLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          aLetter3 = xSplit[2] + "?"
        else:
          aLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          aLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          aLetter4 = xSplit[3] + "?"
        else:
          aLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          aLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          aLetter5 = xSplit[4] + "?"
        else:
          aLetter5 = xSplit[4] + "!"


        aInd = "  "
        bInd = "->"

      elif bLetter1 == "  ":
        xSplit = list(x)

        if xSplit[0] == ansSplit[0]:
          bLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          bLetter1 = xSplit[0] + "?"
        else:
          bLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          bLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          bLetter2 = xSplit[1] + "?"
        else:
          bLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          bLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          bLetter3 = xSplit[2] + "?"
        else:
          bLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          bLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          bLetter4 = xSplit[3] + "?"
        else:
          bLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          bLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          bLetter5 = xSplit[4] + "?"
        else:
          bLetter5 = xSplit[4] + "!"


        bInd = "  "
        cInd = "->"


      elif cLetter1 == "  ":
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          cLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          cLetter1 = xSplit[0] + "?"
        else:
          cLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          cLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          cLetter2 = xSplit[1] + "?"
        else:
          cLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          cLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          cLetter3 = xSplit[2] + "?"
        else:
          cLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          cLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          cLetter4 = xSplit[3] + "?"
        else:
          cLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          cLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          cLetter5 = xSplit[4] + "?"
        else:
          cLetter5 = xSplit[4] + "!"


        cInd = "  "
        dInd = "->"


      elif dLetter1 == "  ":
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          dLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          dLetter1 = xSplit[0] + "?"
        else:
          dLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          dLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          dLetter2 = xSplit[1] + "?"
        else:
          dLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          dLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          dLetter3 = xSplit[2] + "?"
        else:
          dLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          dLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          dLetter4 = xSplit[3] + "?"
        else:
          dLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          dLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          dLetter5 = xSplit[4] + "?"
        else:
          dLetter5 = xSplit[4] + "!"


        dInd = "  "
        eInd = "->"


      elif eLetter1 == "  ":
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          eLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          eLetter1 = xSplit[0] + "?"
        else:
          eLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          eLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          eLetter2 = xSplit[1] + "?"
        else:
          eLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          eLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          eLetter3 = xSplit[2] + "?"
        else:
          eLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          eLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          eLetter4 = xSplit[3] + "?"
        else:
          eLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          eLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          eLetter5 = xSplit[4] + "?"
        else:
          eLetter5 = xSplit[4] + "!"


        eInd = "  "
        fInd = "->"


      elif fLetter1 == "  ":
        xSplit = list(x)
        xSplit = list(x)
        if xSplit[0] == ansSplit[0]:
          fLetter1 = xSplit[0] + "*"
        elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
          fLetter1 = xSplit[0] + "?"
        else:
          fLetter1 = xSplit[0] + "!"


        if xSplit[1] == ansSplit[1]:
          fLetter2 = xSplit[1] + "*"
        elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
          fLetter2 = xSplit[1] + "?"
        else:
          fLetter2 = xSplit[1] + "!"


        if xSplit[2] == ansSplit[2]:
          fLetter3 = xSplit[2] + "*"
        elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
          fLetter3 = xSplit[2] + "?"
        else:
          fLetter3 = xSplit[2] + "!"


        if xSplit[3] == ansSplit[3]:
          fLetter4 = xSplit[3] + "*"
        elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
          fLetter4 = xSplit[3] + "?"
        else:
          fLetter4 = xSplit[3] + "!"


        if xSplit[4] == ansSplit[4]:
          fLetter5 = xSplit[4] + "*"
        elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
          fLetter5 = xSplit[4] + "?"
        else:
          fLetter5 = xSplit[4] + "!"


        fInd = "  "


      else:
        print("You Lose!")
        finish = 1

    #else:
      #print("Not in Dictionary")
      #errored = 1
      #skipTry = 1
  else:
    print("Too Long")
    errored = 2
    skipTry = 1

  if skipTry == 0:
    topBoard = "      __________________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      --------------------------"

    midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      --------------------------"
    midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      --------------------------"
    midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      --------------------------"
    midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      --------------------------"
    midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      --------------------------"

  else:
    input("Countinue? ")
    skipTry = 0
    errored = 0

  if x == answer:
    print("You Win!")
    finish = 1



















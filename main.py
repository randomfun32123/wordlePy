import random

import os

from termcolor import colored

clear = lambda: os.system("clear")

allowedFile = open("allowed-guesses.txt", "r")
answersFile = open("answers-alphabetical.txt", "r")

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

finish = 0


allowed = []

answers = []


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


def wordleGame():

  skipTry = 0

  errored = 0

  finish = 0

  turn = 1

  answer = str(random.choice(answers))

  answer = answer.replace("[", "").replace("]", "").replace("'", "").lower()

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

  printHelp()

  topBoard = "      _____________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      ---------------------"

  midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      ---------------------"
  midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      ---------------------"
  midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      ---------------------"
  midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      ---------------------"
  midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      ---------------------"

  #print(answer)

  while turn != 8:
    clear()
    print(topBoard)
    print(midBoard1)
    print(midBoard2)
    print(midBoard3)
    print(midBoard4)
    print(midBoard5)

    if finish == 1:
      print("The Word is " + answer.capitalize())
      break

    x = str(input("WoRDlE -> ")).lower()
    x2 = "['" + x.capitalize() + "']"
    if len(x) == 5:
      #if x2 in allowed:
        if turn == 1:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            aLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            aLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            aLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            aLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            aLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            aLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            aLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            aLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            aLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            aLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            aLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            aLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            aLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            aLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            aLetter5 = xSplit[4]


          aInd = "  "
          bInd = "->"

          turn += 1


        elif turn == 2:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            bLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            bLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            bLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            bLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            bLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            bLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            bLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            bLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            bLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            bLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            bLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            bLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            bLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            bLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            bLetter5 = xSplit[4]


          bInd = "  "
          cInd = "->"

          turn += 1


        elif turn == 3:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            cLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            cLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            cLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            cLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            cLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            cLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            cLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            cLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            cLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            cLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            cLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            cLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            cLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            cLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            cLetter5 = xSplit[4]


          cInd = "  "
          dInd = "->"

          turn += 1


        elif turn == 4:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            dLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            dLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            dLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            dLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            dLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            dLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            dLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            dLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            dLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            dLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            dLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            dLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            dLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            dLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            dLetter5 = xSplit[4]


          dInd = "  "
          eInd = "->"

          turn += 1


        elif turn == 5:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            eLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            eLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            eLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            eLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            eLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            eLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            eLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            eLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            eLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            eLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            eLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            eLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            eLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            eLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            eLetter5 = xSplit[4]


          eInd = "  "
          fInd = "->"

          turn += 1


        elif turn == 6:
          xSplit = list(x)
          if xSplit[0] == ansSplit[0]:
            fLetter1 = colored(xSplit[0], on_color="green")
          elif (xSplit[0] == ansSplit[1]) or (xSplit[0] == ansSplit[2]) or (xSplit[0] == ansSplit[3]) or (xSplit[0] == ansSplit[4]):
            fLetter1 = colored(xSplit[0], on_color="yellow")
          else:
            fLetter1 = xSplit[0]


          if xSplit[1] == ansSplit[1]:
            fLetter2 = colored(xSplit[1], on_color="green")
          elif (xSplit[1] == ansSplit[0]) or (xSplit[1] == ansSplit[2]) or (xSplit[1] == ansSplit[3]) or (xSplit[1] == ansSplit[4]):
            fLetter2 = colored(xSplit[1], on_color="yellow")
          else:
            fLetter2 = xSplit[1]


          if xSplit[2] == ansSplit[2]:
            fLetter3 = colored(xSplit[2], on_color="green")
          elif (xSplit[2] == ansSplit[0]) or (xSplit[2] == ansSplit[1]) or (xSplit[2] == ansSplit[3]) or (xSplit[2] == ansSplit[4]):
            fLetter3 = colored(xSplit[2], on_color="yellow")
          else:
            fLetter3 = xSplit[2]


          if xSplit[3] == ansSplit[3]:
            fLetter4 = colored(xSplit[3], on_color="green")
          elif (xSplit[3] == ansSplit[0]) or (xSplit[3] == ansSplit[1]) or (xSplit[3] == ansSplit[2]) or (xSplit[2] == ansSplit[4]):
            fLetter4 = colored(xSplit[3], on_color="yellow")
          else:
            fLetter4 = xSplit[3]


          if xSplit[4] == ansSplit[4]:
            fLetter5 = colored(xSplit[4], on_color="green")
          elif (xSplit[4] == ansSplit[0]) or (xSplit[4] == ansSplit[1]) or (xSplit[4] == ansSplit[2]) or (xSplit[4] == ansSplit[3]):
            fLetter5 = colored(xSplit[4], on_color="yellow")
          else:
            fLetter5 = xSplit[4]


          fInd = "  "

          turn += 1

        else:
          print("You Lose!")
          finish = 1

      #else:
        #print("Not in Dictionary")
        #errored = 1
        #skipTry = 1
    else:
      if len(x) < 5:
        print("Your answer is too short")
      else:
        print("Your answer is too long")
      skipTry = 1

    if skipTry == 0:
      topBoard = "      _____________________\n " + aInd + "   | " + aLetter1 + " | " + aLetter2 + " | " + aLetter3 + " | " + aLetter4 + " | " + aLetter5 + " |\n      ---------------------"

      midBoard1 = " " + bInd + "   | " + bLetter1 + " | " + bLetter2 + " | " + bLetter3 + " | " + bLetter4 + " | " + bLetter5 + " |\n      ---------------------"
      midBoard2 = " " + cInd + "   | " + cLetter1 + " | " + cLetter2 + " | " + cLetter3 + " | " + cLetter4 + " | " + cLetter5 + " |\n      ---------------------"
      midBoard3 = " " + dInd + "   | " + dLetter1 + " | " + dLetter2 + " | " + dLetter3 + " | " + dLetter4 + " | " + dLetter5 + " |\n      ---------------------"
      midBoard4 = " " + eInd + "   | " + eLetter1 + " | " + eLetter2 + " | " + eLetter3 + " | " + eLetter4 + " | " + eLetter5 + " |\n      ---------------------"
      midBoard5 = " " + fInd + "   | " + fLetter1 + " | " + fLetter2 + " | " + fLetter3 + " | " + fLetter4 + " | " + fLetter5 + " |\n      ---------------------"

    else:
      input("Countinue? ")
      skipTry = 0
      errored = 0

    if x == answer:
      print("You Win!")
      finish = 1

while True:
  keep = str(input("Start? (Y/n) ")).lower()
  if (keep == "") or (keep == "y"):
    wordleGame()
  else:
    exit()


















#!/usr/bin/python
# !/usr/bin/env python


# 1. wczytanie tekstów z pliku do listy
# 2. wylosowanie tesktu z listy
# 3. wyświetlenie w okienku

# copy SucharOfTheDay.py SucharOfTheDay.pyw


import random

lstAttractors = ["Aaaaa", "Albo", "A wiesz"]


CHESTNUTS_FILE = "chestnuts.txt"
TITLE_TEXT = "Sucharki..."
IDX_ERR_NOT_FOUND_LINE = 0
IDX_ERR_UNKNOWN_IN_PARAM = 1

PAR_LAST_LINE = "last"

ERRORS = {
            IDX_ERR_NOT_FOUND_LINE : "nie zanleziono tekstu z linii:",
            IDX_ERR_UNKNOWN_IN_PARAM : "nieznany parametr wejścia!!!"
         }

# lstErrors = list()
# lstErrors.append("ERR: nie zanleziono tekstu z linii:")
# lstErrors.append("ERR: nieznany parametr wejścia!!!")


from tkinter import *

class MessageDlg:
    def __init__(self,messagetext : str,buttontext : str):
        self.root = Tk()
        self.root.title(TITLE_TEXT)
        self.root.geometry("600x150")


        self.lblINFO = Label(self.root, text=messagetext, font=("Arial", 12))

        val = self.lblINFO.pack(side=TOP)


        # https://stackoverflow.com/questions/30129359/tkinter-button-command-runs-function-without-clicking
        self.btnOK = Button(self.root, text=buttontext, command=lambda : self.btnOKClick())
        self.btnOK.pack(side=BOTTOM)
        # self.btnOK.place(x=40,y=90)

    def btnOKClick(self):
        exit(666 + 111)
        # self.root.quit()
        # print(13)
        pass

    def show(self):
        self.root.mainloop()

#       kody
# -----------------
# 196 - ę
# 313 - ż
# 317 - ą

def such(suchs, rolled, max_rolled):
#     suchs - lista sucharów
#     rolled - wylosowane numery linii
#     max_rolled - max ilość wylosowanych zanim może nastąpić powtórka
    if len(rolled) >= max_rolled:
        print("usuwanie :".format(rolled.pop(0)))
    while True:
        rnd = random.randint(0, len(suchs)-1)
        if not rnd in rolled:
            rolled.append(rnd)
            return (rnd, suchs[rnd])


def test():
    ...
def getERRORMessage(aERRIDX : int) -> str:
    return "ERR: {0}".format(ERRORS.get(aERRIDX, "nieznany błąd..."))

def analizeLine(aLines: list):


    for line in aLines:
        w = ""
        for ch in line:
            ordv = ord(ch)
            if (ord(ch) > 8000):
                # print("{0} - {1}".format(ord(ch), ch))
                w = w + ""
            else:
                if ord(ch) > 126:
                    w = w +{
                            196 : "e",
                            313 : "z",
                            317 : "a"
                            }.get(ord(ch),"_None_")
                else:
                    w = w + ch

        print(w.rstrip())
    print()



def main(args):
    # lstErrors = list()
    # lstErrors.append("ERR: nie zanleziono tekstu z linii:")
    # lstErrors.append("ERR: nieznany parametr wejścia!!!")

    unknowInPar = False
    lines = []
    rndText = TITLE_TEXT
    with open(CHESTNUTS_FILE) as fchestnuts:
        # print("Otwarte")

# Jak nazywa się człowiek, który straszy dynie? Buuudyń...
        line = ""
        line_cnt = 0
        while True:
            line = fchestnuts.readline()

            if not line:
                break
            else:
                if line.find("#") == -1:
                    lines.append(line)
                    line_cnt += 1
                else:
                    continue  # komentarze nas nie interesują
                pass

        # lines = (fchestnuts.read()).split("\n")
        # lines.pop(0)  # w pierwszej linii jakieś śmieci to wyrzuczamy

        # analizeLine(lines)
        # exit

        print("Wczytana liczba sucharków: {0}".format(line_cnt))
        num = -1
        findlinetext = ""
        if len(lines) == 0: #  plik pusty?
            pass
        else:
            if len(args) == 1:  # standardowa procedura czyli losowanie, bo brak argumentów wejścia
                rndText = (lines[random.randint(0, len(lines))-1])
            else:   #   wyświetl wskazany numerem    sucharek
                # print("parametry {0}".format(len(args)))

                num = 1
                argnum = -1
                if args[1].isdigit():
                    argnum = int(args[1])   #   numer pdany przez użytkownika jako par. wejścia
                else:   #   inny par. nie będący numerem
                    if args[1].lower().startswith(PAR_LAST_LINE):
                        argnum = line_cnt
                    else:   #   jakiś inny tekst, który nie jest obsługiwanym parametrem
                        unknowInPar = True
                        lines.clear()   #   czyli nie ma co przechodzić pętli


                for line in lines:
                    if (num == argnum):
                        rndText = line
                        findlinetext = "wybrana linia: {0} = ".format(argnum)
                        break
                    num += 1
                else:
                    if not unknowInPar:
                        num = -1
                        print("{0} {1}".format(getERRORMessage(IDX_ERR_NOT_FOUND_LINE),argnum))
                    else:
                        print("'{1}' - {0}".format(getERRORMessage(IDX_ERR_UNKNOWN_IN_PARAM), args[1]))

                pass


    # print((findlinetext if (findlinetext != "") else "") + rndText)

    rndText = lstAttractors[random.randint(0, len(lstAttractors)-1)] + ", " + rndText
    print(chr(7))
    print((findlinetext if (num != -1) else "") + rndText)

    # wyświetlanie formatki
    msg = MessageDlg(rndText, "Buachachachacha!")
    msg.show()

    # print(fchestnuts.closed)

    return 0


if __name__ == "__main__":
    import sys

    # import os
    # utwórz .pyw z .py
    # thisFileName = sys.argv[0].split(".")[0] + ".pyw"
    # filenameDotPYW += ".pyw"
    # print(filenameDotPYW)
    #
    #
    #
    # tyle pierdolenia powyżej...
    # print("kopia...")
    #
    # os.system("copy {0} {1}".format(sys.argv[0], sys.argv[0].split(".")[0]+".pyw"))


    sys.exit(main(sys.argv))
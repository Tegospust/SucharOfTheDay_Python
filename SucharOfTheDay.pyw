#!/usr/bin/python
# !/usr/bin/env python


# 1. wczytanie tekstów z pliku do listy
# 2. wylosowanie tesktu z listy
# 3. wyświetlenie w okienku

# copy SucharOfTheDay.py SucharOfTheDay.pyw


import random



CHESTNUTS_FILE = "chestnuts.txt"
TITLE_TEXT = "Sucharki..."

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


def main(args):

    lstErrors = list()
    lstErrors.append("ERR: nie zanleziono tekstu z linii:")

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
        print("Wczytana liczba sucharków: {0}".format(line_cnt))
        num = -1
        findlinetext = ""
        if len(lines) == 0: #  plik pusty?
            pass
        else:
            if len(args) == 1:  # standardowa procedura
                rndText = (lines[random.randint(0, len(lines))-1])
            else:   #   wyświetl wskazany numerem    sucharek
                # print("parametry {0}".format(len(args)))

                num = 1
                argnum = int(args[1])
                for line in lines:
                    if (num == argnum):
                        rndText = line
                        findlinetext = "linia: {0} = ".format(argnum)
                        break
                    num += 1
                else:
                    num = -1
                    print("{0} {1}".format(lstErrors[0],argnum))
                pass


    # print((findlinetext if (findlinetext != "") else "") + rndText)
    print((findlinetext if (num != -1) else "") + rndText)

    # wyświetlanie formatki
    msg = MessageDlg(rndText, "Gotowe!")
    msg.show()

    # print(fchestnuts.closed)

    return 0


if __name__ == "__main__":
    import sys
    import os
    # utwórz .pyw z .py
    # thisFileName = sys.argv[0].split(".")[0] + ".pyw"
    # filenameDotPYW += ".pyw"
    # print(filenameDotPYW)
    #
    #
    #
    # tyle pierdolenia powyżej...
    print("kopia...")

    os.system("copy {0} {1}".format(sys.argv[0], sys.argv[0].split(".")[0]+".pyw"))


    sys.exit(main(sys.argv))
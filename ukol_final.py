from turtle import *
bgcolor('khaki1') #nastaví se barva pozadí
penup() #zvedne se tužka, aby "nekreslila"
setposition(-100,-100) 
pendown()
ht()

delka_s=90
speed(0)
color('brown','white')
begin_fill()
for _ in range(3):  #matice 3x3
    for _ in range(3):  #řádek se 3 čtverci
        for _ in range(4): #čtverec
            fd(delka_s)
            lt(90)
        fd(90)
    lt(180)
    fd(3*delka_s)
    rt(90)
    fd(delka_s)
    rt(90)
end_fill()
letter = ["a","b","c"] #popíše jména sloupců
for _ in range(3):
    penup()
    setposition(-60+(_*90),180)
    pendown()
    write(letter[_])

for _ in range(3): #popíše jména řádků
    penup()
    setposition(-120,120-(_*90))
    pendown()
    write(_+1)
    penup()

textinput("welcome", "Vítej ve hře piškvorky")
print("Vítej ve hře piškvorky")
rozsah = range(1,4)
pole = ("a","b","c")

for _ in range(9): # celkem proběhne 9 tahů
    x_cor = 0
    y_cor = 0
    radek = 0
    sloupec = ""
    print("TAH",_+1)

    if (_ % 2==0): 
        print("Hraje Hráč 1\nZadej číslo řádku v rozsahu 1 až 3:\n")
    else:
        print("Hraje Hráč 2\nZadej číslo řádku v rozsahu 1 až 3:\n")
    while(radek not in rozsah):
        radek = int(input())
        if (radek not in rozsah):
            print("Chybně zadáno.\nČíslo řádku musí odpovídat hodnotám 1 až 3.\nZadej číslo znovu.")
        if (radek == 1):
            y_cor = 145
        elif (radek == 2):
            y_cor = 55
        else:
            y_cor = -35

    print(" Nyní zadej písmeno sloupce od a až c:")
    while(sloupec not in pole):
        sloupec = input()
        if (sloupec not in pole):
            print("Chybně zadáno. Sloupec musí nabývat hodnotu a, b ,nebo c.\n Zadej souřadnicici znovu.")
        if (sloupec == "a"):
            x_cor = -75
        elif (sloupec == "b"):
            x_cor = 15
        else:
            x_cor = 105
    if (_ % 2 == 0):
        print("Pomocí zadaných souřadnic byl v grafice zakreslen křížek.\n")

        #zakreslení křížku do grafiky
        setposition(x_cor,y_cor) #tužka se posune na pozici, kterou zadal uživatel
        seth(0)  #nastaví orientaci tužky
        rt(45)
        pendown()
        pencolor ('red')
        pensize(5)
        fd(60)
        penup()
        setposition(x_cor+40,y_cor)
        seth(0)  #nastaví orientaci tužky
        rt(135)
        pendown()
        fd(60)
        penup()

    else:
        print("Pomocí zadaných souřadnic bylo v grafice zakresleno kolečko.\n")
        #zakreslení kolečka do grafiky
        penup()
        setposition(x_cor,y_cor)
        pendown()
        pencolor('blue')
        pensize(5)
        circle(30)
        penup()

print("Děkujeme za hru")
exitonclick()
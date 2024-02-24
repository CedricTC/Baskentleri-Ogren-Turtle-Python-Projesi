import turtle
import random


ulkeler = [
    "Türkiye", "Almanya", "Fransa", "İngiltere", "İtalya", "Japonya", "ABD", "Rusya", "Çin", "Azerbaycan","Kanada", "Brezilya", "Güney Kore", "Hindistan", "İspanya", "Meksika", "Avustralya", "Arjantin", "Suudi Arabistan", "Güney Afrika","Portekiz", "İsveç", "Norveç", "Yunanistan", "İsviçre", "Avusturya", "Belçika", "Hollanda", "Polonya", "İran","İrlanda", "Kolombiya", "Nijerya", "Kenya", "Vietnam", "Malezya", "Singapur", "Tayland", "Filipinler", "Endonezya","Yeni Zelanda", "İsrail", "Mısır", "Fas", "Tunus", "Cezayir", "Ukrayna", "Macaristan", "Çek Cumhuriyeti", "Slovakya"
]

baskentler = [
    "Ankara", "Berlin", "Paris", "Londra", "Roma", "Tokyo", "Washington", "Moskova", "Pekin", "Bakü","Ottawa", "Brasília", "Seul", "Yeni Delhi", "Barselona", "Meksiko", "Sydney", "Buenos Aires", "Riyad", "Pretoria","Lizbon", "Stokholm", "Oslo", "Atina", "Zürih", "Viyana", "Brüksel", "Amsterdam", "Varşova", "Tahran","Dublin", "Bogota", "Abuja", "Nairobi", "Hanoi", "Kuala Lumpur", "Singapur", "Bangkok", "Manila", "Cakarta","Wellington", "Kudüs", "Kahire", "Rabat", "Tunus", "Cezayir", "Kiev", "Budapeşte", "Prag", "Bratislava"
]


win=turtle.Screen() 
win.bgcolor("black")
win.title("Başkentleri Öğren")
win.screensize(700,700)

d=turtle.Turtle()
def draw():
    d.penup()
    d.speed(32)
    d.goto(-250,250)
    d.pendown()
    d.hideturtle()
    d.color("red")
    d.width(5)
    for i in range(4):
        d.forward(500)
        d.right(90)

draw()

ulke=turtle.Turtle()
ulke.penup()
ulke.speed(1)
ulke.goto(0,100)
ulke.penup()
ulke.hideturtle()
ulke.color("red")

sonuc=turtle.Turtle()
sonuc.penup()
sonuc.speed(0)
sonuc.goto(0,-100)
sonuc.penup()
sonuc.hideturtle()
sonuc.color("red")

i = 0
counter=0

while i < 3:
    chosen = random.randint(0,9)
    ulke.write(ulkeler[chosen], align="center", font=("Courier", 50, "normal"))
    answer = turtle.textinput(" ", "Cevabınızı Yazın",)
    if answer.upper() == baskentler[chosen].upper():
        counter=counter+1   
        sonuc.write("Aferin", align="center", font=("Courier", 50, "normal"))          
    else:
        sonuc.write("Yanlış", align="center", font=("Courier", 50, "normal"))
    i=i+1
    ulke.clear()
    sonuc.clear()
ulke.write("Dogru sayınız", align="center", font=("Courier", 30, "normal"))
sonuc.write("{}".format(counter), align="center", font=("Courier", 50, "normal"))

win.mainloop()

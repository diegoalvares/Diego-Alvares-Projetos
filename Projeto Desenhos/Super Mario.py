from tkinter import *

tela_Super_Mario = Tk()
tela_Super_Mario.geometry('900x800')
tela_Super_Mario.resizable(width=False, height=False)
tela_Super_Mario.configure(bg='White')

#---------------- LINHAS PRETAS ------------------------
a1= Label(bg='black')
a1.place(x=270, y=170, height=30, width=180)
a2= Label(bg='black')
a2.place(x=210, y=200, height=30, width=270)
a3= Label(bg='black')
a3.place(x=150, y=230, height=30, width=90)
a4= Label(bg='black')
a4.place(x=270, y=230, height=60, width=30)
a5= Label(bg='black')
a5.place(x=330, y=230, height=60, width=30)
a6= Label(bg='black')
a6.place(x=180, y=260, height=90, width=30)
a7= Label(bg='black')
a7.place(x=210, y=290, height=30, width=30)
a8= Label(bg='black')
a8.place(x=270, y=320, height=30, width=30)
a9= Label(bg='black')
a9.place(x=240, y=350, height=30, width=210)
a10= Label(bg='black')
a10.place(x=300, y=380, height=30, width=120)
a11= Label(bg='black')
a11.place(x=90, y=350, height=30, width=60)
a12= Label(bg='black')
a12.place(x=90, y=320, height=30, width=30)
a13= Label(bg='black')
a13.place(x=120, y=380, height=30, width=30)
a13= Label(bg='black')
a13.place(x=270, y=590, height=30, width=30)
a14= Label(bg='black')
a14.place(x=330, y=590, height=30, width=30)
a15= Label(bg='black')
a15.place(x=300, y=620, height=30, width=30)
a16= Label(bg='black')
a16.place(x=360, y=620, height=30, width=30)
a17= Label(bg='black')
a17.place(x=150, y=620, height=30, width=30)
a18= Label(bg='black')
a18.place(x=150, y=650, height=30, width=240)

#---------------- LINHAS MARRONS ------------------------

b1= Label(bg='#8B4513')
b1.place(x=120, y=260, height=60, width=30)
b2= Label(bg='#8B4513')
b2.place(x=390, y=260, height=30, width=60)
b3= Label(bg='#8B4513')
b3.place(x=450, y=290, height=60, width=30)
b4= Label(bg='#8B4513')
b4.place(x=150, y=380, height=30, width=60)
b5= Label(bg='#8B4513')
b5.place(x=210, y=410, height=30, width=120)
b6= Label(bg='#8B4513')
b6.place(x=150, y=470, height=30, width=90)
b7= Label(bg='#8B4513')
b7.place(x=120, y=500, height=90, width=30)
b8= Label(bg='#8B4513')
b8.place(x=240, y=500, height=30, width=30)
b9= Label(bg='#8B4513')
b9.place(x=210, y=530, height=60, width=30)
b10= Label(bg='#8B4513')
b10.place(x=150, y=590, height=30, width=120)
b11= Label(bg='#8B4513')
b11.place(x=180, y=620, height=30, width=90)
b12= Label(bg='#8B4513')
b12.place(x=300, y=590, height=30, width=30)

#---------------- LINHAS AMARALELAS ------------------------

c1= Label(bg='#FFD700')
c1.place(x=330, y=110, height=60, width=30)
c2= Label(bg='#FFFF00')
c2.place(x=300, y=140, height=30, width=30)
c3= Label(bg='#FFD700')
c3.place(x=330, y=620, height=30, width=30)
c4= Label(bg='#FFD700')
c4.place(x=270, y=620, height=30, width=30)

#---------------- LINHAS AZUIS ------------------------

d1= Label(bg='#4169E1')
d1.place(x=330, y=410, height=30, width=30)
d2= Label(bg='#4169E1')
d2.place(x=360, y=440, height=30, width=30)
d3= Label(bg='#4169E1')
d3.place(x=390, y=470, height=90, width=30)
d4= Label(bg='#4169E1')
d4.place(x=360, y=560, height=30, width=30)
d5= Label(bg='#00FFFF')
d5.place(x=300, y=440, height=30, width=60)
d6= Label(bg='#00FFFF')
d6.place(x=330, y=470, height=90, width=30)
d7= Label(bg='#00FFFF')
d7.place(x=360, y=530, height=30, width=30)
d8= Label(bg='#008B8B')
d8.place(x=240, y=440, height=30, width=60)
d9= Label(bg='#008B8B')
d9.place(x=240, y=470, height=30, width=30)
d9= Label(bg='#008B8B')
d9.place(x=240, y=530, height=30, width=90)
d10= Label(bg='#008B8B')
d10.place(x=240, y=560, height=30, width=60)
d11= Label(bg='#4169E1')
d11.place(x=300, y=560, height=30, width=30)
d11= Label(bg='#008B8B')
d11.place(x=330, y=560, height=30, width=30)

#---------------- LINHAS VERMELHAS ------------------------
e1= Label(bg='#FF0000')
e1.place(x=360, y=110, height=30, width=30)
e2= Label(bg='#FF0000')
e2.place(x=240, y=110, height=30, width=90)
e3= Label(bg='#FF0000')
e3.place(x=180, y=140, height=30, width=60)
e3= Label(bg='#FF0000')
e3.place(x=180, y=170, height=30, width=30)
e4= Label(bg='#FF0000')
e4.place(x=210, y=440, height=30, width=30)
e5= Label(bg='#800000')
e5.place(x=240, y=80, height=30, width=150)
e6= Label(bg='#800000')
e6.place(x=390, y=110, height=60, width=30)
e7= Label(bg='#800000')
e7.place(x=180, y=110, height=30, width=60)
e8= Label(bg='#800000')
e8.place(x=150, y=140, height=30, width=30)
e9= Label(bg='#800000')
e9.place(x=120, y=170, height=30, width=30)
e10= Label(bg='#800000')
e10.place(x=90, y=200, height=60, width=30)
e11= Label(bg='#800000')
e11.place(x=60, y=260, height=90, width=30)
e12= Label(bg='#800000')
e12.place(x=150, y=410, height=30, width=30)
e12= Label(bg='#800000')
e12.place(x=120, y=440, height=60, width=30)
e13= Label(bg='#B22222')
e13.place(x=240, y=140, height=30, width=60)
e14= Label(bg='#B22222')
e14.place(x=210, y=170, height=30, width=60)
e15= Label(bg='#B22222')
e15.place(x=150, y=170, height=30, width=30)
e16= Label(bg='#B22222')
e16.place(x=120, y=200, height=30, width=90)
e17= Label(bg='#B22222')
e17.place(x=180, y=410, height=30, width=30)
e18= Label(bg='#B22222')
e18.place(x=150, y=440, height=30, width=60)

#---------------- LINHAS COR DA PELE ------------------------
f1= Label(bg='#FFA07A')
f1.place(x=120, y=230, height=30, width=30)
f2= Label(bg='#FFA07A')
f2.place(x=90, y=260, height=30, width=30)
f3= Label(bg='#FFA07A')
f3.place(x=150, y=260, height=90, width=30)
f4= Label(bg='#FFA07A')
f4.place(x=240, y=260, height=90, width=30)
f5= Label(bg='#FFA07A')
f5.place(x=240, y=260, height=90, width=30)
f6= Label(bg='#FFA07A')
f6.place(x=300, y=260, height=30, width=30)
f7= Label(bg='#FFA07A')
f7.place(x=360, y=260, height=30, width=30)
f8= Label(bg='#FFA07A')
f8.place(x=270, y=290, height=30, width=180)
f9= Label(bg='#FFA07A')
f9.place(x=210, y=320, height=60, width=30)
f10= Label(bg='#FF6347')
f10.place(x=240, y=230, height=30, width=30)
f11= Label(bg='#FF6347')
f11.place(x=210, y=260, height=30, width=30)
f12= Label(bg='#FF6347')
f12.place(x=300, y=230, height=30, width=30)
f13= Label(bg='#FF6347')
f13.place(x=360, y=230, height=30, width=30)
f14= Label(bg='#FF6347')
f14.place(x=90, y=290, height=30, width=30)
f15= Label(bg='#FF6347')
f15.place(x=120, y=320, height=30, width=30)
f16= Label(bg='#FF6347')
f16.place(x=150, y=350, height=30, width=60)
f17= Label(bg='#FF6347')
f17.place(x=210, y=380, height=30, width=90)
f18= Label(bg='#FF6347')
f18.place(x=300, y=320, height=30, width=150)



tela_Super_Mario.mainloop()
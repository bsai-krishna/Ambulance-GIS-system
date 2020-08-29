from tkinter import *
import csv
from tkinter import ttk

window=Tk()
window.configure(background='light blue')

def start():
    
    if (destination.get() == "" and source.get() == "") or (destination.get()==source.get()):
        print("empty/invalid inputs")
        
    with open("points.csv", "r") as f:
        roads = csv.reader(f)
        next(roads)
        for row in roads:
            if destination.get() == row[6]:
                dest=(int(row[0]),int(row[1]))
            if source.get()==row[6]:
                sour=(int(row[0]),int(row[1]))
        print(dest)
        print(sour)
        s=int(speed.get())
        print(s)
    #calling the main funtion in main.py ... we have to make main_function in main.py
    import main as m
    m.main_function(sour,dest,s)

var = StringVar()
var.set("Pulchowk")
data=("Pulchowk", "Baneswor", "Thapathali", "Maitighar","Gwarko","Patan","RNAC","Balaju","Kapan","Chabel")


lbl=Label(window, text="Ambulance GIS System", fg='black', font=("Helvetica", 20),bg='light blue')
lbl.place(x=70, y=20)

lbl1=Label(window, text=">> Enter your location speed and destination", fg='black', font=("Helvetica", 8),bg='light blue')
lbl1.place(x=80, y=100)
lbl2=Label(window, text=">> See Realtime Traffic at different places", fg='black', font=("Helvetica", 8),bg='light blue')
lbl2.place(x=80, y=120)
lbl3=Label(window, text=">> Get the best path suggested in the map", fg='black', font=("Helvetica", 8),bg='light blue')
lbl3.place(x=80, y=140)

lbl4=Label(window, text="Destination", fg='black', font=("Helvetica", 10),bg='light blue')
lbl4.place(x=160, y=180)

destination = ttk.Combobox(window, values=data)
destination.place(x=130,y=200)

lbl5=Label(window, text="Speed", fg='black', font=("Helvetica", 10),bg='light blue')
lbl5.place(x=160, y=230)
speed=Entry()
speed.place(x=140,y=250)

lbl5=Label(window, text="Where are you?", fg='black', font=("Helvetica", 10), bg='light blue')
lbl5.place(x=150, y=280)

source = ttk.Combobox(window, values=data)
source.place(x=130,y=300)

btn=Button(window, text="Start Driving", fg='white',bg='black',command=start)
btn.place(x=160, y=400)

window.title('Ambulance GIS System')
window.geometry("400x500+10+10")
window.mainloop()
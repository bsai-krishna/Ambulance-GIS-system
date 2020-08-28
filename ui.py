from tkinter import *
#from tkinter.ttk import Combobox
#import main as m
import csv

window=Tk()
window.configure(background='light blue')

def start():
	if (destination.get() == "" and source.get() == "") or (destination.get()==source.get()):
		print("empty/invalid inputs")
		
	with open("points.csv", "r") as f:
		roads = csv.reader(f)
		next(roads)
		for row in roads:
			if destination.get() == row[5]:
				dest=(row[0],row[1])
			if source.get()==row[5]:
				sour=(row[0],row[1])
		print(dest)
		print(sour)
	#calling the main funtion in main.py ... we have to make main_function in main.py
	#m.main_function(sour,dest)

var = StringVar()
var.set("Pulchowk")
data=("Pulchowk", "Baneswor", "Thapathali", "Maitighar","Jawlakhel","Kupondole")


lbl=Label(window, text="Ambulance GIS System", fg='black', font=("Helvetica", 20),bg='light blue')
lbl.place(x=70, y=20)

lbl=Label(window, text="Destination", fg='black', font=("Helvetica", 10),bg='light blue')
lbl.place(x=160, y=130)
destination=Entry()
destination.place(x=140,y=150)
d=destination.get()


#cb=Combobox(window, values=data)
#cb.place(x=60, y=150)

lbl1=Label(window, text="Where are you?", fg='black', font=("Helvetica", 10), bg='light blue')
lbl1.place(x=150, y=280)
source=Entry()
source.place(x=140,y=300)
s=source.get()

#cb1=Combobox(window, values=data)
#cb1.place(x=60, y=300)


btn=Button(window, text="Start Driving", fg='white',bg='black',command=start)
btn.place(x=160, y=400)

window.title('Ambulance GIS System')
window.geometry("400x500+10+10")
window.mainloop()
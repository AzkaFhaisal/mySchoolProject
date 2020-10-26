from tkinter import Tk, ttk

my_apps = Tk()

my_apps.title("My First Python Apps")
my_apps.resizable(True, True)

counterButton1 = 0

label1 = ttk.Label(my_apps, text="Pembuat Handphone \t:")
label1.grid(column=0, row=0)
label2 = ttk.Label(my_apps, text="Android")
label2.grid(column=1, row=0)

label3 = ttk.Label(my_apps, text="Merek Handphone \t:")
label3.grid(column=0, row=1)
label4 = ttk.Label(my_apps, text="One plus")
label4.grid(column=1, row=1)

label5 = ttk.Label(my_apps, text="Jenis Handphone \t\t:")
label5.grid(column=0, row=2)
label6 = ttk.Label(my_apps, text="One plus 8 pro")
label6.grid(column=1, row=2)

label7 = ttk.Label(my_apps, text="Besar Baterai \t\t:")
label7.grid(column=0, row=3)
label8 = ttk.Label(my_apps, text="4150 mAh")
label8.grid(column=1, row=3)

label9 = ttk.Label(my_apps, text="Tahun Pengeluaran \t:")
label9.grid(column=0, row=4)
label10 = ttk.Label(my_apps, text="2020")
label10.grid(column=1, row=4)

def change_color():
	global counterButton1
	button1.configure(text="Color has been changed")
	if counterButton1 % 2 == 0:
		label1.configure(foreground="blue")
	else:
		label1.configure(foreground="red")
	counterButton1 += 1

counterButton1 = 0
button1 = ttk.Button(my_apps, text="Change Color", command=change_color)
button1.grid(column=0, row=5)

if __name__ == "__main__":
	my_apps.mainloop()
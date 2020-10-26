from tkinter import Tk, Label, StringVar, ttk, Entry, Button

def calculate():
	matauangFrom = mata_uang.get()
	matauangTo = toMataUang.get()
	nilai = int(nilai_mata_uang.get())
	additionalFrom = 0
	additionalTo = 0

	if matauangTo == 'Euro':
		matauangTo = 0.0000576
	elif matauangTo == 'Yen':
		matauangTo = 0.00714
	elif matauangTo == 'Dollar':
		matauangTo = 0.0000679
	elif matauangTo == 'Won':
		matauangTo = 0.0768

	result = (nilai)*(matauangTo)

	label_value_res.config(text=str(result))

window = Tk()
window.title("Converter CUrrency")
#window.minsize(800, 600)
window.resizable(False, False)

header_apps = Label(window, text="MATA UANG KONVERTER", font=('arial', 20, 'bold'), bd=20, padx=19, pady=15, bg="turquoise")
header_apps.grid(columnspan=3)

label_from = Label(window, text="FROM", font=('arial', 18, 'bold'), bg="lime",bd=20,padx=10, pady=15, justify="left")
label_from.grid(column= 0, row= 1)

label_value = Label(window, text="VALUE", font=('arial', 18, 'bold'), bg="lime",bd=20,padx=10, pady=15, justify="left")
label_value.grid(column= 1, row= 1)

label_process = Label(window, text="PROCESS", font=('arial', 18, 'bold'), bg="lime",bd=20,padx=10, pady=15, justify="left")
label_process.grid(column= 2, row= 1)

mata_uang = StringVar()
combo_mata_uang = ttk.Combobox(window, textvariable=mata_uang, font=('arial', 18, 'bold'), width=5)
combo_mata_uang['values'] = ['Rupiah']
combo_mata_uang.grid(column = 0, row = 2)
combo_mata_uang.current(0)

nilai_mata_uang = StringVar()
entry_nilai_mata_uang = Entry(window, textvariable=nilai_mata_uang, font=('arial', 18, 'bold'), width=8)
entry_nilai_mata_uang.grid(column=1, row=2)

button_process = Button(window, font=('arial', 18,'bold'), text="OK!", command=calculate)
button_process.grid(column=2, row=2)

toMataUang = StringVar()
combo_toMataUang = ttk.Combobox(window, textvariable=toMataUang, font=('arial', 18, 'bold'), width=5)
combo_toMataUang['values'] = ['Euro', 'Yen', 'Dollar', 'Won']
combo_toMataUang.grid(column = 0, row = 4)
combo_toMataUang.current(0)

label_value_res = Label(window, text="0", font=('arial', 18, 'bold'), bg="lime",bd=20,padx=10, pady=15, justify="left")
label_value_res.grid(column= 1, row= 4)

window.mainloop()
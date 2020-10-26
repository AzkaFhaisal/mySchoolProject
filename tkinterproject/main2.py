from tkinter import Tk, ttk, StringVar

handphone_data = {}


my_apps = Tk()
my_apps.title("My Apps")
#my_apps.resizable(False, False)

#label
label1 = ttk.Label(my_apps, text="Enter the Handhone Creator")
label1.grid(column=0, row=0)

label2 = ttk.Label(my_apps, text="Brand")
label2.grid(column=1, row=0)

label3 = ttk.Label(my_apps, text="Model")
label3.grid(column=2, row=0)

label4 = ttk.Label(my_apps, text="Battery")
label4.grid(column=3, row=0)

label5 = ttk.Label(my_apps, text="Year")
label5.grid(column=4, row=0)

def action_button():
	global counterButton1 
	button1.configure(text="Already Clicked")
	if counterButton1 % 2 == 0:
		label1.configure(foreground="blue")
		label2.configure(foreground="blue")
		label3.configure(foreground="blue")
		label4.configure(foreground="blue")
		label5.configure(foreground="blue")
	else:
		label1.configure(foreground="green")
		label2.configure(foreground="green")
		label3.configure(foreground="green")
		label4.configure(foreground="green")
		label5.configure(foreground="green")
	label1.configure(text=data_handphone_creator.get())
	label2.configure(text=data_brand.get())
	label3.configure(text=data_model.get())
	label4.configure(text=data_battery.get())
	label5.configure(text=data_year.get())
	counterButton1 += 1
	handphone_data[data_handphone_creator.get()] = (data_brand.get(), data_model.get(), data_battery.get(), data_year.get())
	print(handphone_data)

#button
counterButton1 = 0
button1 = ttk.Button(my_apps, text="Click Here", command=action_button)
button1.grid(column=5, row=1)

#entry
data_handphone_creator = StringVar()
data_handphone_creator_entry = ttk.Entry(my_apps, width=12, textvariable=data_handphone_creator)
data_handphone_creator_entry.grid(column=0, row=1)

#focus
data_handphone_creator_entry.focus()

#combobox dropdown list
data_brand = StringVar()
#data_age_combobox = ttk.Combobox(my_apps, width=12, textvariable=data_age)
data_brand_combobox = ttk.Combobox(my_apps, width=12, textvariable=data_brand, state="readonly") #state="readonly"
data_brand_combobox['value'] = ["OTHER","Samsung","Iphone","One Plus","Xiaomi","Huawei"]
data_brand_combobox.grid(column=1, row=1)
data_brand_combobox.current(0)


data_model = StringVar()
data_model_combobox = ttk.Combobox(my_apps, width=15, textvariable=data_model, state="readonly")
data_model_combobox['value'] = ["OTHER","Galaxy A5","Galaxy Note 10","Galaxy S10","10","10 Pro","11","11 Pro","11 Pro Max","8 Pro","One 64 GB","7T","One 16 GB","Redmi K30 5G","Redmi K30i 5G","POCO F2 PRO","Redmi Note 9","Redmi Note 9 Pro","Redmi Note 7","P40 Pro+","P40","P40 Pro","Mate Xs","Mate 30Pro"]
data_model_combobox.grid(column=2, row=1)
data_model_combobox.current(0)

data_battery = StringVar()
data_battery_combobox = ttk.Combobox(my_apps, width=12, textvariable=data_battery, state="readonly")
data_battery_combobox['value'] = ["MORE","5000 mAh","4500 mAh","4150 mAh","4000 mAh","LESS"]
data_battery_combobox.grid(column=3, row=1)
data_battery_combobox.current(0)

data_year = StringVar()
data_year_combobox = ttk.Combobox(my_apps, width=12, textvariable=data_year, state="readonly")
data_year_combobox['value'] = ["MORE",2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,"LESS"]
data_year_combobox.grid(column=4, row=1)
data_year_combobox.current(0)


if __name__ == "__main__":
	my_apps.mainloop()
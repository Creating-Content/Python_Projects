from tkinter import *
from tkinter import ttk
import requests 

def data_get():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d979753f5e4212e6aed0af33c021666c").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=f"{int(data['main']['temp']-273.15)}°C")
    per_label1.config(text=f"{data['main']['pressure']} hPa")

win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("500x600")

name_label = Label(win, text="Cool Weather App", font=("Arial", 30, "bold"), bg="lightblue")
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Arial", 20), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Arial", 20), bg="lightblue")
w_label.place(x=25, y=200, height=40, width=210)
w_label1 = Label(win, text="", font=("Arial", 20), bg="lightblue")
w_label1.place(x=250, y=200, height=40, width=210)

wb_label = Label(win, text="Weather Description", font=("Arial", 17), bg="lightblue")
wb_label.place(x=25, y=260, height=40, width=210)
wb_label1 = Label(win, text="", font=("Arial", 17), bg="lightblue")
wb_label1.place(x=250, y=260, height=40, width=210)

temp_label = Label(win, text="Temperature", font=("Arial", 20), bg="lightblue")
temp_label.place(x=25, y=320, height=40, width=210)
temp_label1 = Label(win, text="", font=("Arial", 20), bg="lightblue")
temp_label1.place(x=250, y=320, height=40, width=210)

per_label = Label(win, text="Pressure", font=("Arial", 20), bg="lightblue")
per_label.place(x=25, y=380, height=40, width=210)
per_label1 = Label(win, text="", font=("Arial", 20), bg="lightblue")
per_label1.place(x=250, y=380, height=40, width=210)

done_button = Button(win, text="Get Weather", font=("Arial", 20, "bold"), command=data_get, bg="blue", fg="white")
done_button.place(y=460, height=50, width=200, x=150)

win.mainloop()

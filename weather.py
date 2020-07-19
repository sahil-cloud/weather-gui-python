import requests
from tkinter import *

def btn_click():
    text = word.get()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={ur api key}'.format(text)
    res = requests.get(url)
    op = res.json()

    weather_status = op['weather'][0]['description']
    temp = op['main']['temp'] - 273
    humidity = op['main']['humidity']
    wind_speed = op['wind']['speed']

    weather_label.configure(text="Weather status:"+ weather_status)
    temp_label.configure(text="Tempreture:"+ str(temp))
    humid_label.configure(text="Humidity:"+ str(humidity))
    wind_label.configure(text="Wind speed:"+ str(wind_speed))

root = Tk()
root.geometry("500x400")


# tkinter code
label = Label(root,text="Weather Forecast",font="luicida 15 bold")
label.place(x=140,y=0)

font = ("Helvetica", 16, "bold")
word = StringVar()
city = Entry(root, textvariable=word, font=font)
city.place(x=120,y=40)

city.insert(0, "Enter city")
city.configure(state=DISABLED)

def on_click(event):
    city.configure(state=NORMAL)
    city.delete(0, END)

    # make the callback only work once
    city.unbind('<Button-1>', on_click_id)


on_click_id = city.bind('<Button-1>', on_click)


sendBtn = Button(root, text="SEARCH", command=btn_click)
sendBtn.place(x=180, y=80)

temp_label = Label(root,font="luicida 14 bold")
temp_label.place(x=80,y=140)

humid_label = Label(root,font="luicida 14 bold")
humid_label.place(x=80,y=170)

wind_label = Label(root, font="luicida 14 bold")
wind_label.place(x=80, y=200)

weather_label = Label(root,font="luicida 14 bold")
weather_label.place(x=80,y=110)
root.mainloop()

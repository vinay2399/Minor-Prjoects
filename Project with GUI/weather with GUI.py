from tkinter import *
import requests, json

def weather_of_city():
    city_name=cityname.get()
    api_key = "2a4ad0843389c0826c569394c4f71f00"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in celcius unit) = " +
					str(current_temperature-273.15) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))
        output=Label(root,text=" Temperature (in celcius unit) = " +
					str(current_temperature-273.15) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description)).grid(row=2,column=0,sticky='w',padx=100,pady=10,columnspan=100,rowspan=10)
    else:
        print('city not found')

root=Tk()
root.grid()
root.geometry("700x500+0+0")
root.title('Weather App')
label=Label(root,text='Enter city: ').grid(row=0,column=0,sticky='E',padx=20,pady=20)
cityname=Entry(root,width=20,bd=5)
cityname.grid(row=0,column=1)
submit = Button(text='Get Weather information',activebackground='white',activeforeground='black',relief='raised',bg='white',fg='black',command=weather_of_city).grid(row=1,column=1)

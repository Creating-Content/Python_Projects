import pyttsx3 as p
import speech_recognition as sre
import datetime as dt
import pyowm as OM
import webbrowser as web
import os
import smtplib as smt

# Initialize pyttsx3
sound = p.init('sapi5')
voices = sound.getProperty('voices')
sound.setProperty('voice', voices[1].id)

# Define speak function to convert text to speech
def speak(audio):
    sound.say(audio)
    sound.runAndWait()

# Greeting function
def greeting():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    elif 18 <= hour < 22:
        speak("Good Evening")
    else:
        speak("Good Night!")
    speak("Namaste! I am Ark. I am your personal Voice Assistant. How may I help you?")

# Command function to recognize user's speech
def command():
    mic = sre.Recognizer()
    with sre.Microphone() as source:
        print("Listening...")
        mic.pause_threshold = 1
        audio = mic.listen(source)

    try:
        print("Recognizing...")
        question = mic.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")
    except Exception as e:
        print("Can you repeat? I couldn't understand.")
        speak("Can you repeat? I couldn't understand. Otherwise, please try again later.")
        return "none"
    return question

# Function to send email
def send_email(to, subject, body):
    msg = smt.SMTP('smtp.gmail.com', 587)
    msg.ehlo()
    msg.starttls()
    msg.login('your_email@gmail.com', 'your_password')
    message = f"Subject: {subject}\n\n{body}"
    msg.sendmail('your_email@gmail.com', to, message)
    msg.quit()
    speak("Email sent Successfully.")

# Function to get weather
def get_weather(city):
    owm = OM('your_openweathermap_api_key')
    weather_manager = owm.weather_manager()
    observation = weather_manager.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    status = w.status
    speak(f"The weather in {city} is {status} with a temperature of {temperature} degrees Celsius.")

if __name__ == "__main__":
    greeting()
    while True:
        question = command().lower()

        # Executing tasks based on the command
        if 'hello' in question:
            speak('Hello Dear, How can I assist you?')
                
        elif 'open youtube' in question:
            web.open("https://www.youtube.com")
        elif 'open google' in question:
            web.open("https://www.google.com")
        elif 'play song' in question:
            sound_dir = "C:\\Users\\ARKA\OneDrive\\Documents\\Voice Assistant"
            song = [file for file in os.listdir(sound_dir) if file.lower().endswith('.mp3')]
            if song:
                print(f"Playing: {song[0]}")
                os.startfile(os.path.join(sound_dir, song[0]))
            else:
                print("No MP3 files found in the specified directory.")
        elif 'get time' in question:
            str_time = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"The Current Time is {str_time}")
        elif 'get date' in question:
            str_date = dt.datetime.now().strftime("%Y-%m-%d")
            speak(f"The Current Date is {str_date}")
        elif "email" in question:
            speak("To whom do you want to send a mail")
            recipient = command()
            speak("What should be the subject of the mail")
            email_subject = command()
            speak("Please dictate the body of the email.")
            email_body = command()
            send_email(recipient, email_subject, email_body)
        elif "weather" in question:
            speak("Sure, which city would you like to check the weather for?")
            city = command()
            if city:
                get_weather(city)
        elif "exit" in question or "bye" in question:
            speak("Goodbye! Have a great day.")
            quit()

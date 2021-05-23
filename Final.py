import keyboard
from pygame import mixer
from colorama import Fore
from pyautogui import click
# from keyboard import press
# from keyboard import write
from selenium import webdriver
from plyer import notification
from scipy.io.wavfile import write

import pyttsx3
import sounddevice
import speech_recognition as sr
import pywhatkit as kit
import webbrowser
import wikipedia
import threading
import datetime
import requests
import winsound
import speedtest
import smtplib
import random
import PyPDF2
import socket
import time
import cv2
import os

# Variable Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)


# The Speak Function Defines the speaking of computer
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish Me Function Helps in Greeting the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak('Good Morning Atharv.. I am Your Assistant Roboto.. How can I help you?')
    if 12 <= hour < 16:
        speak('Good Afternoon Atharv.. I am Your Assistant Roboto.. How can I help you?')
    if 16 <= hour < 19:
        speak('Good Evening Atharv.. I am Your Assistant Roboto.. How can I help you?')
    if 19 <= hour < 24:
        speak('Good Night Atharv.. I am Your Assistant Roboto.. How can I help you?')


# takeCommand function takes the microphone input from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening Command...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print(Fore.GREEN + "Recognizing Command...\n")
        query = r.recognize_google(audio_data=audio, language='en-in')
        print(Fore.GREEN + f"User Command is: {query}\n")

    except Exception as e:
        print(e)
        speak("Sorry Atharv! can you please repeat the Command!")
        return "None"
    return query


# sendEmail function sends the email to the respected person
def sendEmail(userEmail, userPassword, mailtoEmail, mailContent):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(userEmail, userPassword)
    server.sendmail(userEmail, mailtoEmail, mailContent)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'how are you' in query or 'how do you do' in query or 'how is going on' in query:
            speak('Could not be better. Is there anything I can do for you?')

        elif 'hi' in query or 'hello' in query or 'hey' in query:
            speak('Hello Sir, Is there anything I can do for you?')

        elif 'are you there' in query:
            speak("Yes Sir, Always in your service")

        elif 'wikipedia' in query or 'wiki' in query:
            speak('Searching in Wikipedia..')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('From Wikipedia\n')
            print(Fore.GREEN + result)
            speak(result)

        elif 'open google' in query or 'google.com' in query:
            webbrowser.open('google.com')

        elif 'open wiki' in query or 'open wikipedia.com' in query:
            webbrowser.open('wikipedia.com')

        elif 'open youtube' in query or 'open youtube.com' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query or 'open stackoverflow.com' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play in youtube' in query or 'play youtube video' in query:
            speak("What Should I Play in Youtube?")
            print(Fore.GREEN + 'Computer: What Should I Search?')
            search = takeCommand()
            kit.playonyt(search)
        elif 'search in youtube' in query or 'search youtube' in query:
            driver = webdriver.Chrome()
            driver.get('https://www.youtube.com')
            speak("What Should I Search in Youtube?")
            searchInput = takeCommand()
            searchBox = driver.find_element_by_xpath('//*[@id="search"]')
            searchBox.send_keys(searchInput)
            searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            searchButton.click()
        elif 'open vs code' in query or 'open code' in query:
            speak("Opening Vs Code")
            vsPath = 'G:\\Atharv\\Microsoft VS Code\\Code.exe'
            os.startfile(vsPath)
        elif 'close vs code' in query or 'close code' in query:
            os.system('TASKKILL /F /IM Code.exe')

        elif 'open pycharm' in query:
            pyPath = 'G:\\Atharv\\Pycharm Downloaded\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe'
            os.startfile(pyPath)
        elif 'close pycharm' in query or 'close pycharm' in query:
            os.system('TASKKILL /F /IM pycharm64.exe')

        elif 'open chrome' in query:
            chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chromePath)
        elif 'close chrome' in query or 'close chrome' in query:
            os.system('TASKKILL /F /IM chrome.exe')

        elif 'open code blocks' in query:
            blockPath = 'G:\\Atharv\\C++\\CodeBlocks\\codeblocks.exe'
            os.startfile(blockPath)
        elif 'close code blocks' in query or 'close code blocks' in query:
            os.system('TASKKILL /F /IM codeblocks.exe')

        elif 'open explorer' in query:
            exPath = 'C:\\Windows\\explorer.exe'
            os.startfile(exPath)
        elif 'close explorer' in query or 'close explorer' in query:
            os.system('TASKKILL /F /IM explorer.exe')

        elif 'open to do' in query or 'open microsoft to do' in query:
            todoPath = 'C:\\Users\\athar\\OneDrive\\Desktop\\Microsoft To Do.lnk'
            os.startfile(todoPath)

        elif 'open store' in query or 'open microsoft store' in query:
            storePath = 'C:\\Users\\athar\\OneDrive\\Desktop\\Microsoft Store.lnk'
            os.startfile(storePath)

        elif 'open mail' in query or 'open mail app' in query:
            mailPath = 'C:\\Users\\athar\\OneDrive\\Desktop\\Mail.lnk'
            os.startfile(mailPath)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(Fore.GREEN + f"The Time is: {strTime}")
            speak(f"Atharv The Time is: {strTime}")

        elif 'weather' in query or 'temprature' in query:
            speak("Please tell the Name of  the City")
            nameInput = takeCommand()
            api = 'http://api.openweathermap.org/data/2.5/weather?&appid=143454aa39bbe3442a890cdbf3f9db36&q=' + nameInput
            json_link = requests.get(api)
            json_data = json_link.json()
            temp_data = ((json_data['main']['temp']) - 273.15)
            feelTemp_data = ((json_data['main']['feels_like']) - 273.15)
            humidTemp_data = json_data['main']['humidity']
            print(Fore.GREEN + "The temperature is: {:.1f} deg C".format(temp_data))
            speak("The temperature is: {:.0f} ".format(temp_data) + "degree Celcius")
            print(Fore.GREEN + "It Feels Like: {:.1f} deg C".format(feelTemp_data))
            speak("It Feels Like: {:.0f} ".format(feelTemp_data) + "degree Celcius")
            print(Fore.GREEN + "The Humidity is: ", humidTemp_data)
            speak(f"The Humidity is: {humidTemp_data}")

        elif 'text to handwriting' in query:
            print(Fore.GREEN + 'Computer: What is the Text?')
            speak('What is the Text?')
            text = takeCommand()
            kit.text_to_handwriting(text, "handwriting.png")

        elif 'send mail' in query or 'send email' in query:
            try:
                speak('Please Enter your Email Address?')
                userEmail = input("Enter The Email: ")

                speak('Please enter your Password?')
                userPassword = input("Enter The Password: ")

                speak('Please enter The Email Address where You want to Send the Email?')
                mailtoEmail = input("Enter The Email Address where You want to Send the Email: ")

                speak('What is the mail content?')
                mailContent = takeCommand()

                sendEmail(userEmail, userPassword, mailtoEmail, mailContent)
                speak("Congo! The Email Has Been Sent")
            except Exception as e:
                print(e)
                print(Fore.GREEN + "Sorry Atharv I am Not able to send the mail kindly check the information again")
                speak("Sorry Atharv I am Not able to send the mail kindly check the information again")

        elif 'notify' in query or 'notification' in query:
            speak('Please Enter The Title')
            title = input('Enter The Title: ')
            speak('What is the message For The Notification?')
            message = takeCommand()
            speak('In What time you want to show the notification again please enter the value in seconds')
            wait = int(input("Enter The time you want to show the notification again: "))
            speak('The Loop of notification will end only when roboto will be turned off')
            while True:
                notification.notify(
                    title=title,
                    message=message,
                    timeout=5
                )
                time.sleep(wait)

        elif 'record' in query:
            fs = 44100
            second = int(input("Enter for how much seconds you want to record audio? "))
            print("Recording....")
            rec_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
            sounddevice.wait()
            write("record.wav", fs, rec_voice)

        elif 'search google' in query:
            speak("What Should I Search?")
            print(Fore.GREEN + 'Computer: What Should I Search?')
            searchGoogle = takeCommand()
            kit.search(searchGoogle)

        elif 'alarm' in query:
            print(Fore.GREEN + 'Computer: Please tell me the hour?')
            speak('Please tell me the hour?')
            input1 = int(input("Please enter the hour? "))

            print(Fore.GREEN + 'Computer: Please tell me the minute?')
            speak('Please tell me the minute?')
            input2 = int(input("Please enter the minute? "))
            while 1 == 1:
                if input1 == datetime.datetime.now().hour and input2 == datetime.datetime.now().minute:
                    mixer.init()
                    mixer.music.load('C:\\Users\\athar\\Music\\Playlists\\Alarm\\New Day - Patrick Patrikios.mp3')
                    mixer.music.play()
                    time.sleep(20)
                    mixer.music.stop()
                    break
        elif 'music' in query:
            musicDir = 'C:\\Users\\athar\\Music\\Playlists'
            songs = os.listdir(musicDir)
            i = random.randint(0, 11)
            os.startfile(os.path.join(musicDir, songs[i]))
        elif 'open cctv' in query or 'open cctv camera' in query:
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dailation = cv2.dilate(thresh, None, iterations=3)
                contors, _ = cv2.findContours(dailation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for c in contors:
                    if cv2.contourArea(c) < 5000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow(' Atharv Security_Python Camera', frame1)
        elif 'audio book' in query:
            speak('What is the name of the pdf?')
            namepdf = takeCommand()
            book = open(namepdf, 'rb')
            pdf_read = PyPDF2.PdfFileReader(book)
            pages = pdf_read.numPages
            print(pages)
            for num in range(0, pages):
                page = pdf_read.getPage(0)
                text = page.extractText()
                speak(text)
        elif 'open run rate teller' in query:
            print("Welcome to Run Rate teller\n")
            overs = int(input("Enter the number of Overs:"))
            runs = int(input("Enter the runs of the Team:"))
            chase_runs = int(input("Enter the number of Runs which Your Team has to made:"))
            if overs > 100:
                print("Please Enter a valid overs!!")

            elif runs > 700:
                print("Please Enter a valid runs!!")

            elif runs / overs > 36:
                print("In an Over maximum 36 runs can be made!!")

            elif chase_runs / overs > 36:
                print("In an Over maximum 36 runs can be made!!")

            elif chase_runs != 0:
                print(f"The Run Rate of the Team is: {runs / overs}")
                print(f"The Required Run Rate of the Team is: {chase_runs / overs}")

            else:
                print(f"The Run Rate of the Team is: {runs / overs}")
        elif 'chat server' in query:
            host = '127.0.0.1'
            port = 55555

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()
            clients = []
            nicknames = []


            def broadcast(message):
                for client in clients:
                    client.send(message)


            def handle(client):
                while True:
                    try:
                        message = client.recv(1024)
                        broadcast(message)
                    except:
                        index = client.index(client)
                        client.remove(client)
                        nickname = nicknames[index]
                        broadcast(f'{nickname} Left The Chat Room!'.encode('ascii'))
                        nicknames.remove(nickname)
                        break


            def recive():
                while True:
                    client, address = server.accept()
                    print(f"Connected With Address {str(address)}")

                    client.send('Nick'.encode('ascii'))
                    nickname = client.recv(1024).decode('ascii')
                    nicknames.append(nickname)
                    clients.append(client)

                    print(f"Nick Name Of the client is {nickname}")
                    broadcast(f"{nickname} joined the Chat Room!".encode('ascii'))
                    client.send("Connected To The Room!".encode('ascii'))

                    thread = threading.Thread(target=handle, args=(client,))
                    thread.start()


            print("Server has started listening....")
            recive()
        elif 'start chatting' in query or 'join chat room' in query or 'join chatting room' in query:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 55555))

            nickname = input("Please Choose Your Nick Name: ")


            def recive():
                while True:
                    try:
                        message = client.recv(1024).decode('ascii')
                        if message == 'NICK':
                            client.send(nickname.encode('ascii'))
                        else:
                            print(message)
                    except:
                        print("There is a error in connection!")
                        client.close()
                        break


            def write():
                while True:
                    message = f'{nickname}: {input("")}'
                    client.send(message.encode('ascii'))


            recive_thread = threading.Thread(target=recive)
            recive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
        elif 'what are the headlines' in query or 'headlines' in query or 'news' in query:
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 140)
            api2 = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=390417508a024964911177d1052445aa'
            json_link2 = requests.get(api2)
            json_data2 = json_link2.json()
            title_data = json_data2['articles'][0]['title']
            content_data = json_data2['articles'][0]['description']
            print(title_data)
            speak(title_data)
            print(f"{content_data} \n")
            speak(content_data)
            title_data2 = json_data2['articles'][3]['title']
            content_data2 = json_data2['articles'][3]['description']
            print(title_data2)
            speak(title_data2)
            print(f"{content_data2} \n")
            speak(content_data2)
            title_data3 = json_data2['articles'][4]['title']
            content_data3 = json_data2['articles'][4]['description']
            print(title_data3)
            speak(title_data3)
            print(f"{content_data3} \n")
            speak(content_data3)
            title_data4 = json_data2['articles'][5]['title']
            content_data4 = json_data2['articles'][5]['description']
            print(title_data4)
            speak(title_data4)
            print(f"{content_data4} \n")
            speak(content_data4)
            title_data5 = json_data2['articles'][6]['title']
            content_data5 = json_data2['articles'][6]['description']
            print(title_data5)
            speak(title_data5)
            print(f"{content_data5} \n")
            speak(content_data5)
        elif 'speed test' in query or 'internet speed' in query:
            speed = speedtest.Speedtest()
            downloadSpeed = speed.download()
            uploadSpeed = speed.upload()

            mix1 = int(int(downloadSpeed)/800000)
            mix2 = int(int(uploadSpeed)/800000)

            speak(f"The Download speed is: {mix1}Mbps")
            speak(f"The Upload speed is: {mix2}Mbps")
            print(f"The Download speed is: {mix1}Mbps")
            print(f"The Upload speed is: {mix2}Mbps")
        elif 'whatsapp message' in query:
            def sendWhatsappMsg():
                speak("Please tell the name of the Person.. to which you want to send the message?")
                name = takeCommand()
                speak("Please tell the message?")
                mainMessage = takeCommand()
                driver = webdriver.Chrome()
                driver.get('https://web.whatsapp.com')

                time.sleep(10)

                searchInputBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                searchInputBox.send_keys(name)

                time.sleep(5)

                queryBox = driver.find_element_by_xpath('')
                queryBox.click()

                # messageBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                # messageBox.click()


            # webbrowser.open("https://web.whatsapp.com")
                # time.sleep(15)
                # click(x=151, y=190)
                # keyboard.write(name)
                # time.sleep(2)
                # click(x=110, y=312)
                # time.sleep(2)
                # click(x=673, y=699)
                # keyboard.write(mainMessage)
            sendWhatsappMsg()
        elif 'quit' in query or 'exit' in query:
            print(Fore.RED + 'Ending All Running Tasks...')
            print(Fore.RED + 'Quitting...')
            time.sleep(2)
            exit()

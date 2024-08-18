import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
import random
import pyjokes
import requests,json

api_key = "328594b42f178c9e880f40f9c21c1ad2"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + "Ahmedabad"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<12:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")

    speak("I am Donna , tell me how may I help you")


def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        #speak("Say that again please...")
        return"None"
    return query

wake='hello friday' or 'Jarvis'
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query.count(wake)>0:
            speak('yes sir')
            query = takeCommand()
#=========== WIKIPEDIA =========================================
            if "Wikipedia" in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)
#=========== HELLO how are you =================================                
            elif 'hello how are you' in query:
                speak('i am fine sir, how are you? what can i help')
#=========== SPOTIFY ==================================
            elif 'open spotify' in query or 'play a song' in query:
                os.startfile("C:\\Users\\dh1011tu\\OneDrive\\Desktop\\Spotify")
                def spotify():
                    class InvalidSearchError(Exception):
                        pass

                    def get_album_uri(spotify: Spotify, name: str) -> str:
                        """
                        :param spotify: Spotify object to make the search from
                        :param name: album name
                        :return: Spotify uri of the desired album
                        """

                        # Replace all spaces in name with '+'
                        original = name
                        name = name.replace(' ', '+')

                        results = spotify.search(q=name, limit=1, type='album')
                        if not results['albums']['items']:
                            raise InvalidSearchError(f'No album named "{original}"')
                        album_uri = results['albums']['items'][0]['uri']
                        return album_uri

                    def get_artist_uri(spotify: Spotify, name: str) -> str:
                        """
                        :param spotify: Spotify object to make the search from
                        :param name: album name
                        :return: Spotify uri of the desired artist
                        """

                        # Replace all spaces in name with '+'
                        original = name
                        name = name.replace(' ', '+')

                        results = spotify.search(q=name, limit=1, type='artist')
                        if not results['artists']['items']:
                            raise InvalidSearchError(f'No artist named "{original}"')
                        artist_uri = results['artists']['items'][0]['uri']
                        print(results['artists']['items'][0]['name'])
                        return artist_uri

                    def get_track_uri(spotify: Spotify, name: str) -> str:
                        """
                        :param spotify: Spotify object to make the search from
                        :param name: track name
                        :return: Spotify uri of the desired track
                        """

                        # Replace all spaces in name with '+'
                        original = name
                        name = name.replace(' ', '+')

                        results = spotify.search(q=name, limit=1, type='track')
                        if not results['tracks']['items']:
                            raise InvalidSearchError(f'No track named "{original}"')
                        track_uri = results['tracks']['items'][0]['uri']
                        return track_uri

                    def play_album(spotify=None, device_id=None, uri=None):
                        spotify.start_playback(device_id=device_id, context_uri=uri)

                    def play_artist(spotify=None, device_id=None, uri=None):
                        spotify.start_playback(device_id=device_id, context_uri=uri)

                    def play_track(spotify=None, device_id=None, uri=None):
                        spotify.start_playback(device_id=device_id, uris=[uri])

                    # -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

                    client_id = 'b7559059c68a4ef69171e0b6c76c43fb'
                    client_secret = '85a7350fb96b4c4481c31b86cfa9e2d8'
                    device_name = "HP"
                    redirect_uri = 'https://example.com/callback'
                    username = 'fd4hycy4x9sahsya5cr52xnuk'
                    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

                    auth_manager = SpotifyOAuth(
                        client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope,
                        username=username)
                    spotify = sp.Spotify(auth_manager=auth_manager)

                    devices = spotify.devices()
                    deviceID = None
                    for d in devices['devices']:
                        d['name'] = d['name'].replace('’', '\'')
                        if d['name'] == device_name:
                            deviceID = d['id']
                            break

                    # -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x


                    engine.setProperty('rate', 150)


                    def takeCommand():
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Listening...")
                            r.pause_threshold = 1.5
                            audio = r.listen(source)

                        try:
                            print("Recognizing...")
                            query = r.recognize_google(audio, language='en-in')
                            print(f"User said: {query}\n")

                        except Exception as e:

                            print("Say that again please...")
                            return "None"
                        return query

                    def speak(audio):
                        engine.say(audio)
                        engine.runAndWait()

                    speak("i have opened spotify for you, what song would you like me to play")
                    print("i have opened spotify for you, what song would you like me to play")
                    while True:
                        print("Listening")
                        query = takeCommand()
                        print(query)
                        words = query.split()
                        if len(words) <= 1:
                            print('Could not understand. Try again')
                            continue

                        name = ' '.join(words[0:])
                        try:
                            if 'kill' in words:
                                os.system('taskkill /IM "Spotify.exe" /F')
                                speak("ok sir, i have closed spotify")
                                print("ok sir, i have closed spotify")
                                break

                            uri = get_track_uri(spotify=spotify, name=name)
                            play_track(spotify=spotify, device_id=deviceID, uri=uri)
                        except InvalidSearchError:
                            print('InvalidSearchError. Try Again')
                spotify()
#============= WHATSAPP ===============================
            elif 'open WhatsApp'in query:
                os.startfile('C:\\Users\\jayam patel\\AppData\\Local\\WhatsApp\\WhatsApp')
            elif 'close WhatsApp' in query:
                os.system('taskkill /IM "WhatsApp.exe" /F')
                speak("ok sir, i have closed WhatsApp")
                print("ok sir, i have closed WhatsApp")
#=========== CHROME =================================                
            elif 'open Chrome'in query:
                os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome')
            elif 'close Chrome' in query:
                os.system('taskkill /IM "Chrome.exe" /F')
                speak("ok sir, i have closed Chrome")
                print("ok sir, i have closed Chrome")
            
#=========== YOUTUBE =================================
            elif 'open YouTube' in query:
                webbrowser.open("https://www.youtube.com/")
            elif 'close YouTube' in query:
                os.system('taskkill /IM "Chrome.exe" /F')
                speak("ok sir, i have closed YouTube")
                print("ok sir, i have closed YouTube")
#=========== GOOGLE =================================
            elif 'open Google' in query:
                webbrowser.open("https://www.google.com/")
            elif 'close Google' in query:
                os.system('taskkill /IM "Chrome.exe" /F')
                speak("ok sir, i have closed Google")
                print("ok sir, i have closed Google")
#=========== BRAVE =================================
            elif 'open Brave' in query:
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave')
            elif 'close Brave' in query:
                os.system('taskkill /IM "Brave.exe" /F')
                speak("ok sir, i have closed Brave")
                print("ok sir, i have closed Brave")
#=========== INSTAGRAM =================================
            elif 'open Instagram' in query:
                webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen")
            elif 'close Instagram' in query:
                os.system('taskkill /IM "Chrome.exe" /F')
                speak("ok sir, i have closed Instagram")
                print("ok sir, i have closed Instagram")
#=========== MUSIC =================================                
            elif 'play some music' in query:
                music='C:\\Users\\jayam patel\\Desktop\\my stuff\\songs\\New folder'
                songs=os.listdir(music)
                #print(songs)
                os.startfile(os.path.join(music, songs[random.randrange(0,172)]))
#=========== NEXT SONG =================================                
            elif 'next song' in query:
                music='C:\\Users\\jayam patel\\Desktop\\my stuff\\songs\\New folder'
                songs=os.listdir(music)
                print(songs)
                os.startfile(os.path.join(music, songs[random.randrange(0,172)]))
#=========== CODE =================================
            elif 'open code' in query:
                code='C:\\Users\\jayam patel\\Desktop\\my stuff\\python script\\JARVIS\\Jarvis.py'
                os.startfile(code)
                
#=========== TIME =================================              
            elif 'what is the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir, the time is "+strTime)
#=========== EMAIL =================================                
            elif 'send email' in query:

                    def takeCommand2():
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Listening...")
                            r.pause_threshold = 1
                            audio = r.listen(source)

                        print("Recognizing...")
                        query = r.recognize_google(audio, language='en-in')
                        print(f"User said: {query}\n")
                        return query


                    emails = {'Smit': 'smit.desai@gmail.com', 'Dhruv': 'dhruv2104@gmail.com',
                              'Dev': 'devpatel7070@gmail.com', 'friend': 'jjp1735@gmail.com',
                              'Ansh': 'anshjarvis2003@gmail.com', 'Manushi': 'bhavsarmanushi@yahoo.in',
                              'friend': 'rishipatel3103@gmail.com'}

                    speak('send to whom?')
                    email = takeCommand2()
                    while email == '':
                        email = takeCommand2()
                    email_id = ''
                    for i in emails:
                        if i == email:
                            email_id = emails[i]

                    speak("What should I write?")
                    content = ''
                    while content == '':
                        content = takeCommand2()

                    print(content)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('jjp1735@gmail.com', '412003jjp')
                    server.sendmail('jjp1735@gmail.com', email_id, content)
                    server.close()


                    speak('Email has been sent succesfully!')
#=========== GMAIL =================================
            elif 'open gmail' in query:
                webbrowser.open("gmail.com")
#=========== JOKE =================================
            elif 'tell me a joke' in query:
                speak('sure, here is one')
                result=pyjokes.get_joke()
                print(result)
                speak(result)
#=========== WEATHER =================================
            elif 'what is the weather' in query:
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":  

                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy =y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print("The Temperature is " +
                                    str(current_temperature) + "kelvin" +
                          "\n atmospheric pressure is " +
                                    str(current_pressure) + "bar"
                          "\n humidity is " +
                                    str(current_humidiy) + "Percentage" +
                          "\n description " +
                                    str(weather_description))
                    speak("The Temperature is " +
                                    str(current_temperature) + "kelvin" +
                          "\n atmospheric pressure is " +
                                    str(current_pressure) + "bar"
                          "\n humidity is " +
                                    str(current_humidiy) + "Percentage" +
                          "\n description " +
                                    str(weather_description))
#=========== SEARCH GOOGLE =================================                    
            elif "search Google" in query:
                speak("what should I search?")
                tbs = takeCommand()
                webbrowser.open("https://www.google.com/search?q="+tbs)

#=========== SHUT DOWN =================================                    
            elif 'shutdown computer' in query:
                speak("are you sure, you want to shutdown?")
                cmd = takeCommand()
                if cmd == 'yes':
                    os.system("shutdown /s /t 12")
                    speak("okay, your system will shut down in 10 seconds")
                else:
                    speak("okay, shutdown cancelled")
                    pass
#=========== RESTART =================================
            elif 'restart computer' in query:
                speak("are you sure, you want to restart?")
                cmd = takeCommand()
                if cmd == 'okay':
                    os.system("shutdown /r /t 12")
                    speak("okay, your system will restart in 10 seconds")
                else:
                    speak("okay, restart cancelled")
                    pass
            
                                 
#=========== THANK YOU =================================                
        elif "thank you friday" in query:
            speak('my pleasure sir. bye. have a great day')
            exit
            break
        else:
            exit


import pyttsx3 
import datetime 
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import pyjokes

wikipedia.set_lang('es')

engine = pyttsx3.init() 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 

# speak("Hola, soy NoahBot! Un asistente de Inteligencia Artificial") 

def time(): 
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("La Hora es: ")
    speak(time) 
 
# time() 

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("El dia de hoy es: ")
    speak(day)
    speak(month)
    speak(year)

# date()

def wishme():
    speak("Bienvenido de vuelta!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Buenos dias! ")
    elif hour >=12 and hour < 18:
        speak("Buenas Tardes! ")
    elif hour >= 18 and hour < 24:
        speak("Buenas noches! ")
    else:
        speak("Buenas tardes, tardes, noches!")

    speak("AndreiitaAmocitoBello a tu servicio, ¿Como puedo ayudarte?")

# wishme()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Te escucho!..")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=3)
        
    try:
        print("Identificando...")
        query = r.recognize_google(audio, language='es-ES')
        print(query)
        
    except Exception as e:
        print(e)    
        speak("Dilo denuevo porfavor...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aaeb15@gmail.com', 'crushariana4321')
    server.sendmail('aaeb15@gmail.com', to, content)
    server.close()

def screenshot():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"C:\\Users\\User\\Desktop\\ImgNoahBot\\Screenshot_{timestamp}.png"
    img = pyautogui.screenshot()
    img.save(filename)

def jokes():
    joke = pyjokes.get_joke(language='es')
    speak(joke)  

if __name__ == "__main__":  
    wishme()
    while True:
        query = takeCommand().lower()
        if 'hora' in query:
            time()

        elif 'qué día es' in query:
            date()

        elif 'wikipedia' in query or 'busca en wikipedia' in query or 'investiga en wikipedia' in query:
            speak("Buscando...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'enviar correo' in query:
            try:
                speak("Que deberia decir?")
                content = takeCommand()
                to = 'aaeb15@gmail.com'
                sendEmail(to,content)
                speak("Email enviado!")
            except Exception as e:
                print(e)
                speak("No se ha podido enviar el email.")   

        elif 'buscador en google chrome' in query or 'abre el buscador de google chrome' in query or 'investiga en google chrome' in query:
            speak("¿Qué debo buscar?")
            chromepath = "C:/Archivos de programa/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get(chromepath).open_new_tab(url)

        #elif 'abre la siguiente página' in query or 'abre una nueva ventana en el navegador' in query:
            # speak("¿Qué pagina deseas abrir?")
            # chromepath = "C:/Archivos de programa/Google/Chrome/Application/chrome.exe %s"
            # search = takeCommand().lower()
            # wb.get(chromepath).open_new_tab(search + ".com")
        
        elif 'cierra mi sesión' in query:
            os.system("shutdown -1")

        elif 'apaga la compuadora' in query:
            os.system("shutdown /s /t 1")

        elif "reinicia la computadora" in query:
            os.system("shutdown /r /t 1")
        
        elif "quiero escribir un recordatorio" in query or 'quiero un recordatorio' in query or "anota un recordotorio" in query or "te dire un recordatorio" in query or "escribe en los recordatorios de" in query:
            speak("Que recordatorio quieres guardar?")
            data = takeCommand()
            speak("Me dijiste que te recuerde de" + data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()

        elif 'sabes sobre' in query or "dime los recordatorios" in query or "mencioname los recordatorios" in query:
            remember = open('data.txt', 'r')
            speak("Dijiste que te recuerde sobre" + remember.read())

        elif 'captura de pantalla' in query or 'screenshot' in query:
            screenshot()
            speak("Listo, captura tomada!")

        elif 'dime un chiste' in query or 'cuéntame un chiste' in query or 'chiste' in query or 'dame un chiste' in query: 
            jokes()     

        elif 'hasta luego noahbot' in query or 'apágate' in query or 'off' in query or 'Buenas noches NoahBot' in query or 'Gracias por tu servicio Noahbot' in query:
            speak("Apagando, Noahbot se despide!")
            quit()


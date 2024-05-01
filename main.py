import datetime
import webbrowser
import openai
import os
import speech_recognition as sr
import pyttsx3

chatkrlo = ""
def chat(adesh):
    global chatkrlo
    print(chatkrlo)
    openai.api_key = yaha apni api key daalna
    chatkrlo += f"Vivek : {adesh}\n Friday:"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Vivek : {adesh}\n Friday:",
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatkrlo += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

    except Exception as e:
        print(f"An error occurred: {str(e)}")
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ***\n\n"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("task"):
            os.mkdir("task")

        with open(f"task/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def say(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            say("Sorry, I didn't catch that. Could you please repeat?")
            return ""

if __name__ == '__main__':
    print('PyCharm')
    say("Friday A I")
    while True:
        print("listening.....")

        adesh = takecommand()
        if not adesh:
            #say("Sorry, I didn't catch that. Could you please repeat?")
            continue
        if "bye".lower() in adesh:
            say("good bye!!")
            break

        if "open" in adesh:
            website_name = adesh.replace("open", "").strip()  # Extract the website name from the command
            website_url = f"https://www.{website_name}.com"

            say(f"Opening {website_name}... sir")
            webbrowser.open(website_url)
        if "time" in adesh:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"sir the time is{minute}  {hour} bajjakke minute")
        if "open calculator" in adesh.lower():
            os.system('start calc')
        if "Using artificial intelligence".lower() in adesh.lower():
            ai(adesh)
        else:
            chat(adesh)
        #say(adesh)

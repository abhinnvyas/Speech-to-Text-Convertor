from playsound import playsound
import speech_recognition as sr
import tkinter as tk
from tkinter import ttk

recognizer = sr.Recognizer()

class speechToTextConvertor(object):
    def __init__(self) -> None:
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Speech to Text Convertor")
        self.root.geometry("530x300")
        self.root.configure(background="white")
        self.root.resizable(False,False)
        self.text = ""

    def main_frame(self):
        def speech_to_text():
            status.configure(text="Listening...")
            status.update()
            with sr.Microphone() as source:
                playsound("Beep Short .mp3")
                recognizer.adjust_for_ambient_noise(source,duration=1)
                recorder_audio = recognizer.listen(source,timeout=5)
                status.configure(text="Listened...")
                status.update()
            try:
                status.configure(text="Translating")
                status.update()
                lang = language.get()
                lang = lang.split("--")[1]
                self.text = recognizer.recognize_google(recorder_audio,language=lang)
                entry.insert(tk.END,f" {self.text}")
            except Exception as e:
                print(e)
            else:
                status.configure(text="")
                status.update()

        tk.Label(self.root,text="Language :",bg="white").place(x=20,y=10)
        status = tk.Label(self.root,text="",background="white")
        status.place(x=30,y=220)

        language = tk.StringVar()
        comboBox = ttk.Combobox(self.root,textvariable=language,width=40,height=40)
        comboBox["values"] = ('English--en-US',"Hindi--hi")
        comboBox.place(x=90,y=10)
        comboBox.current(0)

        translate = tk.Button(self.root,bg="lightblue",text="Translate",width=20,relief=tk.RIDGE,command=speech_to_text)
        translate.place(x=356,y=7)
        
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.place(x=473,y=54,height=165)
        entry = tk.Text(self.root,height=10, width=55,relief=tk.SUNKEN,bg="lightgrey")
        entry.place(x=30,y=55)
        entry.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=entry.yview)

        exit = tk.Button(self.root,text="EXIT",relief=tk.RIDGE,command=self.root.destroy)
        exit.place(x=400,y=250,width=100)
        
    def main(self):
        self.main_frame()
        self.root.mainloop()

if __name__ == "__main__":
    speechToTextConvertor().main()


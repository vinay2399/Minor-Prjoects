import cv2
import pyautogui
import speech_recognition as sr
r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        #print('listening....')
        audio=r.listen(source)
        #print('fetching string....')
        words=r.recognize_google(audio)
        #print(words)
pyautogui.typewrite(words)
cv2.waitKey(0)

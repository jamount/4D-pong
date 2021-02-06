import webbrowser
import time
import random

while True:
    
    webbrowser.open('https://zombo.com/zombo_words.mp3')
    time.sleep(0.4)
    webbrowser.open('https://zombo.com')  
    seconds = random.randrange(4, 10)
    time.sleep(seconds)
                          

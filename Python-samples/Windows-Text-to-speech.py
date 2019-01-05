import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def shout(*args) :
	for item in args :
		print(item)
		speaker.Speak(item)
    
 shout("Hello World!")

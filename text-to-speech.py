import pyttsx3

# Awaz set karna
engine = pyttsx3.init()
engine.setProperty('rate', 150) # bolne ki speed

text = input("Kya bulwana hai likho: ")

print("Ab suno...")
engine.say(text)
engine.runAndWait()
print("Ho gaya!")
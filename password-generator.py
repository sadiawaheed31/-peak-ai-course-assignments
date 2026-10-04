import random
import string

print("--- Strong Password Generator ---")
length = int(input("Password kitne letters ka chahiye? (jaise 12): "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
all_chars = letters + numbers + symbols

password = "".join(random.choice(all_chars) for i in range(length))

print("\nAapka mazboot password hai:", password)
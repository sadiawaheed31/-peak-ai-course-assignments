import qrcode

# Jis cheez ka QR banana hai
data = input("Link ya text likho jiska QR banana hai: ")

# QR bana rahe hain
img = qrcode.make(data)

# Save kar rahe hain
img.save("mera_qr.png")

print("Ho gaya! Folder me mera_qr.png ke naam se save ho gaya hai.")
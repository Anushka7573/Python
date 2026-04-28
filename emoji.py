# convert text-based emotions into emojis

# Emoji converter - Basic version (No if, no loop)

msg = input("Enter your message :")

msg = msg.replace(":)","simle")
msg = msg.replace(":(","sad")
msg = msg.replace(":D","sorry")
msg = msg.replace("; )","love")

print(msg)
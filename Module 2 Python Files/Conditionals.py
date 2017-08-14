dscp=input("Enter the DSCP value: ")
if dscp=="46":
    print("This is a voice media packet.")
elif dscp=="24":
    print("This is a voice signaling packet.")
else:
    print("This is not a voice packet.")


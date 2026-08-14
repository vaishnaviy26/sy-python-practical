feedback=(input("Enter your feedback:"))
print("feedback format report".upper().center(70))

print("--------------------------------------------------------")
print("original feedback".title())
print("---------------------------")

print("feedback summary".title())
print("total character count:".title(),(len(feedback.split())))
print("total word count:".title(),len(feedback))
print("total space count:".title(),feedback.count(" "))
print("total exlamation:".title(),feedback.count("!"))

print("***********************************************")

print("formated feedback".lstrip())

print("uppercase feedback:",feedback.title().upper())
print("loercase feedback:",feedback.lower())
print("title feedback:",feedback.title())
print("capitalize feedback:",feedback.capitalize())
print("swapcas feedback:",feedback.swapcase())

print("================================================")

print("professional feedback".title().capitalize())
print("word list:",feedback.split())

print("thank you for your valuable feedback".center(70).upper())




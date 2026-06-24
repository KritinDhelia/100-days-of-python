year = int(input("What's your year of birth?"))

if 1980 < year and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
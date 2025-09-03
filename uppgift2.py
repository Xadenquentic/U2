age = float(input("What is your age?: "))
age_in_weeks = age * 52

print("din ålder är", age_in_weeks, "veckor gammal")

height_m = float(input("Hur lång är du i meter?: "))
print("tack! din längd är", height_m, "meter lång")

weight_kg = float(input("hur mycket väger du?: "))
print("tack! du väger", weight_kg, "kg")


bmi_kg = weight_kg / (height_m ** 2)


weight_lbs = weight_kg * 2.20462
height_in = height_m * 39.3701


bmi_lbs = (weight_lbs / (height_in ** 2)) * 703

lbs1 = input("Vill du ha din vikt i LBS?: ja, eller nej: ")

if lbs1.lower() in ["ja", "yes", "yah", "yeh"]:
    print("din vikt är", round(weight_lbs, 2), "pounds")
    print("Här är ditt BMI i lbs/inches akhi:", round(bmi_lbs, 2), "tack för du använde våran tjänst akhi")

    
    if bmi_lbs < 18.5:
        print("bram käka mer💀🙏")
    elif 18.5 <= bmi_lbs < 25:
        print("du är medelviktig!: ")
    elif 25.0 <= bmi_lbs < 30:
        print("Du är en tjockis!: ")
    else:
        print("du är OBESE asså colossal!: ")

elif lbs1.lower() in ["nej", "no", "nah", "neh", "naj"]:
    print("okej akhi du gillar kg!")
    print("Här är ditt BMI (kg/m²):", round(bmi_kg, 2), "Tack för att du använde min service akhi")

    
    if bmi_kg < 18.5:
        print("bram käka mer💀🙏")
    elif 18.5 <= bmi_kg < 25:
        print("du är medelviktig!: ")
    elif 25.0 <= bmi_kg < 30:
        print("Du är en tjockis!: ")
    else:
        print("du är OBESE asså colossal!: ")

print("Här är din BMI (Kg):", round(bmi_kg, 2), "Tack för du använder våran service!")
# matthewmatics :D
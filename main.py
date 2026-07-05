while True:
 print("Convert System")
 print("pick a number")
 print("1- Kilometers -> Miles")
 print("2- Celsius -> Fahrenheit")
 print("3- Kilograms -> Pounds")
 print("4- Meters -> Feet")
 print("5- Liters -> Gallons (US)")
 print("6- Exit")
 number = input()


 if number=="6":
    print("Exit")
    break
 elif number=="1":
    print("Enter value in km to convert")
    Kilo=float(input())
    miles = Kilo * 0.621371
    print(miles)
 elif number=="2":
    print("Enter value in C to convert")
    C=float(input())
    F = (C * 9 / 5) + 32
    print(F)
 elif number=="3":
    print("Enter value in kg to convert")
    kg = float(input())
    lbs = kg * 2.20462
    print(lbs)
 elif number=="4":
    print("Enter value in meters to convert")
    meters= float(input())
    feet = meters * 3.28084
    print(feet)
 elif number=="5":
    print("Enter value in Liters to convert")
    Liters = float(input())
    gallons = Liters * 0.264172
    print(gallons)
 else:
    print("chose from 1-6 ")


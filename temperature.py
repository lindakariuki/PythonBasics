#Use of a controlstatement to determine whether it is too cold or too hot in a room.

temperature = float(input("Enter the current temperature in Celcius:"))

if temperature >= 25.0:
    print("It is too hot!")

elif temperature < 25:
    print("It is too cold!")

else:
    print("Normal temperature!")
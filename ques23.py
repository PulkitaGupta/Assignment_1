def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9


choice = input("Enter '1' to convert Celsius to Fahrenheit, '2' to convert Fahrenheit to Celsius: ")
temp = float(input("Enter temperature to be converted: "))
if choice == '1':
    print(f"{temp} Celsius is equal to {celsius_to_fahrenheit(temp)} Fahrenheit.")
elif choice == '2':
    print(f"{temp} Fahrenheit is equal to {fahrenheit_to_celsius(temp)} Celsius.")
else:
    print("Invalid choice.")

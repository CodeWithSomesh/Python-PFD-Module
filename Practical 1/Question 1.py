# def areaTriangle(base, height):
#     return 0.5 * base * height
#
# def main():
#     base = int(input("Enter base: "))
#     height = int(input("Enter height: "))
#     area = areaTriangle(base, height)
#     print(f'Triangle Area: {area}')
#
#
# if __name__ == "__main__":
#     main()


def convertToFahrenheit(temp):
    return (temp * 1.8) + 32


def main():
    temp = int(input("Temperature in Degree Celcius: "))
    convertedValue = convertToFahrenheit(temp)
    print(f"Temperature in Fahrenheit is {convertedValue}")


if __name__ == "__main__":
    main()

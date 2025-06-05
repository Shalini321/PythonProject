# Problem Statement:
# Given the birthdate and name of the person, you want to create a Python program to determine 
# the corresponding Zodiac sign based on the date.

# Question:
# How can you write a Python program that takes name and birthdate as input and outputs the 
# corresponding Zodiac sign and store it in a file using Pandas?

#----------------------------------------------------------------------------------------------
# Aries: March 21 – April 19
# Taurus: April 20 – May 20
# Gemini: May 21 – June 20
# Cancer: June 21 – July 22
# Leo: July 23 – August 22
# Virgo: August 23 – September 22
# Libra: September 23 – October 22
# Scorpio: October 23 – November 21
# Sagittarius: November 22 – December 21
# Capricorn: December 22 – January 19
# Aquarius: January 20 – February 18
# Pisces: February 19 – March 20
#----------------------------------------------------------------------------------------------
import pandas as pd
from datetime import datetime

# Function to determine zodiac sign
def findZodiacSign(month, day):
    zodiacMonthDates = [
        ((1, 20), (2, 18), "Aquarius"),
        ((2, 19), (3, 20), "Pisces"),
        ((3, 21), (4, 19), "Aries"),
        ((4, 20), (5, 20), "Taurus"),
        ((5, 21), (6, 20), "Gemini"),
        ((6, 21), (7, 22), "Cancer"),
        ((7, 23), (8, 22), "Leo"),
        ((8, 23), (9, 22), "Virgo"),
        ((9, 23), (10, 22), "Libra"),
        ((10, 23), (11, 21), "Scorpio"),
        ((11, 22), (12, 21), "Sagittarius"),
        ((12, 22), (1, 19), "Capricorn")
    ]

    for firstMonthDay, secondMonthDay, zodiacSign in zodiacMonthDates:
        if (month == firstMonthDay[0] and day >= firstMonthDay[1]) or (month == secondMonthDay[0] and day <= secondMonthDay[1]):
            return zodiacSign
    return "Unknown"

try :

    # Input from user
    name = input("Enter your name: ")
    dateOfBirth = input("Enter your Date of Birth (YYYY/MM/DD): ")

    # Convert to datetime
    birthdate = datetime.strptime(dateOfBirth, "%Y/%m/%d")
    zodiacSign = findZodiacSign(birthdate.month, birthdate.day)

    # Create a DataFrame
    data = {
        "Name": [name],
        "DateOfBirth": [dateOfBirth],
        "Zodiac Sign": [zodiacSign]
    }

    df = pd.DataFrame(data)

    # Save to CSV
    fileName = "ZodiacData.csv"
    df.to_csv(fileName, index=False)

    print(f"\n{name}, your Zodiac sign is {zodiacSign}.")
    print(f"Data saved to {fileName}")

except ValueError as err:
    print("Not Valid Data", err)

#------------------------- End of the Program -------------------------------------------
# Filename: TimeDiff.py
# Created by: Brady Collier
# Date created: 01/13/19
# Description: Given two times in military format, find the difference between the two.

# Main Function


def timeDiff():
    # Prompts user to input two military times
    f_time = int(input("Please enter the first time in 4 digit military format (e.g., 1330): "))
    s_time = int(input("Please enter the second time in 4 digit military format (e.g., 1330): "))

    # Calculates the difference
    diff = (s_time - f_time)

    # Separates the difference into hours and minutes
    hour = (diff // 100)
    minute = (diff % 100)

    # Runs all conditions
    # If the difference is negative, it converts it back to positive
    # Note: I was unable to make this 100% successful.
    if diff < 0 and minute > 60:
        hour = ((hour * -1) - 1)
        minute = (minute + 60) % 100
        print("The time difference is ", hour, " hour(s) and ", minute, " minute(s).")

    elif diff < 0 and minute < 60:
        hour = ((hour * -1) - 1)
        minute = (minute * -1) % 100
        print("The time difference is ", hour, " hour(s) and ", minute, " minute(s).")

    # If the minute part is greater than 60 it will add 60 to make it into the proper minutes
    elif diff > 0 and minute > 60:
        minute = (minute + 60) % 100
        print("The time difference is ", hour, " hour(s) and ", minute, " minute(s).")
    else:
        print("The time difference is ", hour, " hour(s) and ", minute, " minute(s).")

# Runs function
timeDiff()
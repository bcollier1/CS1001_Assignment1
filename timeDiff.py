# Filename: TimeDiff.py
# Created by: Brady Collier
# Date created: 01/13/19

def timeDiff():
    f_time = int(input("Please enter the first time in 4 digit military format (e.g., 1330): "))
    s_time = int(input("Please enter the second time in 4 digit military format (e.g., 1330): "))

    diff = (s_time - f_time)

    print("The time difference is ", (diff // 100), "hour(s) and ", ((diff + 60) % 100), "minute(s)")


timeDiff()
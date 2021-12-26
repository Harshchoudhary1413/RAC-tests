import calendar
input_date = input().split() #using the split function we splited the input into date month year (eg. 01 01 2021)
M = int(input_date[0])
D = int(input_date[1])
Y = int(input_date[2])
D = calendar.weekday(Y, M, D)

if D == 0:
    print("MONDAY")
elif D == 1:
    print("TUESDAY")
elif D == 2:
    print("WEDNESDAY")
elif D ==3:
    print("THURSDAY")
elif D ==4:
    print("FRIDAY")
elif D == 5:
    print("SATURDAY")
elif D ==6:
    print("SUNDAY")

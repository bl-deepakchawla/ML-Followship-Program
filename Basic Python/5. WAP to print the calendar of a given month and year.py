import calendar as cal


def display_calender():
    cale_value = input("Enter year and month value which you want to see the calender (month/year): ")
    cale_value = cale_value.split('/')
    print(cal.month((int(cale_value[1])), (int(cale_value[0]))))


display_calender()
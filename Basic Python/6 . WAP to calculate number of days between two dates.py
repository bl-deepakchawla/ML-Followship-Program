from datetime import date


def days_btw_two_dates():
    temp_start_date = input("Enter starting date(year/month/day): ")
    temp_end_date = input("Enter ending date(year/month/day): ")
    start_date = temp_start_date.split('/')
    end_date = temp_end_date.split('/')
    total_days = (date(int(start_date[0]),int(start_date[1]),int(start_date[-1])) - date(int(end_date[0]),int(end_date[1]),int(end_date[-1]))).days
    print("Total no. of days between ", temp_start_date, " and ", temp_end_date, " is ", total_days)


days_btw_two_dates()



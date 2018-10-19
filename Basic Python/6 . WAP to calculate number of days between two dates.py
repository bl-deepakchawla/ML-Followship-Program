from datetime import date


def days_btw_two_dates(start_date, end_date):
    total_days = (date(int(start_date[0]),int(start_date[1]),int(start_date[-1])) - date(int(end_date[0]),int(end_date[1]),int(end_date[-1]))).days
    print("Total no. of days between ", start_date, " and ", end_date, " is ", total_days)


start_date = (2014, 7, 11)
end_date = (2014, 7, 2)
days_btw_two_dates(start_date, end_date)



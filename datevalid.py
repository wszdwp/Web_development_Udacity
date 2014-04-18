#datevalid.py

months = [  'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']
month_abbvs = dict((m[:3].lower(), m) for m in months)

"""
def valid_month(month):
        if month.capitalize() in months:
            return month.capitalize()
"""

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        if short_month in month_abbvs:
            #cap_month = month.capitalize()
            return month_abbvs.get(short_month)

def valid_year(year):
        if year and year.isdigit():
            year = int(year)
            if year >= 1900 and year <= 2020:
                return year

def valid_day(day):
        if day and day.isdigit():
            day = int(day)
            if day >= 1 and day <= 31:
                return day

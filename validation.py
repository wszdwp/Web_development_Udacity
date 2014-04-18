

def valid_day(day):
    if day and day.isdigit():
        dayInt = int(day)
        if dayInt <= 31 and dayInt >= 1:
            return dayInt

def valid_year(year):
    if year and year.isdigit():
        yearInt = int(year)
        if yearInt <= 2020 and dayInt >= 1900:
            return yearInt

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

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        #cap_month = month.capitalize()
        #if short_month in months:
        return month_abbvs.get(short_month)


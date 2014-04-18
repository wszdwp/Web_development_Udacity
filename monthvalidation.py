#!/usr/bin/python
#FileName: monthvalidation.py


months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "Septemper",
          "October",
          "November",
          "December"
          ]
month_abbvs = dict((m[:3}.lower(), m) for m in months)

def valid_month(month):
    for month in months:
        return month.Capitalize()
    return "None"

def valid_month2(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

#print valid_month("January")
#print valid_month("Tom")
# End of monthvalidation.py

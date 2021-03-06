import webapp2

form="""
<form method="post">
What is your birthday?


<label> Month
<input type="text" name="month">
</label>

<label> Day
<input type="text" name="day">
</label>

<label> Year
<input type="text" name="year">
</label>

<br>
<br>
<input type ="submit">
</form>
"""

months = ['January',
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

class MainPage(webapp2.RequestHandler):

    def valid_month(self,month):
        if month.capitalize() in months:
            return month.capitalize()

    def valid_year(self,year):
        if year and year.isdigit():
            year = int(year)
            if year > 1900 and year < 2020:
                return year

    def valid_day(self,day):
        if day and day.isdigit():
            day = int(day)
            if day >= 1 and day <= 31:
                return int(day)

    def get(self):
       # self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)

    def post(self):
        self.response.out.write(self.request)
        """
        user_month = self.valid_month(self.request.get('month'))
        user_day = self.valid_day(self.request.get('day'))
        user_year = self.valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a valid birthday!")
        """

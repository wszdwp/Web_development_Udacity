import webapp2

form="""
<form method="post">
    What is your birthday?
    <br> 
    <label>Month <input type="text" name="month"></label>
    <label>Day <input type="text" name="day"></label>
    <label>Year <input type="text" name="year"></label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type ="submit">
</form>
"""

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

#month_abbvs = dict((m[:3].lower(), m) for m in months)
    
class MainPage(webapp2.RequestHandler):

    def valid_month(self,month):
        if month.capitalize() in months:
            return month.capitalize()
 
    def valid_year(self,year):
        if year and year.isdigit():
            year = int(year)
            if year >= 1900 and year <= 2020:
                return year

    def valid_day(self,day):
        if day and day.isdigit():
            day = int(day)
            if day >= 1 and day <= 31:
                return day
            
    def write_form(self, error=""):
        self.response.out.write(form % {"error": error})
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        #self.response.out.write(self.request)
       
        user_month = self.valid_month(self.request.get('month'))
        user_day = self.valid_day(self.request.get('day'))
        user_year = self.valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.write_form("not valid message")
        else:
            self.response.out.write("Thanks! That's a valid birthday!")

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)


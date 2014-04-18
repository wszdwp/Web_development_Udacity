import webapp2
import cgi
import datevalid

form="""
<form method="post">
    What is your birthday?<br>
    <br> 
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type = "checkbox" name="q" value="1">
    <label>
    Password
    <input type="password" name="pw">
    </label>
    <br>
    <select name="r">
        <option>one</option>
        <option>two</option>
        <option>three</option>
    </select>
    <br>
    <input type ="submit">
</form>
"""


    
class MainPage(webapp2.RequestHandler):
    
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": cgi.escape(month, quote=True),
                                        "day": cgi.escape(day, quote=True),
                                        "year": cgi.escape(year, quote=True)})
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()
        #redirect

    def post(self):
        #self.response.out.write(self.request)
        #get the date input
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        #date validation
        month = datevalid.valid_month(user_month)
        day = datevalid.valid_day(user_day)
        year = datevalid.valid_year(user_year)

        #render the response
        if not (month and day and year):
            self.write_form("not valid message",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        #self.write_form()
        #self.response.out.write(user_year)
        self.response.out.write("Thanks! That's a valid date!")
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThanksHandler)],
                              debug=True)


import webapp2
import validation

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>Month
        <input type="text" name="month">
    </label>

    <label>Day
        <input type="text" name="day">
    </label>

    <label>Year
        <input type="text" name="year">
    </label>
    <br>
    <input type="submit">
</form>
"""



class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, This is my google app engine python World!')
        self.response.out.write(form)

    def post(self):
        user_month = validation.valid_month(self.request.get('month'))
        user_day = validation.valid_day(self.request.get('day'))
        user_year = validation.valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Valid")


"""
class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)
"""       
app = webapp2.WSGIApplication([('/', MainPage)],
                               #('/testform', TestHandler)],
                              debug=True)


#ROT13 czas cyptho
#textarea

import webapp2
import cgi
import cypher

form="""
<form method="post">
    <h2>Enter some text to ROT13:<h2>
    <textarea name="text" style="height: 100px; width: 400px; ">%(text)s</textarea>
    <br>
    <input type ="submit">
</form>
"""

    
class MainPage(webapp2.RequestHandler):
    
    def write_form(self, text=""):
        self.response.out.write(form % {"text": cgi.escape(text, quote=True),
                                        })
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        #self.response.out.write(self.request)
        #get the text input
        user_text = self.request.get('text')
        #text validation
        user_text = cgi.escape(user_text, quote=True)
        #textreplace
        user_text = cypher.cazer(user_text)
        #text = datevalid.valid_month(user_text)
        self.response.out.write(form % {"text": user_text})
        #self.response.out.write(form % {"text": cgi.escape(user_text, quote=True),})

        #render the response

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)


    
    

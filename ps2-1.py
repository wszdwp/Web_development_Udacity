import webapp2
import cgi
import string

page="""
<!DOCTYPE html>

<html>
    <head>
        <title>Unit 2 Rot 13</title>
    </head>

    <body>
        <h2>Enter some text to ROT13:</h2>
       <form method="post">
        <textarea name="text"
                  style="height: 100px; width:400px;">%(text)s</textarea>
        <br>
        <input type="submit">
        </form>
    </body>
</html>
"""
def valid_text(s):
return cgi.escape(s, quote = True)

def rot13(s=""):
    rot13_s = ""
    for c in s:
        ord_c = ord(c)
        if 65 <= ord_c <= 90:
            ord_c = (ord_c - 65 + 13) % 26 + 65
        elif 97 <= ord_c <= 122:
            ord_c = (ord_c - 97 + 13) % 26 + 97
        rot13_s += unichr(ord_c)        
    return rot13_s

class MainHandler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(page %{"text":valid_text(text)})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        text = valid_text(user_text)        
        text = rot13(self.request.get('text')       
        self.write_form(text)

app = webapp2.WSGIApplication([
('/', MainHandler),
], debug=True)
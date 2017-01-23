import webapp2
import random

def getRandomFortune():
    #list of fortunes
    fortunes = ["I see much code in your future", 
    "Cookies are for data, not for eating", 
    "Diet cookies are not cookies at all", 
    "A nugget will do, as a nugget does", 
    "This is not the fortune you are looking for"]
    #select a random fortune
    index = random.randint(0, 4)
    return fortunes[index]
    

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = getRandomFortune()
        fortune_scentence = "Your fortune: " + "<strong>" + fortune + "</strong>"
        fortune_paragraph = "<p>" + fortune_scentence + "</p>"

        lucky_number = random.randint(1,100)
        number_scentence = "Your lucky number is: "+ "<strong>" + str(lucky_number) + "</strong>"
        number_paragraph = "<p>" + number_scentence + "</p>"

        cookie_again_button = "<a href='.'><button>Try Again?</button></a>"

        content = header + number_paragraph + fortune_paragraph + cookie_again_button
        self.response.write(content)

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

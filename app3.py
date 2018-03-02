from flask import Flask, request, session, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import random


# The session object makes use of a secret key.
SECRET_KEY = 567198
app = Flask(__name__)
app.config.from_object(__name__)
account_sid = "..."
auth_token = "..."
client = Client(account_sid, auth_token)
# Try adding your own number to this list!

scoreval = {
    "+15512329533": 0,
    "+12016476485": 0,

}
numbers = ["+15512329533", "+12016476485"]
global t 
t = random.randint(0,7)
print(t)
List_of_excerpts = ["The panel will be at Ballroom B.", "Meeting has been changed to 9:45 AM", "Address is 6121 Winsome Apt 7B.", "Joanna isn’t here yet and not answering her phone. What’s up?", "The quick brown fox jumps over the lazy dog.", "How was your day?", "Do you know the muffin man?", "I can't believe it's not butter!"]
@app.route("/sms", methods=['GET', 'POST'])
def hello():
    def first():
        print(t)
        
        for y in numbers:
            message = client.messages.create(
        to = y,
        body=List_of_excerpts[t],
        from_="+12016895776",
        
        )
            print(message)
    def win():
        z = ""
        if compare() == "False":
            z = ""
            message = client.messages.create(
            to = request.values.get('From'),
            body= "Keep trying!",
            from_="+12016895776",
            
            )
            print(message)
        if compare() == "True":
            z = request.values.get('From')
            update(z)
            
            for y in numbers:
                message = client.messages.create(
            to = y,
            body= scores(),
            from_="+12016895776",
            
            )
                print(message)
            if scorecheck() == False:
                global t
                t = random.randint(0,7)
                return first()
            if scorecheck() == True:
                for y in numbers:
                    message = client.messages.create(
                    to = y,
                    body= "Game Over!" + scorecheck_helper(numbers) + " wins! \n" +"New Game!",
                    from_="+12016895776",
                    
                    )
                    print(message)
                reset()
                t = random.randint(0,7)
                return first()


    def compare():
        if List_of_excerpts[t] == request.values.get('Body'):
            return "True"
        else:
            return "False"

    def update(c):
        scoreval[c] += 1

    def scores():
        s = "Score: "
        def scores_helper(list):
            if len(list) == 1:
                return str(list[0]) + " : " + str(scoreval[list[0]])
            else:
                return str(list[0]) + " : " + str(scoreval[list[0]]) + ", " + scores_helper(list[1:])
        return s + scores_helper(numbers)

    def scorecheck():
        score_limit = 4
        if score_limit in scoreval.values():
            return True
        else:
            return False
        
    def scorecheck_helper(list):
        score_limit = 4
        if scoreval[list[0]] == score_limit:
            return list[0]
        else:
            return scorecheck_helper(list[1:])

    def reset():
        for g in numbers:
            scoreval[g] = 0

    """Respond with the number of text messages sent between two parties."""
    # Increment the counter
    #counter = session.get('counter', 0)
    #counter += 1

    # Save the new counter value in the session
    #session['counter'] = counter
    return win()
    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Friend"

    # Build our reply
    message = '{} has messaged {} times.' \
        .format(name, request.values.get('Body'))

    # Put it in a TwiML response
    resp = MessagingResponse()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    def first():
        
        for y in numbers:
            message = client.messages.create(
        to = y,
        body=List_of_excerpts[t],
        from_="+12016895776",
        
        )
            print(message)
    first()
    app.run(host='0.0.0.0') 
    
import json
from HTMLParser import HTMLParser
import random

from flask import Flask, request, render_template, make_response

from api import wall_list, wall_add, wall_error, wall_clear


app = Flask(__name__)

# The "secret key" is needed for the Flask session machinery. In a real
# application, this should be a unguessable string and should NOT be
# checked into version control. Typically, one stores this as an
# environmental variable outside of the Flask app and gets it with
# os.environ['MY_SECRET_KEY']. For our exercise purposes, though, it's
# fine to have this here.
app.secret_key = 'a4c96d59-57a8-11e4-8b97-80e6500ee2f6'


@app.route("/")
def index():
    """Return index page."""
    return render_template("wall.html")


def _convert_to_JSON(result):
    """Convert result object to a JSON web request."""

    # In order for us to return a response that isn't just HTML, we turn our
    # response dictionary into a string-representation (using json.dumps),
    # then use the flask `make_response` function to create a response object
    # out of this.
    response = make_response(json.dumps(result))

    # We can then set some headers on this response object:

    # Access-Control-Allow-Origin isn't needed for this example, but it's
    # a demonstration of a useful feature: since it should be safe to allow
    # Javascript from websites other than ours to get/post to our API, we
    # explicitly allow this.
    response.headers['Access-Control-Allow-Origin'] = "*"

    # Setting the MIMETYPE to JSON's will explicitly mark this as JSON;
    # this can help some client applications understand what they get back.
    response.mimetype = "application/json"

    return response


@app.route("/api/wall/list")
def list_messages():
    """Return list of wall messages as JSON."""

    result = wall_list()
    return _convert_to_JSON(result)


@app.route("/api/wall/add", methods=['POST'])
def add_message():
    """Add a message and return list of wall messages as JSON."""

    # Get the message from the "m" argument passed in the POST.
    # (to get things from a GET response, we've used request.args.get();
    # this is the equivalent for getting things from a POST response)
    msg = request.form.get('m').strip()

    if msg is None:
        result = wall_error("You did not specify a message to set.")

    elif msg == "":
        result = wall_error("Your message is empty")

    # elif "<" or ">" in msg:
    #     result = wall_error("stop being a dick")

    else:
        result = wall_add(msg)

    return _convert_to_JSON(result)

@app.route("/api/wall/clear")
def clear_wall():
    result = wall_clear()
    print result
    return _convert_to_JSON(result)



affirmations = ["I am the architect of my life; I build its foundation and choose its contents.", 
"Today, I am brimming with energy and overflowing with joy.", 
"My body is healthy; my mind is brilliant; my soul is tranquil.", 
"I am superior to negative thoughts and low actions.", 
"I have been given endless talents which I begin to utilize today.", 
"I forgive those who have harmed me in my past and peacefully detach from them.",
"A river of compassion washes away my anger and replaces it with love.",
"I am guided in my every step by Spirit who leads me towards what I must know and do.",
"(If you're married) My marriage is becoming stronger, deeper, and more stable each day.",
"I possess the qualities needed to be extremely successful.",
"(For business owners) My business is growing, expanding, and thriving.",
"Creative energy surges through me and leads me to new and brilliant ideas.",
"Happiness is a choice. I base my happiness on my own accomplishments and the blessings I've been given.",
"My ability to conquer my challenges is limitless; my potential to succeed is infinite.",
"(For those who are unemployed) I deserve to be employed and paid well for my time, efforts, and ideas. Each day, I am closer to finding the perfect job for me.",
"I am courageous and I stand up for myself.",
"My thoughts are filled with positivity and my life is plentiful with prosperity.",
"Today, I abandon my old habits and take up new, more positive ones.",
"Many people look up to me and recognize my worth; I am admired.",
"I am blessed with an incredible family and wonderful friends.",
"I acknowledge my own self-worth; my confidence is soaring.",
"Everything that is happening now is happening for my ultimate good.",
"I am a powerhouse; I am indestructible.",
"Though these times are difficult, they are only a short phase of life.",
"My future is an ideal projection of what I envision now.",
"My efforts are being supported by the universe; my dreams manifest into reality before my eyes.",
"(For those who are single) The perfect partner for me is coming into my life sooner than I expect.",
"I radiate beauty, charm, and grace.",
"I am conquering my illness; I am defeating it steadily each day.",
"My obstacles are moving out of my way; my path is carved towards greatness.",
"I wake up today with strength in my heart and clarity in my mind.",
"My fears of tomorrow are simply melting away.",
"I am at peace with all that has happened, is happening, and will happen.",
"My nature is Divine; I am a spiritual being.",
"My life is just beginning."]


@app.route("/grab/an/aff")
def get_affirmation():
    return str(random.choice(affirmations))


if __name__ == "__main__":
    app.run(debug=True)
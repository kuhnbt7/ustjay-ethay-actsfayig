import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()

def get_pig_latin_url(txt):

	pig_latin_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
	data = {'input_text':txt}
	result = requests.post(pig_latin_url, data=data)
	return '<a href=' + str(result.url) + '>Click here!</a>'

@app.route('/')
def home():
    new_fact = get_fact()
    pig_latin_url = get_pig_latin_url(new_fact)
    return str('<a>'+pig_latin_url+'</a>')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)


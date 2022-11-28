from flask import Flask, render_template, url_for
from random import sample

app = Flask(__name__)

@app.route('/')
def home():

    msg_list = ['Logic will get you from A to B. Imagination will take you everywhere',
                'There are 10 kinds of people. Those who know binary and those who don\'t',
                'There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.',
                'It\'s not that I\'m so smart, it\'s just that I stay with problems longer',
                'It is pitch dark. You are likely to be eaten by a grue.']
    msg = sample(msg_list,1)[0]

    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run()

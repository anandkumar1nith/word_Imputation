from flask import Flask
from flask import render_template, redirect, url_for,request
from forms import SubmissionForm
from test import fetch_data, locate_missin_word

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

correct_sentence, location = "", ""
vocabulary, bigram_table, trigram_table = fetch_data()

<<<<<<< HEAD
=======

>>>>>>> 0fc5371dcc36188d2b12fac0e9c96821df59fbe3
@app.route('/', methods=['GET', 'POST'])
def index():
	form = SubmissionForm()

	global correct_sentence
	global location
	if form.validate_on_submit():
		sentence = form.sentence.data
		correct_sentence, location = locate_missin_word(sentence, vocabulary, bigram_table, trigram_table)
<<<<<<< HEAD
		correct_sentence = correct_sentence.split(' ')
		return render_template('index.html', form=form, val=True, correct_sentence=correct_sentence, location=location)

	return render_template('index.html', form=form,val=False)
=======
		correct_sentence = [s.split(' ') for s in correct_sentence]
		return render_template('index.html', form=form, val=True, correct_sentence=correct_sentence, location=location)

	return render_template('index.html', form=form, val=False)
>>>>>>> 0fc5371dcc36188d2b12fac0e9c96821df59fbe3


	

if __name__ == '__main__':
	app.run(debug=True)

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/projects/')
def projects():
	return render_template('projects.html')

@app.route('/projects/game/')
def game():
	return render_template('game.html')

@app.route('/projects/kNN/')
def knn():
	return render_template('knn.html')

@app.route('/projects/regression/')
def regression():
	return render_template('regression.html')

@app.route('/projects/ConvNN_MNIST/')
def MNIST_CNN():
	return render_template('ConvNN_MNIST.html')

@app.route('/about/resume/')
def resume():
	return render_template('resume.html')

@app.route('/projects/Disaster_RNN/')
def Disaster_RNN():
	return render_template('Disaster_RNN.html')


if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
  
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
 
    correct_answer = num1 + num2

    return render_template('index.html', n1=num1, n2=num2, real_ans=correct_answer)

@app.route('/check', methods=['POST'])
def check_answer():

    user_guess = int(request.form['guess'])
    real_answer = int(request.form['real_ans'])

    if user_guess == real_answer:
        msg = "Correct! Great Job! 🎉"
        color = "green"
    else:
        msg = f"Oops! The answer was {real_answer}. 😅"
        color = "red"
  
    return render_template('result.html', message=msg, color=color)

if __name__ == '__main__':
    app.run(debug=True)
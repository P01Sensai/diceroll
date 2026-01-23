from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/play/<mode>')
def start_game(mode):

    current_score = request.args.get('score', 0, type=int)

    if mode == 'mix':
        current_op = random.choice(['add', 'sub', 'mul', 'div'])
    else:
        current_op = mode

    if current_op == 'add':
        n1 = random.randint(1, 30)
        n2 = random.randint(1, 20)
        symbol = "+"
        ans = n1 + n2
        
    elif current_op == 'sub':
        n1 = random.randint(10, 30)
        n2 = random.randint(1, 10)
        if n2 > n1: n1, n2 = n2, n1 
        symbol = "-"
        ans = n1 - n2
        
    elif current_op == 'mul':
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        symbol = "×"
        ans = n1 * n2
        
    elif current_op == 'div':
        ans = random.randint(1, 10) 
        n2 = random.randint(2, 10)
        n1 = n2 * ans
        symbol = "÷"

    return render_template('game.html', n1=n1, n2=n2, symbol=symbol, real_ans=ans, mode=mode, score=current_score)

@app.route('/check', methods=['POST'])
def check_answer():

    user_guess = int(request.form['guess'])
    real_answer = int(request.form['real_ans'])
    mode = request.form['mode']
    current_score = int(request.form['current_score']) # Read the hidden score
    
    if user_guess == real_answer:
        new_score = current_score + 1
        msg = "Correct! 🌟"
        color = "green"
        game_over = False
    else:

        new_score = current_score 
        msg = f"Wrong! The answer was {real_answer}. 😅"
        color = "red"
        game_over = True
        
    return render_template('result.html', message=msg, color=color, mode=mode, score=new_score, game_over=game_over)

if __name__ == '__main__':
    app.run(debug=True)
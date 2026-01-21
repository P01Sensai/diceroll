from flask import Flask, render_template
import random

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', dice_value="?")

@app.route('/roll')
def roll_dice():
    result = random.randint(1, 6)
    print(f'Dice rolled: {result}')
    return render_template('index.html', dice_value=result)

if __name__ == '__main__':
    app.run(debug=True)

    
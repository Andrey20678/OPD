from flask import render_template, request
from app import app

def calc(firstval: float, percent: float, count: int): return firstval*((1+percent/100)**count)

@app.route('/')
def index():
    return render_template("index.html", title= "Welcome", ans="") 

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        try:
            num_1 = float(request.form.get('num_1'))
            num_2 = float(request.form.get('num_2'))
            num_3 = int(request.form.get('num_3'))
        except:
            return render_template('index.html', title="Something went Wrong", ans="Ты чёт не то ввёл")
        return render_template('index.html', title="Here is Your Answer", ans=calc(num_1, num_2, num_3))

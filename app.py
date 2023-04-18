from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        return str(a + b)
    return '''
           <form method="post">
               <p>Valor 1: <input type="text" placeholder="Número 1" name="a"></p>
               <p>Valor 2: <input type="text" placeholder="Número 2" name="b"></p>
               <p><input type="submit" value="Somar"></p>
           </form>
           '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

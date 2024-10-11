from flask import Flask, render_template, request, redirect

app = Flask(__name__)

provas = []

@app.route('/')
def index():
    return render_template('index.html', provas=provas)

@app.route('/criar', methods=['POST'])
def criar_prova():
    materia = request.form['materia']
    data = request.form['data']
    assunto = request.form['assunto']
    
    prova = {
        'materia': materia,
        'data': data,
        'assunto': assunto
    }
    
    provas.append(prova)
    
    return redirect('/')

@app.route('/alterar', methods=['POST'])
def alterar_prova():
    old_materia = request.form['old_materia']
    new_materia = request.form['new_materia']
    new_data = request.form.get('new_data')
    new_assunto = request.form.get('new_assunto')
    
    for prova in provas:
        if prova['materia'] == old_materia:
            prova['materia'] = new_materia
            if new_data:
                prova['data'] = new_data
            if new_assunto:
                prova['assunto'] = new_assunto
            break
    
    return redirect('/')

@app.route('/apagar', methods=['POST'])
def apagar_prova():
    materia = request.form['materia']
    
    global provas
    provas = [prova for prova in provas if prova['materia'] != materia]
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

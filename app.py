
from flask import Flask, request, render_template, redirect, url_for
from pony.orm import db_session, select
from models import db, Roupa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@db_session
def index():
    if request.method == 'POST':
        # Recebe os dados do formulário
        nome = request.form.get('nome')
        tamanho = request.form.get('tamanho')
        cor = request.form.get('cor')
        preco = request.form.get('preco')
        genero = request.form.get('genero')
        
        preco = float(preco) if preco else None
        # Adiciona os dados no banco de dados
        Roupa( nome=nome, tamanho=tamanho, cor=cor, preco = preco, genero = genero)
        return redirect(url_for('lista'))
    return render_template('index.html')

@app.route('/lista')
@db_session
def lista():
    roupas = select(r for r in Roupa)[:]
    return render_template('lista.html', roupas=roupas)



@app.route('/excluir/<int:id>', methods=['POST'])
@db_session
def excluir(id):
    roupa = Roupa[id]  # Busca a roupa pelo ID
    
    if roupa:
        roupa.delete()  # Exclui a roupa do banco de dados
        db.commit()     # Persiste a exclusão
        
    return redirect(url_for('lista'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    imc = None
    mensagem = None

    if request.method == 'POST':

        try:

            peso = float(request.form['weight'])
            altura = float(request.form['height'])
            imc = peso / (altura ** 2)

            if imc < 18.5:
                mensagem = 'Atenção! Você está ABAIXO DO PESO NORMAL.'
            elif 18.5 <= imc < 25:
                mensagem = 'Parabéns, você está na faixa do PESO NORMAL.'
            elif 25 <= imc < 30:
                mensagem = 'Atenção! Você está em SOBREPESO.'
            elif 30 <= imc < 40:
                mensagem = 'Alerta! Você está em OBESIDADE.'
            elif imc >= 40:
                mensagem = 'CUIDADO! Você está em OBESIDADE MÓRBIDA.'

        except ValueError:
            mensagem = 'Por favor, insira valores válidos para peso e altura.'

    # Renderizando o template e passando as variáveis 'imc' e 'mensagem'
    return render_template('index.html', imc=imc, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)

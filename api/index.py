from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

@app.route('/historico_clinico')
def historico_clinico():
    return render_template('historico_clinico.html', active_page='historico_clinico')

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html', active_page='configuracoes')

@app.route('/linha_tempo')
def linha_tempo():
    return render_template('linha_tempo.html', active_page='linha_tempo')

@app.route('/paciente/julia')
def paciente_julia():
    return render_template('paciente_julia.html', active_page='paciente')

@app.route('/paciente/mariana')
def paciente_mariana():
    return render_template('paciente_mariana.html', active_page='dashboard') # Mantive dashboard ativo pois veio de lá

@app.route('/paciente/carla')
def paciente_carla():
    return render_template('paciente_carla.html', active_page='dashboard') # Mantive dashboard ativo pois veio de lá

@app.route('/exames/novo')
def novo_exame():
    # Não há item de menu específico para "novo exame", mantemos sem highlight ou dashboard
    return render_template('novo_exame.html', active_page='dashboard')

@app.route('/analise')
def analise():
    return render_template('analise.html', active_page='analise')

@app.route('/decisao')
def decisao():
    return render_template('decisao.html', active_page='decisao')

# Necessário para Vercel
if __name__ == '__main__':
    app.run(debug=True)
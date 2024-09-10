from flask import Flask, redirect, url_for, session, render_template, request
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

# Configuração OAuth para SUAP
oauth.register(
    name='suap',
    client_id="seu-client-id",
    client_secret="seu-client-secret",
    api_base_url='https://suap.ifrn.edu.br/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    fetch_token=lambda: session.get('suap_token')
)

@app.route('/')
def index():
    if 'suap_token' in session:
        meus_dados = oauth.suap.get('v2/minhas-informacoes/meus-dados').json()
        return render_template('user.html', user_data=meus_dados)
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))

@app.route('/boletim', methods=['POST'])
def boletim():
    if 'suap_token' not in session:
        return redirect(url_for('index'))

    ano = request.form.get('ano')
    semestre = request.form.get('semestre')
    
    # Pegar os boletins do SUAP
    boletins = oauth.suap.get(f'v2/minhas-informacoes/boletim/{ano}/{semestre}').json()
    
    meus_dados = oauth.suap.get('v2/minhas-informacoes/meus-dados').json()
    return render_template('user.html', user_data=meus_dados, boletins=boletins, ano=ano, semestre=semestre)

if __name__ == '__main__':
    app.run(debug=True)

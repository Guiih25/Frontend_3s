from flask import Flask, render_template, url_for, flash, redirect, request
from sqlalchemy.exc import SQLAlchemyError

from database import db_session,local_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yuri alberto'

login_manager = LoginManager(app)
login_manager.login_view ='login'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    return db_session.execute(user).scalar_one_or_none()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                if resultado_email.check_password(senha):
                    login_user(resultado_email)
                    flash('Login Sucesso', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Senha incorreta', 'danger')
                    return render_template("login.html")
            else:
                flash('email não encontrado', 'danger')
                return render_template("login.html")
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado Sucesso', 'success')
    return redirect(url_for('login'))

# @app.route('/cadastro', methods=['GET', 'POST'])
# def novo_funcionario():
#     if request.method == 'POST':
#         nome = request.form.get('form-nome')
#         data_nascimento = request.form.get('form-data')
#         cpf = request.form.get('form-cpf')
#         email = request.form.get('form-email')
#         senha = request.form.get('form-senha')
#         cargo = request.form.get('form-cargo')
#         salario = request.form.get('form-salario')
#         if not nome or not data_nascimento or not cpf or not email or not senha or not cargo or not salario:
#             flash('Preencha todos os campos', 'danger')
#             return render_template("cadastro.html")
#         verificar_email = select(Funcionario).where(Funcionario.email == email)
#         resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
#         if resultado_email:
#             flash(f"Email {email} ja existe", "danger")
#             return render_template("cadastro.html")
#         try:
#             novo_usuario = Funcionario(nome=nome, email=email)
#             novo_usuario.set_password(senha)
#             db_session.add(novo_usuario)
#             db_session.commit()
#             flash(f'Usuario {nome} criado com sucesso', 'success')
#             return redirect(url_for('login'))
#         except SQLAlchemyError as e:
#             flash(f'Erro na base de dados', 'danger')
#             print(e)
#             return redirect(url_for('cadastro_usuario'))
#         except Exception as e:
#             flash(f'Erro ao cadastrar usuario', 'danger')
#             print(e)
#             return redirect(url_for('cadastro_usuario'))
#     return render_template("cadastro.html
@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionario')
@login_required
def funcionario():
    func_sql = select(Funcionario)
    resultado = db_session.execute(func_sql).scalars().all()

    return render_template("funcionario.html", resultado=resultado)

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/tabela_cadastro', methods=['GET', 'POST'])  # Adicionado methods
def tabela_cadastro():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = request.form.get('form-data')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = request.form.get('form-salario')

        if not nome or not email or not senha:
            flash('Preencha todos os campos obrigatórios', 'danger')
            return render_template("login.html")

        # Verifica se o e-mail já existe
        verificar_email = select(Funcionario).where(Funcionario.email == email)
        resultado_email = db_session.execute(verificar_email).scalar_one_or_none()

        if resultado_email:
            flash(f"Email {email} já existe", "danger")
            return render_template("login.html")

        try:
            novo_funcionario = Funcionario(
                nome=nome,
                email=email,
                cpf=cpf,
                cargo=cargo,
                salario=salario,
                data_nascimento=data_nascimento
            )

            novo_funcionario.set_password(senha)

            db_session.add(novo_funcionario)
            db_session.commit()  # Aqui é onde o dado realmente vai pro banco

            flash(f'Usuário {nome} criado com sucesso', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            db_session.rollback()  # Boa prática: desfazer caso dê erro
            print(f"Erro detalhado: {e}")
            flash(f'Erro ao cadastrar usuário', 'danger')
            return redirect(url_for('login'))

    # Se for GET, ele apenas exibe a página
    return render_template("login.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash ("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:

            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            sub = n1 - n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, sub=sub)
        else:

            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multi = n1 * n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, multi=multi)
        else:

            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            div = n1 / n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, div=div)
        else:
            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/area_triangulo', methods=['GET', 'POST'])
def area_triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multi = n1 * n2
            area_t = multi / 2
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, area_t=area_t)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")


@app.route('/area_quadrado', methods=['GET', 'POST'])
def area_quadrado():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multi = n1 * n2
            area_q = multi / 2
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, area_q=area_q)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")


@app.route('/area_circulo', methods=['GET', 'POST'])
def area_circulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_c = 3.14 * (n1 * n2)
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, area_c=area_c)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")

@app.route('/area_hexagono' ,methods=['GET', 'POST'])
def area_hexagono():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            area_h = (n1 * n2) / 2 * 6
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, area_h=area_h)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")

@app.route('/perimetro_triangulo', methods=['GET', 'POST'])
def perimetro_triangulo():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3 = int(request.form['form-n3'])
            peri_t = n1 + n2 + n3
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, n2=n2, n3=n3, peri_t=peri_t)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")

@app.route('/perimetro_quadrado' ,methods=['GET', 'POST'])
def perimetro_quadrado():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            peri_q = n1 + n1 + n1 + n1
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, peri_q=peri_q)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")

@app.route('/perimetro_circulo' ,methods=['GET', 'POST'])
def perimetro_circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            peri_c = n1 * 2 * 3.14
            flash("Realizado com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, peri_c=peri_c)
        else:
            flash("O campo esta vazio", 'alert-danger')
    return render_template("geometria.html")



if __name__ == '__main__':
    app.run(debug=True)

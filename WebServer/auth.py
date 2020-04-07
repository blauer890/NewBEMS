from flask import Blueprint, render_template, request

bp = Blueprint('auth',__name__,url_prefix='/auth')

# TODO implement flask login
@bp.route('/register', methods=('GET', 'POST'))
def user_login():
    if request.method == 'POST':
        print(request.form['password'])
        print(request.form['username'])
        return redirect(
    else:
        return render_template('auth.html')
    

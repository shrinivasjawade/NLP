# from flask import Flask 
# app =  Flask(__name__)
# @app.route('/')
# def hello_world():
#     return ("welcome to flask Application")

# @app.route('/hello')
# def hello():
#     return ('Hello World')

# @app.route('/welcome')
# def welcome():
#     return ('this is welcome page')
 

# if __name__  == '__main__':
#     app.run(debug =  True)## when we add debug  = true   then there is no need to rerun the code again ,just save it and refresh the page  and it will replicate update

# ######q3
# from flask import Flask 
# app =  Flask(__name__)
# @app.route('/<name>')
# def hello_world(name):
#     return ('Hello %s '%name)
# if __name__  == '__main__':
#     app.run(debug=True)


# q4 #### direct to page  

# from flask import Flask 
# app =  Flask(__name__)
# @app.route('/<name>')
# def hello_world(name):
#     return ("hello %s" %name)

# @app.route('/')
# def hello():
#     return ('this is Home Page')

# if __name__  == '__main__':
#     app.run(debug=True)



####q5  ###redirecting to main page 
# from flask import Flask ,redirect, url_for
# app =  Flask(__name__)


# @app.route('/admin')
# def hello_admin():
#     return ("helo Admin")

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return ('hello %s as Guest' %guest)

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect (url_for('hello_guest',guest =  name))

# if __name__  == '__main__':
#     app.run(debug=True)


#################################q6 ##http methods 

from flask import Flask ,redirect, url_for
app =  Flask(__name__)


@app.route('/admin')
def hello_admin():
    return ("helo Admin")

@app.route('/guest/<guest>')
def hello_guest(guest):
    return ('hello %s as Guest' %guest)

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect (url_for('hello_guest',guest =  name))

if __name__  == '__main__':
    app.run(debug=True)

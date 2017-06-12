from flask import Flask, render_template, session, request, redirect
app=Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1
    return render_template('index.html', count = session['count'])

@app.route('/plustwo', methods=['POST'])
def addTwo():
    session['count'] = session['count'] + 1
    return redirect('/')
    
@app.route('/reset', methods=['POST'])
def resetcount():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
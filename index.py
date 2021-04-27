from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_url_path='', static_folder='static')

videos = {
    'flutter': {
        'label': 'flutter', 
        'amount': 6
    }, 
    'react': {
        'label': 'react', 
        'amount': 5
    },
    'react_native': {
        'label': 'react native', 
        'amount': 5
    },
    'elixir': {
        'label': 'elixir', 
        'amount': 5
    },
    'node': {
        'label': 'node js', 
        'amount': 5
    }
}

@app.route('/')
def home():    
    return render_template("display.html", videos=videos, title='NLW5', path='/video')    

@app.route('/curso/<name>')
def player(name):    
    title = videos[f'{name}']['label']
    return render_template("player.html", videos=videos, link=f'{name}', title=f'{title}', path='/video')    

if __name__ =='__main__':
    app.run(debug=True, port=5069)
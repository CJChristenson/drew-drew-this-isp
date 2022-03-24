from flask import Flask, render_template, request
import os


template_dir = os.path.abspath('./website/')
app = Flask(__name__, template_folder=template_dir)



@app.route('/')
def home():
      return render_template('index.html')

@app.route('/howcpuswork')
def howcpuswork():
      return render_template('howcpuswork.html')
@app.route('/how8bitwork')
def how8bitwork():
      return render_template('how8bitwork.html')
@app.route('/cpuprogram')
def cpuprogram():
      return render_template('cpuprogram.html')

@app.route('/stream')
def stream():
      return render_template('stream.html')

@app.route('/faq')
def faq():
      return render_template('faq.html')


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=(os.environ.get('VAPOR_LOCAL_PORT')))

from flask import Flask, render_template 
import os


template_dir = os.path.abspath('./website/')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def hello():
      return render_template('home.html')
  


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=(os.environ.get('VAPOR_LOCAL_PORT')))

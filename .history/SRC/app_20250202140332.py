from flask import Flask, render_template
import os  

#acceder a los directorios
Template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) #unir la carpeta principal
Template_dir = os.path.join(Template_dir, 'SRC', 'Templates') #unir las dos carpetas

app = Flask(__name__, template_folder = Template_dir ) #inicializacion de flask


#rutas de la app
@app.route('/')
def home():

    return render_template('index.html')


if __name__ =='__name__':
    app.run(debug=True, port=4000)
    
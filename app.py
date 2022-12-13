from flask import Flask , render_template , Response
from flask import request
from flask_cors import CORS # pip install flask-cors

from camera import *
from uart import *

app = Flask(__name__,static_url_path='/static')
CORS(
    app,
    resources={r"/plant/*": {"origins":"*"}},
    supports_credentials=True
)

@app.route('/plant/test',methods=['GET'])
def hello():
    return 'hello flask'

@app.route('/plant/path',methods=['GET','POST'])
def take_picture():
    result = plant_picture()
    return result

@app.route('/plant/led',methods=['GET'])
def ledc_ontroll():
    is_led = ""
    led_value = request.args.get('val','test')
    if ( str(led_value) == 'true'):
        is_led = "1"
    elif ( str(led_value) == 'false'):
        is_led = "0"
    print(is_led)
    send_string(is_led)
    return led_value

def main():
    app.debug = True
    app.run(host="10.150.150.72", port="5000")
if __name__ == '__main__':
    main()
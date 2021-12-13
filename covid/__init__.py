from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '23a5790e1f41f07432ba8af4552b44fb'

from covid import routes

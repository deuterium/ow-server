import os, socket
from flask import Flask
from flask_restful import Api
from app.objects import CVEProduct, CVEVendor, CVEID

#from app.reversedproxy import ReverseProxied

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

# app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )
app.config['SECRET_KEY'] = 'you-will-never-guess'

api.add_resource(CVEVendor  , '/api/cve/vendor')
api.add_resource(CVEID      , '/api/cve/<string:cve_id>')
api.add_resource(CVEProduct , '/api/cve/product/<string:product_id>')

# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# first run stuff can go here, or launching other jobs
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("SEVER STARTED: http://{}:8888".format(s.getsockname()[0]))
s.close()


from app import routes
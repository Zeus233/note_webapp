from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # 使用SQLite
app.config.from_object('config') # 如果你想使用config.py
app.config['JWT_SECRET_KEY'] = 'key---'  # 替换为你自己的密钥
# cors = CORS(app, resources={r"/*":{"origins": "*"}})
CORS(app,supports_credentials=True)

jwt = JWTManager(app)




db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 导入视图
from views import *

if __name__ == '__main__':
    app.run(debug=True)

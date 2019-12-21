# /run.py
import os

from src.app import create_app


os.environ['FLASK_ENV'] = 'development'
os.environ['DATABASE_URL'] = 'postgres://postgres:passwd@localhost:5432/mydb'
os.environ['JWT_SECRET_KEY'] = 'hhgaghhgsdhdhdd'
os.environ['port'] = '5432'
os.system('env')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    # print(env_name)
    app = create_app(env_name)
    # run app
    app.run()

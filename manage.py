import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from src.app import create_app, db

os.environ['FLASK_ENV'] = 'development'
os.environ['DATABASE_URL'] = 'postgres://postgres:passwd@localhost:5432/mydb'
os.environ['JWT_SECRET_KEY'] = 'hhgaghhgsdhdhdd'
os.environ['port'] = '5432'
# os.system('env')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
# print('env_name:')
env_name = os.getenv('FLASK_ENV')
# print('env_name:', env_name)
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
# print("MigrateCommand: ", MigrateCommand)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

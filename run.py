# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    # run app
    
    # Test part2
    # app.run()

    # part 3
    app.run(host='0.0.0.0', port=port)

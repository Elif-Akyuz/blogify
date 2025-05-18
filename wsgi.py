import sys
import os
from app import app as application

# Path to your virtual environment
virtualenv_path = '/home/elifakyuz/.virtualenvs/myenv'
if virtualenv_path not in sys.path:
    sys.path.insert(0, virtualenv_path)

# Add your project directory to the sys.path
project_home = '/home/elifakyuz/blogify'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate the virtual environment
activate_this = os.path.join(virtualenv_path, 'bin/activate_this.py')
exec(open(activate_this).read(), dict(__file__=activate_this))

if __name__ == "__main__":
    app.run()






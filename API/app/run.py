import sys
import pdb
#pdb.set_trace()
from app import cria_app
app = cria_app(config='settings.py')

#from app import create_app


#app = create_app('config')

print(app.config['HOST'])
print(app.config['PORT'])
print(app.config['DEBUG'])
if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])


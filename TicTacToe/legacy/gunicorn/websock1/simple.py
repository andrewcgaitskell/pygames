from app import app

PORT = 5002;
#ADDRESS = '127.0.0.1'
ADDRESS = '0.0.0.0'

if __name__ == '__main__':
    server.run(app,port=5002,debug=True)

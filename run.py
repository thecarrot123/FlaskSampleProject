from main import app
import sys

if __name__ == '__main__':
    port = '5050'
    if len(sys.argv) == 2 and sys.argv[1].isnumeric():
        port = sys.argv[1]
    app.run(debug=True,port=port)
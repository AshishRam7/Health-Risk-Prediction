#!flask/bin/p
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/members')
def members():

    return {"members":["Member1","Member2","Member3"]}


#@app.route('/calculator/add', methods=['POST'] ,endpoint='add')
#def add():
 #  ans = float(data['a'])+ float(data['b']);
 #   print(ans)
  #  return jsonify({'solution': ans})

if __name__ == "__main__":
    app.run(debug=True)

    


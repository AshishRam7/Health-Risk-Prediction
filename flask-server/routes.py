from flask import Flask, redirect, url_for, request,jsonify
app = Flask(__name__)


lst=[]
@app.route('/success/<name>/<name1>/<name2>/<name3>/<name4>/<name5>')
def success(name,name1,name2,name3,name4,name5):
   lst.append(int(name))
   lst.append(int(name1))
   lst.append(int(name2))
   lst.append(float(name3))
   lst.append(int(name4))
   lst.append(int(name5))
   return lst




@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
      age = request.form['age']
      restingbp = request.form['restingbp']
      maxhr = request.form['maxhr']
      gender = request.form['gender']
      fasting = request.form['fasting']

      exercis = request.form['exereciseangina']

      return redirect(url_for('success',name = age,name1=restingbp,name2=maxhr,name3=gender,name4=fasting,name5=exercis))
    else:
        age = request.args.get('age')
        restingbp = request.args.get('restingbp')
        maxhr = request.args.get('maxhr')
        gender = request.args.get('gender')
        fasting = request.args.get('fasting')
        exercis = request.args.get('exereciseangina')
    return redirect(url_for('success',name = age,name1=restingbp,name2=maxhr,name3=gender,name4=fasting,name5=exercis))


if __name__ == '__main__':
   app.run(debug = True)
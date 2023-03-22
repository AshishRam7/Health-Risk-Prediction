from flask import Flask, redirect, url_for, request,jsonify
app = Flask(__name__)


lst=[]
lst2=[]
@app.route('/success/<name>/<name1>/<name2>/<name3>/<name4>/<name5>/<name6>')
def success(name,name1,name2,name3,name4,name5,name6):
   lst.append(int(name))
   lst.append(int(name1))
   lst.append(int(name2))
   lst.append(float(name3))
   lst.append(int(name4))
   lst.append(int(name5))
   lst2.append(name6)
   return lst2




@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':

      age = request.form['age']
      restingbp = request.form['restingbp']
      maxhr = request.form['maxhr']
      gender = request.form['gender']
      fasting = request.form['fasting']

      exercis = request.form['exereciseangina']
      email1=request.form['email1']

      return redirect(url_for('success',name = age,name1=restingbp,name2=maxhr,name3=gender,name4=fasting,name5=exercis,name6=email1))
    else:
        age = request.args.get('age')
        restingbp = request.args.get('restingbp')
        maxhr = request.args.get('maxhr')
        gender = request.args.get('gender')
        fasting = request.args.get('fasting')
        exercis = request.args.get('exereciseangina')
        email1 = request.args.get('email1')
    return redirect(url_for('success',name = age,name1=restingbp,name2=maxhr,name3=gender,name4=fasting,name5=exercis,name6=email1))


if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("login.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
	if(request.method=="POST"):
		try:
				cname = request.form['cname']
				cpwd = request.form['cpwd']
				cmobile = request.form['cmobile']

				with sql.connect("database.db") as con:
					cur = con.cursor()
					cur.execute ("INSERT INTO customers(cname, cpwd, cnum) VALUES(?,?,?)",(cname, cpwd, cmobile) )

					con.commit()
					msg = "Record successfully added"
		except:
					con.rollback()
					msg = "error in insert operation"

		finally:
					return render_template("submit.html",msg = msg)
					con.close()

@app.route('/success', methods=['POST','GET'])
def success():
	if(request.method=="POST"):
		try:
				cname = request.form['uname']
				cpwd = request.form['upwd']

				with sql.connect("database.db") as con:
					cur = con.cursor()
					cur.execute ("Select * from customers where cname = ? and cpwd = ?",(cname, cpwd))
					row = cur.fetchall()
					if len(row)==1:
						msg = "Login Successful"
		except:
					msg = "User Not Present"

		finally:
					return render_template("success.html",msg = msg)
					con.close()


@app.route('/signup')
def signup():
	return render_template("signup.html")

if __name__ == '__main__':
	app.run()

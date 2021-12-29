from flask import *
from database import *
from flask import session as login_session
import requests
import json
import pyttsx3
import os

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


# you can use the headers to pass in hidden info, here we are sending a secret Key (think of it as a password)
headers = {'Authorization': 'Key d8599b4cc62441b4b418201457af695c'}

api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

engine = pyttsx3.init()


@app.route('/',methods = ['GET','POST'])
def home():
	login_session['admin']=False
	if request.method == 'POST':
		image = request.form['url']
		text = request.form['name']
		if image!=None and text!="":
			data ={"inputs": [
      				{
        			"data": {
          				"image": {
            				"url": image
          						}
        					}
      				}
    		]}
			response = requests.post(api_url, headers=headers, data=json.dumps(data))
			response_dict = json.loads(response.content)
			try:
				output = response_dict["outputs"][0]["data"]["concepts"]
				print(output)
				x=""
				for i in output:
					x +=  i['name'] + ", "
				add_blog(text,image,x)
				engine.say(x)
				engine.runAndWait()
				engine.stop()
			except:
				return redirect(url_for('addImage'))


	return render_template("index.html",blogs=return_all_blogs())

@app.route('/addImages')
def addImage():
	return render_template("addImage.html")

@app.route('/admin',methods=['GET','POST'])
def admin():
	if request.method == 'POST':
		user = request.form['user']
		passw = request.form['pass']
		if user == 'admin' and passw == '123456':
			login_session['admin'] = True
			return redirect(url_for('managment'))
	return render_template("admin.html")

@app.route('/managment')
def managment():
	if login_session['admin']:
		return render_template("managment.html", blogs=return_all_blogs())
	return redirect(url_for('admin'))

@app.route('/delete/<int:blog_id>',methods=['GET','POST'])
def delete_blog(blog_id):
	if login_session['admin']:
		delete_blog1(blog_id)
		return redirect(url_for('managment'))
	return redirect(url_for('admin'))

@app.route('/blog_managment/<int:blog_id>',methods=['GET','POST'])
def blog_managment(blog_id):
	if login_session['admin']:
		if request.method=='POST':
			title = request.form['name']
			image = request.form['url']
			if image!="" and title!="":
				data ={"inputs": [
	      				{
	        			"data": {
	          				"image": {
	            				"url": image
	          						}
	        					}
	      				}
	    		]}
				response = requests.post(api_url, headers=headers, data=json.dumps(data))
				response_dict = json.loads(response.content)
				output = response_dict["outputs"][0]["data"]["concepts"]
				print(output)
				x=""
				for i in output:
					x +=  i['name'] + ", "
				edit_blog(blog_id,title,image,x)
				return redirect(managment)
		return render_template("blog_managment.html",blog=return_blog(blog_id))
	return redirect(url_for('admin'))

@app.route('/logout')
def logout():
	login_session['admin']=False
	return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

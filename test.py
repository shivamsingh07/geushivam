from flask import Flask
import os

app=Flask(_name_)

port=int(os.getenv("PORT"))

@app.route('/')
def hello_world();
	return 'welcome'

if name__='__main__':
	#port=1245
	app.run(host='0.0.0.0',port=port)

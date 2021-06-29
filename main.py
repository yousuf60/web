from flask import Flask ,flash,render_template ,request
app=Flask(__name__)
app.config['SECRET_KEY']=';saj;'
@app.route('/',methods=['GET','POST'])
def main():
	flash('hello and welcome',category='yes')
	if request.method=='POST':
		Any=request.form['ANY']
		print(Any)
		if len(Any)>1000:
			flash('too many',category='no')
		else:
			with open('latest.txt','a')as b:
				b.write('\n-\n')
				b.write(Any+'\n')
				b.write('--')
	with open('latest.txt','r')as s:
		k=s.readlines()
	return render_template('main.html',k=k)
if __name__ =='__main__':
	app.run(debug=True)

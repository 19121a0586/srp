import numpy as np
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('homepage.html')
    return render_template('earthquake.html')
#@app.route('/')
#def earth():
#    return render_template('earthquake.html')

@app.route('/pre',methods=['POST'])
def pre():
    
    val=[float(x) for x in request.form.values()]
    fival=[np.array(val)]
    prediction=model.predict(fival)
    pred=float(prediction)
    return render_template('earthquake.html',prediction_text="predicted value is:{}".format(pred))
    

    
if __name__ == "__main__":
    app.run(debug=True)

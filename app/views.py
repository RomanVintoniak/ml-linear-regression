from flask import render_template, request
from app import app, model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        hoursStudied = int(request.form['hoursStudied'])
        prevScore = int(request.form['prevScore'])
        activities = int(request.form['activities'])
        sleepHours = int(request.form['sleepHours'])
        sampleQuestionPapersPracticed = int(request.form['sampleQuestionPapersPracticed'])
        
        data = [
            hoursStudied, 
            prevScore, 
            activities, 
            sleepHours, 
            sampleQuestionPapersPracticed
        ]
        
        result = model.predict([data])
        result = "{:.2f}".format(result[0])
         
        return render_template('predict.html', result=result)
    
    return render_template('predict.html')
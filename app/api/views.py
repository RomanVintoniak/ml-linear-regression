from flask import jsonify, request
from app import model
from . import api

@api.route('/prediction', methods=['GET'])
def api_prediction():
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "no input data provided"}), 400
    
    if (not data.get('hoursStudied') or not data.get('prevScore') 
        or not data.get('activities') or not data.get('sleepHours')
        or not data.get('sampleQuestionPapersPracticed')):
        return jsonify({"message": "not all keys"}), 422
    
    hoursStudied = int(data.get('hoursStudied'))
    prevScore = int(data.get('prevScore'))
    activities = int(data.get('activities'))
    sleepHours = int(data.get('sleepHours'))
    sqpp = int(data.get('sampleQuestionPapersPracticed'))
    
    data_for_predict = [
        hoursStudied,
        prevScore, 
        activities, 
        sleepHours, 
        sqpp
    ]
    
    result = model.predict([data_for_predict])
    result = "{:.2f}".format(result[0])
    
    return jsonify({
        "score": result
    }), 200

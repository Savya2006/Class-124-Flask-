from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        'Contact':"987XXXXXXX",
        'Name':"ABC",
        'done':False,
        'id':1
    },
    {
        'Contact':"984XXXXXXX",
        'Name':"XYZ",
        'done':False,
        'id':2
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide The Data"
        },400)

    task={
        'id':task[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json('Contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"succes",
        "message":"Task Added Succesfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)
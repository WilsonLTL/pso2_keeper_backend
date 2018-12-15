import logging,json
from flask_cors import CORS
from flask import Flask,jsonify,request
app = Flask(__name__)
CORS(app)


@app.route('/',methods=['POST'])
def enter_api_system():
    result = {
        "result": "enter api system"
    }
    return jsonify(result)


@app.route('/get_player_card_data', methods=['POST'])
def get_player_card_data():
    with open('config/player_card.json') as f:
        data = json.load(f)
        return jsonify(data)


@app.route('/get_mission_card_data', methods=['POST'])
def get_mission_card_data():
    with open('config/mission_card.json') as f:
        data = json.load(f)
        return jsonify(data)


@app.route('/update_player_card_data', methods=['POST'])
def update_player_card_data():
    result = request.json
    with open('config/player_card.json', 'w') as f:
        result = {
            "player_card":result
        }
        json.dump(result, f)
        f.close()
        return jsonify({"status":True})


@app.route('/update_mission_card_data', methods=['POST'])
def update_mission_card_data():
    print(request.json)
    result = request.json
    with open('config/mission_card.json', 'w') as f:
        result = {
            "mission":result["mission"],
            "mission_card":result["mission_card"]
        }
        json.dump(result, f)
        f.close()
        return jsonify({"status":True})


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)
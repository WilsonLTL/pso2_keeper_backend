import logging,json,glob
from flask_cors import CORS
from flask import Flask,jsonify,request
from pathlib import Path
from random import *
app = Flask(__name__)
CORS(app)

# config_location = "/home/ubuntu/pso2_keeper_backend/"
config_location =""
global mission
global player_card
global quote
global new_player_card
new_player_card = {"player_card":[]}


@app.route('/',methods=['POST','GET'])
def enter_api_system():
    result = {
        "result": "enter api system"
    }
    return jsonify(result)


@app.route('/reset',methods=['POST'])
def reset():
    with open(config_location+'backup/config/mission_card.json') as f:
        data = json.load(f)
        global mission
        mission = data["mission"]
        global quote
        quote = data["quote"]
        f.close()
    with open(config_location + 'config/mission_card.json', 'w') as f2:
        json.dump(data, f2)
        f2.close()
    with open(config_location+'backup/config/player_card.json') as f3:
        data = json.load(f3)
        f3.close()
    with open(config_location + 'config/player_card.json', 'w') as f4:
        json.dump(data, f4)
        f4.close()
    return jsonify({"result":"success"})


@app.route('/get_player_card_data', methods=['POST'])
def get_player_card_data():
    with open(config_location+'config/player_card.json') as f:
        data = json.load(f)
        global player_card
        player_card = data
        f.close()
        return jsonify(data)


@app.route('/get_mission_card_data', methods=['POST'])
def get_mission_card_data():
    with open(config_location+'config/mission_card.json') as f:
        data = json.load(f)
        global mission
        mission = data["mission"]
        global quote
        quote = data["quote"]
        f.close()
        return jsonify(data)


@app.route('/update_player_card_data', methods=['POST'])
def update_player_card_data():
    res = request.json
    with open(config_location+'config/player_card.json', 'w') as f:
        result = {
            "player_card":res
        }
        # for x in player_card["player_card"]:
        #     for r in res:
        #         if x["name"] == r["name"]:
        #             result["player_card"].append(r)
        #             break
        # for w in new_player_card["player_card"]:
        #     result["player_card"].append(w)
        # new_player_card["player_card"] = []
        global player_card
        player_card = result
        json.dump(result, f)
        f.close()
        return jsonify({"status":True})


@app.route('/update_mission_card_data', methods=['POST'])
def update_mission_card_data():
    result = request.json
    with open(config_location+'config/mission_card.json', 'w') as f:
        result = {
            "mission":mission,
            "mission_card":result["mission_card"],
            "quote":quote
        }
        json.dump(result, f)
        f.close()
        return jsonify({"status":True})


@app.route('/update_mission_data', methods=['POST'])
def update_mission_data():
    result = request.json
    with open(config_location + 'config/mission_card.json', 'w') as f:
        global mission
        mission = result["mission"]
        global quote
        quote = result["quote"]
        result = {
            "mission": mission,
            "mission_card": result["mission_card"],
            "quote": quote
        }
        json.dump(result, f)
        f.close()
        return jsonify({"status": True})


@app.route('/update_notebook', methods=['POST'])
def update_notebook():
    result = request.json
    with open(config_location + 'config/mission_card.json', 'r') as f:
        data = json.load(f)
        global mission
        global quote
        mission["notebook"] = result["notebook"]
        result = {
            "mission": mission,
            "mission_card": data["mission_card"],
            "quote":quote
        }
        f.close()
    with open(config_location + 'config/mission_card.json', 'w') as f1:
        json.dump(result, f1)
        f1.close()
    return jsonify({"status": True})


@app.route('/add_new_player', methods=['POST'])
def add_new_player():
    result = request.json
    print(result)
    print(player_card)
    player_card["player_card"].append(result["player"])
    print("new player"+str(result["player"]))
    with open(config_location + 'config/player_card.json', 'w') as f:
        json.dump(player_card, f)
        f.close()
    return jsonify(player_card)


@app.route('/add_reg_player', methods=['POST'])
def add_reg_player():
    result = request.json
    try:
        with open(config_location + 'registered_player/'+str(result["access_token"])+'.json', 'r') as f:
            data = json.load(f)
            player ={
                "id":result["access_token"],
                "name":data["player_name"],
                "avatar":data["player_image"],
                "class":result["class"],
                "leader":False,
                'PS':''
            }
            player_card["player_card"].append(player)
            print(len(player_card["player_card"]))
            print(player_card["player_card"])
            f.close()
            with open(config_location + 'config/player_card.json', 'w') as f2:
                json.dump(player_card, f2)
                f2.close()
        return jsonify(player_card)
    except Exception as e:
        print(e)
        return jsonify({"status":False})


@app.route('/reg_new_player', methods=['POST'])
def reg_new_player():
    result = request.json
    new_userID = randint(1, 1000)
    new_user_file = Path(config_location+"registered_player/PSO2-ARKS" + str(new_userID) + ".json")
    while new_user_file.is_file():
        new_userID = randint(1, 1000)
        new_user_file = Path(config_location + "registered_player/PSO2-ARKS" + str(new_userID) + ".json")
    with open(config_location + 'registered_player/PSO2-ARKS'+str(new_userID)+'.json', 'w') as f:
        json.dump(result, f)
        f.close()
    return jsonify({"status":True,"user_access_token":"PSO2-ARKS"+str(new_userID)})


@app.route('/user_login', methods=['POST'])
def user_login():
    result = request.json
    # for player in glob.glob(config_location+"registered_player/*.json"):
    try:
        with open(config_location + "registered_player/" + result["player_access_token"] + ".json", 'r') as f:
            data = json.load(f)
            if result["player_password"] == data["player_password"]:
                f.close()
                return jsonify(
                    {
                        "status": True,
                        "playercard": data
                     }
                )
            else:
                f.close()
                return jsonify({"status": False})
    except Exception as e:
        print(e)
        return jsonify({"status": False})


@app.route('/user_update', methods=['POST'])
def user_update():
    result = request.json
    print(result)
    try:
        with open(config_location + "registered_player/" + result["access_token"] + ".json", 'w') as f:
            result = {
                "player_name": result["name"],
                "player_image": result["avatar"],
                "player_password": result["password"]
            }
            json.dump(result, f)
            f.close()
        return jsonify({"status": True,"playercard": result})

    except Exception as e:
        print(e)
        return jsonify({"status": False})


@app.route('/line_get_user_file', methods=['POST'])
def line_get_user_file():
    try:
        result = str(request.data).split("&")
        lineID = result[0].split("lineID=")[1]
        accesstoken = result[1].split("=")[1].split("'")[0]
        with open(config_location + 'registered_player/' + accesstoken + ".json","r") as f:
            data = json.load(f)
            print(data)
            result = {
                "status": True,
                "play_name": data["player_name"],
                "access_token": accesstoken,
                "lineID": lineID
            }
        return jsonify(result)
    except Exception as e:
        return jsonify({"status":False})


if __name__ == '__main__':
    with open(config_location+'config/player_card.json') as f:
        data = json.load(f)
        global player_card
        player_card = data

    with open(config_location+'config/mission_card.json') as f:
        data = json.load(f)
        global mission
        mission = data["mission"]
        global quote
        quote = data["quote"]
        # app.run(host="0.0.0.0", port=5000)
        app.run(threaded=True, host="0.0.0.0", port=3000)
        # app.run(host="172.31.28.201",port=8080)

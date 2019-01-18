from pocha import it,describe
import requests


@describe('routing testing')
def _():
    @it('routing:api system check')
    def test_init():
        url = "http://127.0.0.1:8080/"
        payload = ""
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "7759277d-6293-49e5-b194-5b0a2085b1e1"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        # assert (response.text == "...")

    @it('routing:get_player_card_data')
    def test1():
        url = "http://127.0.0.1:8080/get_player_card_data"
        payload = ""
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "7759277d-6293-49e5-b194-5b0a2085b1e1"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        # assert (response.text == "...")

    @it('routing:get_mission_card_data')
    def test2():
        url = "http://127.0.0.1:8080/get_mission_card_data"
        payload = ""
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "7759277d-6293-49e5-b194-5b0a2085b1e1"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        # assert (response.text == "...")
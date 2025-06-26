#Дмитрий Чибрин, 31-я когорта - дипломный проект
import sender_stand_request
import data

def get_track():
    track = sender_stand_request.post_new_order(data.order_body)
    return track.json().get("track")

def test_get_order():
    response = sender_stand_request.get_order(get_track())
    assert response.status_code == 200



import requests


# # в невалидном формате даты
for checkin in "15-05-2015", "##$@@", 108, 5.5, {"name": "name"}, ["name1", "name2"], True:

    try:
       url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
       response = requests.get(url)
       assert response.json(), " Checkin invalid date format"

    except requests.exceptions.JSONDecodeError:
        assert True, "Response is not in JSON format"
        print ("♥")


        # try:
        #     response_as_dict = response.json()
        # except json.JSONDecodeError:
        #     assert False, f"Response is not in JSON format.Response text is {response.text}"
        #
        # assert name in response_as_dict, f"Response JSON doesn't have key {name} "
        # assert response_as_dict[name] == expected_value, error_message
#
#
#
# #дата заезда выходит за диапазон предусмотренных значений
# checkin = "3000-05-15"
# url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
# response = requests.get(url)
#
# assert not response.json(), "Checkin date is out of range"



#
# # пустое поле даты
# checkin = " "
# url = f"https://restful-booker.herokuapp.com/booking?checkin={checkin}"
# response = requests.get(url).json()
# assert not response, "Checkin date is out of range"

    #print(response.text)


# response = requests.get("https://restful-booker.herokuapp.com/booking/5455")
# print(response.text)

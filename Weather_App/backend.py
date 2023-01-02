import requests


API_KEY = "***YOUR API***"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    print(filtered_data)
    nr_values = days * 8
    filtered_data = filtered_data[:nr_values]

    return filtered_data


print(get_data(place="Sofia", days=4))

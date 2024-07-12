import requests

API_KEY = "d780f9b9c1581240a047518ea4c6858d"


def get_data(place, forecast_days=None):
    url = F"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    data_filtred = data['list']
    nr_values = 8 * forecast_days
    data_filtred = data_filtred[ :nr_values]

    return data_filtred


if __name__ == "__main__":
    data = get_data(place="Tokio", forecast_days=3)

    print(data)

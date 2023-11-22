import os
import time
from datetime import datetime
from requests_html import HTMLSession
from icecream import ic

def get_weather_data(query):
    url = f"https://www.google.com/search?q=weather+{query}"
    
    try:
        s = HTMLSession()
        r = s.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        })
        
        temp_max = ic(r.html.find("div.wNE31c", first=True).find("span.wob_t")[0].text)
        temp_min = ic(r.html.find("div.wNE31c", first=True).find("span.wob_t")[-2].text)
        desc_day = ic(r.html.find("g-img.uW5pk", first=True).find("img#dimg_1", first=True).attrs.get("alt"))
        temp_current = ic(r.html.find("span#wob_tm", first=True).text)
        unit = ic(r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text)
        desc_current = ic(r.html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text)
        rain_current = ic(r.html.find("div.wtsRwe", first=True).find("span#wob_pp", first=True).text)
        air_humidity_current = ic(r.html.find("div.wtsRwe", first=True).find("span#wob_hm", first=True).text)
        wind_speed_current = ic(r.html.find("div.wtsRwe", first=True).find("span#wob_ws", first=True).text)
        date_time = ic(datetime.now())
        
        return {
            "status": True,
            "temp_max": temp_max,
            "temp_min": temp_min,
            "desc_day": desc_day,
            "temp_current": temp_current,
            "unit": unit,
            "desc_current": desc_current,
            "rain_current": rain_current,
            "air_humidity_current": air_humidity_current,
            "wind_speed_current": wind_speed_current,
            "date_time": date_time
        }
    except Exception as e:
        print(f"Erro ao obter dados do tempo: {e}")
        return {
            "status": False,
            "temp_max": None,
            "temp_min": None,
            "desc_day": None,
            "temp_current": None,
            "unit": None,
            "desc_current": None,
            "rain_current": None,
            "air_humidity_current": None,
            "wind_speed_current": None,
            "date_time": None
        }

def save_to_csv(data, data_file_path, logs_file_path, execution_time, user):
    with open(data_file_path, 'a', encoding='utf-8') as file:
        if data['status']:
            print(f"{data['air_humidity_current']},{data['desc_current']},{data['desc_day']},{data['unit']},{data['rain_current']},{data['temp_current']},{data['temp_max']},{data['temp_min']},{data['wind_speed_current']},{data['date_time']}", file=file)
        else:
            print(f"{None},{None},{None},{None},{None},{None},{None},{None},{None},{None}", file=file)

    with open(logs_file_path, "a", encoding='utf-8') as file:
        print(f"{user},{execution_time},{data['status']}", file=file)


def main():
    initial_time = time.time()
    
    query = "cacador sc"
    weather_data = get_weather_data(query)

    final_time = time.time()
    execution_time = final_time - initial_time

    user = os.environ.get('USER') or os.environ.get('USERNAME')

    path = os.curdir
    data_path = os.path.join(path, 'data')
    os.makedirs(data_path, exist_ok=True)

    data_file_path = os.path.join(data_path, 'weather_report_data.csv')

    logs_file_path = os.path.join(data_path, 'logs.csv')

    save_to_csv(weather_data, data_file_path, logs_file_path, execution_time, user)

if __name__ == "__main__":
    ic()
    main()
    ic()


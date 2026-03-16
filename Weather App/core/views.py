import requests
from datetime import datetime, timedelta

from django.shortcuts import render

api_key = "410ac148b776aafbf58a8ec881116115"
GOOGLE_API = 'AIzaSyAze-kyMnzg2lIFJCXQZdG0zakDg_UyvsM'
SEARCH_ENGINE_ID = 'e5d5b8cd13de442fa'

def home(request):
    city = request.POST.get('city', 'Kathmandu')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    query = f"{city} HD"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'

    city_url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgsize=medium"

    try:
        # Get OpenWeather API data
        info = requests.get(url)
        result = info.json()

        if "weather" not in result:
            raise ValueError("Invalid API response")

        description = result['weather'][0]['description']
        icon = f"http://openweathermap.org/img/wn/{result['weather'][0]['icon']}@2x.png"
        temperature = round(result['main']['temp'])
        feels_like = round(result['main']['feels_like'])
        city_name = result.get('name', city)
        city_time_offset = result.get('timezone', 0)

        utc_time = datetime.utcnow()
        city_time = (utc_time + timedelta(seconds=city_time_offset)).strftime("%Y-%m-%d %H:%M:%S")

        # Get city image from Google Custom Search API
        data = requests.get(city_url).json()
        search_items = data.get("items", [])
        if search_items and len(search_items) > 1:
            image_url = search_items[1]['link']
        elif search_items:
            image_url = search_items[0]['link']
        else:
            image_url = None

        context = {
            'description': description,
            'feels_like': feels_like,
            'icon': icon,
            'temperature': temperature,
            'city_time': city_time,
            'city_name': city_name,
            'image_url': image_url
        }

    except Exception as e:
        context = {'error': f"Error fetching weather data: {str(e)}"}

    return render(request, 'home.html', context)

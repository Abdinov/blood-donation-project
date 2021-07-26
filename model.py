import requests

def location(query):
    endpoint = f"http://dev.virtualearth.net/REST/v1/Locations/US/WA/98052/Redmond/1%20Microsoft%20Way?o=json&key=ArYtgpC--9RSfpY3gyjgKhRhx6fCVwDNd_2D850Y8iEYWng7HPoOSo_4cUOKMysY"
    #response = requests.get(endpoint).json()
    response = requests.get(endpoint).json()
    address = response['resourceSets'][0]['resources'][0]['point']['coordinates']
    print(address)
    return "hello"
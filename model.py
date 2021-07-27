import requests

def location(query):
    endpoint = f"http://dev.virtualearth.net/REST/v1/Locations/US/%7BadminDistrict%7D/{query}/%7Blocality%7D/%7BaddressLine%7D?include&key=ArYtgpC--9RSfpY3gyjgKhRhx6fCVwDNd_2D850Y8iEYWng7HPoOSo_4cUOKMysY"
    #response = requests.get(endpoint).json()
    response = requests.get(endpoint).json()
    address = response['resourceSets'][0]['resources'][0]['point']['coordinates']

    # print(address)
    return address



def destination(address):
    long = address[0]
    lad = address[1]
    string = str(long) + "," + str(lad)
    # print(address)
    endpoint = f'https://dev.virtualearth.net/REST/v1/LocalSearch/?query=blooddonation&userLocation={string}&key=Asu_IrTxezA_IbYyg0yFSIrm-9lUaRx8ndlEBciPABl05_j7zzt3RiQy-6gyc_xQ'
    # print(endpoint)
    locations = requests.get(endpoint).json()
    # print(locations)
    lst = locations['resourceSets'][0]['resources']
    # print (lst)
    return lst



    # response = requests.get(endpoint).json()

    # bloodcenter_name = response['resourceSets'][0]['resources']
    # print(bloodcenter_name)

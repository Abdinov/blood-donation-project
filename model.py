import requests

def location(query):
    endpoint = "https://dev.virtualearth.net/REST/v1/LocalSearch/?query={query}&userLocation={point}&key={Asu_IrTxezA_IbYyg0yFSIrm-9lUaRx8ndlEBciPABl05_j7zzt3RiQy-6gyc_xQ}"
    response = requests.get(endpoint).json()
    return response
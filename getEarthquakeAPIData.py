import requests

response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-01-01&endtime=2020-01-02')
content = response.json()
# print("Total cases=",len(content))
# print(content)

if response.status_code == 200:
    for row in content['features']:
        coordinates = row['geometry']['coordinates']
        print(coordinates)
else:
    print("Failed to retrieve data from the API.")

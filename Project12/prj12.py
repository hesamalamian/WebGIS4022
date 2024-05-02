import requests

#configuration
url = "https://localhost:8080/geoserver/web/?13"
workspace = "kashanmap"
store = "KashanMap"
layer = "new"
username = "admin"
password = "geoserver"

#creating layer
Layer_url = f"{url}/rest/workspace/{workspace}/datastore/{store}/featuretypes"
headers = {'Content-headers':'text/xml'}
data = f"""<featureType><name>new</name></featureType>"""
respoonse = requests.post(Layer_url,auth=(username,password),headers=headers, data=data)

#validation
if respoonse.status_code == 201:
    print("Successful")
else:
    print("Failed")
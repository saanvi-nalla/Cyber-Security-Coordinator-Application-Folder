import requests

BASE="http://localhost:5000"

#get fileids 
r = requests.get(BASE + "/listfiles")
data=r.json()

print("Data from listfiles")
print(data)

#get firstfile_id
fid = data["file_IDs"]

r = requests.get( BASE + "/requestfile", params={"file_id": fid}
                 )

enc = r.json()

print("Data from requestfile")
print(enc)

enc["password"] = "bad_password1234"

r = requests.get ( BASE + "/readfile", params=enc )

print("Server Response")

print(r.json())


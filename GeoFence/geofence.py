import gps
from time import strftime
import json
from firebase_admin import credentials, initialize_app, storage

geofence = []
# Init firebase with your credentials
cred = credentials.Certificate("a.json")
initialize_app(cred, {'storageBucket': 'getfit-94c47.appspot.com'})
print("Geofencing Enabled")

while True:
    flag = 0
    time = str(strftime("%H:%M"))
    month = str(strftime("%Y-%m"))
    day  = str(strftime("%d"))
    newLoc = gps.gps()
    #Avoids duplicate data and adding the coordinates
    if newLoc not in geofence:
        geofence.append(newLoc)
    #Sends data on first day of month
    if day == "01":
        if time == "00:00":
            if flag == 0:
                #Writing data in file with year and month in format YYYY-MM
                filename = month + ".txt"
                f = open(filename, "w")
                f.write(str(geofence))
                print("Done")
                f.close()
                #Uploading data to firebase
                bucket = storage.bucket()
                blob = bucket.blob(filename)
                blob.upload_from_filename(filename)
                blob.make_public()
                flag = 1
        
        
        
    


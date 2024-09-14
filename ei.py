#Program to perform classification in Edge Impulse
import requests
import json

#---Get Sample ID---#

def getSampleId():
    url = "https://studio.edgeimpulse.com/v1/api/Project-ID/raw-data"
    querystring = {"category":"testing"}
    headers = {
        "cookie": "jwt=JWT",
        "accept": "application/json",
        "x-api-key": "API KEY"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    sample_json = json.loads(response.text)
    sample_id = sample_json['samples'][0]['id']
    
    return(sample_id)


#---Classify Sample---#

def classifySample(sample_id):
    url = "https://studio.edgeimpulse.com/v1/api/Project-ID/classify/" + str(sample_id)
    headers = {
        "cookie": "jwt=JWT",
        "accept": "application/json",
        "x-api-key": "API KEY"
    }

    response = requests.request("POST", url, headers=headers)
    classify_json = json.loads(response.text)
    classify = classify_json['classifications'][0]['result']
    Firecracker = 0
    Human        = 0
    Gunfire      = 0
    Noise        = 0
    n = float(len(classify))

    for i in range(len(classify)):
        Firecracker +=(classify[i]['Fireracker'])
        Human +=(classify[i]['Human'])
        Gunfire +=(classify[i]['Gunfire'])
        Noise +=(classify[i]['Noise'])
    Firecracker = (Firecracker/n)
    Human = (Human/n)
    Gunfire = (Gunfire/n)
    Noise = (Noise/n)
    result = {"Firecracker":Firecracker,"Human":Human,"Gunfire":Gunfire,"Noise":Noise}
    return max(result,key=result.get)


#---Delete Sample---#

def deleteSample(sample_id):
    url = "https://studio.edgeimpulse.com/v1/api/Project-ID/raw-data/" + str(sample_id)
    headers = {
        "cookie": "jwt=JWT",
        "accept": "application/json",
        "x-api-key": "API KEY"
    }

    response = requests.request("DELETE", url, headers=headers)
    
    return(response.status_code)

def analyseRisk():
    sampleId = getSampleId()
    value = classifySample(sampleId)
    deleteSample(sampleId) 
    return value   

if __name__ == '__main__':
    analyseRisk()


import os
import subprocess
import ei,iot

def main():
    while True:
        #Recording sample for 5s using arecord
        #os.system('arecord -D sysdefault:CARD=1 -d 5 -f cd -t wav sample.wav')
        if os.path.exists('sample.wav'):
            #Uploading sample to Edge Impulse using Edge Impulse CLI
            upload_response  = subprocess.Popen("edge-impulse-uploader --category testing sample.wav", stdout=subprocess.PIPE, shell=True).communicate()[0].decode('utf-8')
            upload_status    = int(upload_response.split('\n')[-2].split(':')[2].split('.')[0])
            print(upload_response)
            if upload_status == 0:
                print("Upload Done")
                #Classifying the uploaded sample
                value        = ei.analyseRisk()
                if value in ["Firecracker","Human","Gunfire"]:
                    alert = {value:1}
                    #Sending value to IOT CONNECT dashboard if alert is triggered
                    iot.sendtoiot(alert)    
            else:
                print("Upload Failure")
                break
        else:
            continue
if __name__=='__main__':
    main()

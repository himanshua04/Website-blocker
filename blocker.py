import time
from datetime import datetime as dt
temp=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com"]
starting_time=8
end_time=16
content=""
while True:
    if(dt.now().hour>starting_time and dt.now().hour<end_time):
        print("Working hours......")
        with open(temp,'+r')as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("fun time...")
        with open(temp,'r') as file:
            content=file.readlines()
            print(len(content))
            for i in range(len(content)):
                for website in website_list:
                    if(website in content[i] ):
                        content[i]=""
                        print("true")
        with open(temp,'w')as file:
            for i in range(len(content)):
                file.write(content[i])
    time.sleep(5)

import time
from datetime import datetime as dt

hosts_temp = r"/Users/abc/Documents/GitHub /PyPractice/Projects/WebBlocker/hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com", "www.reddit.com", "reddit.com"]


# Objective of this program is the stop services to certain websites while in working hours.
# datetime parameters are yr, m, d, hr, min, sec, microsecs and auto generated
before = dt(dt.now().year, dt.now().month, dt.now().day, 8)
after = dt(dt.now().year, dt.now().month, dt.now().day, 16)

while True:
    # checking the time between certain times; from
    if before < dt.now() < after:
        # modifying hosts file manually
        print("Currently Working")
        # if one of the website in my website list is found pass else add to the hosts file
        with open(hosts_temp, 'r+') as file:
            content = file.read() # contains all the content of the host file
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    # writing to the file to block the websites
                    file.write(redirect+" "+ websites+"\n")
    else:
        # this will remove the website from the hosts file to unblock those sites
        with open(hosts_path, 'r+') as file:
            content = file.readlines() # contains all the content of the host file
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Wooohooo Fun times are some good Times. ")
    time.sleep(60)  # checking time every min

    # TODO implement scheduling this python script in my Linux/Mac Machine 
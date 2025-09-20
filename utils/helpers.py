from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import unicodedata
import json
import argparse
import os

def get_soup(url):
    print(f"[INFO] Extrayendo de URL: {url!r}")
    safe_url = quote(url, safe=":/?&=")
    page = urlopen(safe_url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html,"html.parser")

def safe_filename(name: str) -> str:
    name = unicodedata.normalize("NFKD",name).encode("ascii","ignore").decode("ascii")
    name = name.replace(" ", "_")
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.upper()

def read_sections_file():
    helpers_dir = os.path.dirname(os.path.abspath(__file__))

    data_dir = os.path.join(helpers_dir, "..", "data")
    sections_file_path = os.path.join(data_dir, "sections.json")

    try:
        with open(sections_file_path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'[ERROR] : Archivo de configuración no encontrado en: {sections_file_path}')
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] : Error de lectura en el archivo JSON: {e}")
        return {}

def get_section(name):
    config = read_sections_file()
    if not config:
        return None

    return config.get('sections', {}).get(name)

def normalize_section_title(title: str) -> str:
    title = unicodedata.normalize("NFKD", title).encode("ASCII", "ignore").decode("utf-8")
    
    title = re.sub(r"[&|/-]", "_", title)
    title = re.sub(r"\s+", "_", title)
    title = re.sub(r"[^A-Za-z0-9_]", "", title)
    title = re.sub(r"_+", "_", title)
    
    title = title.strip("_")

    return title.upper() 

def logo() -> str:  
    return r""" 
  __  __ _         _____                                      
 |  \/  | |       / ____|                                     
 | \  / | | __   | (___   ___ _ __ __ _ _ __  _ __   ___ _ __ 
 | |\/| | |/ /    \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
 | |  | |   < _   ____) | (__| | | (_| | |_) | |_) |  __/ |   
 |_|  |_|_|\_(_) |_____/ \___|_|  \__,_| .__/| .__/ \___|_|   
                                       | |   | |              
                                       |_|   |_|                         
    """ 

def get_info() -> str:
    return f"{logo()} \n Desarrollado por: zNahuelz - GitHub: https://github.com/zNahuelz"
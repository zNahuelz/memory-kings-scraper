import re
import json
from utils.models import Section
from utils.helpers import get_soup
from utils.helpers import normalize_section_title 
from pathlib import Path
from urllib.parse import urljoin
SITE_URL = "https://www.memorykings.pe"

def get_section_list():
    sections = []
    page = get_soup(SITE_URL)
    ul = page.find('ul',class_="products flex grid-1-4 grid-1-3-m grid-1-2-s grid-1-1-xs pt-2")
    if not ul:
        print("[WARN] : No se encontró la lista de secciones. Debe crear el archivo /data/sections.json manualmente, consulte la documentación.")
        return sections
    lis = ul.find_all('li')
    for li in lis:
        a_tag = li.find('a')
        if not a_tag or not a_tag.get('href'):
            continue
        url = urljoin(SITE_URL, a_tag['href'])

        title_tag = li.find('p',class_='text-center')
        if not title_tag:
            continue
        name = title_tag.get_text(strip=True)

        section = Section(title=name,url=url,children_number=0,childs=[])
        sections.append(section)
    return sections

def export_sections_to_json(sections, output_file="data/sections.json"):
    sections_dict = {}
    for section in sections:
        normalized_title = normalize_section_title(section.title)
        sections_dict[normalized_title] = section.url
    final_dict = {"sections":sections_dict}

    Path(output_file).parent.mkdir(parents=True,exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_dict,f,ensure_ascii=False,indent=4)
    print(f"[INFO] : Secciones guardadas en: {output_file}")


def main():
    sections = get_section_list()
    for section in sections:
        section.title = normalize_section_title(section.title)
    export_sections_to_json(sections)

if __name__== '__main__':
    main()
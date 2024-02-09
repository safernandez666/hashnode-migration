import re
import os
import json
from zipfile import ZipFile

def create_post_md(title, date, slug, image, content):
    md_content = f"""---
title: "{title}"
date: "{date}"
slug: "{slug}"
image: "{image}"
---

{content}
"""
    folder_path = "posts"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"{slug}.md")
    with open(file_path, "w") as file:
        file.write(md_content)

def zip_folder(nombre_carpeta, nombre_zip):
    with ZipFile(nombre_zip, 'w') as zipf:
        # Recorre todos los archivos en la carpeta
        for carpeta_raiz, _, archivos in os.walk(nombre_carpeta):
            for archivo in archivos:
                # Obtiene la ruta completa del archivo
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                # Agrega el archivo al archivo ZIP
                zipf.write(ruta_archivo, os.path.relpath(ruta_archivo, nombre_carpeta))

# Load data from phrases.json file
with open('posts.json', 'r') as file:
    data = json.load(file)

# Iterate over each item and print the Title
for item in data:
    cleaned_string = re.sub(r'<(?!img\s).*?>', '', item["Content"])  # Remove all HTML tags except img
    create_post_md(item["Title"], item["Date"], item["Title"].replace("/", "-"), "Insert Image URL Here", cleaned_string)
    img_urls = re.findall(r'<img.*?src="(.*?)".*?>', item["Content"])  # Extract img URLs
    print("Se creo el Archivo ", item["Title"] + ".md")
    print("Image URLs:", img_urls)

# Zip Var
folder = 'posts'
file_zip = 'archivo.zip'

zip_folder(folder, file_zip)

print("Carpeta comprimida exitosamente.")

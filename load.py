import json
import re, os

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


# Load data from phrases.json file
with open('posts.json', 'r') as file:
    data = json.load(file)


# Iterate over each item and print the Title
for item in data:
    cleaned_string = re.sub(r'<[^>]*>', '', item["Content"])
    print(cleaned_string)
    create_post_md(item["Title"], item["Date"], item["Title"].replace("/", "-"), "Insert Image URL Here", cleaned_string)

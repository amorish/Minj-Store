import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_card(match):
    src = match.group(1)
    return f'<a href="{src}" target="_blank" class="port-card stg" style="display:block; text-decoration:none; color:inherit;">\n        <div class="port-thumb">\n          <img src="{src}"'

# Find all <div class="port-card stg"> and replace with <a href="..."
# We need to capture the img src
pattern = r'<div class="port-card stg">\s*<div class="port-thumb">\s*<img src="([^"]+)"'
content = re.sub(pattern, replace_card, content)

# Replace the closing </div> of the port-card with </a>
# This is tricky because there are other divs inside.
# Actually, replacing exactly the structure is safer.

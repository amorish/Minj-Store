import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    inner_content = match.group(1)
    src = match.group(2)
    return f'<a href="{src}" target="_blank" class="port-card stg" style="display:block; text-decoration:none; color:inherit;">{inner_content}\n      </a>'

pattern = r'<div class="port-card stg">(.*?<img src="([^"]+)".*?)\n      </div>'
content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed")

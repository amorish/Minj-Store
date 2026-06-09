import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reverse the bad replacement
# Bad format: <a href="[inner_content]" target="_blank" class="port-card stg" style="...">[src]      </a>
pattern = r'<a href="(.*?)".*?>([^<]+)\s*</a>'

def fix(match):
    inner = match.group(1)
    return f'<div class="port-card stg">{inner}\n      </div>'

# We have to be careful with flags=re.DOTALL
content = re.sub(r'<a href="(\n\s*<div class="port-thumb">.*?)".*?>([^<]+)\s*</a>', fix, content, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored")

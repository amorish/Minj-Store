import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace "I'm Minj Store" -> "I'm Manish"
content = content.replace("I'm Minj Store.", "I'm Manish.")
content = content.replace("मैं मिंज स्टोर हूँ।", "मैं मनीष हूँ।")
content = content.replace("আমি Minj Store।", "আমি মনীশ।")

# 2. Make portfolio cards clickable
# Each card looks like:
#       <div class="port-card stg">
#         <div class="port-thumb">
#           <img src="..."
# ...
#       </div>

# Find all port-card blocks
def replacer(match):
    src = match.group(1)
    inner_content = match.group(2)
    return f'<a href="{src}" target="_blank" class="port-card stg" style="display:block; text-decoration:none; color:inherit;">{inner_content}      </a>'

pattern = r'<div class="port-card stg">(.*?<img src="([^"]+)".*?)\n      </div>'
content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating portfolio.html")

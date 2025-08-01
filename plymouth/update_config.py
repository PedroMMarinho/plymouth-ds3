import json
import random
import re
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
items_path = os.path.join(script_dir, "items.json")
script_path = os.path.join(script_dir, "ds3.script")

with open(items_path, "r", encoding="utf-8") as f:
    items = json.load(f)

entry = random.choice(items)
image_path = entry["image"]

title = entry["name"].strip() + '\\\\n'

description = entry["description"]

paragraphs = description.split('\n\n')

escaped_parts = []
for i, paragraph in enumerate(paragraphs):
    if paragraph.strip():  
        lines = paragraph.split('\n')
        for line in lines:
            if line.strip(): 
                escaped_line = line.strip().replace('"', '\\\\"')
                escaped_parts.append(f'"{escaped_line}"')
    
    if i < len(paragraphs) - 1:
        escaped_parts.append('""')

description_array = f"[{', '.join(escaped_parts)}]"

# Read the ds3.script file
with open(script_path, "r", encoding="utf-8") as f:
    script = f.read()

# Replace image path
script = re.sub(
    r'(?<=# === ITEM IMAGE ===\n)item_image = Image\(".*?"\);',
    f'item_image = Image("{image_path}");',
    script
)

# Replace title text
script = re.sub(
    r'(# === Create Title Text ===\n)title_text = ".*?";',
    rf'\1title_text = "{title}";',
    script,
    flags=re.DOTALL
)

# Replace description text array
script = re.sub(
    r'(# === Create Description Text ===\n)description_text = \[.*?\];',
    rf'\1description_text = {description_array};',
    script,
    flags=re.DOTALL
)

# Save updated script back
with open(script_path, "w", encoding="utf-8") as f:
    f.write(script)

print(f"✅ Updated with: {entry['name']} ({image_path})")
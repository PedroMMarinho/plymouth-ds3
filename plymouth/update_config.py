import json
import random
import re
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

items_path = os.path.join(script_dir, "items.json")
script_path = os.path.join(script_dir, "ds3.script")

with open(items_path, "r", encoding="utf-8") as f:
    items = json.load(f)

# Select a random item
entry = random.choice(items)

image_path = entry["image"]

# Title: clean it and ensure it ends with a literal \n
title = entry["name"].strip() + '\\\\n'

# Description: Split by single \n for each array entry, add empty string after each part
description_parts = entry["description"].split('\n')

# Remove empty parts (handles duplicate \n at the end)
description_parts = [part.strip() for part in description_parts if part.strip()]

escaped_parts = []
for part in description_parts:
    escaped_part = part.replace('"', '\\\\"')
    escaped_parts.append(f'"{escaped_part}"')
    escaped_parts.append('""')

if escaped_parts and escaped_parts[-1] == '""':
    escaped_parts.pop()

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

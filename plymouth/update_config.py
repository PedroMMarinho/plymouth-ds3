import json
import random
import re

# Load items
with open("items.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Choose a random item
entry = random.choice(items)

# Image path
image_path = entry["image"]

# Title: clean it and ensure it ends with a literal \n
title = entry["name"].strip() + '\\\\n'

# Description: Split by single \n for each array entry
description_parts = entry["description"].split('\n')

# Remove empty parts (handles duplicate \n at the end)
description_parts = [part.strip() for part in description_parts if part.strip()]

escaped_parts = []
for part in description_parts:
    # Escape quotes only (no \n added)
    escaped_part = part.replace('"', '\\\\"')
    escaped_parts.append(f'"{escaped_part}"')

description_array = f"[{', '.join(escaped_parts)}]"

# --- Read and update script ---

with open("ds3.script", "r", encoding="utf-8") as f:
    script = f.read()

# Replace image path
script = re.sub(
    r'(?<=# === ITEM IMAGE ===\n)item_image = Image\(".*?"\);',
    f'item_image = Image("{image_path}");',
    script
)

# Replace title text - Fixed regex pattern
script = re.sub(
    r'(# === Create Title Text ===\n)title_text = ".*?";',
    rf'\1title_text = "{title}";',
    script,
    flags=re.DOTALL
)

# Replace description text array - Fixed regex pattern  
script = re.sub(
    r'(# === Create Description Text ===\n)description_text = \[.*?\];',
    rf'\1description_text = {description_array};',
    script,
    flags=re.DOTALL
)

# Save back
with open("ds3.script", "w", encoding="utf-8") as f:
    f.write(script)

print(f"✅ Updated with: {entry['name']} ({image_path})")

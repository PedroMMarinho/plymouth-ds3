import csv
import json
import os
import shutil

# === Config ===
csv_file = 'info.csv'
sprite_input_dir = 'output_sprites'
sprite_output_dir = 'sprites'
json_file = 'items.json'

# === Ensure output dir exists ===
os.makedirs(sprite_output_dir, exist_ok=True)

# === Load existing JSON data if present ===
if os.path.exists(json_file):
    with open(json_file, 'r', encoding='utf-8') as jf:
        items_data = json.load(jf)
else:
    items_data = []

# === Read CSV and process each entry ===
with open(csv_file, newline='', encoding='utf-8') as csvf:
    reader = csv.DictReader(csvf, quotechar='"')
    for row in reader:
        try:
            name = row['Name']
            description = row['Description']
            image_id = int(row['ImageId'])

            # Format image name
            image_name = name.lower().replace(' ', '_')
            input_image_path = os.path.join(sprite_input_dir, f"sprite_{image_id:02d}.png")
            output_image_path = os.path.join(sprite_output_dir, f"{image_name}.png")

            # Copy the sprite image
            if os.path.exists(input_image_path):
                shutil.copy(input_image_path, output_image_path)
            else:
                print(f"⚠️  Image not found: {input_image_path}")
                continue

            # Add to JSON
            item_entry = {
                "name": name,
                "description": description,
                "image": f"sprites/{image_name}.png"
            }
            items_data.append(item_entry)
            print(f"✅ Added: {name} -> {output_image_path}")

        except ValueError as ve:
            print(f"❌ Error parsing row: {row}\n{ve}")


# === Save to JSON ===
with open(json_file, 'w', encoding='utf-8') as jf:
    json.dump(items_data, jf, indent=4, ensure_ascii=False)

print(f"\n🎉 Done. JSON saved to {json_file}")

from PIL import Image
import os

# === Configuration ===
output_dir = "output_sprites"        # Directory to save individual sprites
sprites_per_row = 12                 # Number of sprites horizontally
frame_index = 0

# === Load image ===
for images in range (1,14):
    input_path = f"spritesheet{images}.png"
    image = Image.open(input_path)
    sheet_width, sheet_height = image.size
    print(f"Original image size: {sheet_width}x{sheet_height}")

    # === Calculate frame size ===
    sprite_width = sheet_width // sprites_per_row
    sprite_rows = sheet_height // sprite_width
    sprite_height = sheet_height // sprite_rows

    print(f"Each sprite size: {sprite_width}x{sprite_height}")
    print(f"Total sprites: {sprites_per_row * sprite_rows}")

    # === Create output dir ===
    os.makedirs(output_dir, exist_ok=True)

    # === Split and save each sprite ===
    for row in range(sprite_rows):
        for col in range(sprites_per_row):
            x = col * sprite_width
            y = row * sprite_height
            sprite = image.crop((x, y, x + sprite_width, y + sprite_height))
            sprite_path = os.path.join(output_dir, f"sprite_{frame_index:02d}.png")
            sprite.save(sprite_path)
            
            print(f"Saved sprite {frame_index:02d} at {sprite_path}")
            frame_index += 1
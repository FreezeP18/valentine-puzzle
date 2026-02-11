from PIL import Image
import os

INPUT = r"C:\Users\sebas\OneDrive\Escritorio\valentine-puzzle-main\images\full-image.png"
   # pongan acá su imagen (misma carpeta que el script)
OUTDIR = r"C:\Users\sebas\OneDrive\Escritorio\valentine-puzzle-main\images"

os.makedirs(OUTDIR, exist_ok=True)

img = Image.open(INPUT).convert("RGBA")
w, h = img.size

tile_w = w // 3
tile_h = h // 3

# Guardar full-image.png
img.save(os.path.join(OUTDIR, "full-image.png"))

# Guardar tiles 1..9 (izq->der, arriba->abajo)
n = 1
for row in range(3):
    for col in range(3):
        left = col * tile_w
        upper = row * tile_h
        right = (col + 1) * tile_w
        lower = (row + 1) * tile_h
        tile = img.crop((left, upper, right, lower))
        tile.save(os.path.join(OUTDIR, f"tile-{n}.png"))
        n += 1

print("Listo: tiles y full-image.png en /images")

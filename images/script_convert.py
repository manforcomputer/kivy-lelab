from PIL import Image

# Ouvrir l'animation WebP
img = Image.open("giphy1.webp")

# Sauvegarder en GIF animé
img.save("giphy1.gif", format="GIF", save_all=True, loop=0)

#!/usr/bin/env python3
from PIL import Image
import os
import sys


def convert_webp_to_gif(input_file, output_file=None):
    """
    Convertit un fichier WebP animé en GIF
    """
    if not output_file:
        output_file = input_file.replace('.webp', '.gif')

    try:
        print(f"📁 Conversion de {input_file} vers {output_file}")
        img = Image.open(input_file)
        print(f"✅ Image chargée : {img.size}, {getattr(img, 'n_frames', 1)} frames")

        img.save(output_file, format='GIF', save_all=True, loop=0, duration=100)
        print(f"✅ Conversion terminée ! Fichier : {output_file}")

    except FileNotFoundError:
        print(f"❌ Erreur : Fichier {input_file} non trouvé")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Utilisation en ligne de commande
    if len(sys.argv) > 1:
        convert_webp_to_gif(sys.argv[1])
    else:
        # Conversion par défaut
        convert_webp_to_gif('images/giphy1.webp')
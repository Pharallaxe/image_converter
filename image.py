# Importer les modules nécessaires
from PIL import Image  # Pour manipuler les images
import os  # Pour interagir avec le système de fichiers


def convert_image(image_path, output_quality, resolutions, final_directory):
    # Extraire le nom de base et l'extension du fichier
    base_name, ext = os.path.splitext(os.path.basename(image_path))

    for resolution in resolutions:
        # Créer un sous-dossier pour chaque résolution dans le dossier 'final'
        resolution_directory = os.path.join(final_directory, str(resolution))

        # Vérifier si le dossier existe, sinon le créer
        if not os.path.exists(resolution_directory):
            os.makedirs(resolution_directory)

        # Ouvrir l'image originale et la redimensionner
        with Image.open(image_path) as img:
            # Récupérer les dimensions originales
            original_width, original_height = img.size

            # Calculer le facteur d'échelle pour conserver le ratio
            if original_width > original_height:
                scale = resolution / original_width
                new_width = resolution
                new_height = int(original_height * scale)
            else:
                scale = resolution / original_height
                new_width = int(original_width * scale)
                new_height = resolution

            # Redimensionner l'image tout en gardant les proportions
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convertir en mode RGB si nécessaire pour le format JPEG
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Chemin pour enregistrer le fichier JPG
            jpg_path = os.path.join(resolution_directory, f"{base_name}.jpg")
            # Enregistrer l'image en format JPG avec la qualité spécifiée
            try:
                img.save(jpg_path, quality=output_quality)
                print(f"Succès : {base_name}.jpg avec la résolution {resolution}")
            except Exception as e:
                print(f"Échec : {base_name}.jpg avec la résolution {resolution} - {e}")

            # Chemin pour enregistrer le fichier WebP
            webp_path = os.path.join(resolution_directory, f"{base_name}.webp")
            # Enregistrer l'image en format WebP avec la qualité spécifiée
            try:
                img.save(webp_path, "WEBP", quality=output_quality)
                print(f"Succès : {base_name}.webp avec la résolution {resolution}")
            except Exception as e:
                print(f"Échec : {base_name}.webp avec la résolution {resolution} - {e}")


# Fonction pour traiter toutes les images dans le dossier par défaut
def process_all_images(default_directory, output_quality, resolutions, final_directory):
    # Lister tous les fichiers dans le dossier 'default'
    for file in os.listdir(default_directory):
        # Vérifier si le fichier est une image JPG
        if file.lower().endswith(('.jpg', '.png', '.webp')):
            # Chemin complet vers le fichier image
            image_path = os.path.join(default_directory, file)
            # Convertir l'image avec les paramètres donnés
            convert_image(image_path, output_quality,
                          resolutions, final_directory)


# Obtenir le chemin du répertoire où se trouve le script
current_directory = os.getcwd()
print(current_directory)

# Définir les chemins des dossiers 'default' et 'final'
default_directory = os.path.join(current_directory, 'default')
final_directory = os.path.join(current_directory, 'final')

# Définir la qualité de sortie pour les images converties (entre 0 et 100)
output_quality = 80

# Résolutions désirées (en pixels)
desired_resolutions = [320, 480, 640, 1280, 1920]

# Lancer le traitement de toutes les images JPG dans le dossier 'default'
process_all_images(default_directory, output_quality,
                   desired_resolutions, final_directory)

# Pause finale pour éviter la fermeture de la fenêtre
input("Appuyez sur Entrée pour fermer la fenêtre...")
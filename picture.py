# Importer les modules nécessaires
from PIL import Image  # Pour manipuler les images
import os  # Pour interagir avec le système de fichiers

# Fonction pour convertir une image
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
            # Redimensionner l'image en gardant les proportions (on suppose une image carrée)
            img = img.resize((resolution, resolution), Image.Resampling.LANCZOS)
            
            # Chemin pour enregistrer le fichier JPG
            jpg_path = os.path.join(resolution_directory, f"{base_name}.jpg")
            # Enregistrer l'image en format JPG avec la qualité spécifiée
            img.save(jpg_path, quality=output_quality)
            
            # Chemin pour enregistrer le fichier WebP
            webp_path = os.path.join(resolution_directory, f"{base_name}.webp")
            # Enregistrer l'image en format WebP avec la qualité spécifiée
            img.save(webp_path, "WEBP", quality=output_quality)

# Fonction pour traiter toutes les images dans le dossier par défaut
def process_all_images(default_directory, output_quality, resolutions, final_directory):
    # Lister tous les fichiers dans le dossier 'default'
    for file in os.listdir(default_directory):
        # Vérifier si le fichier est une image JPG
        if file.lower().endswith('.jpg'):
            # Chemin complet vers le fichier image
            image_path = os.path.join(default_directory, file)
            # Convertir l'image avec les paramètres donnés
            convert_image(image_path, output_quality, resolutions, final_directory)

# Obtenir le chemin du répertoire où se trouve le script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Définir les chemins des dossiers 'default' et 'final'
default_directory = os.path.join(script_directory, 'default')
final_directory = os.path.join(script_directory, 'final')

# Définir la qualité de sortie pour les images converties (entre 0 et 100)
output_quality = 80

# Résolutions désirées (en pixels)
desired_resolutions = [1920, 1280, 840, 640, 480, 320]

# Lancer le traitement de toutes les images JPG dans le dossier 'default'
process_all_images(default_directory, output_quality, desired_resolutions, final_directory)

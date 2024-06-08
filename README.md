# Application de Conversion d'Images

![Illustration de l'auteur](./img/pharallaxe.png)


Ce projet est une application Python qui permet de convertir des images JPG en différentes résolutions et de les enregistrer en formats JPG et WebP. Les images sont prises d'un dossier source et enregistrées dans des sous-dossiers selon les résolutions spécifiées.

## Licence
Ce projet est sous licence [Apache](./LICENSE).

## Contenu

- [Application de Conversion d'Images](#application-de-conversion-dimages)
  - [Licence](#licence)
  - [Contenu](#contenu)
  - [Fonctionnalités](#fonctionnalités)
  - [Prérequis](#prérequis)
  - [Structure du Projet](#structure-du-projet)
  - [Utilisation](#utilisation)
  - [Fonctionnement du Script](#fonctionnement-du-script)
    - [convert\_image()](#convert_image)
    - [process\_all\_images()](#process_all_images)
  - [Exemple](#exemple)

## Fonctionnalités

- **Redimensionnement d'images** : Convertit les images à différentes résolutions.
- **Formats multiples** : Enregistre les images en formats JPG et WebP.
- **Gestion des dossiers** : Crée des sous-dossiers pour chaque résolution dans un dossier de destination.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine ainsi que les modules suivants :

- [Pillow](https://python-pillow.org/) : Pour manipuler les images.

Vous pouvez installer Pillow via pip :
```bash
pip install pillow
```

## Structure du Projet
```bash
.
├── default/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── final/
│   └── (images converties seront ici)
└── script.py
```

- **default/** : Contient les images JPG d'origine.
- **final/** : Les images converties sont enregistrées dans ce dossier.
- **script.py** : Le script Python principal qui gère la conversion des images.

## Utilisation
1) Préparation :

   - Placez vos images JPG dans le dossier "default".
   - Assurez-vous que le dossier final existe ou sera créé automatiquement.

2) Exécution du Script :

- Lancez le script script.py depuis le terminal ou votre environnement Python préféré :
```bash
python script.py
```
Ou un simple double-clic sur le script python dans le dossier.

3) Résultats :

- Les images converties seront enregistrées dans des sous-dossiers dans final/, chaque sous-dossier correspondant à une résolution.

## Fonctionnement du Script

### convert_image()
```python
convert_image(image_path, output_quality, resolutions, final_directory)
```

Cette fonction prend les paramètres suivants :

- image_path : Chemin de l'image à convertir.
- output_quality : Qualité de l'image de sortie (entre 0 et 100).
- resolutions : Liste des résolutions désirées.
- final_directory : Chemin du dossier où les images converties seront enregistrées.

Actions :

- Ouvre l'image spécifiée.
- Redimensionne l'image à chaque résolution indiquée.
- Enregistre l'image redimensionnée en formats JPG et WebP dans des sous-dossiers selon la résolution.

### process_all_images()
```python
process_all_images(default_directory, output_quality, resolutions, final_directory)
```

Cette fonction prend les paramètres suivants :

- default_directory : Dossier contenant les images d'origine.
- output_quality : Qualité de l'image de sortie.
- resolutions : Liste des résolutions désirées.
- final_directory : Chemin du dossier où les images converties seront enregistrées.

Actions :

- Parcourt tous les fichiers du dossier default.
- Vérifie si les fichiers sont des images JPG.
- Appelle convert_image pour chaque image JPG.


## Exemple
Supposons que vous ayez une image image1.jpg dans le dossier default, et que vous ayez défini les résolutions suivantes : [1920, 1280, 840, 640, 480, 320]. Après l'exécution du script, la structure du dossier final ressemblera à ceci :

```bash
python
Copier le code
final/
├── 1920/
│   ├── image1.jpg
│   └── image1.webp
├── 1280/
│   ├── image1.jpg
│   └── image1.webp
...
```

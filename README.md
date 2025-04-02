# Projet Malaria-IA

## Description
Malaria-IA est un projet d'intelligence artificielle visant à faciliter le diagnostic du paludisme (malaria) à partir d'images microscopiques de cellules sanguines. Ce système utilise des techniques de vision par ordinateur et d'apprentissage profond pour identifier les cellules infectées par le parasite Plasmodium, responsable du paludisme.

## Problématique
Le paludisme reste l'une des maladies infectieuses les plus meurtrières au monde, particulièrement dans les régions tropicales et subtropicales. Le diagnostic rapide et précis est crucial pour un traitement efficace, mais il nécessite souvent l'expertise de techniciens qualifiés, qui peuvent être rares dans les zones les plus touchées. Ce projet vise à créer un outil d'aide au diagnostic accessible et fiable pouvant être utilisé même dans des environnements à ressources limitées.

## Objectifs
- Développer un modèle d'IA capable de distinguer les cellules sanguines infectées par le paludisme des cellules saines
- Atteindre une précision élevée pour minimiser les faux positifs et les faux négatifs
- Créer une interface simple permettant l'utilisation du système par du personnel médical avec une formation minimale
- Permettre un déploiement dans des environnements à ressources limitées

## Technologies utilisées
- **Python** : Langage de programmation principal
- **TensorFlow/Keras** : Frameworks pour la création et l'entraînement des modèles de deep learning
- **OpenCV** : Bibliothèque pour le traitement d'images
- **Scikit-learn** : Outils pour l'analyse des données et l'évaluation des modèles
- **Matplotlib/Seaborn** : Visualisation des données et des résultats
- **Flask/Streamlit** : Développement de l'interface utilisateur web

## Structure du projet
```
Malaria-IA/
├── data/
│   ├── raw/              # Images microscopiques brutes
│   └── processed/        # Images prétraitées pour l'entraînement
├── models/               # Modèles entraînés et checkpoints
├── notebooks/            # Jupyter notebooks pour l'exploration et le développement
├── src/
│   ├── data/             # Scripts pour le chargement et le prétraitement des données
│   ├── features/         # Scripts pour l'extraction de caractéristiques
│   ├── models/           # Définition et entraînement des modèles
│   └── visualization/    # Code pour la visualisation des résultats
├── tests/                # Tests unitaires et d'intégration
├── app/                  # Application web pour l'interface utilisateur
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
```

## Installation et configuration

### Prérequis
- Python 3.8 ou supérieur
- Pip (gestionnaire de paquets Python)
- Git

### Étapes d'installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/DahliaNoir71/Malaria-IA.git
   cd Malaria-IA
   ```

2. Créer et activer un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Télécharger les données (si non incluses dans le dépôt) :
   ```bash
   python src/data/download_data.py
   ```

## Utilisation

### Prétraitement des données
```bash
python src/data/preprocess.py
```

### Entraînement du modèle
```bash
python src/models/train_model.py
```

### Évaluation du modèle
```bash
python src/models/evaluate_model.py
```

### Lancement de l'interface utilisateur
```bash
python app/run.py
```
Après le lancement, l'interface sera accessible à l'adresse http://localhost:5000

## Performances du modèle
- Précision : ~95%
- Sensibilité : ~94%
- Spécificité : ~96%
- Score F1 : ~0.95

## Jeu de données
Le modèle est entraîné sur un ensemble de données public contenant des images microscopiques de cellules sanguines, classées comme "infectées" ou "non infectées". Le jeu de données comprend des milliers d'images permettant un apprentissage robuste.

## Contributions
Les contributions sont les bienvenues ! Pour contribuer au projet :
1. Créez un fork du dépôt
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence
Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

## Contact
DahliaNoir71 - [Profil GitHub](https://github.com/DahliaNoir71)

Lien du projet : [https://github.com/DahliaNoir71/Malaria-IA](https://github.com/DahliaNoir71/Malaria-IA)

## Remerciements
- NIH (National Institutes of Health) pour le jeu de données public
- L'équipe de développement et les contributeurs
- Tous ceux qui travaillent pour éradiquer le paludisme dans le monde

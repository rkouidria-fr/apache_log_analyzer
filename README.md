# Projet d'Analyseur de Journaux
Ce projet combine la génération de journaux d'accès Apache et l'analyse
de ces journaux pour extraire des informations utiles.


## Installation

### Prérequis

- Python 3 doit être installé sur votre machine.

### 1. Clonez le dépôt :
   ```sh
   git clone <url-du-depot>
   cd log_analyzer_project
   ```

### 2. Installer les dépendances :
    ```sh
    python -m venv venv

    # Windows
    .\venv\Scripts\activate
    # Linux et macOS
    source venv/bin/activate

    pip install -r requirements.txt
    ```

### 3. A la fin de votre utilisation :
Pour quitter un environnement virtuel (venv), vous pouvez utiliser la commande suivante :

    ```sh
    deactivate
    ```

Cela désactivera l'environnement virtuel et vous ramènera à l'environnement système par défaut.

## Utilisation


1. Génération de Journaux fictifs
Exécutez le script pour générer des journaux d'accès fictifs :

    ``` sh
    python scripts/generate_logs.py
    ```

2. Analyse de Journaux
Exécutez le script pour analyser les journaux générés :

    ``` sh
    python scripts/analyze_logs.py
    ```

3. Exploration du résultat dans le dossier results


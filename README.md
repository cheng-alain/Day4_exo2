# Task Manager CLI

Un gestionnaire de tâches en ligne de commande avec fonctionnalités avancées.

## Fonctionnalités

- Ajouter, lister et supprimer des tâches
- Stockage des tâches dans un fichier JSON
- Gestion des sous-commandes via `argparse`
- Journalisation des actions
- Support des variables d'environnement
- Tests unitaires

## Installation

1. Clonez ce dépôt :
   ```
   git clone <url-du-dépôt>
   cd advanced_cli_task_manager
   ```

## Utilisation

### Ajouter une tâche

```
python3 -m task_manager.cli add "Description de la tâche" --priority 1
```

Priorités disponibles :
- 1 = Haute
- 2 = Moyenne (par défaut)
- 3 = Basse

### Lister toutes les tâches

```
python3 -m task_manager.cli list
```

### Supprimer une tâche

```
python3 -m task_manager.cli delete <id>
```

### Afficher l'aide

```
python3 -m task_manager.cli --help
```

## Variables d'environnement

- `TASKS_FILE_PATH` : Chemin vers le fichier JSON pour stocker les tâches (par défaut : `tasks.json`)

## Développement

### Exécuter les tests

```
python3 -m unittest discover tests
```

## Structure du projet

```
advanced_cli_task_manager/
│── task_manager/         # Code source de l'outil CLI
│   │── __init__.py
│   │── cli.py            # Point d'entrée CLI
│   │── core.py           # Logique principale
│   │── logger.py         # Configuration de la journalisation
│   │── config.py         # Gestion de la configuration
│── tests/                # Tests unitaires
│   │── test_core.py
│── tasks.json            # Fichier JSON pour stocker les tâches
│── logs/                 # Dossier pour les fichiers de journalisation
│── README.md             # Documentation
```
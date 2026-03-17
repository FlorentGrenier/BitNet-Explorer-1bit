⚠️ Work in Progress

# 🔬 BitNet-Explorer: 1.58-bit Ternary Computing Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Microsoft BitNet](https://img.shields.io/badge/Model-BitNet--b1.58-red)](https://huggingface.co/microsoft/bitnet-b1.58-3B)

> **Experimental CLI to explore the future of frugal AI. Run LLMs on CPU using ternary weights {-1, 0, 1}.**

## 🌟 Overview

Following Microsoft's breakthrough paper *"The Era of 1-bit LLMs"*, this repository provides a lightweight sandbox to test the **BitNet b1.58** architecture. Unlike traditional models that rely on heavy floating-point multiplications, BitNet uses **ternary logic**, significantly reducing energy consumption and memory footprint while maintaining competitive performance.

### Key Features
- **Pure CPU Inference**: Optimized for standard processors, breaking the expensive GPU dependency.
- **Minimalist CLI**: A clean, interactive terminal interface using `Rich`.
- **Performance Monitoring**: Real-time tracking of RAM usage and generation speed.

## 🚀 Getting Started

### Installation
```bash
git clone [https://github.com/YOUR_USERNAME/BitNet-Explorer.git](https://github.com/YOUR_USERNAME/BitNet-Explorer.git)
cd BitNet-Explorer
pip install -r requirements.txt
```
Usage
Bash

python main.py

📊 BitNet vs. Standard LLMs (Expected Gains)
Metric	Standard (FP16/BF16)	BitNet (1.58-bit)	Improvement
Weight Representation	16 bits	1.58 bits (ternary)	~10x reduction
Hardware Ops	Matrix Multiplication	Addition/Subtraction	Massive Energy Saving
Memory (2B Model)	~4-5 GB	< 1 GB	🔥
⚠️ Research Disclaimer & Limitations

This repository is for research and educational purposes only. As highlighted by Microsoft:

    Language: Primarily optimized for English.

    Accuracy: May produce hallucinations or biased content.

    Sensitivity: Elevated defect rates for critical queries (e.g., elections).

    Safety: Not production-ready. Always verify critical information.

🤝 Contributing

This is an exploratory project. Feel free to open issues or PRs if you want to help benchmark new kernels or improve the CLI experience!

Inspired by the Microsoft Research Paper: "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits"


---

### 💡 Pourquoi ce README est efficace pour toi :

1.  **Les Badges :** Ça donne tout de suite un aspect "sérieux" et maintenu.
2.  **La Table de Comparaison :** Elle résume visuellement l'intérêt du projet sans avoir à lire tout le code.
3.  **La citation de Microsoft :** En citant l'article de recherche, tu montres que tu as fait ta veille technologique.
4.  **Le Disclaimer :** En reprenant les points sur les biais et les élections que nous avons vus, tu te protèges et tu montres ton éthique de développeur.

### Prochaine étape pour toi :
1.  Crée ton repo sur GitHub.
2.  Ajoute ce `README.md`.
3.  Ajoute ton fichier `requirements.txt`.
4.  Ajoute ton code `main.py` (celui qu'on a ébauché avec la librairie `bitnet`).

**Est-ce que tu veux que je te prépare aussi le script de "Benchmark" pour remplir la partie performance du README avec tes propres chiffres ?**


----
Celui-ci est ton "laboratoire". C'est là que tu mets en avant la rupture technologique.

    L'objectif : Tester les limites de l'inférence ternaire (-1, 0, 1).

    Contenu : * La CLI ultra-minimaliste.

        Des scripts de benchmark (RAM vs CPU).

        Une section "Observations" où tu listes honnêtement les biais et les limites linguistiques que tu as trouvés (comme le disclaimer de Microsoft).

    Ton argument : "Je défriche le futur de l'IA frugale.


⚠️ Important Disclaimer & Limitations

Ce projet est une implémentation à but de recherche. Le modèle BitNet b1.58 présente des caractéristiques spécifiques à prendre en compte :

    Biais & Langue : Principalement optimisé pour l'anglais ; peut refléter des biais présents dans les données d'entraînement.

    Fiabilité : Risque d'hallucinations, particulièrement sur des sujets sensibles (élections, médical, juridique).

    Usage : Non recommandé pour des applications commerciales critiques sans tests de sécurité approfondis (SFT/DPO supplémentaires).


TODO : C'est la question piège classique quand on travaille sur des projets de recherche qui sortent tout juste des labos !

Pour ton projet, la réponse courte est : Utilise le dépôt GitHub de Microsoft.

Voici pourquoi et comment faire la distinction :
1. Le projet PyPI (pip install bitnet)

C'est une implémentation non-officielle (communautaire).

    Avantage : Très simple à installer.

    Inconvénient : Elle peut être en retard sur les dernières recherches ou ne pas inclure les optimisations de kernels (le code bas niveau qui fait que c'est vraiment rapide) que Microsoft a développées. Pour un projet "Explorer", ça manque un peu de crédibilité.

2. Le repo GitHub microsoft/BitNet (L'Officiel)

C'est la source de vérité.

    Avantage : C'est ici que se trouvent les outils officiels pour convertir les modèles et les kernels d'inférence (en C++ et Python) qui permettent réellement de supprimer les multiplications.

    Le défi : C'est un peu plus complexe à installer car tu ne fais pas juste un pip install. Tu dois souvent cloner le repo et installer les dépendances locales.

🛠️ Ce que je te conseille pour ton Repo GitHub :

Pour avoir un projet qui a l'air vraiment sérieux (niveau ingénieur IA), utilise l'implémentation de Microsoft mais simplifie-la pour tes utilisateurs.

Dans ton main.py, voici comment tu devrais l'intégrer proprement :

Au lieu d'utiliser une bibliothèque tierce, tu vas cloner le dossier bitnet du repo Microsoft dans ton propre projet. Cela permet aux gens de voir exactement comment les couches BitLinear sont construites.

Voici la marche à suivre pour ton installation :

    Clone le repo Microsoft dans un coin : git clone https://github.com/microsoft/BitNet.git

    Copie le dossier contenant la logique du modèle (souvent nommé bitnet_llama ou similaire) dans ton projet.

    Dans ton requirements.txt, utilise les versions de bibliothèques recommandées par Microsoft (souvent des versions spécifiques de torch).

Pourquoi c'est mieux pour ton portfolio ?

Si tu utilises le repo de Microsoft, tu peux écrire dans ton README :

    "Built upon the official Microsoft Research implementation, ensuring architectural fidelity to the 1.58-bit ternary logic."

Ça montre que tu sais aller chercher l'information à la source (le repo officiel) plutôt que de te reposer sur un package PyPI dont on ne connaît pas forcément la maintenance.
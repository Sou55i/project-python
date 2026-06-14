# Module 03 — Le web et les APIs

Énormément de données vivent sur Internet. Ce module t'apprend à les **récupérer
automatiquement** : appeler une API, télécharger une page, en extraire des informations.

> Fichiers du module : `appeler_api.py`, `scraping.py`.
> ⚠️ Ces scripts ont besoin d'une **connexion Internet** et des bibliothèques `requests`
> et `beautifulsoup4` (`pip install -r python/requirements.txt`).

---

## 1. Comment le web fonctionne (en 2 minutes)

Quand tu ouvres un site, ton navigateur fait une **requête** à un **serveur**, qui renvoie
une **réponse**. C'est le protocole **HTTP**. Une analogie : tu (le **client**) commandes
un plat à un serveur de restaurant ; il va en cuisine (le **serveur**) et te rapporte
l'assiette (la **réponse**).

Chaque requête vise une **URL** (l'adresse) et utilise une **méthode** :

| Méthode | Sert à | Analogie |
|---------|--------|----------|
| `GET` | **Récupérer** des données | « Donne-moi le menu » |
| `POST` | **Envoyer** des données | « Voici ma commande » |

La réponse contient un **code de statut** qui dit si ça s'est bien passé :

| Code | Signification |
|------|---------------|
| `200` | OK ✅ tout s'est bien passé |
| `404` | Not Found ❌ la page n'existe pas |
| `403` | Forbidden 🚫 accès interdit |
| `500` | erreur côté serveur 🔥 |

> 💡 Moyen mnémotechnique : **2xx** = succès, **3xx** = redirection, **4xx** = ta faute
> (mauvaise URL…), **5xx** = la faute du serveur.

---

## 2. C'est quoi une API ?

Une **API** (*Application Programming Interface*) est une porte d'entrée qu'un service web
ouvre **pour les programmes** (et non pour les humains). Au lieu d'une jolie page web, elle
renvoie des **données brutes**, presque toujours au format **JSON** (vu au module 02).

Exemple : tu demandes la météo à une API en visitant une URL, et elle te répond :

```json
{ "ville": "Paris", "temperature": 18, "ciel": "nuageux" }
```

Ton programme peut alors **lire** ce JSON et l'utiliser. C'est **la façon propre** de
récupérer des données : le service te les donne dans un format pensé pour les machines.

---

## 3. La bibliothèque `requests`

`requests` est **l'outil de référence** pour faire des requêtes HTTP en Python. Sa
simplicité est légendaire :

```python
import requests

reponse = requests.get("https://api.exemple.com/meteo")

print(reponse.status_code)   # 200 si tout va bien
donnees = reponse.json()     # convertit la réponse JSON en dictionnaire Python
print(donnees["temperature"])
```

Quelques réflexes importants :
- **Toujours vérifier** `status_code` (ou utiliser `reponse.raise_for_status()`) avant
  d'exploiter les données : peut-être que le serveur a renvoyé une erreur.
- **Mettre un délai** (`timeout=10`) pour ne pas attendre indéfiniment si le serveur ne
  répond pas.

---

## 4. Le scraping : lire une page web faite pour les humains

Quand un site **n'a pas d'API**, on peut quand même extraire des infos en lisant
directement son **HTML** (le code qui décrit la page). C'est le **web scraping**.

Le HTML est une structure de **balises** imbriquées :

```html
<h1>Titre de la page</h1>
<p class="prix">19,99 €</p>
```

La bibliothèque **BeautifulSoup** transforme ce texte HTML en une structure qu'on peut
fouiller facilement :

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
titre = soup.find("h1").text                 # le texte du 1er <h1>
prix = soup.find("p", class_="prix").text     # le <p class="prix">
```

> ⚖️ **Éthique et légalité du scraping** : vérifie les **conditions d'utilisation** du site
> et son fichier `robots.txt`. Ne surcharge pas un serveur (espace tes requêtes). Privilégie
> **toujours une API** si elle existe. Le scraping de données personnelles est encadré par
> la loi (RGPD en Europe).

---

## 5. La différence API vs scraping (à retenir)

| | API | Scraping |
|--|-----|----------|
| Format reçu | JSON propre, stable | HTML « brut », pensé pour l'affichage |
| Fiabilité | élevée (format garanti) | fragile (casse si le site change de design) |
| Quand l'utiliser | dès qu'elle existe ✅ | en dernier recours, si pas d'API |

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/03_web_apis/appeler_api.py
python3 python/automatisation/03_web_apis/scraping.py
```

Les scripts utilisent des sites publics **prévus pour l'entraînement**
(`open-meteo.com` pour l'API météo, `example.com` pour le scraping), donc tu peux les
lancer sans risque.

➡️ Module suivant : [`04_taches_scripts`](../04_taches_scripts/).

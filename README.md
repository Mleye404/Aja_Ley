# AJA LEY — Plateforme e-commerce

> **FOR EVERY MOOD. EVERY YOU.**

Plateforme e-commerce développée avec **Django** pour **AJA LEY**, une marque de mode féminine proposant des robes, ensembles, abayas et tenues de cérémonie.

Projet académique réalisé par **Mouhamadou Leye & Khady Ka** dans le cadre du **MILIA — École Polytechnique de Thiès**.

---

## 📌 À propos

L'objectif du projet est de proposer une plateforme permettant aux clientes de découvrir les collections AJA LEY, consulter les produits, renseigner leurs mensurations, constituer un panier et transmettre leur commande directement à la marque via WhatsApp.

Le projet constitue une **V1 fonctionnelle** pouvant évoluer par la suite vers une solution e-commerce plus complète.

---

## ✨ Fonctionnalités

- 🛍️ Catalogue de produits et catégories
- 📸 Galerie photos pour les produits
- 🏷️ Gestion des produits disponibles et en rupture de stock
- 🛒 Panier
- 📏 Mensurations associées à chaque article
- 👤 Commande avec ou sans compte
- 📦 Gestion des informations et frais de livraison
- 📱 Commande via WhatsApp
- 💳 Paiement manuel dans la V1
- 🔐 Authentification et gestion des comptes
- ⭐ Favoris
- ⚙️ Administration Django
- 📊 Dashboard de gestion
- 🌐 API REST
- 🇫🇷 / 🇬🇧 Interface multilingue
- 📱 Design responsive

---

## 🛒 Parcours client

```text
Boutique
   ↓
Produit
   ↓
Mensurations
   ↓
Panier
   ↓
Checkout
   ↓
Récapitulatif
   ↓
Commande
   ↓
WhatsApp
   ↓
Paiement manuel
````

Chaque article peut conserver ses propres mensurations, ce qui permet de commander plusieurs produits avec des mesures différentes.

---

## 🚚 Livraison

| Destination   |              Tarif |
| ------------- | -----------------: |
| Thiès         |         1 000 FCFA |
| Dakar         |         2 000 FCFA |
| Autres villes |       Configurable |
| International | Devis personnalisé |

---

## 🏗️ Architecture

```text
ajaley/
├── core/        # Pages principales
├── accounts/    # Comptes et authentification
├── products/    # Produits, catégories, images et API
├── cart/        # Panier et mensurations
├── orders/      # Checkout et commandes
├── payments/    # Structure du paiement
├── dashboard/   # Administration de la boutique
├── templates/   # Templates HTML
├── static/      # CSS, JavaScript et assets
└── media/       # Images des produits
```

---

## 🛠️ Technologies

* **Python**
* **Django 5.1.4**
* **Django REST Framework 3.15.2**
* **SQLite**
* **HTML / CSS / JavaScript**
* **Django Templates**
* **Django Admin**

---

## ⚙️ Installation

### 1. Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

Sous Windows :

```bash
venv\Scripts\activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Initialiser la base de données

```bash
python manage.py migrate
```

### 4. Charger les données AJA LEY

```bash
python manage.py seed_ajaley
```

### 5. Créer un administrateur

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

---

## 🔗 Accès

**Site :**

```text
http://127.0.0.1:8000/
```

**Administration Django :**

```text
http://127.0.0.1:8000/admin/
```

**Dashboard :**

```text
http://127.0.0.1:8000/dashboard/
```

**API produits :**

```text
http://127.0.0.1:8000/api/products/
```

---

## 📱 AJA LEY

**FOR EVERY MOOD. EVERY YOU.**

Instagram : [@ajaley.us](https://www.instagram.com/ajaley.us)

WhatsApp Sénégal : **+221 77 699 09 26**

WhatsApp International : **+1 317 319 9999**

---

## 👥 Équipe

**Mouhamadou Leye & Khady Ka**

**MILIA — École Polytechnique de Thiès**

---

© AJA LEY — Projet académique

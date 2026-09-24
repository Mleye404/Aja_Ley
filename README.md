**AJA LEY — Plateforme e-commerce (Django)**  
Projet académique réalisé par **Mouhamadou Leye** &  **Khady Ka** dans le cadre du MILIA  
   
 (École Polytechnique de Thiès), pour la marque de mode féminine **AJA LEY**.  
*FOR EVERY MOOD. EVERY YOU.*  
**1. Installation**  
python3 -m venv venv  
 source venv/bin/activate        # Windows : venv\Scripts\activate  
 pip install -r requirements.txt  
   
 python manage.py migrate  
 python manage.py seed_ajaley    # charge les catégories + les 14 vrais produits + leurs vraies photos  
 python manage.py createsuperuser  
 python manage.py runserver  
   
Le site est ensuite disponible sur http://127.0.0.1:8000/  
   
 L'admin Django sur http://127.0.0.1:8000/admin/  
   
 Le dashboard maison sur http://127.0.0.1:8000/dashboard/ (compte staff requis)  
   
 L'API REST sur http://127.0.0.1:8000/api/products/  
**2. Architecture**  
ajaley/  
 ├── core/        -> pages statiques (accueil, à propos, contact)  
 ├── accounts/    -> authentification, profil, adresses  
 ├── products/    -> catalogue, catégories, photos, favoris, API REST  
 ├── cart/        -> panier + mensurations par article (invitée ou connectée)  
 ├── orders/      -> checkout, adresse de livraison, frais, commandes  
 ├── payments/    -> paiement simulé (Wave / Orange Money)  
 ├── dashboard/   -> tableau de bord administrateur  
 ├── templates/   -> tous les templates HTML (héritage de base.html)  
 ├── static/      -> CSS, logo, photo de Khadija  
 └── media/       -> photos produits uploadées (chargées par seed_ajaley au démarrage)  
   
**3. Parcours client **  
Boutique → Produit → Ajouter au panier → Mensurations → Panier → Checkout  
   
 (infos + adresse) → Choix Wave / Orange Money → Paiement simulé → Confirmation.  
Chaque article du panier conserve **ses propres mensurations** (poitrine, taille,  
   
 hanches, épaules, longueur souhaitée, longueur des manches).  
**4. Comptes de test**  
- **Admin Django** : créé via createsuperuser (voir ci-dessus).  
- Les clientes peuvent commander en tant qu'invitées ou créer un compte  
   
 via /compte/inscription/ (entièrement optionnel).  
**5. Frais de livraison**  
Thiès : 1 000 FCFA · Dakar : 2 000 FCFA · autres villes du Sénégal : administrables  
   
 depuis Django Admin (ShippingRate) · international : devis personnalisé via WhatsApp.  
**6. Paiement**  
Le paiement (Wave / Orange Money) est **simulé** pour cette première version  
   
 (modèle Payment avec statuts PENDING / PAID / FAILED / CANCELLED).  
   
 L'architecture permet de brancher les vraies API plus tard sans refaire le  
   
 système de commandes.  
**7. Multilingue**  
FR (langue principale) / EN, activable via le bouton FR|EN dans la topbar.  
   
 Les chaînes sont préparées avec {% trans %} ; pour générer les traductions :  
python manage.py makemessages -l en  
 python manage.py compilemessages  
   
**8. Versions**  
Le projet est testé avec **Django 5.1.4** et  **djangorestframework 3.15.2** (voir requirements.txt). N'installez pas une version de Django plus récente sans vérifier la compatibilité avec DRF au préalable — une version trop récente de Django peut casser DRF (erreur cc_delim_re).  
**9. Design — passe de finition (v2)**  
Cette version inclut une passe visuelle et responsive supplémentaire, en conservant  
   
 la structure et les fonctionnalités déjà en place :  
- **Hero** repensé façon campagne de mode (photo plus grande, mieux cadrée sur  
   
 Khadija, badge discret, respiration accrue autour du texte).  
- **Notre histoire** utilise désormais khadija2.jpeg.  
- **Nos collections** affiche une vraie photo produit par catégorie (Robes,  
   
 Ensembles, Abayas, Cérémonie) au lieu d'un bloc vide.  
- **Icônes** de la navbar et des « avantages » remplacées par des SVG discrets  
   
 (au lieu d'émojis).  
- **Menu mobile** fonctionnel (bouton hamburger, panneau avec recherche,  
   
 navigation, WhatsApp) — géré par static/js/main.js.  
- Le bouton flottant est désormais un vrai bouton **WhatsApp** (icône  
   
 téléphone), plus aucun faux bouton de « chat ».  
- Passe responsive complète : navbar, hero, collections, catalogue, fiche  
   
 produit, galerie, panier, formulaires et checkout ont été vérifiés sur  
   
 mobile (~390px), tablette et desktop.  
Pour régénérer les photos de catégories après un flush de la base, relancer  
   
 simplement :  
python manage.py seed_ajaley  
   
**11. Correctif menu mobile (v3)**  
Le menu mobile a été entièrement reconstruit avec un système plus robuste :  
   
 un panneau plein écran en overlay (glissant depuis la droite, fond assombri  
   
 en arrière-plan), totalement indépendant du flux normal de la page — au lieu  
   
 d'un menu déroulant intégré qui pouvait mal s'afficher selon les navigateurs.  
   
 Testé et vérifié sur mobile (390px), tablette (820px) et desktop (1920px).  
**13. Nouvelle palette (v4)**  
La palette a été entièrement revue pour un rendu plus premium et distinctif :  
- **Émeraude profond** (--violet dans le CSS) — couleur d'accent principale  
   
 (CTA, liens actifs, icônes).  
- **Or antique** (--or) — bouton d'appel à l'action du Hero, touches  
   
 premium.  
- **Terracotta profond** (--bordeaux) — prix, badge « Rupture de stock ».  
- **Vert sapin quasi-noir** (--noir) — footer, titres, badge « Nouveau ».  
- **Ivoire chaud / champagne clair** (--creme, --ivoire, --rose-2) —  
   
 fonds.  
Cette combinaison émeraude + or contraste élégamment avec les couleurs  
   
 chaudes des vêtements (rose, moutarde, bordeaux, orange) et évite le rendu  
   
 « site e-commerce générique ». Toutes les couleurs restent centralisées dans  
   
 les variables CSS en haut de static/css/style.css — un seul endroit à  
   
 modifier pour tout changer à nouveau.  
**14. Notes**  
- Toutes les images utilisées (logo, photo de la propriétaire, 32 photos des  
   
 14 produits) sont les vrais assets fournis — aucune image générée ou  
   
 trouvée en ligne n'a été utilisée.  
- Les 5 produits en rupture de stock restent visibles dans le catalogue avec  
   
 un badge dédié et un bouton d'achat désactivé.  

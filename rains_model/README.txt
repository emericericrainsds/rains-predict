 A) Phase d'apprentissage/Modélisation:
    A partir de la base de données au format csv des informations météo journalières, une phase d'apprentissage automatique 
    est effectué afin de définir des modèles de prédiction:
        . Chaque ville a son propre modèle
        . Les predictions "pour le lendemain" (RainTommorow) ne se font que pour les "journées courantes sans pluie" (RainToday)

    Procedure de génération des modèles:
    des fichiers aux format 'ipynb ont été développés.
    Nous avons utilisé et nous recommandons "Google  Colab" pour sa simplicité de mise en oeuvre, sa souplesse et ses performance

    1) vous devez disposer d'un compte google et vous y connecter.

    2) copier le répertoire 'rains_model' dans votre 'google drive'
    https://drive.google.com/drive/my-drive
    à partir de la page web de votre 'google drive' rentrer dans ce répertoire et
    ouvrir le fichier 'Modelisation.ipynb' avec 'google colaboratory'.

    3) dans la rubrique 'Bibliothèque logicielle/Variables globales', modifier la variable 'g_['gdrive_path']'
    afin d'indiquer le path de 'rains_model' dans votre 'Google Drive'.

    4)Replier 'Bibliothèque logicielle' et lancer toutes ses cellules

    5) faites de même avec 'Audit, exploration et nettoyage des données'
    ... l'interface vous demandera de vous connecter à votre compte

    6) faites de même avec 'Entraînement et évaluation des modèle'

    ... Les modèles de prédictions sont généré dans le répertoire 'rains_model/modeles'

    Vous pouvez consulter les performances/résultats des modélisations dans:
    'Entraînement et évaluation des modèle/Passe 1/Modélisation/Résultats'

B) tests
    Le fichier 'ApplyModel.ipynb' permet de tester les modèles générés.

    1) L'ouvrir avec 'Google colaboratory'.

    2) Adapter le Google drive path comme précedement ('Drive')

    3) Executer toutes les cellules (Menu:Execution/tout executer)

    ... 'Test One Row': y:  [0]
                        RainTomorrow:  No

    ... 'Test on complete file': pour chaque ville (Excepté Newcastle suite pb non encore déterminé) une matrice de confusion 
    est calculée à partir de leur modèle propre et du fichier csv d'origine: 
    à comparer avec les résultats de Modelisation.ipynb: 'Entraînement et évaluation des modèle/Passe 1/Modélisation/Résultats'

   Exemple Adelaide:
   Test:
   LogisticRegression(max_iter=400, solver='newton-cg')
   vp= 76 fp= 24 vn= 689 fn= 67

    Suite Modélisation:
        yType 	tag_job 	DF_type 	methode 	   cross_valid 	sampled 	balanced_accuracy 	accuracy 	VP 	FP 	VN 	FN
   6 	yBool 	1P 	        AllNum 	  Logistic_regressionS 	False 	False 	    0.71 	           0.88 	    21 	8 	220 26

    ...etc

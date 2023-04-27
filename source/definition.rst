.. _definition.rst:

Définition d'une faille zéro day
################################
Dans cette partie nous allons définir ce qu'est, à proprement parler, une faille zéro day afin que cela soit clair lorsque nous utiliserons ce terme dans le travail.

Les vulnérabilités informatiques
==================================
Comment font les attaquants de systèmes informatiques pour leur porter atteinte ? Par quelle magie arrivent-ils à démarrer une voiture à distance, à voler tout ce qu'il y a sur un compte en banque ou encore à contrôler un ordinateur ?
Et bien il n'y a rien de mystérieux derrière ces manipulations mais plutôt une notion technique que nous appelons vulnérabilité (de "vulnerability" en anglais) ou plus communément faille.

Cette vulnérabilité est en réalité un point faible dans un système de type informatique. Elle peut se trouver dans un composant logiciel ou matériel, car la cause de celle-ci est une conception contenant des faiblesses.
Souvent, ces failles sont des défauts logiciels, donc de programmation.
Ainsi, ces problèmes liés au fonctionnement du logiciel sont normalement découverts, puis un correctif est mis en place. 
Ceci est une des raisons pour lesquelles les mises à jour de logiciels existent, afin de modifier l'anomalie du logiciel et aussi de protéger contre l'exploitation possible de cette vulnérabilité que nous nommons exploit.

Les particularités de la faille zéro day
====================================
Si une faille est découverte dans un logiciel, elle peut très bien se retrouver dans nombreux d'autres logiciels utilisant un code similaire ou même pareil.
C'est pourquoi il existe un nombre incalculable de failles connues dont les correctifs existent.
Ainsi, cela nous évite de rendre notre logiciel vulnérable à certaines attaques ou s'il l'est déjà, il est bien plus facile de corriger cette faiblesse.

Cependant, que se passe-t-il si cette faille est totalement inédite ? C'est à ce moment que nous parlons de faille zéro day.
En effet, une faille ou vulnérabilité zéro day a la particularité de ne pas avoir été découverte auparavant.
Il est alors assez évident qu'il n'existe pas encore de correctif pour cette anomalie logicielle et même l'éditeur du logiciel n'en connait pas encore l'existence.
Le terme "zéro day" ne qualifie pas la gravité de la faille, qui dépend fortement des cas mais plutôt le fait qu'à l'instant zéro, au "jour" zéro, au moment de la trouvaille, elle n'est pas identifiée par la sécurité informatique de l'éditeur.
Cette vulnérabilité existe, sans être reconnue.
Par conséquent, dès l'instant où la faille est déterminée et qu'un correctif est ou peut être mis en place, la vulnérabilité n'est plus considérée comme zéro day.

La dangerosité de ces failles réside bien évidemment dans le fait qu'elles peuvent être à tout moment exploitées par une personne malintentionnée puisqu'aucune correction n'est disponible à ce moment.
Il faut alors que ces erreurs soient identifiées et corrigées dans les plus brefs délais, sans quoi le système est vulnérable à des exploits zéro day.
Ces exploits sont des malwares développés par des cybercriminels qui exploitent cette vulnérabilité afin d'en tirer un certain profit.
Les différents types de profits seront abordés plus tard, dans un autre chapitre de ce travail.


La chronologie d'une faille zéro day
====================================
Certains chercheurs, notamment Leyla Bilge et Tudor Dumitras, se sont penchés précisément sur le déroulement général lors de l'exploitation d'une telle faille et ont noté la présence 
de sept étapes distinctes :cite:p:`titan:steps`:

1) L'introduction de la vulnérabilité
 L'éditeur du système introduit sans le vouloir une erreur dans celui-ci.
2) La publication du kit d'exploit zéro day
 Une personne mal intentionnée ayant des connaissances en informatique découvre la faille et prépare, de son côté, un kit complet
 permettant son exploitation, autrement dit un code d'exploitation alors que la vulnérabilité est encore ouverte (non corrigée).
3) La découverte de la faille 
 L'éditeur ou le développeur se rend compte de la vulnérabilité ainsi que de son exploitation.
 Puis, il l'identifie correctement.
4) La divulgation de la vulnérabilité
 Des chercheurs en sécurité informatique ou l'éditeur logiciel fait une annonce publique de la faille. 
 Cette étape peut se dérouler bien longtemps après la précédente car la réputation de l'entreprise est en jeu.
 Tout le monde en connait alors l'existence, cybercriminels et utilisateurs du système compris. 
5) La publication d'antivirus
 Les attaquants ont déjà créé l'exploit zéro day, mais la faille a été identifiée,
 alors les personnes éditant des antivirus se chargent de reconnaitre sa signature afin de créer la protection adéquate et de la publier.
 (Cependant les cybercriminels peuvent toujours essayer de trouver de nouveaux moyens permetttant d'exploiter la vulnérabilité dans le système)
6) La sortie d'un correctif
 Pour remédier à cette faille, l'éditeur du système publie un correctif.
 Cette étape prend plus ou moins de temps selon l'importance que les fournisseurs donnent à la vulnérabilité mais aussi selon 
 la difficulté de résolution du problème informatique.
7) Extension du correctif de sécurité 
 Le correctif se déploie théoriquement partout, chez tous les utilisateurs finaux.
 Le temps que prend cette étape est souvent bien long, car il faut que chaque utilisateur obtienne et applique le dispositif correcteur.
 En effet, dans le but de réduire la durée de cette étape, il faudrait que les individus utilisant un système activent les mises à jours automatiques pour celui-ci et
 prêtent toujours une certaine attention aux notifications recommandant des mises à jours. 
 

 






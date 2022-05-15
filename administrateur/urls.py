from os import name
from django.urls import path
from . import views


urlpatterns=[
    ############# abdo#####################################################
    path('home',views.home,name='home'),
    ############# gestion des formations#####################################################
    path('listeformations',views.listeformations,name='listeformations'),
    path('ajouterFor',views.ajouterFor,name='ajouterFor'),
    path('modifierFor/<int:id>',views.modifierFor,name='modifierFor'),
    path('supprimerFor/<int:id>',views.supprimerFor,name='supprimerFor'),
    ############# gestion des admins#####################################################
    path('listeadmins',views.listeadmins,name='listeadmins'),
    path('ajouteradd',views.ajouteradd,name='ajouteradd'),
    path('modifieradd/<int:id>',views.modifieradd,name='modifieradd'),
    path('supprimeradd/<int:id>',views.supprimeradd,name='supprimeradd'),

    ############# inass#####################################################
    ############################ Gestion These ########################################### 
    path('ajouterthese',views.ajouterthese,name='ajouterthese'),
    path('listethese',views.listethese,name='listethese'),
    path('supprimerthese/<int:id>',views.supprimerthese,name='supprimerthese'),
    path('modifierthese/<int:id>',views.modifierthese,name='modifierthese'),

    ############# salim#####################################################

    path('listeretudiant',views.listeretudiant,name='listeretudiant'),
    path('ajouterEtd',views.ajouterEtd,name='ajouterEtd'),
    path('modifierEtd/<id>',views.modifierEtd,name='modifierEtd'),
    path('supprimerEtd/<id>',views.supprimerEtd,name='supprimerEtd'),
    ############# assia#####################################################
    ############################ Gestion Encadrant ###########################################     
    path('listeEncadrants',views.listeEncadrants,name='listeEncadrants'),
    path('ajouterEncadrant',views.ajouterEncadrant,name='ajouterEncadrant'),
    path('modifierEncadrant/<int:id>',views.modifierEncadrant,name='modifierEncadrant'),
    path('supprimerEncadrant/<int:id>',views.supprimerEncadrant,name='supprimerEncadrant'),
    path('listeformationsEncadrant',views.listeformationsEncadrant,name='listeformationsEncadrant'),
]
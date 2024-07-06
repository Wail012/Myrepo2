from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfesseurDetailView
urlpatterns = [
    path('', views.welcome1,name='welcome1'),
    #path('', views.gestionwelcome),
    path('login',views.login,name="login"),
    path('ajout',views.ajouter,name="ajout"),
    path('ajouterprof',views.ajouterprof,name="ajouterprof"),
    path('ajouteretud',views.ajouteretud,name="ajouteretud"),
    path('afficherinfo',views.affichage,name="afficherinfo"),
    path('suppetud',views.suppetud,name="suppetud"),
    path('suppens',views.suppens,name="suppens"),
    path('modifetud1',views.modifetud1,name="modifetud1"),
    path('modifprof',views.modifprof,name="modifprof"),
    path('modifetud2',views.modifetud2,name="modifetud2"),
    path('modifprof2',views.modifprof2,name="modifprof2"),
    path('adminabs',views.adminabs,name="adminabs"),
    path('adminabs2',views.adminabs2,name="adminabs2"),
    path('suppabs/<int:myid>',views.suppabs,name="suppabs"),
    path('absetud',views.absetud,name="absetud"),
    path('noteprof',views.noteprof,name="noteprof"),
    path('noteprof2',views.noteprof2,name="noteprof2"),
    path('etudnote',views.etudnote,name="etudnote"),
    path('etudp',views.etudp,name="etudp"),
    path('profp',views.profp,name="profp"),
    path('subscription',views.subscription,name="subscription"),
    path('status',views.status,name="status"),
    path('adminsubs',views.adminsubs,name="adminsubs"),
    path('voirsubs/<int:myid>',views.voirsubs,name="voirsubs"),
    path('acceptersubs',views.acceptersubs,name="acceptersubs"),
    path('refusersubs',views.refusersubs,name="refusersubs"),
    path('ajoutclasse',views.ajoutclasse,name="ajoutclasse"),
    path('gestionemp',views.gestionemp,name="gestionemp"),
    path('gestionemp2',views.gestionemp2,name="gestionemp2"),
    path('etudemp',views.etudemp,name="etudemp"),
    path('welcomeadmin',views.welcomeadmin,name="welcomeadmin"),
    path('etudwelcome',views.etudwelcome,name="etudwelcome"),
    path('profwelcome',views.profwelcome,name="profwelcome"),
    path('subswelcome',views.subswelcome,name="subswelcome"),
    path('profemp',views.profemp,name="profemp"),
    path('<int:pk>/', ProfesseurDetailView.as_view(), name='professeur_detail'),

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
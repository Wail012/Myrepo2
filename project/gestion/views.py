from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  etudiant,professeur,admin1,absence,cours,note,classe,etudiant1,option,module,emp,notec2,enote,smodule,notemodule
from .forms import Etudiants,Prof,Abs,Note,Etudiants1,classe1,Note1
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Create your views here.
global user
def welcome1(request):
   return render(request,'gestion/welcome1.html')
def gestionwelcome(request):
    return render(request,'gestion/welcome.html')

def ajouter(request):
    
    return render(request, 'gestion/formulaire.html',{'x':3})






class ProfesseurDetailView(DetailView):
    model = professeur
    template_name = 'profp.html'  # Replace with your template name
    context_object_name = 'p'

def ajouteretud(request):
    Y=0
    if request.method=="POST":
      
      username=request.POST.get('CNE')
      etudiant1= etudiant.objects.filter(CNE=username)
      if etudiant1.exists() :
         Y=1
     #CNE= request.POST.get('CNE')
     # nom= request.POST.get('nom')
     #prenom= request.POST.get('prenom')
     #sexe= request.POST.get('sexe')
     #tel= request.POST.get('tel')
     #adresse= request.POST.get('adresse')
   #  anneebac= request.POST.get('annebac')
    # data = etudiant(CNE=CNE,nom=nom,prenom=prenom,sexe=sexe,tel=tel,email=email,adresse=adresse,anneebac=anneebac)
      else:
       Y=2
       Etudiants(request.POST).save()
    
    x={'et':Etudiants,'x':0,'y':Y}
    return render(request, 'gestion/formulaire.html',x)

def ajouterprof(request):
    Y=0
    if request.method=="POST":
       username=request.POST.get('CIN')
       prof1= professeur.objects.filter(CIN=username)
       if prof1.exists() :
         Y=3
       else:  
        p=Prof(request.POST,request.FILES)
        p.save()
        Y=4
    x={'et':Prof,'x':1,'y':Y}
    return render(request, 'gestion/formulaire.html',x)

def login(request):
  
   if request.method=="POST":
      username=request.POST.get(str('username'))
      password=request.POST.get(str('password'))
      etudiant2= etudiant.objects.filter(CNE=username,nom=password)
      ad1= admin1.objects.filter(id1=username,nom=password)
      prof1= professeur.objects.filter(CIN=username,nom=password)
      etudins=etudiant1.objects.filter(CNE1=username,nom1=password)
      if etudiant2.exists() :
         R=1
        
         request.session['username1']=username
         request.session['role1']=R
         x={'data':etudiant1, 'f':1}
         return redirect(etudwelcome)
        
      if prof1.exists():
         R=2
         request.session['username1']=username
         request.session['role1']=R
         x={'data':prof1, 'f':2}
         return redirect(profwelcome)
           
      if ad1.exists():
          R=3
          request.session['username1']=username
          request.session['role1']=R
         
          return render(request,'gestion/welcome.html')   
      if etudins.exists():
          request.session['username1']=username
          return redirect(subswelcome)    
      else:
        messages.info(request,'Username or password is incorrect')
       
      
     
      
   return render(request, 'gestion/login.html')


def affichage(request):
    if  request.session['role1'] == 1:
     etudiant1= etudiant.objects.raw("SELECT * FROM gestion_etudiant WHERE CNE = %s",request.session['username1'])
     x={'data':etudiant1}
    else:
     prof1= professeur.objects.raw("SELECT * FROM gestion_professeur WHERE CIN = %s",request.session['username1'])
     x={'data':prof1}  
    return render(request, 'gestion/affiche1.html',x)

def suppetud(request):
    y=0
    if request.method=="POST":
      y=1
      username=request.POST.get("id")
      etudiant1= etudiant.objects.filter(CNE=username)
      if etudiant1.exists() :
         etudiant1.delete()

         y=2
    p={'x':y}

    return render(request, 'gestion/suppetud.html',p)

def suppens(request):
    y=0
    if request.method=="POST":
      y=1
      username=request.POST.get("id")
      prof1= professeur.objects.filter(CIN=username)
      if prof1.exists() :
         prof1.delete()

         y=2
    p={'x':y}

    return render(request, 'gestion/suppens.html',p)

def welcomeadmin(request):
   return render(request, 'gestion/welcome.html')

def etudwelcome(request):
   e=etudiant.objects.get(CNE=request.session['username1'])
   return render(request, 'gestion/affiche1.html',{'e':e})

def profwelcome(request):
   e=professeur.objects.get(CIN=request.session['username1'])
   return render(request, 'gestion/affiche2.html',{'e':e})

def subswelcome(request):
   e=etudiant1.objects.get(CNE1=request.session['username1'])
   return render(request, 'gestion/subscription1.html',{'e':e})



def modifetud1(request):
   x=0
   if request.method=="POST":
       x=1
       username=request.POST.get('id')
      
       user1=request.POST.get('id')
       etudiant1= etudiant.objects.filter(CNE=username)
       
       if etudiant1.exists() :
        global val
        def val():
           return user1
        return redirect(modifetud2)

   p={'x':x}   
   return render(request, 'gestion/modifetud1.html',p)


def modifprof(request):
   x=0
   if request.method=="POST":
       x=1
       username=request.POST.get('id')
      
       user1=request.POST.get('id')
       prof1= professeur.objects.filter(CIN=username)
       
       if prof1.exists() :
        request.session['profmodif']=user1
        
        return redirect(modifprof2)

   p={'x':x}   
   return render(request, 'gestion/modifprof1.html',p)


# def modifetud2(request):
#    x=0
#    if request.method=="POST":
#        x=1
#        user2=val()
#        etudiant1= etudiant.objects.get(pk=user2)
#        form=Etudiants(request.POST, instance=etudiant1)
#        form.save()
      
        

#    x={'et':Etudiants,'x':x}
#    return render(request, 'gestion/modifetud2.html',x)
def modifetud2(request):
   user2=val()
   user3=etudiant.objects.get(CNE=user2)
   option2=option.objects.all()
   classe2=classe.objects.all()
   x=0
   if request.method=="POST":
      x=1
      etud2=etudiant(CNE=request.POST['CNE'],nom=request.POST['nom'],prenom=request.POST['prenom'],sexe=request.POST['sexe'],option1=option.objects.get(nom=request.POST['option1']),tel=request.POST['tel'],
                     email=request.POST['email'],adresse=request.POST['adresse'],anneebac=request.POST['anneebac'],parcours=request.POST['parcours'],classe=classe.objects.get(num_classe=request.POST['classe']))
      etud2.save()
   return render(request, 'gestion/modifetud3.html',{'option':option2,'classe':classe2,'et':user3,'x':x})

def modifprof2(request):
   x=0
   if request.method=="POST":
       x=1
       
       prof1= professeur.objects.get(pk=request.session['profmodif'])
       form=Prof(request.POST,request.FILES, instance=prof1)
       form.save()
      
        

   x={'et':Prof,'x':x}
   return render(request, 'gestion/modifprof2.html',x)

def adminabs(request):
 x=0
 if request.method=="POST":
    x=1
    username=request.POST.get('id')
      
    user1=request.POST.get('id')
    etudiant1=etudiant.objects.filter(CNE=username)
       
    if etudiant1.exists() :
       request.session['useradminabs']=user1
       
      
       return redirect(adminabs2)
       


 p={'x':x}  
 return render(request, 'gestion/adminabs.html',p)

def adminabs2(request):
   abs=absence.objects.filter(num_et=request.session['useradminabs'])
   etud1=etudiant.objects.get(CNE=request.session['useradminabs'])
   module1=module.objects.filter(option=etud1.option1)
   cours1=cours.objects.all()
   x={'x':abs,'y':cours1,'m':module1}
   if request.method=="POST":
       
       execuse1=request.POST.get('execuse')
       
       #cours1=cours.objects.get(nom=request.POST.get('cours'))
       et=etudiant.objects.get(CNE=request.session['useradminabs'])
       form=absence(num_et=et,execuse=execuse1,cours=cours.objects.get(nom=request.POST.get('cours2')),date=request.POST.get('date1'))
       form.save()
   return render(request, 'gestion/adminabs2.html',x)

def suppabs(request, myid):
   abs= absence.objects.get(pk=myid)
   abs.delete()
   return redirect(adminabs2)

def absetud(request):

   user2=absence.objects.filter(num_et=request.session['username1'])

   x={'x':user2}
   return render(request, 'gestion/absetud.html',x)

# def noteprof(request):
#   x={'e':Note(request.POST)}
#   if request.method=="POST":
#      classe1=Note(request.POST)
#      selected_classe_id=classe1.data.get("num_classe")
#      request.session['cours1']=classe1.data.get("num_cours")
     
#      x={'p':etudiant.objects.filter(classe=selected_classe_id),'e':Note(request.POST)}
#      p=etudiant.objects.filter(classe=selected_classe_id)
#      global val22
#      def val22():
#       return p
#      for i in p:
        
#       print(i)
#      return redirect(noteprof2)
#   return render(request, 'gestion/noteprof1.html',x)

# def noteprof2(request):
#    x={'p':val22()}
#    if request.method=="POST":
#     for i in val22():
#       user1=etudiant.objects.get(pk=i.CNE)
#       prof1=professeur.objects.get(pk=request.session['username1'])
#       cours1=cours.objects.get(prof=prof1,nom=request.session['cours1'])
#       user2=classe.objects.get(num_classe=i.classe.num_classe)
      
#       user=note(num_et=user1,num_classe=user2,num_cours=cours1,note=request.POST.get(str(i.CNE)))
#       user.save()
#       print(request.POST.get(str(i.CNE)))

#    return render(request, 'gestion/noteprof2.html',x)

def noteprof(request):
   prof=professeur.objects.get(CIN=request.session['username1'])
   cours1=cours.objects.filter(prof=prof)
   modules1=module.objects.all()
   option1=option.objects.all()
   classe3=classe.objects.all()
   emp1=emp.objects.all()
   et=""
   if request.method=="POST":
      cl=int(request.POST.get('classe3'))
      cl1=classe.objects.get(pk=cl)
      c=request.POST.get('cours3')
      request.session['c3']=c
      request.session['ev']=request.POST.get('ev3')
      et=etudiant.objects.filter(classe=cl1)
      global val22
      def val22():
       return et
      return redirect(noteprof2)
      #request.session['et']=etudiant.objects.filter(classe=cl1)
   return render(request, 'gestion/noteprof1.html',{'c':cours1,'cl':classe3,'e':emp1,'p':prof.CIN,'l':et})

def noteprof2(request):
     et=val22()
     s=0
     if request.method=="POST":
      for i in et:
        
           user1=etudiant.objects.get(pk=i.CNE)
           prof1=professeur.objects.get(pk=request.session['username1'])
           cours1=cours.objects.get(prof=prof1,nom=request.session['c3'])
           user2=classe.objects.get(num_classe=i.classe.num_classe)
           if request.session['ev'] == "ct1":
            user=note(num_et=user1,num_classe=user2,num_cours=cours1,note=request.POST.get(str(i.CNE)))
           if request.session['ev'] == "ct2":
            user=notec2(num_et=user1,num_classe=user2,num_cours=cours1,note=request.POST.get(str(i.CNE)))
           if request.session['ev'] == "examen":
            user=enote(num_et=user1,num_classe=user2,num_cours=cours1,note=request.POST.get(str(i.CNE)))  
           user.save()
      # if request.session['ev'] == "examen":
      #    module1=module.objects.filter(option=user1.option1)
      #    cours2=cours.objects.get(prof=prof1,nom=request.session['c3'])
      #    for j in et:
      #      user1=etudiant.objects.get(pk=j.CNE)
           
      #      prof1=professeur.objects.get(pk=request.session['username1'])
      #      cours1=cours.objects.get(prof=prof1,nom=request.session['c3'])
      #      module2=module.objects.get(nom=cours1.module.nom)
      #      user2=classe.objects.get(num_classe=j.classe.num_classe)
      #      n1=note.objects.get(num_et=user1,num_cours=cours1,num_classe=user2)
      #      n2=notec2.objects.get(num_et=user1,num_cours=cours1,num_classe=user2)
      #      n3=enote.objects.get(num_et=user1,num_cours=cours1,num_classe=user2)
      #      nm=notemodule(num_et=user1,num_cours=cours2,module=module2,num_classe=user2,note=((n1.note)*0.25+(n2.note)*0.25+(n3.note)*0.75))
      #      nm.save()
           
      # if request.session['c3'] == "applestore":       
      #     for j in et:
      #        user1=etudiant.objects.get(pk=j.CNE)
      #        s=0

     return render(request, 'gestion/noteprof2.html',{'p':et})    
                    
def etudnote(request):
   note1=note.objects.filter(num_et=request.session['username1'])
   note2=notec2.objects.filter(num_et=request.session['username1'])
   note3=enote.objects.filter(num_et=request.session['username1'])
   etud=etudiant.objects.get(CNE=request.session['username1'])
   module1=module.objects.filter(option=etud.option1)
   #sm=smodule.objects.all()
   

   return render(request, 'gestion/etudnote.html',{'p1':note1,'m':module1,'p2':note2,'p3':note3})
   
def etudp(request):
   etud=etudiant.objects.get(CNE=request.session['username1'])  
   return render(request, 'gestion/etudp.html',{'p':etud}) 

def profp(request):
   prof=professeur.objects.get(CIN=request.session['username1'])  
   return render(request, 'gestion/profp.html',{'p':prof}) 


def subscription(request):
   x=0
   if request.method=="POST":
       username=request.POST.get('CNE1')
      
       etud2=etudiant.objects.filter(CNE=username)
       if etud2.exists():
          x=1
       else:
          x=2
          CNE1 = request.POST['CNE1']
          nom2 = request.POST['nom1']
          prenom1 = request.POST['prenom1']
          sexe1 = str(request.POST['sexe1'])
          tel1 = request.POST['tel1']
          email1 = request.POST['email1']
          adresse1 = request.POST['adresse1']
          anneebac1 = request.POST['anneebac1']
          option11_id = request.POST['option11']
          classe1_id = request.POST['classe1']
          status ="pending"
          parcours2=request.POST.get('parcours1')
          etudiant3 = etudiant1(
            CNE1=CNE1,
            nom1=nom2,
            prenom1=prenom1,
            sexe1=sexe1,
            tel1=tel1,
            email1=email1,
            adresse1=adresse1,
            anneebac1=anneebac1,
            option11_id=option11_id,
            classe1_id=classe1_id,
            status=status,
            parcours1=parcours2

        )
          etudiant3.save()

   x={'x':x,'classes':classe.objects.all(),'options':option.objects.all()}       
   return render(request, 'gestion/subscription.html',x)

def status(request):
   etud=etudiant1.objects.get(CNE1=request.session['username1'])
   return render(request, 'gestion/status.html',{'et':etud})

def adminsubs(request):
   subs=etudiant1.objects.filter(status="pending")
   return render(request,'gestion/adminsubs.html',{'subs':subs})


def voirsubs(request, myid):
   etud=etudiant1.objects.get(CNE1=myid)
   request.session['idsubs']=myid
   return render(request,'gestion/voirsubs.html',{'p':etud})
   

def acceptersubs(request):
   etud1=etudiant1.objects.get(CNE1=request.session['idsubs'])
   etud1.status="accepted"
   etud1.save()
   etud3=etudiant(
   CNE = etud1.CNE1,
   nom =etud1.nom1,
   prenom = etud1.prenom1,
   sexe = etud1.sexe1,
   tel = etud1.tel1,
   email = etud1.email1,
   adresse = etud1.adresse1,
   anneebac = etud1.anneebac1,
   option1 = etud1.option11,
   classe = etud1.classe1,
   parcours=etud1.parcours1
   )
   etud3.save()
   return redirect(adminsubs)

def refusersubs(request):
    etud1=etudiant1.objects.get(CNE1= request.session['idsubs'])
    etud1.status="declined"
    etud1.save()
    return redirect(adminsubs)


def ajoutclasse(request):
   Y=0
   if request.method=="POST":
       user=request.POST.get('num_classe')
       classe2= classe.objects.filter(num_classe=user)
       if classe2.exists() :
         Y=3
       else:  
        classe1(request.POST).save()
        Y=4
   x={'et':classe1,'x':1,'y':Y}
   return render(request,'gestion/ajoutclasse.html',x)


def gestionemp(request):
   x={'e':Note1}
   if request.method=="POST":
      classe1=Note1(request.POST).data.get("num_classe")
      request.session['classe3']=classe1

      return redirect(gestionemp2)
   return render(request,'gestion/gestionemp.html',x)

def gestionemp2(request):
   if request.method=="POST":
      a=str(request.POST.get('cours1'))
      b=str(request.POST.get('cours2'))
      c=str(request.POST.get('cours3'))
      d=str(request.POST.get('cours4'))
      e=str(request.POST.get('cours5'))
      f=str(request.POST.get('cours6'))
      return gestionemp3(a,b,c,d,e,f,request)
   #emp1=emp.objects.get(num_classe=request.session['classe3'])
   classe3=classe.objects.get(num_classe=request.session['classe3'])
   module2=module.objects.filter(option=classe3.num_opt)
   
   user3=cours.objects.all()
   x={'e':module2,'c':user3}
   return render(request,'gestion/gestionemp2.html',x)

def gestionemp3(a,b,c,d,e,f,request):
   p=0
   print(a)
   print(b)
   a1=cours.objects.get(nom=a)
   b1=cours.objects.get(nom=b)
   c1=cours.objects.get(nom=c)
   d1=cours.objects.get(nom=d)
   e1=cours.objects.get(nom=e)
   f1=cours.objects.get(nom=f)
   classe3=classe.objects.get(num_classe=request.session['classe3'])
   emp2=emp.objects.all()
   emp3=emp.objects.filter(num_classe=request.session['classe3'])
   if emp3.exists():
       emp3=emp.objects.get(num_classe=request.session['classe3'])
   for i in emp2:
      if (i.prof1 == a1.prof.CIN or i.prof2 == b1.prof.CIN or i.prof3 == c1.prof.CIN or i.prof4 == d1.prof.CIN or i.prof5 == e1.prof.CIN or i.prof6 == f1.prof.CIN) and i != emp3:
         p=1
   if p == 0:      
    emp1=emp(num_classe=classe3,cours1=a,cours2=b,prof1=a1.prof.CIN,prof2=b1.prof.CIN,cours3=c,cours4=d,prof3=c1.prof.CIN,prof4=d1.prof.CIN,cours5=e,cours6=f,prof5=e1.prof.CIN,prof6=f1.prof.CIN)
    emp1.save()
    p=3
   module2=module.objects.filter(option=classe3.num_opt)
   user3=cours.objects.all()
   x={'e':module2,'c':user3,'x':p}
   return render(request,'gestion/gestionemp2.html',{'e':module2,'c':user3,'x':p})

def etudemp(request):
   etud=etudiant.objects.get(CNE= request.session['username1'])
   user=emp.objects.get(num_classe=etud.classe)

   return render(request,'gestion/etudemp.html',{'e':user})

def profemp(request):
   prof=professeur.objects.get(CIN= request.session['username1'])
   user=emp.objects.all()

   return render(request,'gestion/profemp.html',{'e':user,'p':int(request.session['username1'])})
from django.db import models
x=[(' homme','homme'),('femme','femme')]
y=[(' Bac+2','Bac+2'),(' Bac+3','Bac+3'),(' Bac+4','Bac+4'),(' Bac+5','Bac+5')]
n=[(' Premiere annee',' Premiere annee'),(' Deuxieme annee',' Deuxieme annee'),(' Troisieme annee',' Troisieme annee'),(' Quatrieme annee',' Quatrieme annee'),(' Cinquieme annee',' Cinquieme annee')]
# Create your models here.
class option(models.Model):
    nom=models.CharField(max_length=100, primary_key=True)

class classe(models.Model):
    num_classe=models.IntegerField(primary_key=True)
    num_opt=models.ForeignKey(option, on_delete=models.CASCADE)
    n_etude=models.CharField(max_length=40,choices=n)

class etudiant(models.Model):
    CNE=models.IntegerField(max_length=100, primary_key=True)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    sexe=models.CharField(max_length=10,choices=x)
    tel=models.IntegerField()
    email=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    anneebac=models.IntegerField()
    option1=models.ForeignKey(option, on_delete=models.CASCADE)
    classe=models.ForeignKey(classe, on_delete=models.CASCADE)
    parcours=models.CharField(max_length=10,choices=y)

class etudiant1(models.Model):
    CNE1=models.IntegerField(max_length=100, primary_key=True)
    nom1=models.CharField(max_length=100)
    prenom1=models.CharField(max_length=100)
    sexe1=models.CharField(max_length=10,choices=x)
    tel1=models.IntegerField()
    email1=models.CharField(max_length=100)
    adresse1=models.CharField(max_length=100)
    anneebac1=models.IntegerField()
    option11=models.ForeignKey(option, on_delete=models.CASCADE)
    classe1=models.ForeignKey(classe, on_delete=models.CASCADE)
    parcours1=models.CharField(max_length=10,choices=y)
    status=models.CharField(max_length=100)
    
class professeur(models.Model):
    CIN=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    sexe=models.CharField(max_length=10,choices=x)
    tel=models.IntegerField()
    email=models.CharField(max_length=100)
    titre=models.CharField(max_length=100)
    salaire=models.IntegerField() 
    file = models.FileField(upload_to='uploads/')    

class admin1(models.Model):
    id1=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=100) 

class module(models.Model):
    nom=models.CharField(max_length=100, primary_key=True)
    option=models.ForeignKey(option, on_delete=models.CASCADE)



class cours(models.Model):
    nom=models.CharField(max_length=100, primary_key=True)
    prof=models.ForeignKey(professeur, on_delete=models.CASCADE)
    module=models.ForeignKey(module, on_delete=models.CASCADE)

class absence(models.Model):
    num_abs=models.AutoField(primary_key=True)
    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    date=models.DateField()
    execuse=models.TextField()
    cours=models.ForeignKey(cours, on_delete=models.CASCADE)


   
class salle(models.Model):
    num_salle=models.IntegerField(primary_key=True)
    nplace=models.IntegerField()
   

from django.core.exceptions import ValidationError


class profsalle(models.Model):
    num_salle=models.ForeignKey(salle, on_delete=models.CASCADE)
    CIN=models.ForeignKey(professeur, on_delete=models.CASCADE)
    cours=models.ForeignKey(cours, on_delete=models.CASCADE)
    heure=models.IntegerField()

class note(models.Model):
    

    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    num_cours=models.ForeignKey(cours, on_delete=models.CASCADE)
    num_classe=models.ForeignKey(classe, on_delete=models.CASCADE)
    note=models.IntegerField()   

class notec2(models.Model):
    
    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    num_cours=models.ForeignKey(cours, on_delete=models.CASCADE)
    num_classe=models.ForeignKey(classe, on_delete=models.CASCADE)
    note=models.IntegerField()

class enote(models.Model):
    
    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    num_cours=models.ForeignKey(cours, on_delete=models.CASCADE)
    num_classe=models.ForeignKey(classe, on_delete=models.CASCADE)
    note=models.IntegerField()

class emp(models.Model):
    num_classe=models.ForeignKey(classe, on_delete=models.CASCADE,primary_key=True)
    cours1=models.CharField(max_length=100)
    cours2=models.CharField(max_length=100)
    prof1=models.IntegerField()
    prof2=models.IntegerField()
    cours3=models.CharField(max_length=100)
    cours4=models.CharField(max_length=100)
    prof3=models.IntegerField()
    prof4=models.IntegerField()
    cours5=models.CharField(max_length=100)
    cours6=models.CharField(max_length=100)
    prof5=models.IntegerField()
    prof6=models.IntegerField()

class notemodule(models.Model):
    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    num_cours=models.ForeignKey(cours, on_delete=models.CASCADE)
    num_classe=models.ForeignKey(classe, on_delete=models.CASCADE)
    module=models.ForeignKey(module, on_delete=models.CASCADE)
    note=models.IntegerField()

class smodule(models.Model):
    module=models.ForeignKey(module, on_delete=models.CASCADE)
    n=models.IntegerField()

class gmodule(models.Model):
    num_et=models.ForeignKey(etudiant, on_delete=models.CASCADE)
    module=models.ForeignKey(module, on_delete=models.CASCADE)
    note=models.IntegerField()
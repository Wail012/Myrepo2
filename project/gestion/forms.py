from django import forms
from .models import etudiant,professeur,absence,note,etudiant1,classe



class Etudiants(forms.ModelForm):
   class Meta:
      model=etudiant
      fields='__all__'
class Etudiants1(forms.ModelForm):
   class Meta:
      model=etudiant1
      fields='__all__'
class Prof(forms.ModelForm):
   class Meta:
      model=professeur
      fields='__all__'  
      

class Abs(forms.ModelForm):
   class Meta:
      model=absence
      fields=["date","execuse","cours"]

class Note(forms.ModelForm):
   class Meta:
      model=note
      fields=["num_classe","num_cours"]

class Note1(forms.ModelForm):
   class Meta:
      model=note
      fields=["num_classe"]      

class classe1(forms.ModelForm):
   class Meta:
      model=classe
      fields='__all__'  

      
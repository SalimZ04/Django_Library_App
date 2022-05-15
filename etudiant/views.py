from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages

# Create your views here.
def home(request):
    cursor=connection.cursor()
    cursor.execute('select * from formation')
    Formations=cursor.fetchall()
    cursor.close()
    return render(request,'etudiant/home.html',{'Formations':Formations})

def listethese(request,id):

    if request.method=='POST':
        titre=request.POST.get('titre')
        encadrent=request.POST.get('encadrent')
        cursor=connection.cursor()
        cursor.execute('select t.id,etd.id,e.id,concat(etd.nom," ",etd.prenom),concat(e.nom," ",e.prenom),t.titre from etudiant etd,encadrent e,these t where e.id=t.EncadrentID and etd.id=t.EtudiantID and e.FormationID="'+str(id)+'"  and t.titre like"'+str(titre)+'%" and concat(e.nom," ",e.prenom) like"'+str(encadrent)+'%"')
        theses=cursor.fetchall()
        cursor.close
        
        return render(request,'etudiant/listethese.html',{'theses':theses})

    cursor=connection.cursor()
    cursor.execute('select t.id,etd.id,e.id,concat(etd.nom," ",etd.prenom),concat(e.nom," ",e.prenom),t.titre,t.Contenu from etudiant etd,encadrent e,these t where e.id=t.EncadrentID and etd.id=t.EtudiantID and e.FormationID='+str(id))
    theses=cursor.fetchall()
    cursor.close
    cursor.execute('SELECT e.id,concat(e.nom," ",e.prenom) from encadrent e,formation f where f.id=e.FormationID and e.FormationID='+str(id))
    encadrents=cursor.fetchall()
    cursor.close
    return render(request,'etudiant/listethese.html',{'theses':theses,'encadrents':encadrents})

def these(request,id):
    cursor=connection.cursor()
    cursor.execute('select t.id,concat(etd.nom," ",etd.prenom),concat(e.nom," ",e.prenom),t.titre,t.date,t.duree,t.contenu,e.FormationID from etudiant etd,encadrent e,these t where e.id=t.EncadrentID and etd.id=t.EtudiantID and t.id='+str(id))
    these=cursor.fetchone()
    cursor.close
    return render(request,'etudiant/these.html',{'these':these})
from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages
from .models import These
# Create your views here.

############# abdo#####################################################

def home(request):
    return render(request,'administrateur/home.html')
                                        #gestion des formations
def listeformations(request):
    cursor=connection.cursor()
    cursor.execute('select * from formation')
    Formations=cursor.fetchall()
    return render(request,'administrateur/listeformations.html',{'Formations':Formations})

def ajouterFor(request):
    
    if request.method=='POST':
        nom=request.POST.get('nom')
        cursor=connection.cursor()
        cursor.execute('insert into formation (nom) VALUES ("'+nom+'")')
        return redirect('listeformations')

    return render(request,'administrateur/ajouterFor.html')

def modifierFor(request,id):

    if request.method=='POST':
        nom=request.POST.get('nom')
        cursor=connection.cursor()
        cursor.execute('update formation set nom="'+nom+'" where id='+str(id))
        return redirect('listeformations')

    cursor=connection.cursor()
    cursor.execute('select * from formation where id='+str(id))
    formation=cursor.fetchone()
    return render(request,'administrateur/modifierFor.html',{'formation':formation})

def supprimerFor(request,id):
    try:
        cursor=connection.cursor()
        cursor.execute('delete from formation where id='+str(id))
        return redirect('listeformations')
    except:
        messages.success(request,'Impossible de supprimer cet formation sans supprimer ses encadrant')
        return redirect('listeformations')
                                                
                                                #gestion des admins

def listeadmins(request):
    cursor=connection.cursor()
    cursor.execute('select * from admin')
    admins=cursor.fetchall()
    return render(request,'administrateur/listeadmin.html',{'admins':admins})

def ajouteradd(request):
    
    if request.method=='POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        cursor=connection.cursor()
        cursor.execute('insert into admin (nom,prenom,login,passwd) VALUES ("'+nom+'","'+prenom+'","'+login+'","'+mdp+'")')
        return redirect('listeadmins')

    return render(request,'administrateur/ajouteradd.html')

def modifieradd(request,id):

    if request.method=='POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        cursor=connection.cursor()
        cursor.execute('update admin set nom="'+nom+'",passwd="'+mdp+'",prenom="'+prenom+'",login="'+login+'" where id='+str(id))
        return redirect('listeadmins')

    cursor=connection.cursor()
    cursor.execute('select * from admin where id='+str(id))
    admin=cursor.fetchone()
    return render(request,'administrateur/modifieradd.html',{'admin':admin})

def supprimeradd(request,id):

    cursor=connection.cursor()
    cursor.execute('delete from admin where id='+str(id))
    return redirect('listeadmins')

############# inass#####################################################
###################### Gestion Des theses ########################
def ajouterthese(request):
    if request.method=='POST':
        EtudiantID=str(request.POST.get('etd'))
        EncadrentID=str(request.POST.get('encadrent'))
        Titre=request.POST.get('titre')
        Date=request.POST.get('date')
        Duree=str(request.POST.get('duree'))
        Contenu=request.POST.get('contenu')
        data=These(EtudiantID=EtudiantID,EncadrentID=EncadrentID,Titre=Titre,Date=Date,Duree=Duree,Contenu=Contenu)
        data.save()
        #cursor.execute('insert into these (EtudiantID,EncadrentID,Titre,Date,Duree,Contenu) VALUES ("'+etdID+'","'+encadrentID+'","'+titre+'","'+date+'","'+duree+'","'+contenu+'")')
        return redirect('listethese')

    cursor=connection.cursor()
    cursor.execute('select id,CONCAT(Nom," ",Prenom)from etudiant')
    etds=cursor.fetchall()
    cursor.execute('select id,CONCAT(Nom," ",Prenom) from encadrent')
    encadrents=cursor.fetchall()
    cursor.close()
    return render(request,'administrateur/ajouterthese.html',{'etds' :etds,'encadrents':encadrents})

def listethese(request):
    cursor=connection.cursor()
    cursor.execute('select T.ID,CONCAT(E.Nom," ",E.Prenom),CONCAT(N.Nom," ",N.Prenom),Titre,Date,Duree,Contenu  from etudiant E,encadrent N,these T where E.ID=T.EtudiantID and N.ID=T.EncadrentID')
    theses=cursor.fetchall()
    return render(request,'administrateur/listethese.html',{'theses':theses})

def supprimerthese(request,id):

    cursor=connection.cursor()
    cursor.execute('delete from these where id='+str(id))
    return redirect('listethese')

def modifierthese(request,id):
    if request.method=='POST':
        EtudiantID=request.POST.get('etd')
        EncadrentID=request.POST.get('encadrent')
        Titre=request.POST.get('titre')
        Date=request.POST.get('date')
        Duree=request.POST.get('duree') 
        Duree=str(Duree)
        Contenu=request.POST.get('contenu')
        data=These(id,EtudiantID=EtudiantID,EncadrentID=EncadrentID,Titre=Titre,Date=Date,Duree=Duree,Contenu=Contenu)
        data.save()
        #cursor.execute('update these set EtudiantID="'+etdID+'",EncadrentID="'+encadrentID+'",Titre="'+titre+'",Date="'+date+'",Duree="'+duree+'",Contenu="'+contenu+'" where id='+str(id))
        return redirect('listethese')

    cursor=connection.cursor()
    cursor.execute('select id,CONCAT(Nom," ",Prenom)from etudiant')
    etds=cursor.fetchall()
    cursor.execute('select id,CONCAT(Nom," ",Prenom) from encadrent')
    encadrents=cursor.fetchall()
    cursor.close()
    cursor=connection.cursor()
    cursor.execute('select CONCAT(E.Nom," ",E.Prenom),CONCAT(N.Nom," ",N.Prenom),Titre,Date,Duree,Contenu,E.id,N.id  from etudiant E,encadrent N,these T where E.ID=T.EtudiantID and N.ID=T.EncadrentID and T.ID='+str(id))
    ths=cursor.fetchone()
    date= ths[3].isoformat()
    return render(request,'administrateur/modifierthese.html',{'etds' :etds,'encadrents':encadrents,'ths' :ths,'date' :date})


############# salim#####################################################

def listeretudiant(request):
    cursor=connection.cursor()
    cursor.execute('select * from etudiant')
    Etudiants=cursor.fetchall()
    cursor.close()
    return render(request,'administrateur/listeretudiant.html',{'Etudiants':Etudiants})

def ajouterEtd(request):
    
    if request.method=='POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        tele=request.POST.get('tele')
        email=request.POST.get('email')
        cursor=connection.cursor()
        cursor.execute('insert into etudiant (nom,prenom,email,tele,login,passwd) VALUES ("'+nom+'","'+prenom+'","'+email+'","'+tele+'","'+login+'","'+mdp+'")')
        cursor.close()
        return redirect('listeretudiant')

    return render(request,'administrateur/ajouterEtd.html')

def modifierEtd(request,id):

    if request.method=='POST':
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        tele=request.POST.get('tele')
        email=request.POST.get('email')
        cursor=connection.cursor()
        cursor.execute('update etudiant set nom="'+nom+'",passwd="'+mdp+'",prenom="'+prenom+'",tele="'+tele+'",email="'+email+'",login="'+login+'" where id='+str(id))
        cursor.close()
        return redirect('listeretudiant')

    cursor=connection.cursor()
    cursor.execute('select * from etudiant where id='+str(id))
    etd=cursor.fetchone()
    return render(request,'administrateur/modifierEtd.html',{'etd':etd})

def supprimerEtd(request,id):
    try:
        cursor=connection.cursor()
        cursor.execute('delete from etudiant where id='+str(id))
        return redirect('listeretudiant')
    except:
        messages.success(request,'Impossible de supprimer cet étudiant sans supprimer ses thèses')
        return redirect('listeretudiant')
############# assia#####################################################
###################### Gestion Des encadrants ########################
def listeformationsEncadrant(request):
    cursor=connection.cursor()
    cursor.execute('select * from formation')
    FormationPourEncadrant=cursor.fetchall()
    return render(request,'encadrant/ajouterEncadrant.html',{'FormationPourEncadrant':FormationPourEncadrant})

def listeEncadrants(request):
    cursor=connection.cursor()
    cursor.execute('select * from encadrent e inner join formation f where e.FormationID=f.ID')
    Encadrants=cursor.fetchall()
    return render(request,'encadrant/listeEncadrants.html',{'Encadrants':Encadrants})

def ajouterEncadrant(request):
    
    if request.method=='POST':
        idFormation=request.POST.get('idFormation')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        email=request.POST.get('email')
        tele=request.POST.get('tele')
        cursor=connection.cursor()
        cursor.execute('insert into encadrent(FormationID,Nom,Prenom,Email,Tele) VALUES ("'+idFormation+'","'+nom+'","'+prenom+'","'+email+'","'+tele+'")')
        return redirect('listeEncadrants')
    cursor1=connection.cursor()
    cursor1.execute('select * from formation')
    FormationPourEncadrant=cursor1.fetchall()
    return render(request,'encadrant/ajouterEncadrant.html',{'FormationPourEncadrant':FormationPourEncadrant})


    #return render(request,'encadrant/ajouterEncadrant.html')

def modifierEncadrant(request,id):

    if request.method=='POST':
        idFormation=request.POST.get('idFormation')
        nomEnc=request.POST.get('nomEnc')
        prenomEnc=request.POST.get('prenomEnc')
        tele=request.POST.get('tele')
        email=request.POST.get('email')
        cursor=connection.cursor()
        cursor.execute('UPDATE `encadrent` SET `FormationID`="'+idFormation+'",`Nom`="'+nomEnc+'",`Prenom`="'+prenomEnc+'",`Email`="'+email+'",`Tele`="'+tele+' " where id='+str(id))
        return redirect('listeEncadrants')

    cursor=connection.cursor()
    cursor.execute('select * from encadrent e inner join formation f where e.FormationID=f.ID and e.id='+str(id))
    Encadrant=cursor.fetchone()
    cursor1=connection.cursor()
    cursor1.execute('select * from formation')
    FormationPourEncadrant=cursor1.fetchall()
    return render(request,'encadrant/modifierEncadrant.html',{'Encadrant':Encadrant,'FormationPourEncadrant':FormationPourEncadrant})

def supprimerEncadrant(request,id):
    try:
        cursor=connection.cursor()
        cursor.execute('delete from encadrent where id='+str(id))
        return redirect('listeEncadrants')
    except:
        messages.success(request,'Impossible de supprimer cet encadrent sans supprimer ses thèses')
        return redirect('listeEncadrants')
from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'login/home.html')

def loginadd(request):

    if request.method=='POST':
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        cursor=connection.cursor()
        cursor.execute('select * from admin where login="'+login+'" and passwd="'+mdp+'"')
        admin=cursor.fetchone()
        if not(admin):
            messages.success(request,'Login ou Mot de passe Invalide')
            return render(request,'login/loginadd.html')
        else:
            request.session['id'] = admin[0]
            request.session['nom'] = admin[1]
            request.session['prenom'] = admin[2]
            request.session['login'] = admin[3]
            request.session['mdp'] = admin[4]
            return redirect('administrateur/home')
            

    return render(request,'login/loginadd.html')

def loginetd(request):

    if request.method=='POST':
        login=request.POST.get('login')
        mdp=request.POST.get('mdp')
        cursor=connection.cursor()
        cursor.execute('select * from etudiant where login="'+login+'" and passwd="'+mdp+'"')
        admin=cursor.fetchone()
        if not(admin):
            messages.success(request,'Login ou Mot de passe Invalide')
            return render(request,'login/loginetd.html')
        else:
            request.session['id'] = admin[0]
            request.session['nom'] = admin[1]
            request.session['prenom'] = admin[2]
            request.session['email'] = admin[3]
            request.session['tele'] = admin[4]
            request.session['login'] = admin[5]
            request.session['mdp'] = admin[6]
            return redirect('etudiant/home')
            

    return render(request,'login/loginetd.html')

def DeconnecterEtd(request):
    request.session['id'] = ""
    request.session['nom'] = ""
    request.session['prenom'] = ""
    request.session['email'] = ""
    request.session['tele'] = ""
    request.session['login'] = ""
    request.session['mdp'] = ""
    return redirect('loginetd')


def DeconnecterAdd(request):
    request.session['id'] = ""
    request.session['nom'] = ""
    request.session['prenom'] = ""
    request.session['login'] = ""
    request.session['mdp'] = ""
    return redirect('loginadd')
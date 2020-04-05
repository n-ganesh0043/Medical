from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View,DeleteView
from .models import diseasemodel,medicalmodels,Userregistrationmodel
# Create your views here.
def index(request):
    return render(request,"index.html")


class user_registration(View):
    def get(self,request):
        return render(request,"user_registration.html")
    def post(self,request):
        fn=request.POST.get('a1')
        ln=request.POST.get('a2')
        ag=request.POST.get('a3')
        gen=request.POST.get('a4')
        adr=request.POST.get('a5')
        un=request.POST.get('a6')
        psd=request.POST.get('a7')
        Userregistrationmodel(first_name=fn,last_name=ln,age=ag,gender=gen,address=adr,username=un,password=psd).save()
        messages.success(request,"registered successfullyy !!!!!!")
        return redirect('user_registration')


class adminpage(View):
    def get(self,request):
        return render(request,"admin.html")
    def post(self, request):
        un=request.POST.get('b1')
        ps=request.POST.get('b2')
        if un=='ganesh' and ps=='grpspk':
            return render(request,"adminhomepage.html")
        else:
            return render(request,"admin.html",{"mess":"invalid username or password!!!!!!! TRY AGAIN..."})

class disease_home_page(View):
    def get(self,request):
        ds=diseasemodel.objects.all()
        return render(request,"disease_home_page.html",{"data":ds})
    def post(self,request):
        des_nm=request.POST.get('b3')
        symt=request.POST.get('b4')
        diseasemodel(dis_name=des_nm,sysmtoms=symt).save()
        messages.success(request,"details submited successfully!!!!")
        return redirect('disease_home_page')


def delete_des(request):
    del_no=request.GET.get("dis_name")
    diseasemodel.objects.filter(dis_name=del_no).delete()
    return redirect('disease_home_page')


def update_des(request):
    i=request.POST['u1']
    res=diseasemodel.objects.get(id=i)
    return render(request,"des_update.html",{"data":res})


def updated_des(request):
    du=request.POST['u2']
    dst=request.POST['u3']
    diseasemodel.objects.filter(dis_name=du).update(sysmtoms=dst)
    return redirect('disease_home_page')


class medicene_page(View):
    def get(self,request):
        md=medicalmodels.objects.all()
        return render(request,"medicene_page.html",{"data":md})
    def post(self,request):
        de=request.POST.get('m1')
        sy=request.POST.get('m2')
        med=request.POST.get('m3')
        med_ds=request.POST.get('m4')
        medicalmodels(des_name=de,sysm=sy,med_name=med,med_desp=med_ds).save()
        messages.success(request,"details are saved successfully!!!!!!!!!!!!")
        return redirect('medicene_page')


def delete_med(request):
    dd=request.GET.get('id')
    medicalmodels.objects.filter(id=dd).delete()
    return redirect('medicene_page')


def update_med(request):
    mm=request.POST['m6']
    res=medicalmodels.objects.get(id=mm)
    return render(request,'med_update.html',{"data":res})


def updated_med(request):
    um=request.POST.get('m7')
    umd=request.POST.get('m8')
    medicalmodels.objects.filter(med_name=um).update(med_desp=umd)
    return redirect('medicene_page')


def reports_adm(request):
    md=medicalmodels.objects.all()
    return render(request,"reports_adm.html",{"data":md})


class user_login(View):
    def get(self,request):
       return render(request,"user_login.html")
    def post(self,request):
        un=request.POST.get('un1')
        ps=request.POST.get('un2')
        try:
          Userregistrationmodel.objects.get(username=un,password=ps)
          return render(request,"user_home_page.html",{"name":un})
        except Userregistrationmodel.DoesNotExist:
            messages.error(request,"invalid username or password !!!! dude.. [TRY AGAIN]")
            return redirect('user_login')


def report_usr(request):
    ur=Userregistrationmodel.objects.all()
    return render(request,"report_usr.html",{"data":ur})


class srch_med(View):
    def get(self,request):
        return render(request,"search_med.html")
    def post(self,request):
        print('1')
        ds=request.POST.get('dd1')
        print(ds)
        print('2')
        try:
            res=medicalmodels.objects.filter(des_name=ds)
            print(res)
            return render(request,"search_med.html",{"data":res})
        except medicalmodels.DoesNotExist:
            messages.error(request,'Invalid disease name please check and enter valid name!!!!')
            return redirect('srch_med')


class change_pswd(View):
    def get(self,request):
        return render(request,"change_password.html")
    def post(self,request):
        cu=request.POST.get('cp1')
        cp=request.POST.get('cp2')
        try:
            res=Userregistrationmodel.objects.get(username=cu,address=cp)
            return render(request,"change_password.html",{"success":res.password})
        except:
            messages.error(request,"invalid username or address please check again dude!!!!!!!!!!")
            return redirect('change_pswd')

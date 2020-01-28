from django.shortcuts import render,redirect
from .models import userlogin, project, task, message
from .forms import userloginform, addprojectform, addtaskform, messageform
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        typedata = request.POST.get("is_usertype")

        if username is not None and password is not None and email is not None:
            row = userlogin.objects.filter(username = username, password = password, email = email, is_usertype = typedata)

            if len(row) > 0:
                if typedata == "Manager":

                    request.session["username"] = row[0].empid
                    id = row[0].empid
                    return redirect("http://localhost:8000/manager/")
                elif typedata == "Employee":
                    request.session["username"] = row[0].empid
                    id = row[0].empid
                    return redirect("http://localhost:8000/employee/")


    form = userloginform()

    return render(request,"login.html", {'form': form})

@login_required()
def logout(request):
    del request.session["username"]

    return redirect("http://localhost:8000/")



@login_required()
def manager(request):
    PTname = request.POST.get('Pname')
    CTname = request.POST.get('Cname')
    CTdetails = request.POST.get('Cdetails')
    PTdescription = request.POST.get('Pdescription')
    PTdeadline = request.POST.get('Pdeadline')
    PTstartdate = request.POST.get('Pstartdate')
    PTmanagedby = request.POST.get('Pmanagedby')
    PTcontract = request.POST.get('Pcontract')
    PTtextresource = request.POST.get('Ptextresource')

    if PTname is not None and CTname is not None and CTdetails is not None and PTdescription is not None and PTdeadline is not None and PTstartdate is not None and PTmanagedby is not None and PTcontract is not None and PTtextresource is not None:
        new_object = project(Pstatus=0, Pname=PTname, Cname=CTname, Cdetails=CTdetails, Pdescription=PTdescription,
                             Pdeadline=PTdeadline, Pstartdate=PTstartdate, Pmanagedby=PTmanagedby, Pcontract=PTcontract,
                             Ptextresource=PTtextresource)
        new_object.save()

        return redirect("http://localhost:8000/manager/")

    fProject = addprojectform()
    obj = project.objects.all()
    return render(request, "manager.html", {'obj': obj, 'fProject':fProject})


@login_required()
def employee(request):

    return render(request, "employee.html", None)

@login_required()
def addproject(request):

    PTname =request.POST.get('Pname')
    CTname =request.POST.get('Cname')
    CTdetails=request.POST.get('Cdetails')
    PTdescription =request.POST.get('Pdescription')
    PTdeadline =request.POST.get('Pdeadline')
    PTstartdate =request.POST.get('Pstartdate')
    PTmanagedby = request.POST.get('Pmanagedby')
    PTcontract = request.POST.get('Pcontract')
    PTtextresource =request.POST.get('Ptextresource')

    if PTname is  not None and CTname is  not  None and CTdetails is not None and PTdescription is not None and PTdeadline is not None and PTstartdate is not None and  PTmanagedby is not None and  PTcontract is not None and PTtextresource is not None:
        new_object =project(Pstatus=0,Pname=PTname,Cname=CTname,Cdetails=CTdetails,Pdescription=PTdescription,Pdeadline=PTdeadline,Pstartdate=PTstartdate,Pmanagedby=PTmanagedby,Pcontract=PTcontract, Ptextresource=PTtextresource)
        new_object.save()

        return redirect("http://localhost:8000/manager/")

    fProject = addprojectform()
    return render(request,"addProject.html",{'fProject':fProject})

@login_required()
def viewprojectdetails(request):
    id = request.GET.get('id')
    request.session["pid"] = id

    if id is not None:
        row = project.objects.filter(Pid = id)
        tasks = task.objects.filter(Pid=id)

    return render(request, "viewprojectdetails.html", {'row': row, 'tasks':tasks,'Pid': id})


@login_required()
def addtask(request):
    TPid = request.session.get('pid')
    TPtitle = request.POST.get('Ttitle')
    TPstatus = 0
    TPtechnology = request.POST.get('Ttechnology')
    TPassignedto = request.POST.get('Tassignedto')
    TPassignedby = request.POST.get('Tassignedby')
    TPassigndate = request.POST.get('Tassigneddate')
    TPdealine = request.POST.get('Tdeadline')

    if TPtechnology is not None and TPtitle is not None and TPstatus is not None and TPtechnology is not None and TPassignedto is not None and TPassignedby is not None and TPassigndate is not None and TPdealine is not None:
        new_object = task(Pid=TPid, Ttitle=TPtitle, Tstatus=TPstatus, Ttechnology=TPtechnology,
                          Tassignedto=TPassignedto, Tassignedby=TPassignedby, Tassigneddate=TPassigndate,
                          Tdeadline=TPdealine)
        new_object.save()
        return redirect('http://localhost:8000/viewprojectdetails?id=' + request.session.get('pid'))

    fTask = addtaskform()
    return render(request, "addtask.html", {'fTask': fTask})


def employeetask(request):

    id = request.session["username"]

    etitle = request.POST.get('Ttitle')
    eassigneddate = request.POST.get('Tassigneddate')
    edeadline = request.POST.get('Tdeadline')
    eassignedto = request.POST .get('Tassignedto')


    obj = task.objects.filter(Ttitle = etitle, Tassigneddate = eassigneddate, Tdeadline = edeadline, Tassignedto = id)
    if id == eassignedto:
        return redirect("http://localhist:8000/employeetask/")




    return render(request, "employeetask.html", {'obj': obj})


def messageview(request):
    msg = request.POST.get('msg')
    sender_uname = 1
    rec_uname = 2

    if msg is not None:
        new_object = message(sender_username=sender_uname, receiver_username=rec_uname, content=msg)
        new_object.save()

        return redirect("http//localhost:8000/message/")

    obj = message.objects.all()

    return render(request, "message.html", {'msg': obj})





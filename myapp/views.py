from django.shortcuts import render,HttpResponse
from myapp.models import Firewall,Subnets,Allowed
import pandas as pd
import numpy as np
# Create your views here.


def create_db(request):
    inputs = []
    subnets = []
    index = 1
    f1 = Firewall.objects.filter(firewall_Name=request.GET['fw_name'])
    if len(f1) == 0:
        f1=Firewall(firewall_Name=request.GET['fw_name'])
        f1.save()
    else:
        f1 = f1[0]    
    for i,j in enumerate(request.GET):        
        inputs.append((request.GET.get('input'+str(index),None)))
        subnets.append((request.GET.get('subnet'+str(index),None)))
        index+=1

    for i,j in enumerate(inputs):
        if j!= None:
            s1 = Subnets(name=j,ip=subnets[i])
            s1.save()
            f1.rows.add(s1)
            f1.save()            
    return HttpResponse('<p>Success</p>')

def  pd_to_table(request):
    firewall_name = request.GET['fw']
    pd.set_option('display.max_colwidth', -1)
    f1 = Firewall.objects.get(firewall_Name=firewall_name)
    indexes = {}
    subnets = []
    list1 =[]
    list2 = []
    for i in f1.rows.all():
        indexes[i.name] = i.ip
        subnets.append(i.name)
    for i,j in enumerate(subnets):
        list1 = []
        for k,l in enumerate(subnets):
            
            list1.append('<select id="select_'+str(i)+'_'+str(k)+'" name="select_'+str(i)+'_'+str(k)+'"><option value="A">Allowed</option><option value="NA">Not Allowed</option></select>')
            tuple1 = tuple(list1)
        list2.append(tuple1)
    df = pd.DataFrame(np.array(list2),index=subnets,columns=subnets)
    # df.fillna('<select id="select_1"><option value="A">Allowed</option value="NA"><option>Not Allowed</option></select>',inplace=True)
    html = df.to_html(escape=False,table_id='table1')    

    return render(request,'base.html',context={'html':html})

def main_view(request):
    return render(request,'base.html')
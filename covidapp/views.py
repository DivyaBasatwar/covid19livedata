from django.shortcuts import render

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "054f30d9e3msh59854003bbcc89ap1e73d8jsnea828cd05698",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)



# Create your views here.
def helloworldview(request):
    mylist = []
    noOfResults = response['results']
    for x in range(noOfResults):
        mylist.append(response['response'][x]['country'])
    if request.method=="POST":
        selectedCountry = request.POST['selectedCountry']
        noOfResults = response['results']
        for x in range(noOfResults):
            if selectedCountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
                print(response['response'][x]['cases']['active'])
        context = {'mylist':mylist, 'selectedCountry':selectedCountry, 'new':new, 'active':active, 'critical':critical, 'recovered':recovered, 'deaths':deaths, 'total':total}
        return render(request, 'helloworld.html', context)

    context = {'mylist':mylist}
    return render(request,'helloworld.html', context);

from django.shortcuts import render
from graphs.graphs import FeaturesPieChart, BugsPieChart

def graphs(request):
    """ Charts """
    return render(request, 'features-graphs.html',
                  {'FeaturesPieChart': FeaturesPieChart(),
                   'BugsPieChart': BugsPieChart()
                   })

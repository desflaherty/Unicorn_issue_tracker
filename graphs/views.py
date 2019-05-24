from django.shortcuts import render
from graphs import FeaturesPieChart, BugsPieChart

def graphs(request):
    """ Charts """
    return render(request, 'features-graphs.html',
                  {'feature_chart': FeaturesPieChart(),
                   'bugs_chart': BugsPieChart()
                   })

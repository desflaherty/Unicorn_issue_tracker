import pygal
from bugs.models import Bugs
from features.models import Features
from pygal.style import Style

custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#53E89B',
    foreground_strong='#53A0E8',
    foreground_subtle='#630C0D',
    colors=('red', 'orange', 'green'),

    value_font_size=30,
    legend_font_size=20,
    tooltip_font_size=30,
    no_data_font_size=30
)

def chart_total(feature_type):
    """Renders graphs by a feature status.  """
    status = feature_type.objects.filter(status='ToDo').count()
    status1 = feature_type.objects.filter(status='Doing').count()
    status2 = feature_type.objects.filter(status='Done').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style,
                        inner_radius=.5)

    p_chart.add('ToDo', status)
    p_chart.add('Doing', status1)
    p_chart.add('Done', status2)
    return p_chart.render()
    
    
def FeaturesPieChart():
   chart = chart_total(Features)
   return chart
   
def BugsPieChart():
    chart = chart_total(Bugs)
    return chart
    
    
    
    
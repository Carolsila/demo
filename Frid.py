#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas as pd



# In[125]:


#cotton production
df_c=pd.read_csv('cotton.csv')


# In[141]:


#copy data
df_co=df_c.copy()
df_co


# In[127]:



#shapin the fabricdata
df_co1=df_co.melt(id_vars='Factors',value_vars=list(df_co.columns[1:]))
df_co1


# In[128]:


#Fibre production
df_p=pd.read_csv('lca.csv')
df_p1=df_p.copy()


# In[129]:


#fabric production
df_f=pd.read_csv('Fabric.csv')


# In[130]:


#copying the fabric data frame.
df_fa=df_f


# In[131]:


#shapin the fabricdata
df_fa1=df_f.melt(id_vars='Factors',value_vars=list(df_fa.columns[1:]))
df_fa1


# In[132]:


#Copying the fabrics data
df_pr=df_p.copy()


# In[133]:


#shaping the data
df_p1=df_pr.melt(id_vars='Factors',value_vars=list(df_pr.columns[1:]))
df_p1


# In[134]:


import plotly.express as px


# In[135]:


px.bar(
       df_p1, 
       x = 'Factors', 
       y = 'value', 
       color = 'variable',
        barmode = 'group', 
        #orientation = 'h',
        #color_discrete_sequence = ['#ED2F8E', '#2ADED5', '#BA3FFF', '#FFE101'],
        title = "<b>Environmental impact per  item<b>"
        #template = 'plotly_white'
        )


# In[140]:


#from jupyter_dash import JupyterDash

import dash
from dash import dcc, Dash
from dash import html
from dash.exceptions import PreventUpdate
from dash import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
def blank_fig():
    fig = go.Figure(go.Scatter(x=[], y = []))
    fig.update_layout(template = None,
                     plot_bgcolor="rgba( 0, 0, 0, 0)",
                     paper_bgcolor="rgba( 0, 0, 0, 0)",)
    fig.update_xaxes(showgrid = True, showticklabels = True, zeroline=True)
    fig.update_yaxes(showgrid = True, showticklabels = True, zeroline=True)

    return fig
app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1(
                'Environmental Impact of Cotton Fabric Producution',
                
                id = 'title'
            )
           
        ], id = 'title-area'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div(dcc.Dropdown(id = 'g1dd-a', 
                    options = list(df_co.columns[1:]), 
                    multi=True, 
                    clearable = False,
                    value = list(df_co.columns[1:])), className = 'hlf')
                ], className = 'dropdown-area', id = 'dd-area1'),
                
            html.Div([
                dcc.Graph(id = 'graph1')#, figure = blank_fig())
            ], id = 'g1', className = 'graph-container'),
            ], id = 'q1', className = 'container-a1'),
            

            html.Div([
                html.Div([
                    #html.Div(dcc.Dropdown(id = 'g2dd-a', options = list(df_pr.columns[1:]),multi=True,clearable = False,value = list(df_pr.columns[1:])[0]), className = 'thrd'),
                    html.Div(dcc.Dropdown(id = 'g2dd-b',options = list(df_pr['Factors']),multi=True,clearable = False,value = list(df_pr['Factors'])),className = 'thrd'),
                    
                ], className = 'dropdown-area', id = 'dd-area2'),
                                          
                html.Div([
                    dcc.Graph(id = 'graph2')#, figure = blank_fig())
                ], id = 'g2', className = 'graph-container'),

            ], id = 'h2', className = 'container-a2'),
            html.Div([
                html.Div([
                    html.Div(dcc.Dropdown(
                        id = 'g3dd-a',
                        options = list(df_p1.columns[1:]),
                        clearable = False,
                        value = list(df_p1.columns[1:])[0],
                        multi = False
                    ), className = 'g3-dd'),
                    html.Div(dcc.Dropdown(
                        id = 'g3dd-b',
                        options = list(df_p1['Factors']), 
                        multi=True, 
                        clearable=False, 
                        value = list(df_p1['Factors'])
                    ), className = 'g3-dd')
                    #html.Img(src = app.get_asset_url('logo.jpg'), className = 'logo')
                    
                ], className = 'v-dropdown-area'),
                html.Div([
                dcc.Graph(id = 'graph3')#, figure = blank_fig())
                ], id = 'g3', className = 'graph-container'),
            ], id = 'q3', className = 'container-b'),

        ], id = 'main')
    ], id = 'dashboard')
], id = 'layout')


@app.callback(
    Output('graph1', 'figure'),
    Input('g1dd-a', 'value')
)
def update_g1(variables):
    if len(variables) == 0:
        raise PreventUpdate
   # dff = df[['Months', 'Carbon Savings - Kg', 'Water Savings - Litres', 'Waste Savings - Kg']]
   # dff = dff.groupby('Months', as_index = False).sum()
    #dff['month_numeric'] = dff['Months'].map(month_dict)
    #dff = dff.sort_values('month_numeric')
    #dff = dff.melt(id_vars = 'Months', value_vars=list(dff.columns[1:]))
    dff=df_co.copy()
    #dff=dff.groupby('Factors',as_index=False)
    dff=dff.melt(id_vars='Factors',value_vars=list(dff.columns[1:]))    
    dff = dff[dff['variable'].isin(variables)]
            
    
    fig = px.bar(
        dff, 
        x = 'Factors', 
        y = 'value', 
        color = 'variable', 
        color_discrete_sequence = ['#00CCFF', '#2ADED5', '#BA3FFF', '#FFE101'],
        #color_discrete_sequence = ['#e6701d', '#3566c1', '#ffc61c', '#a7a6a7']
        barmode= 'group',
        title = "<b>Environmental Impact of Cotton Sheets production<b>",
        #markers = True,
       
        template = 'plotly_dark'
        )
    fig.update_layout(
        title = dict(font_size = 20, x = 0.5, xanchor = 'center'),
        margin = dict(t = 55),
        width=1000,
        height=500,
        plot_bgcolor = 'rgba(0, 0, 0, 0)', 
        paper_bgcolor = 'rgba(0, 0, 0, 0)', 
        font = dict(color = '#dadada'))
        #legend = dict(orientation = 'h', title = '', x = 0.5, xanchor = 'center', y = -0.2))
    fig.update_xaxes(title = "<b>Factors<b>", showgrid = False, ticks = 'outside', ticklen = 5, tickcolor = 'rgba(0, 0, 0, 0)')
    fig.update_yaxes(title = "<b>Value of factors<b>", ticks = 'outside', ticklen = 5, tickcolor = 'rgba(0, 0, 0, 0)')
    return fig


@app.callback(
    Output('graph2', 'figure'),
    [#Input('g2dd-a', 'value'),
     Input('g2dd-b', 'value')]
     #Input('g2dd-c', 'value')]
)
def update_g2(Factors):#factors:
    #if len(months) == 0 or len('items') == 0:
        #raise PreventUpdate
    df_bar = df_pr.melt(id_vars= ['Factors'], value_vars=df_pr.columns[1:])
   # df_bar = df_bar[df_bar['variable'] == variable]
    df_bar = df_bar[df_bar['Factors'].isin(Factors)]
    #df_bar = df_bar[df_bar['Item'].isin(items)]
    fig = px.bar(
        df_bar, 
        x = 'Factors', 
        y = 'value', 
        width=1000,
        height=500,
        
        color = 'variable',
         barmode = 'group', 
         #orientation = 'h',
         #color_discrete_sequence = ['#ED2F8E', '#2ADED5', '#BA3FFF', '#FFE101'],
         title = "<b>Environmental Impact of Fabrics Production<b>",
         template = 'plotly_white'
         )
    fig.update_layout(
            title = dict(font_size = 20, x = 0.5, xanchor = 'center'),
            margin = dict(t = 55),#b = 10),
            plot_bgcolor = 'rgba(0, 0, 0, 0)', 
            paper_bgcolor = 'rgba(0, 0, 0, 0)', 
            font = dict(color = '#dadada')) 
            #legend = dict(orientation = 'h', title = '', x = 0.5, xanchor = 'center', y = -0.099))
    fig.update_xaxes(title = "<b>Factors<b>", showgrid = False, ticks = 'outside', ticklen = 5, tickcolor = 'rgba(0, 0, 0, 0)')
    fig.update_yaxes(title = "<b>Value of factors<b>", gridcolor = 'grey', showgrid = False, ticks = 'outside', ticklen = 5, tickcolor = 'rgba(0, 0, 0, 0)')
    return fig



@app.callback(
    Output('graph3', 'figure'),
    [Input('g3dd-a', 'value'),
     Input('g3dd-b', 'value')]
)
def update_g3(variable, items):
   # if len(items) == 0:
      #  raise PreventUpdate
    df_donut = df_p1.copy()
    #df_donut = df_donut[df_donut['Factors'].isin(items)]
    fig = px.pie(
        df_donut, 
        names= 'Factors', 
        values = 'value', 
        hole = 0.5, 
        color_discrete_sequence = ['#00A3FF','#FF2E2E','#FFF000', '#2ADED5', '#BA3FFF', '#FFE101'],
        #color=['purple','red','blue'],
        title = f"<b>Environmental Impact of cotton Shirt Fabric production<b>", template="simple_white")
    fig.update_layout(
            title = dict(font_size = 20, x = 0.5, xanchor = 'center'),
            margin = dict(t = 55, b = 30),
            plot_bgcolor = 'rgba(0, 0, 0, 0)', 
            paper_bgcolor = 'rgba(0, 0, 0, 0)', 
            font = dict(color = '#dadada'), 
            legend = dict(orientation = 'h', title = 'Cotton shirt fabric', x = 0.5, xanchor = 'center', y = -0.1))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig




app.run_server( debug = True)


# In[ ]:





# In[ ]:





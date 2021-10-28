import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

######################################################################################
################################# INICIALIZAÇÃO APP ##################################
######################################################################################

app = dash.Dash(__name__, 
                suppress_callback_exceptions=True, # por termos callbacks de elementos 
                                                   # que não existem no app.layout,
                                                   # isso gera alertas sendo útil 
                                                   # para supressão dos mesmos 
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
                                                   # utilizamos bootstrap no navbar

server = app.server
######################################################################################
###################################### NAVBAR ########################################
######################################################################################

navbar = dbc.NavbarSimple(
    children=[
        dbc.Button(html.Span([html.I(id="span_botao",className="fas fa-bars ml-2")]),style=({"marginRight":"64rem"}), outline=True, color="info", className="mr-1", id="btn_sidebar"),
        dbc.NavItem(dbc.NavLink("KPIs", href="/page-kpis")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Página 1", href="/page-1"),
                dbc.DropdownMenuItem("Página 2", href="/page-2"),
                dbc.DropdownMenuItem("Página 3", href="/page-3"),
                dbc.DropdownMenuItem("Página de KPIs", href="/page-kpis"),
            ],
            nav=True,
            in_navbar=True,
            label="Status",
            align_end = True,
        ),
    ],
    brand="Everton",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,)

######################################################################################
###################################### SIDEBAR #######################################
######################################################################################

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",}
SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",}
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Página 1", href="/page-1", id="page-1-link"),
                dbc.NavLink("Página 2", href="/page-2", id="page-2-link"),
                dbc.NavLink("Página 3", href="/page-3", id="page-3-link"),
                dbc.NavLink("Página de KPIs", href="/page-kpis", id="page-kpis-link")            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,)

######################################################################################
################################# CONTEÚDO DA PÁGINA #################################
######################################################################################

CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "margin-top":".5rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",}
CONTENT_STYLE_sidebar_hidden = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "margin-top":".5rem",
    "background-color": "#f8f9fa",}
content = html.Div(

    id="page-content",
    style=CONTENT_STYLE)

######################################################################################
###################################### LAYOUT ########################################
######################################################################################

# layout da página principal
app.layout = html.Div([
    navbar,
    sidebar,
    content,
    dcc.Store(id='side_click'),

    dcc.Location(id='url', refresh=False)])
home_page = html.Div([
    html.H1('HOME'),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page KPI', href='/page-kpis'),])

# página de path errado
index_page = html.Div([
    html.H1('URL não encontrada'),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page KPI', href='/page-kpis'),])

###########################################################################################
#################################### PAGINA 1 #############################################
###########################################################################################

# layout ####
page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-1-content'),
    html.Br(),
    
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to KPIs Page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),],
    )
# callback ####
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)

###########################################################################################
#################################### PAGINA 2 #############################################
###########################################################################################

# layout ####
page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to KPIs page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])

###########################################################################################
#################################### PAGINA 3 #############################################
###########################################################################################

# layout ####
page_3_layout = html.Div([
    html.H1('Page 3'),


    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),



    html.Div(id='page-3-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to KPIs Page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])

# callback ####
@app.callback(dash.dependencies.Output('page-3-content', 'children'),
              [dash.dependencies.Input('page-3-radios', 'value')])
def page_3_radios(value):
    return 'You have selected "{}"'.format(value)

@app.callback(dash.dependencies.Output('output-state', 'children'),
              dash.dependencies.Input('submit-button', 'n_clicks'),
              dash.dependencies.State('input-1-state', 'value'),
              dash.dependencies.State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return ('The Button has been pressed {} times,'
            'Input 1 is "{}",'
            'and Input 2 is "{}"').format(n_clicks, input1, input2)


###########################################################################################
#################################### PAGINA KPIS #############################################
###########################################################################################

# layout ####
page_kpis_layout = html.Div([
    html.H1('KPIs'),

    html.Div(id='page-kpis-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])







###########################################################################################
############################## Mudança de página do app ###################################
###########################################################################################

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-kpis':
        return page_kpis_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ])
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE_sidebar_hidden
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

###########################################################################################
############################### Inicialização do APP ######################################
###########################################################################################
import os
if __name__ == '__main__':
    app.run_server(debug=False,port=os.getenv("PORT",5000))
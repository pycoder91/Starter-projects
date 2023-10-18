import plotly.graph_objects as go
import numpy as np 
from dash import Dash, dcc, html, Input, Output, State,callback
import dash_bootstrap_components as dbc

def check_exist(i,j,k):
    if 0<=i<=2 and 0<=j<=2 and 0<=k<=2:
        return True
    else:
        return False

def check_3d_cube(cube_3d,turn):
    exists=list()
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if cube_3d[i][j][k]==turn:
                    if(check_exist(i+1,j,k)):
                        if(cube_3d[i+1][j][k]==turn):
                            if(check_exist(i+2,j,k)):
                                if(cube_3d[i+2][j][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,k*3])
                    if(check_exist(i,j+1,k)):
                        if(cube_3d[i][j+1][k]==turn):
                            if(check_exist(i,j+2,k)):
                                if(cube_3d[i][j+2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,k*3])
                    if(check_exist(i,j,k+1)):
                        if(cube_3d[i][j][k+1]==turn):
                            if(check_exist(i,j,k+2)):
                                if(cube_3d[i][j][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,j*3,(k+2)*3])
                    if(check_exist(i+1,j+1,k)):
                        if(cube_3d[i+1][j+1][k]==turn):
                            if(check_exist(i+2,j+2,k)):
                                if(cube_3d[i+2][j+2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,k*3])
                    if(check_exist(i+1,j,k+1)):
                        if(cube_3d[i+1][j][k+1]==turn):
                            if(check_exist(i+2,j,k+2)):
                                if(cube_3d[i+2][j][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,(k+2)*3])
                    if(check_exist(i,j+1,k+1)):
                        if(cube_3d[i][j+1][k+1]==turn):
                            if(check_exist(i,j+2,k+2)):
                                if(cube_3d[i][j+2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,(k+2)*3])
                    if(check_exist(i+1,j-1,k)):
                        if(cube_3d[i+1][j-1][k]==turn):
                            if(check_exist(i+2,j-2,k)):
                                if(cube_3d[i+2][j-2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j-2)*3,k*3])
                    if(check_exist(i+1,j,k-1)):
                        if(cube_3d[i+1][j][k-1]==turn):
                            if(check_exist(i+2,j,k-2)):
                                if(cube_3d[i+2][j][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,(k-2)*3])
                    if(check_exist(i,j+1,k-1)):
                        if(cube_3d[i][j+1][k-1]==turn):
                            if(check_exist(i,j+2,k-2)):
                                if(cube_3d[i][j+2][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,(k-2)*3])
                    if(check_exist(i+1,j+1,k+1)):
                        if(cube_3d[i+1][j+1][k+1]==turn):
                            if(check_exist(i+2,j+2,k+2)):
                                if(cube_3d[i+2][j+2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,(k+2)*3])
                    if(check_exist(i+1,j-1,k+1)):
                        if(cube_3d[i+1][j-1][k+1]==turn):
                            if(check_exist(i+2,j-2,k+2)):
                                if(cube_3d[i+2][j-2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j-2)*3,(k+2)*3])                
                    if(check_exist(i+1,j+1,k-1)):
                        if(cube_3d[i+1][j+1][k-1]==turn):
                            if(check_exist(i+2,j+2,k-2)):
                                if(cube_3d[i+2][j+2][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,(k-2)*3])  
    return (exists)              

def cubes(size, pos_x, pos_y, pos_z, color):
    info_x=pos_x//3
    # create points
    x, y, z = np.meshgrid(
        np.linspace(pos_x-size/2, pos_x+size/2, 2), 
        np.linspace(pos_y-size/2, pos_y+size/2, 2), 
        np.linspace(pos_z-size/2, pos_z+size/2, 2),
    )
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    return go.Mesh3d(x=x, y=y, z=z, alphahull=1, flatshading=True, color=color,opacity=0.5, lighting={'diffuse': 0.1, 'specular': 2.0, 'roughness': 0.5})
fig = go.Figure()
# set edge length of cubes
size = 1
# add outer cube
fig.update_layout(
        autosize=True,
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        width=500,
        height=500,
        margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4)
    )
fig.layout.uirevision=True
# add inner center cube
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
                f=go.FigureWidget(fig.add_trace(cubes(size,i*3,j*3,k*3, "pink")))

# Build App
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ]
)
x = np.array([0,1])
y = np.array([1,1])
z = np.array([1,1])

# app layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dcc.Graph(
                    id='graph',
                    figure=fig,
                    config={
                        'scrollZoom': True,
                        'displayModeBar': False,
                    }
                ),
                width={'size': 5, 'offset': 0}
            ), justify='around'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(
                            html.Button(
                                'Restart',
                                id='refresh_button'
                            ),
                            href='/'
                        ),
                        html.Div(id="box"),
                        dcc.Markdown(
                            '''
                            # Functionality:
                            - if you have this IP then you should logically know what this does
                            - use the "Restart" button to restart
                            '''
                        ) 
                    ], width={'size': 5, 'offset': 0}
                ),
            ], justify='around'
        )
    ], fluid=True
)
data_prev=None
turn="blue"
cube_3d=list()
exists=list()
for i in range(0,3):
    tempk=[]
    for j in range(0,3):
        tempj=["-","-","-"]
        tempk.append(tempj)
    cube_3d.append(tempk)

@ app.callback(
    Output('graph', 'figure'),
    State('graph', 'figure'),
    Input('graph', 'clickData')
)
def display_click_data(graph_figure,data):
    global turn,data_prev,exists,cube_3d
    print(cube_3d)
    # print("data",data)
    # print("data_prev",data_prev)
    try:
        if(len(exists)<2):
        # print(curve_no)
            if(data_prev==None or data["points"][0]["curveNumber"]!=data_prev["points"][0]["curveNumber"]):
                curve_no=data["points"][0]['curveNumber']
                data_prev=data
                if cube_3d[((curve_no//3)//3)%3][((curve_no//3)%3)][(curve_no%3)]=="-":
                    cube_3d[((curve_no//3)//3)%3][((curve_no//3)%3)][(curve_no%3)]=turn
                    graph_figure["data"][curve_no]["color"]=turn
                    exists=check_3d_cube(cube_3d,turn)
                    if(len(exists)>=2):
                        for i in range(0,len(exists),2):
                            graph_figure["data"].append({'line': {'color': 'white', 'width': 20},"mode":"lines","x":[exists[i][0],exists[i+1][0]],"y":[exists[i][1],exists[i+1][1]],"z":[exists[i][2],exists[i+1][2]],"type":"scatter3d"})
                        cube_3d=list()
                        for i in range(0,3):
                            tempk=[]
                            for j in range(0,3):
                                tempj=["-","-","-"]
                                tempk.append(tempj)
                            cube_3d.append(tempk)
                        turn="blue"
                    # print(graph_figure["data"])
                    if turn=="blue":
                        turn="red"
                    else:
                        turn="blue"
                    return graph_figure
                else:
                    return graph_figure
            else:
                return graph_figure
        else:
            return graph_figure
    except:
        return graph_figure
    # go.FigureWidget(fig.add_trace(cubes(size,(((curve_no//3)//3)%3)*3,((curve_no//3)%3)*3,(curve_no%3)*3, "blue")))
@app.callback(
    Output("box","children"),
    Input("refresh_button","n_clicks")
)
def restart(click):
    global cube_3d,exists,turn
    cube_3d=list()
    for i in range(0,3):
        tempk=[]
        for j in range(0,3):
            tempj=["-","-","-"]
            tempk.append(tempj)
        cube_3d.append(tempk)
    turn="blue"
    exists=list()
    return html.Div("")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8050")

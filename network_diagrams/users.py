import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

# enable svg export
cyto.load_extra_layouts()

dim_x = 800
dim_y = 400

elements = [
    # Parent node
    {
        'data': {
            'id': 'p_coll',
            'label': 'collections'
        }
    },
    {
        'data': {
            'id': 'p_ex',
            'label': 'experiments'
        }
    },
    {
        'data': {
            'id': 'p_pub',
            'label': 'publications'
        }
    },
    {
        'data': {
            'id': 'p_group',
            'label': 'group'
        }
    },

    # nodes
    {
        'data': {
            'id': 'User_1',
            'label': 'Dylan W'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Gr_1',
            'label': 'MIT',
            'parent': 'p_group'
        },
        'position': {
            'x': dim_x / 2 - 50,
            'y': dim_y / 2 - 100
        }
    },
    {
        'data': {
            'id': 'Gr_2',
            'label': 'CRIPT',
            'parent': 'p_group'
        },
        'position': {
            'x': dim_x / 2 + 50,
            'y': dim_y / 2 - 100
        }
    },
    {
        'data': {
            'id': 'Ex_1',
            'label': 'Anionic po',
            'parent': 'p_ex'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Ex_2',
            'label': 'ATRP of sty',
            'parent': 'p_ex'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'Ex_3',
            'label': 'ROMP catal',
            'parent': 'p_ex'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 100
        }
    },
    {
        'data': {
            'id': 'Ex_4',
            'label': 'ROMP catal',
            'parent': 'p_ex'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 150
        }
    },
    {
        'data': {
            'id': 'Ex_5',
            'label': 'ROMP mono',
            'parent': 'p_ex'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 200
        }
    },
    {
        'data': {
            'id': 'Pub_1',
            'label': 'Recent tre',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Pub_2',
            'label': 'Kinetic st',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'Coll_1',
            'label': 'ROMP kinet',
            'parent': 'p_coll'
        },
        'position': {
            'x': dim_x / 2 + 150,
            'y': dim_y / 2 + 150
        }
    },

    # Edges
    {
        'data': {
            'source': 'User_1',
            'target': 'p_group'
        }
    },
    {
        'data': {
            'source': 'User_1',
            'target': 'p_ex'
        }
    },
    {
        'data': {
            'source': 'User_1',
            'target': 'p_pub'
        }
    },
    {
        'data': {
            'source': 'User_1',
            'target': 'p_coll'
        }
    }
]

network_styles = [
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'font-family': 'arial',
            'font-weight': 'bold',
            'text-halign': 'center',
            'text-valign': 'center',
            'width': 'label',
            'height': 'label',
            'shape': 'round-rectangle',
            'border-width': 3,
            'border-color': [0, 0, 0],
            'padding': 10,
            'background-color': [217, 125, 125],
        }
    },
    {
        'selector': 'edge',
        'style': {
            'curve-style': 'bezier',
            'line-color': 'black'
            # 'source-arrow-color': 'black',
            # 'source-arrow-shape': 'triangle'
        }
    },

    # style class
    {
        'selector': '[id ^= "In_"]',
        'style': {
            'background-color': 'red'
        }
    },
    {
        'selector': '[id ^= "Proc_"]',
        'style': {
            'background-color': 'orange'
        }
    },
    {
        'selector': '[id ^= "Prod_"]',
        'style': {
            'background-color': 'blue'
        }
    },
    {
        'selector': '[id ^= "Meas_"]',
        'style': {
            'background-color': 'green'
        }
    },
    {
        'selector': '[id ^= "At_"]',
        'style': {
            'background-color': 'gray'
        }
    },
    {
        'selector': '[id ^= "gr_"]',
        'style': {
            'background-color': 'gray'
        }
    },
    {
        'selector': '[styling = "t_down"]',
        'style': {
            'text-valign': 'bottom'
        }
    },
    {
        'selector': '[id ^= "p_"]',
        'style': {
            'text-valign': 'top',
            'background-color': 'gray'
        }
    }
]

styles = {
    'output': {
        'overflow-y': 'scroll',
        'overflow-wrap': 'break-word',
        'height': 'calc(100% - 25px)',
        'border': 'thin lightgrey solid'
    },
    'tab': {'height': 'calc(98vh - 115px)'}
}


app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='network',
        layout={
            'name': 'preset'
        },
        style={
            'width': '800px',
            'height': '400px'
        },

        stylesheet=network_styles,
        elements=elements
    ),
    html.Div('Download graph:'),
    html.Button("as svg", id="btn-get-svg")
])



@app.callback(
        Output("network", "generateImage"),
        Input("btn-get-svg", "n_clicks")
    )
def get_image(tab):
    print(tab)
    # File type to output of 'svg, 'png', 'jpg', or 'jpeg' (alias of 'jpg')
    ftype = tab

    # 'store': Stores the image data in 'imageData' !only jpg/png are supported
    # 'download'`: Downloads the image as a file with all data handling
    # 'both'`: Stores image data and downloads image as file.
    action = 'download'

    ctx = dash.callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if input_id != "tabs":
            action = "download"
            ftype = input_id.split("-")[-1]

    return {
        'type': ftype,
        'action': action
        }


if __name__ == '__main__':
    app.run_server(debug=True)


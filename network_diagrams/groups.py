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
            'id': 'p_users',
            'label': 'users'
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
            'id': 'Gr_1',
            'label': 'CRIPT'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Gr_2',
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
            'id': 'Gr_3',
            'label': 'Citrine',
            'parent': 'p_group'
        },
        'position': {
            'x': dim_x / 2 + 50,
            'y': dim_y / 2 - 100
        }
    },
    {
        'data': {
            'id': 'User_1',
            'label': 'Dylan W',
            'parent': 'p_users'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'User_2',
            'label': 'Eric M',
            'parent': 'p_users'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'User_3',
            'label': 'Chris B',
            'parent': 'p_users'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 100
        }
    },
    {
        'data': {
            'id': 'User_4',
            'label': 'Tzyy-Shyang L',
            'parent': 'p_users'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 150
        }
    },
    {
        'data': {
            'id': 'User_5',
            'label': 'Vinay H',
            'parent': 'p_users'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 200
        }
    },
    {
        'data': {
            'id': 'Pub_1',
            'label': 'CRIPT database',
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
            'label': 'BigSMILES',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'Pub_3',
            'label': 'PolyDat',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 + 100
        }
    },

    # Edges
    {
        'data': {
            'source': 'Gr_1',
            'target': 'p_group'
        }
    },
    {
        'data': {
            'source': 'p_users',
            'target': 'Gr_1'
        }
    },
    {
        'data': {
            'source': 'p_pub',
            'target': 'Gr_1'
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


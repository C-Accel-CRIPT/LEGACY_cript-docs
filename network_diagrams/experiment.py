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
            'id': 'p_mat',
            'label': 'materials'
        }
    },
    {
        'data': {
            'id': 'p_proc',
            'label': 'process'
        }
    },
    {
        'data': {
            'id': 'p_data',
            'label': 'data'
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
            'id': 'p_user',
            'label': 'users'
        }
    },

    # nodes
    {
        'data': {
            'id': 'Expt',
            'label': 'ROMP kinetic'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'User_1',
            'label': 'Dylan W',
            'parent': 'p_user'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2 - 100
        }
    },
    {
        'data': {
            'id': 'pub_1',
            'label': 'Kinetic Study',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'pub_2',
            'label': 'Kinetic Study',
            'parent': 'p_pub'
        },
        'position': {
            'x': dim_x / 2 - 200,
            'y': dim_y / 2 + 50,
        }
    },
    {
        'data': {
            'id': 'mat_1',
            'label': 'G3 Catalyst',
            'parent': 'p_mat'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 - 100
        }
    },
    {
        'data': {
            'id': 'mat_2',
            'label': 'dichloromet',
            'parent': 'p_mat'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 - 50
        }
    },
    {
        'data': {
            'id': 'mat_3',
            'label': 'norbornene-',
            'parent': 'p_mat'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'mat_4',
            'label': 'ethyl vinyl',
            'parent': 'p_mat'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'mat_5',
            'label': 'poly(norborene',
            'parent': 'p_mat'
        },
        'position': {
            'x': dim_x / 2 + 200,
            'y': dim_y / 2 + 100
        }
    },
    {
        'data': {
            'id': 'proc_1',
            'label': 'ROMP polymeri',
            'parent': 'p_proc'
        },
        'position': {
            'x': dim_x / 2 - 100,
            'y': dim_y / 2 + 200,
        }
    },
    {
        'data': {
            'id': 'data_1',
            'label': '1H NMR',
            'parent': 'p_data'
        },
        'position': {
            'x': dim_x / 2 + 100,
            'y': dim_y / 2 + 200
        }
    },
    {
        'data': {
            'id': 'data_2',
            'label': 'SEC',
            'parent': 'p_data'
        },
        'position': {
            'x': dim_x / 2 + 100,
            'y': dim_y / 2 + 250
        }
    },

    # Edges
    {
        'data': {
            'source': 'Expt',
            'target': 'p_pub'
        }
    },
    {
        'data': {
            'source': 'Expt',
            'target': 'p_user'
        }
    },
    {
        'data': {
            'source': 'Expt',
            'target': 'p_mat'
        }
    },
    {
        'data': {
            'source': 'Expt',
            'target': 'p_proc'
        }
    },
    {
        'data': {
            'source': 'Expt',
            'target': 'p_data'
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
    'tab': {
        'height': 'calc(98vh - 115px)'
    }
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

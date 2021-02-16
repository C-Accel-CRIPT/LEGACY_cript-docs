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
            'id': 'p_user',
            'label': 'users'
        }
    },
    {
        'data': {
            'id': 'p_expt',
            'label': 'experiment'
        }
    },
    {
        'data': {
            'id': 'p_ingr',
            'label': 'identity'
        }
    },
    {
        'data': {
            'id': 'p_proce',
            'label': 'procedure'
        }
    },
    {
        'data': {
            'id': 'p_attr',
            'label': 'attribute'
        }
    },
    {
        'data': {
            'id': 'p_out',
            'label': 'out'
        }
    },

    # nodes
    {
        'data': {
            'id': 'proc_1',
            'label': 'polymerization'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'user_1',
            'label': 'Dylan W',
            'parent': 'p_user'
        },
        'position': {
            'x': dim_x / 4,
            'y': dim_y / 4
        }
    },
    {
        'data': {
            'id': 'expt_1',
            'label': 'anionic polym',
            'parent': 'p_expt'
        },
        'position': {
            'x': 3 * dim_x / 4,
            'y': dim_y / 4
        }
    },
    {
        'data': {
            'id': 'ingr_1',
            'label': 'styrene',
            'parent': 'p_ingr'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'ingr_2',
            'label': 'sec-bu li',
            'parent': 'p_ingr'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'ingr_3',
            'label': 'toluene',
            'parent': 'p_ingr'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 100
        }
    },
    {
        'data': {
            'id': 'ingr_4',
            'label': 'methanol',
            'parent': 'p_ingr'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 150
        }
    },
    {
        'data': {
            'id': 'proce_1',
            'label': 'In an argon f',
            'parent': 'p_proce'
        },
        'position': {
            'x': dim_x / 2,
            'y': dim_y / 2 + 150
        }
    },
    {
        'data': {
            'id': 'out_1',
            'label': 'polystyrene',
            'parent': 'p_out'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2
        }
    },
{
        'data': {
            'id': 'attr_1',
            'label': 'time',
            'parent': 'p_attr'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 100
        }
    },
{
        'data': {
            'id': 'attr_2',
            'label': 'temp',
            'parent': 'p_attr'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 150
        }
    },
{
        'data': {
            'id': 'attr_3',
            'label': 'samp_rate',
            'parent': 'p_attr'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 200
        }
    },

    # Edges
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_ingr'
        }
    },
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_user'
        }
    },
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_attr'
        }
    },
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_proce'
        }
    },
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_expt'
        }
    },
    {
        'data': {
            'source': 'proc_1',
            'target': 'p_out'
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

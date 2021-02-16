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
            'id': 'p_iden',
            'label': 'identity'
        }
    },
    {
        'data': {
            'id': 'p_prop',
            'label': 'properties'
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

    # nodes
    {
        'data': {
            'id': 'Mat_1',
            'label': 'poly(styrene)'
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
            'id': 'iden_1',
            'label': 'Poly(1-phenylet',
            'parent': 'p_iden'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'iden_2',
            'label': '9003-53-6',
            'parent': 'p_iden'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 50
        }
    },
    {
        'data': {
            'id': 'iden_3',
            'label': '{[$]CC(c1ccccc1',
            'parent': 'p_iden'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 100
        }
    },
    {
        'data': {
            'id': 'iden_4',
            'label': 'C8H8',
            'parent': 'p_iden'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 2 + 150
        }
    },
    {
        'data': {
            'id': 'prop_1',
            'label': 'conv_mon_nmr',
            'parent': 'p_prop'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'prop_2',
            'label': 'm_n_nmr',
            'parent': 'p_prop'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 50
        }
    },
{
        'data': {
            'id': 'prop_3',
            'label': 'm_n_sec',
            'parent': 'p_prop'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 100
        }
    },
{
        'data': {
            'id': 'prop_4',
            'label': 'd_sec',
            'parent': 'p_prop'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': dim_y / 2 + 150
        }
    },
{
        'data': {
            'id': 'proc_1',
            'label': 'anionic polym',
            'parent': 'p_proc'
        },
        'position': {
            'x': 2 * dim_x / 4 - 70,
            'y': dim_y / 2 + 150
        }
    },
{
        'data': {
            'id': 'data_1',
            'label': 'nmr_1h',
            'parent': 'p_data'
        },
        'position': {
            'x': 2 * dim_x / 4 + 70,
            'y': dim_y / 2 + 150
        }
    },
{
        'data': {
            'id': 'data_2',
            'label': 'sec',
            'parent': 'p_data'
        },
        'position': {
            'x': 2 * dim_x / 4 + 70,
            'y': dim_y / 2 + 200
        }
    },

    # Edges
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_iden'
        }
    },
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_user'
        }
    },
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_prop'
        }
    },
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_proc'
        }
    },
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_data'
        }
    },
    {
        'data': {
            'source': 'Mat_1',
            'target': 'p_expt'
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

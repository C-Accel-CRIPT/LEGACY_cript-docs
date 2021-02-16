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
    # nodes
    {
        'data': {
            'id': 'Gr',
            'label': 'Groups'
        },
        'position': {
            'x': dim_x/6,
            'y': 2*dim_y/5
        }
    },
    {
        'data': {
            'id': 'User',
            'label': 'Users'
        },
        'position': {
            'x': 2*dim_x/6,
            'y': 2*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Ex',
            'label': 'Experiments'
        },
        'position': {
            'x': 3*dim_x/6,
            'y': 2*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Pub',
            'label': 'Publications'
        },
        'position': {
            'x': 2*dim_x/6,
            'y': 3*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Col',
            'label': 'Collections'
        },
        'position': {
            'x': 2*dim_x/6,
            'y': dim_y/5
        }
    },
    {
        'data': {
            'id': 'Mat_p',
            'label': 'Materials\n(polymers)',
        },
        'position': {
            'x': 4*dim_x/6,
            'y': 1*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Mat_o',
            'label': 'Materials\n(other)',
        },
        'position': {
            'x': 4.7*dim_x/6,
            'y': 1*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Pr',
            'label': 'Process'
        },
        'position': {
            'x': 4*dim_x/6,
            'y': 2*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Data',
            'label': 'Data'
        },
        'position': {
            'x': 4*dim_x/6,
            'y': 3*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Mod',
            'label': 'Modules'
        },
        'position': {
            'x': 4*dim_x/6,
            'y': 4*dim_y/5
        }
    },
    {
        'data': {
            'id': 'Lake',
            'label': 'Date Lake'
        },
        'position': {
            'x': 5*dim_x/6,
            'y': 3*dim_y/5
        }
    },
    {
        'data': {
            'id': 'vs',
            'label': 'Version Control'
        },
        'position': {
            'x': 2.5 * dim_x / 6,
            'y': 4 * dim_y / 5
        }
    },
    # Edges
    {
        'data': {
            'source': 'Lake',
            'target': 'Data'
        }
    },
    {
        'data': {
            'source': 'Mod',
            'target': 'Data'
        }
    },
    {
        'data': {
            'source': 'Pr',
            'target': 'Data'
        }
    },
    {
        'data': {
            'source': 'Gr',
            'target': 'User'
        }
    },
    {
        'data': {
            'source': 'Gr',
            'target': 'Pub'
        }
    },
    {
        'data': {
            'source': 'Pub',
            'target': 'User'
        }
    },
    {
        'data': {
            'source': 'Ex',
            'target': 'User'
        }
    },
    {
        'data': {
            'source': 'Ex',
            'target': 'Pub'
        }
    },
    {
        'data': {
            'source': 'Ex',
            'target': 'Col'
        }
    },
    {
        'data': {
            'source': 'Col',
            'target': 'User'
        }
    },
    {
        'data': {
            'source': 'Col',
            'target': 'Gr'
        }
    },
    {
        'data': {
            'source': 'Ex',
            'target': 'Mat_p'
        }
    },
    {
        'data': {
            'source': 'Pr',
            'target': 'Mat_p'
        }
    },
    {
        'data': {
            'source': 'Pr',
            'target': 'Ex'
        }
    },
{
        'data': {
            'source': 'Data',
            'target': 'Ex'
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
            'text-wrap': 'wrap'
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


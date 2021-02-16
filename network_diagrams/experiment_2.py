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

    # nodes
    {
        'data': {
            'id': 'In_1',
            'label': 'G3 Catalyst'
        },
        'position': {
            'x': dim_x / 5,
            'y': dim_y / 5
        }
    },
    {
        'data': {
            'id': 'In_2',
            'label': 'dichloromet'
        },
        'position': {
            'x': dim_x / 5,
            'y': 2 * dim_y / 5
        }
    },
    {
        'data': {
            'id': 'In_3',
            'label': 'norbornene'
        },
        'position': {
            'x': dim_x / 5,
            'y': 3 * dim_y / 5
        }
    },
    {
        'data': {
            'id': 'In_4',
            'label': 'ethyl vinyl'
        },
        'position': {
            'x': dim_x / 5,
            'y': 4 * dim_y / 5,
        }
    },
    {
        'data': {
            'id': 'Proc_1',
            'label': 'ROMP Polymeri'
        },
        'position': {
            'x': 2 * dim_x / 5,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Prod_1',
            'label': 'poly(norborene'
        },
        'position': {
            'x': 3.5 * dim_x / 5,
            'y': dim_y / 2
        }
    },
    {
        'data': {
            'id': 'Data_1',
            'label': '1H NMR'
        },
        'position': {
            'x': 3 * dim_x / 5,
            'y': 3 * dim_y / 4
        }
    },
    {
        'data': {
            'id': 'Data_2',
            'label': 'SEC'
        },
        'position': {
            'x': 4 * dim_x / 5,
            'y': 3 * dim_y / 4
        }
    },


    # Edges
    {
        'data': {
            'source': 'Proc_1',
            'target': 'In_1'
        }
    },
    {
        'data': {
            'source': 'Proc_1',
            'target': 'In_2'
        }
    },
    {
        'data': {
            'source': 'Proc_1',
            'target': 'In_3'
        }
    },
    {
        'data': {
            'source': 'Proc_1',
            'target': 'In_4'
        }
    },
    {
        'data': {
            'source': 'Prod_1',
            'target': 'Proc_1'
        }
    },
    {
        'data': {
            'source': 'Prod_1',
            'target': 'Data_1'
        }
    },
    {
        'data': {
            'source': 'Prod_1',
            'target': 'Data_2'
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
            'color': 'white',
            'text-halign': 'center',
            'text-valign': 'center',
            'width': 'label',
            'height': 'label',
            'shape': 'round-rectangle',
            'border-width': 3,
            'border-color': [0, 0, 0],
            'padding': 10,
        }
    },
    {
        'selector': 'edge',
        'style': {
            'curve-style': 'bezier',
            'line-color': 'black',
            'source-arrow-color': 'black',
            'source-arrow-shape': 'triangle'
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
        'selector': '[id ^= "Data_"]',
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

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
            'id': 'mat_1',
            'label': 'material node'
        }
    },
    # nodes
    {
        'data': {
            'id': 'data_1',
            'label': 'raw data from sec\n signal vs. time'
        },
        'position': {
            'x': dim_x / 6,
            'y': dim_y / 3
        }
    },
    {
        'data': {
            'id': 'mod_1',
            'label': 'sec raw data analysis'
        },
        'position': {
            'x': 1.6 * dim_x / 6,
            'y': 2 * dim_y / 3
        }
    },
    {
        'data': {
            'id': 'data_2',
            'label': 'sec processed data\nMW vs. population'
        },
        'position': {
            'x': 3 * dim_x / 6,
            'y': dim_y / 3
        }
    },
    {
        'data': {
            'id': 'mod_2',
            'label': 'sec property calculation'
        },
        'position': {
            'x': 3.5 * dim_x / 6,
            'y': 2 * dim_y / 3
        }
    },
    {
        'data': {
            'id': 'prop_1',
            'label': 'm_n',
            'parent': 'mat_1'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': 2 * dim_y / 5
        }
    },
    {
        'data': {
            'id': 'prop_2',
            'label': 'd',
            'parent': 'mat_1'
        },
        'position': {
            'x': 5 * dim_x / 6,
            'y': 3 * dim_y / 5
        }
    },

    # Edges
    {
        'data': {
            'source': 'mod_1',
            'target': 'data_1'
        }
    },
    {
        'data': {
            'source': 'data_2',
            'target': 'mod_1'
        }
    },
    {
        'data': {
            'source': 'mod_2',
            'target': 'data_2'
        }
    },
    {
        'data': {
            'source': 'mat_1',
            'target': 'mod_2'
        }
    },

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
            'line-color': 'black',
            'source-arrow-color': 'black',
            'source-arrow-shape': 'triangle'
        }
    },

    # style class
    {
        'selector': '[id ^= "mod_"]',
        'style': {
            'background-color': [158, 149, 144]
        }
    },
    {
        'selector': '[id ^= "mat_"]',
        'style': {
            'text-valign': 'top',
            'background-color': [158, 149, 144]
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


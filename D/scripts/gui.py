import ipywidgets as widgets
import json
import numpy as np
from IPython.display import display


def get_data():
    with open('../config.json', 'r') as f:
        data = json.load(f)
        n_amount, compare_with, port = data['n_amount'], data['compare_with'], data['port']
        return n_amount, int(compare_with), port

def change_network(x):
    with open('../config.json', 'r') as f:
        data = json.load(f)
        data['compare_with'] = str(x['new'])

    with open('../config.json', 'w') as f:
        f.write(json.dumps(data))

def main():
    n_amount, compare_with, port = get_data()

    n = widgets.Box([
        widgets.Label(value='Compare With Network:'),
        widgets.RadioButtons(
        options=np.arange(1, n_amount+1),
        value=compare_with
        ,            layout={'width': 'max-content'})
    ])
    n.observe(change_network, 'value')
    display(n)

if __name__ == '__main__':
    main()
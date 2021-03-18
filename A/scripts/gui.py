import ipywidgets as widgets
import json
import numpy as np
from IPython.display import display


def get_data():
    with open('../config.json', 'r') as f:
        data = json.load(f)
        n_amount, current_network, port = data['n_amount'], data['current_network'], data['port']
        return n_amount, int(current_network), port

def change_network(x):
    with open('../config.json', 'r') as f:
        data = json.load(f)
        data['current_network'] = str(x['new'])

    with open('../config.json', 'w') as f:
        f.write(json.dumps(data))

def main():
    n_amount, current_network, port = get_data()
    n = widgets.RadioButtons(
        options=np.arange(1, n_amount+1),
        value=current_network,
        description='Network:'
    )
    p = widgets.IntText(
    value=port,
    description='Port:',
    disabled=True
)
    n.observe(change_network, 'value')
    display(n,p)

if __name__ == '__main__':
    main()
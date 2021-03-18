import ipywidgets as widgets
import json
import numpy as np
from IPython.display import display


def get_data():
    with open('../config.json') as f:
        data = json.load(f)
        n_amount, b_network, port = data['n_amount'], data['b_network'], data['port']
        return n_amount, b_network, port

def main():
    n_amount, b_network, port = get_data()
    n = widgets.RadioButtons(
        options=np.arange(1, n_amount+1),
        value=b_network,
        description='Network:'
    )
    p = widgets.IntText(
    value=port,
    description='Port:',
    disabled=True
)
    display(n,p)

if __name__ == '__main__':
    main()
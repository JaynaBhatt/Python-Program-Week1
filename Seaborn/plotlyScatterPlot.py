import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

import plotly
plotly.tools.set_credentials_file(username='jaynabhatt9', api_key='SDapnbSwsGDGBC3gQApf')

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)


trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-scatter')
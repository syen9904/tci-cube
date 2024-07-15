# pipeline it on render
# construct plot
# Questions

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Function to create 3D scatter plot
def create_3d_scatter_plot(points):
    fig = go.Figure(data=[go.Scatter3d(
        x=points['x'],
        y=points['y'],
        z=points['z'],
        mode='markers',
        marker=dict(
            size=5,
            color='blue'
        )
    )])

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='X Axis', range=[0, 6]),
            yaxis=dict(title='Y Axis', range=[0, 6]),
            zaxis=dict(title='Z Axis', range=[0, 6])
        ),
        width=300,  # Adjusted width for smartphone screens
        margin=dict(r=20, b=10, l=10, t=10)
    )

    return fig

# Sample points inside a cube
points = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [5, 4, 3, 2, 1],
    'z': [2, 3, 4, 5, 6]
})

# Streamlit app
st.title("3D Scatter Plot")

st.plotly_chart(create_3d_scatter_plot(points))

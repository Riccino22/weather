import streamlit as st
import plotly.graph_objs as go

# Datos de ejemplo
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

# Crear los trazados (traces)
trace1 = go.Scatter(
    x=x,
    y=y1,
    mode='lines',
    name='y = x^2'
)

trace2 = go.Scatter(
    x=x,
    y=y2,
    mode='lines',
    name='y = x'
)

# Crear la figura y agregar los trazados
fig = go.Figure()
fig.add_trace(trace1)
fig.add_trace(trace2)

# Configurar el layout
fig.update_layout(
    title='Gráfico de Líneas Múltiples',
    xaxis_title='X Axis',
    yaxis_title='Y Axis'
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

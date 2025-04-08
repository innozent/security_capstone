from nicegui import ui
import numpy as np
import plotly.graph_objects as go

def create_attack_plot():
    """Create a sample attack visualization plot"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Attack Pattern'))
    fig.update_layout(
        title='Attack Visualization',
        xaxis_title='Time',
        yaxis_title='Intensity',
        showlegend=True
    )
    return fig

def setup_attack_ui():
    """Setup the attack UI components"""
    with ui.card().classes('w-full'):
        ui.label('Attack Options').classes('text-xl font-bold')
        
        # Create plot element
        plot_container = ui.plotly(create_attack_plot()).classes('w-full h-64')
        
        # Add some attack parameters
        with ui.row():
            intensity = ui.number('Attack Intensity', value=1.0, min=0.1, max=5.0)
            duration = ui.number('Duration (s)', value=10, min=1, max=60)
        
        def on_attack():
            perform_attack(plot_container, intensity.value, duration.value)
            
        ui.button('Launch Attack', on_click=on_attack)

def perform_attack(plot_container, intensity, duration):
    """Perform the attack operation"""
    ui.notify('Attack initiated!')
    
    # Update the plot with new random data
    x = np.linspace(0, duration, 100)
    y = np.sin(x) * intensity + np.random.random(100) * 0.5
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Live Attack'))
    fig.update_layout(
        title='Live Attack Visualization',
        xaxis_title='Time',
        yaxis_title='Intensity',
        showlegend=True
    )
    
    # Update the plot
    plot_container.update_figure(fig) 
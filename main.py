import os
import pickle
from nicegui import app, ui
# from modules.dataset import setup_dataset_ui, setup_normal_ui, load_dataset, app_state
from modules.attack import setup_attack_ui
from secml.data.loader import CDataLoaderCIFAR10

def save_state(state):
    with open('app_state.pkl', 'wb') as f:
        pickle.dump(state, f)

def load_state():
    if os.path.exists('app_state.pkl'):
        with open('app_state.pkl', 'rb') as f:
            return pickle.load(f)
    return None

class AppState:
    def __init__(self):
        self.dataset = None
        self.normal = None

@ui.page('/')
async def index():
    await ui.context.client.connected() 
    with ui.tabs() as tabs:
        tab_dataset = ui.tab('Dataset')
        tab_normal = ui.tab('Baseline')
        tab_attack = ui.tab('Attacking')
        tab_defend = ui.tab('Defending')
    with ui.tab_panels(tabs, value=tab_dataset).classes('w-full'):
        with ui.tab_panel(tab_dataset):
            setup_dataset_ui()
        with ui.tab_panel(tab_normal):
            setup_normal_ui()
        with ui.tab_panel(tab_attack):
            setup_attack_ui()
        with ui.tab_panel(tab_defend):
            with ui.card():
                ui.label('Defending')
                ui.button('Defend')

def setup_dataset_ui():
    with ui.card().classes('w-full'):
        ui.label('Dataset').classes('text-xl font-bold')
        ui.button('Load Dataset', on_click=load_dataset)
    with ui.column().bind_visibility_from(app_state, 'dataset'):
        with ui.card().classes('w-full').style('height: 100px;') as card:
            with ui.row():
                ui.label('Dataset').classes('text-xl font-bold')
                print(app_state.dataset[0].X)
                ui.button('Load Dataset', on_click=load_dataset)
        
def load_dataset():
    ui.notify('Loading dataset...')
    loader = CDataLoaderCIFAR10()
    app_state.dataset = loader.load()
    save_state(app_state)
    ui.notify('Dataset loaded')
    
def setup_normal_ui():
    with ui.card().classes('w-full'):
        ui.label('Normal').classes('text-xl font-bold')
        ui.button('Load Normal')
        ui.button('Create Normal')
        ui.button('Delete Normal')
        ui.button('Save Normal')
                
if __name__ in {"__main__", "__mp_main__"}:
    app_state = load_state()
    if app_state == None:
        app_state = AppState()
        
    ui.run(port=8080, storage_secret='1234567890', reload=True, title="Security-AI")

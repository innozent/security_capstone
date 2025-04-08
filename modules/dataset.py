# from nicegui import app, ui
# from secml.data.loader import CDataLoaderCIFAR10

# def setup_dataset_ui():
#     with ui.card().classes('w-full'):
#         ui.label('Dataset').classes('text-xl font-bold')
#         ui.button('Load Dataset', on_click=load_dataset)
#     with ui.column().bind_visibility_from(app.storage.tab['app_state'], 'dataset'):
#         with ui.card().classes('w-full').style('height: 100px;') as card:
#             with ui.row():
#                 ui.label('Dataset').classes('text-xl font-bold')
#                 ui.button('Load Dataset', on_click=load_dataset)
        
# def load_dataset():
#     ui.notify('Loading dataset...')
#     loader = CDataLoaderCIFAR10()
#     app_state.dataset = loader.load()
#     app.storage.tab['app_state'] = app_state
#     ui.notify('Dataset loaded')
#     print(app.storage.tab.keys())
    
# def setup_normal_ui():
#     with ui.card().classes('w-full'):
#         ui.label('Normal').classes('text-xl font-bold')
#         ui.button('Load Normal')
#         ui.button('Create Normal')
#         ui.button('Delete Normal')
#         ui.button('Save Normal')
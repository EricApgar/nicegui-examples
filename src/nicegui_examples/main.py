from nicegui import ui

from nicegui_examples.widgets.main import MainWidget


with ui.row().classes('gap-6'):
    MainWidget()

ui.run(title='Hello World', port=8000)  # reload=False
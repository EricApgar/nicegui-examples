import weakref

from nicegui import ui

from nicegui_examples.elements.buttons import ButtonOnOff


class LedControlWidget:
    def __init__(self, parent=None) -> None:
        
        self.parent = weakref.proxy(parent)

        self.is_button_on: bool=False


        ui.label(text='LED Controls').classes('text-md font-medium')
        with ui.row().classes('items-center gap-4'):
            self.button_on_off = ButtonOnOff()


class VirtualLed:
    def __init__(self):
        pass

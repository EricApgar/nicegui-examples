from typing import Callable

from nicegui import ui


class ButtonOnOff:
    '''
    A simple on/off button with color change.
    '''

    def __init__(self, parent=None, callback: Callable=None):

        self.parent = parent

        self.callback = callback
        self.is_on: bool = False

        self.button: ui.button = ui.button(
            text='OFF',
            on_click=self.on_toggle
            ).props('push color=grey outline')


    def on_toggle(self) -> None:

        if self.is_on:
            self.button.props('push color=yellow outline')

            if self.callback is not None:
                self.callback()
            
            self.button.text = 'OFF'
            self.button.props('push color=red outline')

            self.is_on = False

        else:
            self.button.props('push color=yellow outline')

            if self.callback is not None:
                self.callback()

            self.button.text = 'ON'
            self.button.props('push color=green')

            self.is_on = True

        return


    def set_callback(self, callback: Callable):

        self.button.on_click = callback

        return

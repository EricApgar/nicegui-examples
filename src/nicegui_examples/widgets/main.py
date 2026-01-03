import weakref
import queue

from nicegui import ui

from nicegui_examples.widgets.led_control import LedControlWidget
from nicegui_examples.widgets.connection import ConnectionWidget


class MainWidget:
    def __init__(self):

        self.led: LedControlWidget = None

        self.log_queue: 'queue.Queue[str]' = queue.Queue()
        self.log_area: ui.textarea = None
        self.log_button: ui.button = None
        self.log_timer: ui.timer = None

        with ui.card().classes('w-[40rem]'):
            ui.label(text='Button Widget').classes('text-lg font-medium w-full text-center')

            ui.separator()

            self.led = LedControlWidget(parent=self)

            # ui.separator()

            # self.connection = ConnectionWidget(parent=self)

            ui.separator()

            self.log_area = ui.textarea(
                label='Log',
                placeholder='Logs appear here...',
                value=''
                ).props('readonly').classes('w-full').style('height: 220px; overflow:auto')

            self.log_button = ui.button(
                text='Clear Log',
                on_click=self.clear_log,
                ).props('push color=primary')

        self.log_timer = ui.timer(
            interval=0.2,
            callback=self.flush_logs,
            active=True)


    def flush_logs(self) -> None:

        updated: bool = False
        while True:
            try:
                line = self.log_queue.get_nowait()
            except queue.Empty:
                break
            else:
                self.log_area.value = (self.log_area.value + line + '\n').lstrip()
                updated = True

        return


    def clear_log(self) -> None:

        self.log_area = ''

        return

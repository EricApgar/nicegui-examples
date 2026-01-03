import weakref

from nicegui import ui


class LedControlWidget:
    def __init__(self, parent=None) -> None:
        
        self.parent = weakref.proxy(parent)

        self.button: ui.button = None
        self.button_is_on: bool = False

        self.rate_select: ui.number = None

        self.led: ui.element = None
        self.led_is_lit: bool = False

        ui.label(text='LED Controls').classes('text-md font-medium')
        with ui.row().classes('items-center gap-4'):
            self.button = ui.button(
                text='OFF',
                on_click=self.on_toggle
                ).props('push color=grey outline')

            self.rate_select = ui.number(
                label='Rate (Hz)',
                value=1,
                min=1,
                max=10,
                step=1,
                format='%.0i',
                ).classes('w-15')
            self.rate_select.on('change', lambda e: self.on_rate_select_change(e))

            self.led = ui.element('div').classes('w-6 h-6 rounded-full bg-gray-700 border border-gray-500')
            self.led_timer = ui.timer(
                interval=0.5,
                callback=self.flip_led_color,
                active=False)


    def on_toggle(self, e) -> None:

        if self.button_is_on:  # Button already on, turn off.
            self.button.text = 'OFF'
            self.button.props('push color=red outline')

            self.led_timer.active = False
            self.set_led_color(on=False)

        else:  # Button already off, turn on.
            self.button.text = 'ON'
            self.button.props('push color=green')

            self.led_timer.active = True

        self.button_is_on = not self.button_is_on

        return


    def on_rate_select_change(self, e):

        self.led_timer.interval = 1 / (2 * self.rate_select.value)

        return
    

    def flip_led_color(self) -> None:

        on = False if self.led_is_lit else True

        self.set_led_color(on=on)

        self.led_is_lit = not self.led_is_lit

        return


    def set_led_color(self, on: bool) -> None:

        if on:  # Set to on color.
            self.led.classes(
                remove='bg-gray-700 border-gray-500',
                add='bg-blue-500 border-blue-300 shadow-lg')
        else:  # Set to off color.
            self.led.classes(
                remove='bg-blue-500 border-blue-300 shadow-lg',
                add='bg-gray-700 border-gray-500')

        return

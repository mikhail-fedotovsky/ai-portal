import copilot
from nicegui import ui

image = "../static/ai.jpeg"

copilot.create()


ui.markdown('[AI Portal](http://127.0.0.1:8080)').classes('text-h3 absolute-upper text-left')

with ui.row().classes('w-full flex items-center justify-center gap-0'):
    with ui.card().style('width: 33%; display: inline-block;'):
        with ui.link(target="/copilot"):
            ui.image(image).style('width: 100%')
        with ui.card_section():
            ui.label('Copilot').classes('text-h3 absolute-bottom text-right')
    with ui.card().style('width: 33%; display: inline-block;'):
        with ui.link(target="/sql"):
            ui.image(image).style('width: 100%')
        with ui.card_section():
            ui.label('SQL генератор').classes('text-h3 absolute-bottom text-right')
    with ui.card().style('width: 33%; display: inline-block;'):
        with ui.link(target="/summary"):
            ui.image(image).style('width: 100%')
        with ui.card_section():
            ui.label('Суммаризатор').classes('text-h3 absolute-bottom text-right')

with ui.row().classes('w-full flex items-center justify-center gap-0'):
    with ui.card().classes('w-4/12 inline-block no-shadow no-border'):
        with ui.link(target="/idea"):
            ui.image(image).classes('w-full')
        with ui.card_section():
            ui.label('Генератор идей').classes('text-h3 absolute-bottom text-right')
    with ui.card().classes('w-4/12 inline-block no-shadow no-border'):
        ui.image(image).classes('w-full')
        with ui.card_section():
            ui.label('Confluence').classes('text-h3 absolute-bottom text-right')
    with ui.card().classes('w-4/12 inline-block no-shadow no-border'):
        ui.image(image).classes('w-full')
        with ui.card_section():
            ui.label('........').classes('text-h3 absolute-bottom text-right')

ui.run(title='AI Portal')

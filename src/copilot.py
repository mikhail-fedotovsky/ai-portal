from typing import List, Tuple
from nicegui import context, ui

import open_ai


def create() -> None:
    @ui.page('/copilot')
    def main():
        chain_with_history = open_ai.create_chain(
            model="openchat:7b",
            base_url='http://localhost:11434/v1/',
            temp=0
        )

        messages: List[Tuple[str, str]] = []
        thinking: bool = False

        @ui.refreshable
        def chat_messages() -> None:
            for name, text in messages:
                ui.chat_message(text=text, name=name, sent=name == 'You')
            if thinking:
                ui.spinner(size='3rem').classes('self-center')
            if context.get_client().has_socket_connection:
                ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')

        async def send() -> None:
            nonlocal thinking
            message = text.value
            messages.append(('You', text.value))
            thinking = True
            text.value = ''
            chat_messages.refresh()

            messages.append(('AI', ''))
            async for chunks in chain_with_history.astream({"input": message},
                                                           {"configurable": {"session_id": "unused"}}):
                thinking = False
                messages[-1] = ('AI', messages[-1][-1] + chunks)
                chat_messages.refresh()

        ui.add_style(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')

        # the queries below are used to expand the contend down to the footer (content can then use flex-grow to expand)
        ui.query('.q-page').classes('flex')
        ui.query('.nicegui-content').classes('w-full')

        with ui.tabs().classes('w-full') as tabs:
            chat_tab = ui.tab('Chat')
        with ui.tab_panels(tabs, value=chat_tab).classes('w-full max-w-2xl mx-auto flex-grow items-stretch'):
            with ui.tab_panel(chat_tab).classes('items-stretch'):
                chat_messages()

        with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
            with ui.row().classes('w-full no-wrap items-center'):
                placeholder = 'message'
                text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3') \
                    .classes('w-full self-center').on('keydown.enter', send)
            ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
                .classes('text-xs self-end mr-8 m-[-1em] text-primary')
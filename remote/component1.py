import inspect
import wwwpy.remote.component as wpc
import js

import logging

logger = logging.getLogger(__name__)


class Component1(wpc.Component, tag_name='component-1'):
    button1: js.HTMLButtonElement = wpc.element()

    def init_component(self):
        # language=html
        self.element.innerHTML = """
<div>component-1</div>
<button data-name="button1">button1</button>
"""

    async def after_init_component(self):
        import micropip
        await micropip.install('typing-extensions')

    async def button1__click(self, event):
        logger.debug(f'{inspect.currentframe().f_code.co_name} event fired %s', event)
        from pudb.remote import set_trace
        set_trace(reverse=True,port=12345)




import time
from pathlib import Path

from wwwpy.common import quickstart
from wwwpy.server import tcp_port
from wwwpy.server.configure import Project, setup
from wwwpy.server.convention import default_config, add_project
from wwwpy.server.settingslib import user_settings
from wwwpy.webservers.available_webservers import available_webservers

import logging

logger = logging.getLogger(__name__)

def start_default(directory: Path, port: int, dev_mode=False) -> Project:
    quickstart.warn_if_unlikely_project(directory)

    config = default_config(directory, dev_mode)
    config.remote_folders.add('pudb')
    config.remote_folders.add('urwid')
    config.remote_folders.add('wcwidth')
    config.remote_folders.add('urwid_readline')
    project = setup(config, user_settings())
    add_project(project)

    webserver = available_webservers().new_instance()
    webserver.set_routes(*project.routes)

    while tcp_port.is_port_busy(port):
        logger.warning(f'port {port} is busy, retrying...')
        [time.sleep(0.1) for _ in range(20) if tcp_port.is_port_busy(port)]

    webserver.set_port(port).start_listen()

    return project


if __name__ == '__main__':
    start_default(Path(__file__).parent.parent, 8000, dev_mode=True)
    while True:
        time.sleep(1000)
import os
from pathlib import Path

import hubbleds

NB_PATH = Path(hubbleds.__file__).parent / "HubbleDS.ipynb"
SERVICE_PREFIX = os.environ["JUPYTERHUB_SERVICE_PREFIX"]


c.ServerProxy.servers = {
    "test-server": {
        "command": ["python", "-m", "http.server", "{port}"],
        "absolute_url": False,
        "launcher_entry": {"title": "Test Server"},
    },
    "hubble": {
        "command": [
            "voila",
            f"{NB_PATH.resolve()}",
            "--port={port}",
            "--no-browser",
            "--debug",
            "--Voila.base_url={base_url}hubble/",
            "--Voila.server_url=/",
            "--Voila.tornado_settings={{'allow_origin': '*'}}",
            "--VoilaConfiguration.template=cosmicds-default",
            "--VoilaConfiguration.enable_nbextensions=true",
            "--VoilaConfiguration.file_whitelist=['.*']",
            "--VoilaConfiguration.show_tracebacks=true",
            "--VoilaConfiguration.http_keep_alive_timeout=30",
            "--VoilaConfiguration.iopub_timeout=100",
        ],
        "absolute_url": False,
        "launcher_entry": {"title": "Hubble Data Story"},
        "timeout": 15
    },
}

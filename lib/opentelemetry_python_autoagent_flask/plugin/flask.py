from opentelemetry_python_autoagent.plugin.base import BasePlugin


class FlaskPlugin(BasePlugin):

    def get_options(self):

        return {}


__all__ = ['FlaskPlugin']

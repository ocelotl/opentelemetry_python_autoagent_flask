from opentelemetry_python_autoagent.plugin.base import BasePlugin

from jaeger_client import Config
import flask


tracer = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
        'reporter_batch_size': 1,
    },
    service_name='opentelemetry_python_autoagent',
).initialize_tracer()


class FlaskPlugin(BasePlugin):

    def monkeypatch(self):

        class PatchedFlask(flask.Flask):

            def __init__(self, *args, **kwargs):

                super(PatchedFlask, self).__init__(*args, **kwargs)

                @self.before_request
                def start_trace():

                    print('before_request')

                @self.after_request
                def end_trace(response):

                    print('after_request')

                    return response

        flask.Flask = PatchedFlask


__all__ = ['FlaskPlugin']

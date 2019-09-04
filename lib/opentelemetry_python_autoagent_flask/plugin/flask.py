from opentracing.propagation import Format
from opentracing.ext.tags import (
    SPAN_KIND,
    SPAN_KIND_RPC_SERVER,
    COMPONENT,
    HTTP_METHOD,
    HTTP_URL,
)
from opentelemetry_python_autoagent.plugin.base import BasePlugin

# FIXME avoid a hard dependecy to a specific client
from jaeger_client import Config
import flask

from flask import request


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

                self._current_scope = None

                @self.before_request
                def start_trace():

                    scope = tracer.start_active_span(
                        request.endpoint,
                        child_of=tracer.extract(
                            Format.HTTP_HEADERS, request.headers
                        ),
                        tags={SPAN_KIND: SPAN_KIND_RPC_SERVER}
                    )

                    self._current_scope = scope

                    span = scope.span

                    span.set_tag(COMPONENT, 'Flask')
                    span.set_tag(HTTP_METHOD, request.method)
                    span.set_tag(HTTP_URL, request.base_url)
                    span.set_tag(SPAN_KIND, SPAN_KIND_RPC_SERVER)

                    print('before_request')

                @self.after_request
                def end_trace(response):

                    self._current_scope.close()

                    print('after_request')

                    return response

        flask.Flask = PatchedFlask


__all__ = ['FlaskPlugin']

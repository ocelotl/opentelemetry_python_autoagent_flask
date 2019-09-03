from importlib.util import spec_from_file_location, module_from_spec

from opentelemetry_python_autoagent.plugin.base import BasePlugin

from flask_opentracing import FlaskTracing


class FlaskPlugin(BasePlugin):

    def run(self, path, tracer):
        """
        Runs the file defined in path
        """

        spec = spec_from_file_location('flask.app', path)
        module = module_from_spec(spec)

        from ipdb import set_trace
        set_trace()

        spec.loader.exec_module(module)

        FlaskTracing(tracer, True, module.app)

        module.__name__ = '__main__'

        spec.loader.exec_module(module)


__all__ = ['FlaskPlugin']

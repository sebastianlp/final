from flask import render_template
from flask.views import View

class ListView(View):
    
    def get_template_name(self):
        raise NotImplementedError()
    
    def render_template(self, context):
        return render_template(self.get_template_name(), **context)
    
    def dispatch_request(self):
        # Mi variable context es enviada a la vista y tiene lo que necesito de informacion para mostrar en el listado
        context = {'objects': self.get_objects()}
        return self.render_template(context)
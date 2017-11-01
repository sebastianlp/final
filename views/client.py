from views.list import ListView

class ClientView(ListView):
    
    def get_template_name(self):
        return 'client.html'

    def get_objects(self):
        # aca va la query al csv
        return {'Client1'}
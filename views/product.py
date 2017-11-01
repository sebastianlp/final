from views.list import ListView

class ProductView(ListView):
    
    def get_template_name(self):
        return 'product.html'

    def get_objects(self):
        # aca va la query al csv
        return {'Product1'}
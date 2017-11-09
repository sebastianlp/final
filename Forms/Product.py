
from wtforms import Form, StringField, validators

class ProductForm(Form):
  productName = StringField('Producto', [validators.Length(min=3, max=25)])
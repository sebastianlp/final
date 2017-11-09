from wtforms import Form, StringField, validators

class ClientForm(Form):
  clientName = StringField('Cliente', [validators.Length(min=3, max=25)])
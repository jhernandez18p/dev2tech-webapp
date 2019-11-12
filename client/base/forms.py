from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class SuscribeForm(forms.Form):

    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )


class ContactForm(forms.Form):

    name = forms.CharField(
        label='Escriba su nombre',
        widget=forms.TextInput( attrs = {'placeholder': 'John Doe' } )
    )
    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )
    phone = forms.CharField(
        label='Escriba su número de teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    comment = forms.CharField(
        label="Escriba sus comentarios",
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'contacto'
        self.helper.layout = Layout(
            Field('name', css_class="form-control"),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('comment', css_class="form-control"),
            Submit('submit', 'Contactar')
        )


class QuotationForm(forms.Form):

    AMOUNT = (
        ('0-1K','0$ - 1,000.00$'),
        ('1K-5K','1,000.00$ - 5,000.00$'),
        ('5K-10K','5,000.00$ - 10,000.00$'),
        ('10K-15K','10,000.00$ - 15,000.00$'),
        ('unknown','No estoy seguro')
    )
    SERVICES = (
        ('web','Expertos digitales trabajando para ti.'),
        ('social media','Marketing digital al alcance de tus manos.'),
        ('email','Servicio de email profresional.'),
        ('cloud','Administración y mantenimiento de servicios en la nube.')
    )
    name = forms.CharField(
        label='Escriba su nombre',
        widget=forms.TextInput( attrs = {'placeholder': 'John Doe' } )
    )
    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )
    phone = forms.CharField(
        label='Escriba su número de teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    country = forms.CharField(
        label="País",
        widget=forms.TextInput(attrs={'placeholder': 'Pamamá'})
    )
    company = forms.CharField(
        label="Nombre de su empresa",
        widget=forms.TextInput(attrs={'placeholder': 'Dev2tech'})
    )
    invest = forms.ChoiceField(
        label="Monto de inversión",
        choices=AMOUNT
    )
    subject = forms.ChoiceField(
        label="Tipo de servicio",
        choices=SERVICES
    )
    comment = forms.CharField(
        label="Describa su proyecto",
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class="form-control"),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('subject', css_class='form-control'),
            Field('country', css_class='form-control'),
            Field('company', css_class='form-control'),
            Field('invest', css_class="form-control"),
            Field('comment', css_class="form-control"),
            Submit('submit', 'Solicitar Cotización')
        )


class PromoQuotationForm(forms.Form):

    AMOUNT = (
        ('450','Solo quiero pagar $450.00'),
        ('1K-5K','Si, de 1,000.00$ - 5,000.00$'),
        ('5K-10K','Si, de 5,000.00$ - 10,000.00$'),
        ('10K-15K','Si, 10,000.00$ - 15,000.00$'),
        ('unknown','No estoy seguro.')
    )

    name = forms.CharField(
        label='Escriba su nombre',
        widget=forms.TextInput( attrs = {'placeholder': 'John Doe' } )
    )

    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )
    
    phone = forms.CharField(
        label='Escriba su número de teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    
    country = forms.CharField(
        label="País",
        widget=forms.TextInput(attrs={'placeholder': 'Pamamá'})
    )
    
    company = forms.CharField(
        label="Nombre de su empresa",
        widget=forms.TextInput(attrs={'placeholder': 'Dev2tech'})
    )

    has_prev_web = forms.BooleanField(
        label="¿Tiene o ya ha tenido algún sitio web?",
        widget=forms.CheckboxInput(),
        required=True
    )
    
    invest = forms.ChoiceField(
        label="¿Estaría ud. dispuesto/a a invertir más de $450,00?",
        choices=AMOUNT
    )
    
    comment = forms.CharField(
        label="Describa como le gustaria que sea su nueva pagina web",
        widget=forms.Textarea()
    )

    add_support = forms.BooleanField(
        label="¿Le gustaría agregar soporte y mantenimiento por solo $33,00 / mes?",
        widget=forms.CheckboxInput(),
        required=True
    )

    add_email = forms.BooleanField(
        label="¿Le gustaría agregar 5 buzones de correo electrónico profesional por solo $25,00 / mes?",
        widget=forms.CheckboxInput(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class="form-control"),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('country', css_class='form-control'),
            Field('company', css_class='form-control'),
            Field('has_prev_web', css_class=''),
            Field('invest', css_class="form-control"),
            Field('comment', css_class="form-control"),
            Field('add_support', css_class=""),
            Field('add_email', css_class=""),
            Submit('submit', 'QUIERO MI SITIO WEB')
        )
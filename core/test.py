from django.test import TestCase
from core.forms import CasaForm
from core.models import Casa
from django.urls import reverse

class CasaModelTest(TestCase):
    
    @classmethod

    def test_name_label(self):
        casa=Casa.objects.get(id=1)
        field_label = casa._meta.get_field('direccion').verbose_name
        self.assertEquals(field_label,'direccion')

    def test_name_max_length(self):
        casa=Casa.objects.get(id=1)
        max_length = casa._meta.get_field('direccion').max_length
        self.assertEquals(max_length,100)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/templates/home/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_valid_form(self):
        g = Casa.objects.create(name='direccion', summary='comuna')
        data = {'name': g.name, 'summary': g.summary,}
        form = CasaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Casa.objects.create(name='', summary='')
        data = {'name': g.name, 'summary': g.summary,}
        form = CasaForm(data=data)
        self.assertFalse(form.is_valid())
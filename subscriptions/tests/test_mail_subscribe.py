from django.test import TestCase
from django.core import mail

# Create your tests here.



class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Guilherme', cpf='12345678901', email='guilherme.tavares@aluno.riogrande.ifrs.edu.br', phone='53 12345-1234')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
    
    
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'guilherme.tavares@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_Email_body(self):
        contents = (
            'Guilherme',
            '12345678901',
            'guilherme.tavares@aluno.riogrande.ifrs.edu.br',
            '53 12345-1234'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
from django.test import TestCase
from django.urls import reverse
from .models import Article
import datetime as dt

class ArticlesViewTest(TestCase):
    def test_articles_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 302)
        
    def test_articles_view_not_authenticated(self):
        
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('login'))

    def test_write_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('Write'))
        self.assertEqual(response.status_code, 302)
        data = {
            'title': 'Test Article',
            'content': 'This is a test article.',
            'tags': 'test, article',
        }
        response = self.client.post(reverse('Write'), data)
        self.assertEqual(response.status_code, 302)

    def test_write_view_not_authenticated(self):
        response = self.client.get(reverse('Write'))
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('login'))

    def test_myarticles_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('MyArticles'))
        self.assertEqual(response.status_code, 302)
        

    def test_myarticles_view_not_authenticated(self):
        response = self.client.get(reverse('MyArticles'))
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('login'))

    def test_crud_articles(self):
        obj = Article.objects.create(title="TEST",content="TEST",tags="TEST",files="TEST",author="TEST",date=dt.datetime.today())
        obj.save()
        obj = Article.objects.all()
        obj = Article.objects.filter(title="TEST")
        obj.update(
            title = "TESTY",
            content = "TESTY",
            tags = "TESTY",
            date = dt.datetime.today(),

        )
        obj = Article.objects.filter(title="TESTY")
        obj.delete()
        return True
    

    
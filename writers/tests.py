from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class WriterViewTest(TestCase):
    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'password': 'testpassword',
            're_enter': 'testpassword',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)


    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  


    def test_logout_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('login'))
        if '_auth_user_id' in self.client.session:
            self.assertFalse(self.client.session['_auth_user_id'])

    def test_logout_view_not_authenticated(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('login'))
    

    
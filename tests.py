import git
from django.test import TestCase
from django.urls import reverse


class HelloTestCase(TestCase):
    def test__index__verify_commit(self):
        commit_sha = git.Repo().commit().hexsha
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('commit', response.json())
        self.assertEqual(response.json()['commit'], commit_sha)

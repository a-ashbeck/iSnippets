from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.TextField()
    code_snippet = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        """ returns a human readable version of the Snippet object """
        return 'Title: {0}\n Language: {2}\n Snippet: {3}\n Description: {3}\n'.format(self.title, self.language, self.code_snippet, self.description)

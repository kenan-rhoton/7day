from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=200)
    block = models.CharField(max_length=200)

    def addToBlock(self, block):
        self.block = block

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sections = models.ManyToManyField(Section)

    def addSection(self, s):
        self.sections.add(s)
        self.save()

from django.db import models

class AuthorManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    objects = AuthorManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return f"{self.id} {self.name}"

class BookManager(models.Manager):
    def get_by_natural_key(self, title, author): # OR title, author ??
        return self.get(title=title, author__name=author)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, models.DO_NOTHING, related_name="books")

    objects = BookManager()

    def natural_key(self):
        return (self.title,) + self.author.natural_key()

    natural_key.dependencies = ["testbug.Author"]

    class Meta:
        unique_together = [["title", "author"]]

    def __str__(self):
        return f"{self.id}: '{self.title}' by {self.author}"

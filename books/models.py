from django.db import models
from django.contrib import admin
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	def __str__(self):
		return self.name

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	haeadshot = models.ImageField(upload_to='/tmp')
	def __str__(self):
		return '%s %s' %(self.first_name,self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	atuhors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	def __str__(self):
		return self.title
class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date')
	list_filter = ('publisher','publication_date')
	ordering = ('-publication_date',)
	search_fields = ('title',)


admin.site.register(Book,BookAdmin)
# Create your models here.

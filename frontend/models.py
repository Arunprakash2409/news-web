from django.db import models


# Category's
class category(models.Model):
    title = models.CharField(max_length = 500)
    category_image = models.ImageField(upload_to = 'image/')
    
    # change pruler into singlear
    class Meta:
        verbose_name_plural = 'categories'



    def __str__(self):
        return self.title

# new's
class News(models.Model):
    #link the catagery
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = 'image/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    keyword = models.TextField()

    # change pruler into singlear

    class Meta:
        # to display the data in reverse
        ordering = ['-id']
        verbose_name_plural = 'News'


    def __str__(self):
        return self.title



# commands or reviews
class comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length= 200)
    command = models.TextField()
    status = models.BooleanField(default=False)



    def __str__(self):

        return self.command



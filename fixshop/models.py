from django.db.models import  CharField, IntegerField, ImageField, \
    BooleanField, AutoField, ForeignKey, ManyToManyField, Model, FileField

# Create your models here.
class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    price = IntegerField(default=0)
    desc = CharField(max_length=1000)
    picture = FileField(upload_to='items')
    views_count = IntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(Model):
    id = AutoField(primary_key=True)
    checkouted = BooleanField(default=False)
    session = CharField(max_length=100, verbose_name='user who bought', null=True)
    items = ManyToManyField(Item, verbose_name='items in cart')


class ItemViews(Model):
    session = CharField(max_length=100, verbose_name='user who bought', null=True)
    item_id = ForeignKey(Item, verbose_name='what item')







#poll = models.ForeignKey(Poll, verbose_name="the related poll")
#sites = models.ManyToManyField(Site, verbose_name="list of sites")
#place = models.OneToOneField(Place, verbose_name="related place")
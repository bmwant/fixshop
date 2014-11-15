import os
from django.contrib import admin
from django.conf import settings

# Register your models here.

from fixshop.models import Item


from django import forms



class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item

    picture = forms.FileField()

    """
    def clean_picture(self):
        data = self.cleaned_data['picture']
        # upload
        #print(data, type(data))
        #self.save_picture(data)
        return data


    def save_picture(self, pic_file):
        FOLDER_PATH = os.path.join(settings.BASE_DIR, 'static/images')
        file_name = os.path.join(FOLDER_PATH, pic_file.name)
        with open(file_name, 'wb+') as destination:
            for chunk in pic_file.chunks():
                destination.write(chunk)
    """

class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm




admin.site.register(Item, ItemAdmin)
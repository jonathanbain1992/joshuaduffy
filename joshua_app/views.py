from django.shortcuts import *
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class index(TemplateView):
    #template_name = 'index.html'

    context_dict = {}
    context_dict['signup_title'] = "lets be friends"
    context_dict['bio_title'] = "Hello World."
    context_dict['bio_content'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id faucibus orci. Morbi libero erat, dictum sit amet pharetra eget, fringilla at turpis. Quisque nec ipsum fermentum nulla finibus tincidunt quis quis magna. Ut eu porttitor diam. Morbi ut justo venenatis, porta metus sed, scelerisque mi. Mauris vel risus nec lectus elementum pellentesque et et orci. Integer vel sagittis felis, eget scelerisque nunc. Ut libero lorem, congue vel fringilla"
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", self.context_dict)

class about(TemplateView):
    #template_name = 'index.html'

    context_dict = {}
    context_dict["test_text"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eget pulvinar tortor. Donec vulputate ex eget sapien iaculis facilisis. Donec a felis accumsan, eleifend mi eget, condimentum massa. Sed ut condimentum felis, eget tristique quam. Morbi imperdiet, mauris non fringilla sodales, elit magna consequat ligula, eget dictum erat nulla et urna. Pellentesque blandit erat ac sagittis lacinia. Nulla congue neque vehicula felis ullamcorper, et finibus tellus maximus. Pellentesque eget ante id augue ultricies vestibulum in vel dui. Nam fringilla velit at consectetur feugiat.Cras at imperdiet sem. Nulla luctus venenatis risus, eu consequat arcu pretium id. Etiam sed interdum magna. Nam sodales vulputate mattis. Pellentesque laoreet purus orci, vel viverra magna blandit vitae. Phasellus lobortis euismod metus a egestas. Nunc suscipit dolor et justo congue, ut convallis sem facilisis. Vivamus aliquet, nibh vitae blandit ultricies, eros sapien porta vestibulum elit libero in lectus. Proin molestie sapien nisi, vitae condimentum libero tincidunt sed. Donec at urna interdum erat pharetra pulvinar ac id felis. Ut quis euismod enim. Mauris eros nisl, porttitor ac vulputate a, mollis et felis. Aenean ex diam, feugiat ut commodo ut, mattis a libero. Ut ac volutpat dui, ut luctus leo."
    def get(self, request, *args, **kwargs):
        return render(request, "about.html", self.context_dict)

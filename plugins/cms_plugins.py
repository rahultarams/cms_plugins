import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import Properties


@plugin_pool.register_plugin
class PropertieslistingPlugin(CMSPluginBase):

    name = _("Properties listing")
    model = Properties
    render_template = "listing.html"



    def render(self, context, instance, placeholder):
        #property_id = context['property_id']
        context['properties'] = Properties.objects.all()
        return context


@plugin_pool.register_plugin
class PropertyDetailPlugin(CMSPluginBase):
    name = _("Properties Detail")
    model = Properties
    render_template = 'property_detail.html'
    #allow_children = False

    def render(self, context, instance, placeholder):
        property_id = instance.id
        print("render executed")
        print(instance.name)
        context['property'] = Properties.objects.get(pk=property_id)
        return context

#plugin_pool.register_plugin(PropertyDetailPlugin)

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
        #if context['request'].LANGUAGE_CODE == 'ar':
        #    self.render_template = 'arabic.html'
        print(context['request'].LANGUAGE_CODE)
        context['properties'] = Properties.objects.all()
        return context


@plugin_pool.register_plugin
class PropertyDetailPlugin(CMSPluginBase):
    name = _("Properties Detail")
    model = Properties
    render_template = 'property_detail.html'
    #allow_children = False

    def render(self, context, instance, placeholder):
        req = context['request']
        param1 = req.GET.get('param1')
        context['property'] = Properties.objects.get(pk=param1)
        return context

#plugin_pool.register_plugin(PropertyDetailPlugin)

# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'

def global_vars(request):
    if hasattr(request, 'cart'):
        return {'cart': request.cart}
    return {}

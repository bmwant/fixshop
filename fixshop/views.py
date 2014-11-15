import json
import operator
import random
from functools import wraps, partial
from django.shortcuts import render_to_response, get_object_or_404, \
    redirect
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from django.conf import settings

from fixshop.models import Item, Cart, ItemViews


#todo: add needed variables to locals of decorated functions
def load_cart(view):
    """
    Load cart before each request
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        my_cart = request.session.get('cart_id')
        request.ses_id = request.session._get_or_create_session_key()
        if my_cart:
            cart = Cart.objects.get(pk=my_cart)
        else:
            cart = Cart(session=request.ses_id)
            cart.save()
            request.session['cart_id'] = cart.id
        request.cart = cart

        res = view(request, *args, **kwargs)
        return res
    return wrapper


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def best_matches(items_dict, sample_count=10):
    """
    Gets a dictionare with items, sorts it by values and
    returns a list of best matches or random sample from 10 first best mathces
    """
    items_limit = settings.RELATED_ITEMS
    dict_sorted = sorted(items_dict.items(), key=operator.itemgetter(1))
    dict_sorted = dict_sorted[:sample_count]
    random.shuffle(dict_sorted)
    dict_sorted = dict_sorted[:items_limit]
    return [x[0] for x in dict_sorted]


def related_data(item, better_ux=True):
    samle_count = settings.RELATED_ITEMS
    if better_ux:
        samle_count = 10

    viewed_with_me = {}

    ItemViews.objects.update()
    # exact user that has watched list of items
    unique_sessions = set()

    for item_view in ItemViews.objects.all():
        unique_sessions.add(item_view.session)

    for ses in unique_sessions:
        is_my_item = ItemViews.objects.filter(session=ses, item_id=item)
        if is_my_item:
            views_for_ses = ItemViews.objects.filter(session=ses)
            for ses_view in views_for_ses:
                c_item = ses_view.item_id
                if c_item in viewed_with_me:  # for big amount of data use id of item as key instead of item
                    viewed_with_me[c_item] += 1
                else:
                    viewed_with_me[c_item] = 0

    viewed_with_me = best_matches(viewed_with_me, samle_count)
    if item in viewed_with_me:
        viewed_with_me.remove(item)

    Cart.objects.update()
    carts = Cart.objects.all()
    in_cart_with_me = {}
    for c_cart in carts:
        if item in c_cart.items.all():
            for c_item in c_cart.items.all():
                if c_item in in_cart_with_me:
                    in_cart_with_me[c_item] += 1
                else:
                    in_cart_with_me[c_item] = 1

    in_cart_with_me = best_matches(in_cart_with_me, samle_count)
    if item in in_cart_with_me:
        in_cart_with_me.remove(item)
        

    bought_with_me = {}
    try:
        carts = carts.filter(checkouted=True)
        for c_cart in carts:
            if item in c_cart.items.all():
                for c_item in c_cart.items.all():
                    if c_item in bought_with_me:
                        bought_with_me[c_item] += 1
                    else:
                        bought_with_me[c_item] = 1
        if item in bought_with_me:
            del bought_with_me[item]
    except Cart.DoesNotExist:
        pass

    bought_with_me = best_matches(bought_with_me, samle_count)
    if item in bought_with_me:
        bought_with_me.remove(item)

    return {
        'in_cart_with_me': in_cart_with_me,
        'bought_with_me': bought_with_me,
        'viewed_with_me': viewed_with_me
    }

@load_cart
def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))



@load_cart
def cart(request):
    c_cart = request.cart
    items = c_cart.items.all()
    total_sum = 0
    for item in items:
        total_sum += item.price
    return render_to_response('cart.html', {'items': items, 'total_sum': total_sum, 'cart': c_cart})


@load_cart
def grid(request):
    """
    List all our items for very one category
    """
    items = Item.objects.all()
    return render_to_response('grid.html', {'items': items, 'cart': request.cart})


@load_cart
def item_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_views = ItemViews.objects.get_or_create(session=request.ses_id, item_id=item)
    item.views_count += 1
    item.save()
    context_dict = {'item': item, 'cart': request.cart}
    context_dict.update(related_data(item))
    return render_to_response('view.html', context_dict)


@load_cart
def add_to_cart(request, item_id):
    cart = request.cart
    item = Item.objects.get(pk=item_id)
    cart.items.add(item)

    return HttpResponse(cart.items.count())

@load_cart
def clear_cart(request):
    """
    Remove all items from cart
    """
    cart = request.cart
    cart.items.clear()
    cart.save()
    return redirect('cart')


@load_cart
def checkout(request):
    """
    Mark all items in cart as purchased
    """
    cart = request.cart
    cart.checkouted = True
    cart.save()
    new_cart = Cart()
    new_cart.save()
    request.session['cart_id'] = new_cart.id
    return HttpResponse('Ok')

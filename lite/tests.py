from django.test import TestCase

# Create your tests here.


def func(shop_id,**kwargs):
    print shop_id,kwargs

func(1,a=1,b=2)
func(1,**{'a':1,'b':2})
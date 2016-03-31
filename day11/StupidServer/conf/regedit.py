#!/usr/bin/env python3
#_*_coding:utf-8_*_


from core import views
actions = {
    "syncdb":views.syncdb,
    "insertdata":views.insert_data,
    "initialize":views.initialize,
    # "syncdb":views.syncdb,
    # "syncdb":views.syncdb,
}
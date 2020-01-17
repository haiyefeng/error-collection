# -*- coding: utf-8 -*-
__author__ = u"孺牛系统"
__copyright__ = "Copyright © 2012-2017 Tencent BlueKing. All Rights Reserved."

from rest_framework.routers import DefaultRouter, DynamicRoute, Route


class CustomDefaultRouter(DefaultRouter):
    routes = [
        # List route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        # Dynamically generated list routes.
        # Generated using @list_route decorator
        # on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes.
        # Generated using @detail_route decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
        Route(
            url=r'^remote/{prefix}{trailing_slash}$',
            mapping={
                'get': 'get_requests',
                'post': 'post_requests',
                'put': 'put_requests',
                'delete': 'delete_requests',
            },
            name='{basename}-request',
            initkwargs={'suffix': 'Request'}
        )
    ]

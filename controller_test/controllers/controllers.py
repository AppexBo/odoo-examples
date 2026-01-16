# -*- coding: utf-8 -*-
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http

class WebsiteSale(WebsiteSale):
    def _prepare_checkout_page_values(self, order_sudo, **query_params):
        response = super()._prepare_checkout_page_values(order_sudo, **query_params)
        response['custom_value'] = 'Hello, world'
        return response

    def _get_shop_payment_values(self, order, **kwargs):
        response = super()._get_shop_payment_values(order, **kwargs)
        response['custom_value'] = 'Hello, world'
        return response
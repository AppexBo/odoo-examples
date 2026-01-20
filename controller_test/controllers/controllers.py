from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.blog.controllers.controllers import BlogController
from odoo.http import Controller, request, route


class WebsiteSaleExtended(WebsiteSale):
    def _prepare_checkout_page_values(self, order_sudo, **query_params):
        response = super()._prepare_checkout_page_values(order_sudo, **query_params)
        response['custom_value'] = 'Hello, world'
        return response

    def _get_shop_payment_values(self, order, **kwargs):
        response = super()._get_shop_payment_values(order, **kwargs)
        response['custom_value'] = 'Hello, world'
        return response


class BlogControllerExtended(BlogController):
    @route('/blog/api/entries', type='json', auth='public', methods=['POST'])
    def get_entries_json(self, limit=10, offset=0, include_content=False, **kw):
        response = super().get_entries_json(limit=limit, offset=offset, **kw)
        if include_content:
            for entry in response['entries']:
                blog_entry = request.env['blog.entry'].sudo().browse(entry['id'])
                entry['content'] = blog_entry.content
        return response

    @route('/blog/api/stats', type='json', auth='public', methods=['POST'])
    def get_blog_stats_json(self, **kw):
        total_entries = request.env['blog.entry'].sudo().search_count([])
        total_tags = request.env['blog.tag'].sudo().search_count([])
        entries_by_author = {}
        for entry in request.env['blog.entry'].sudo().search([]):
            author_name = entry.author_id.name if entry.author_id else 'Unknown'
            entries_by_author[author_name] = entries_by_author.get(author_name, 0) + 1
        return {
            'total_entries': total_entries,
            'total_tags': total_tags,
            'entries_by_author': entries_by_author,
        }
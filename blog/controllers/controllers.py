from odoo.http import Controller, request, route


# ObjectController
class BlogController(Controller):
    @route('/blog/api/entries', type='json', auth='public', methods=['POST'])
    def get_entries_json(self, limit=10, offset=0, **kw):
        entries = request.env['blog.entry'].sudo().search_read(
            [],
            ['id', 'title', 'slug', 'author_id', 'create_date'],
            limit=limit,
            offset=offset,
            order='create_date desc'
        )
        total = request.env['blog.entry'].sudo().search_count([])
        return {
            'entries': entries,
            'total': total,
            'limit': limit,
            'offset': offset,
        }

    @route('/blog/api/entry/<int:entry_id>', type='json', auth='public', methods=['POST'])
    def get_entry_json(self, entry_id, **kw):
        entry = request.env['blog.entry'].sudo().browse(entry_id)
        if not entry.exists():
            return {'error': 'Entry not found'}
        return {
            'title': entry.title,
            'content': entry.content,
            'slug': entry.slug,
            'author_id': [entry.author_id.id, entry.author_id.name],
            'create_date': entry.create_date.isoformat() if entry.create_date else None,
            'tags': [{'id': tag.id, 'name': tag.name} for tag in entry.tag_ids],
        }

    @route('/blog/api/search', type='json', auth='public', methods=['POST'])
    def search_entries_json(self, query='', limit=10, **kw):
        domain = [('title', 'ilike', query)] if query else []
        entries = request.env['blog.entry'].sudo().search_read(
            domain,
            ['id', 'title', 'slug'],
            limit=limit,
            order='create_date desc'
        )
        return {
            'query': query,
            'entries': entries,
            'count': len(entries),
        }
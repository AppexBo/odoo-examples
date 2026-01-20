from odoo import http
from odoo.http import Controller, request, route


class ExampleController(Controller):
    @route('/examples/hello', type='http', auth='public', website=False)
    def hello_world(self, **kw):
        return request.make_response('<h1>Hello World from Controller!</h1>')

    @route('/examples/records', type='http', auth='user', website=False)
    def list_records(self, **kw):
        records = request.env['example.record'].search([])
        return request.render(
            'examples_advanced.records_list_template',
            {
                'records': records,
            }
        )

    @route('/examples/record/<int:record_id>', type='http', auth='user', website=False)
    def view_record(self, record_id, **kw):
        record = request.env['example.record'].browse(record_id)
        if not record.exists():
            return request.not_found()
        return request.render(
            'examples_advanced.record_detail_template',
            {
                'record': record,
            }
        )

    @route('/examples/api/data', type='json', auth='user', methods=['POST'])
    def get_data_json(self, **kw):
        records = request.env['example.record'].search([])
        return {
            'count': len(records),
            'records': [{
                'id': r.id,
                'name': r.name,
                'value': r.value,
            } for r in records],
        }

    @route('/examples/api/count', type='json', auth='public', methods=['GET', 'POST'])
    def get_count(self, **kw):
        count = request.env['example.record'].get_records_count()
        return {'count': count}
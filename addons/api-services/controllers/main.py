import json
from odoo import http
from odoo.http import request, Response

class ApiServiceController(http.Controller):

    @http.route('/api/services', auth='public', methods=['GET'], type='json', cors='*')
    def list_services(self, **kwargs):
        services = request.env['api.service'].sudo().search([])
        result = []
        for service in services:
            result.append({
                'id': service.id,
                'name': service.name,
                'description': service.description,
            })
        return result

    @http.route('/api/services', auth='public', methods=['POST'], type='json', cors='*')
    def create_service(self, **post):
        # Espera JSON con keys: name, description
        try:
            name = post.get('name')
            description = post.get('description', '')
            if not name:
                return {'error': 'El campo name es obligatorio.'}
            service = request.env['api.service'].sudo().create({
                'name': name,
                'description': description,
            })
            return {
                'id': service.id,
                'name': service.name,
                'description': service.description,
            }
        except Exception as e:
            return {'error': str(e)}

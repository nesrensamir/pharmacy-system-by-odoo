 -*- coding: utf-8 -*-
 from odoo import http


 class Os21Pharmacy(http.Controller):
     @http.route('/os21_pharmacy/os21_pharmacy/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/os21_pharmacy/os21_pharmacy/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('os21_pharmacy.listing', {
             'root': '/os21_pharmacy/os21_pharmacy',
             'objects': http.request.env['os21_pharmacy.os21_pharmacy'].search([]),
         })

     @http.route('/os21_pharmacy/os21_pharmacy/objects/<model("os21_pharmacy.os21_pharmacy"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('os21_pharmacy.object', {
             'object': obj
         })

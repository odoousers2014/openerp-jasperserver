# -*- coding: utf-8 -*-
##############################################################################
#
#    jasper_server module for OpenERP
#    Copyright (c) 2008-2009 EVERLIBRE (http://everlibre.fr) Eric VERNICHON
#    Copyright (C) 2009 SYLEAM ([http://www.syleam.fr]) Christophe CHAUVET
#
#    This file is a part of jasper_server
#
#    jasper_server is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasper_server is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see [http://www.gnu.org/licenses/].
#
##############################################################################

{
    'name': 'Jasper Server Interface',
    'version': '0.2',
    'category': 'Tools',
    'description': """This module interface JasperServer For Reports.""",
    'author': 'Everlibre,SYLEAM',
    'website': 'http://everlibre.fr',
    'depends': [
        'base',
    ],
    'init_xml': [],
    'update_xml': [
        'view/menu.xml',
        'view/oojasper.xml',
        #'report/report.xml',
        'wizard/wizard.xml',
    ],
    'demo_xml': [],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

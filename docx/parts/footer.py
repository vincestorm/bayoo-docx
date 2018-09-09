# encoding: utf-8

"""|FooterPart| and closely related objects"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from docx.opc.part import XmlPart


class FooterPart(XmlPart):
    """Package part containing a footer."""

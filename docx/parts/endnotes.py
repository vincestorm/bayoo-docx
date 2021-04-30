from __future__ import absolute_import, division, print_function, unicode_literals

from ..opc.constants import CONTENT_TYPE as CT
from ..opc.packuri import PackURI
from ..opc.part import XmlPart
from ..oxml import parse_xml

import os

class EndnotesPart(XmlPart):
    """
    Definition of Endnotes Part
    """
    @classmethod
    def default(cls, package):
        partname = PackURI("/word/endnotes.xml")
        content_type = CT.WML_ENDNOTES
        element = parse_xml(cls._default_endnotes_xml())
        return cls(partname, content_type, element, package)

    @classmethod
    def _default_endnotes_xml(cls):
        path = os.path.join(os.path.split(__file__)[0], '..', 'templates', 'default-endnotes.xml')
        with open(path, 'rb') as f:
           xml_bytes = f.read()
        return xml_bytes
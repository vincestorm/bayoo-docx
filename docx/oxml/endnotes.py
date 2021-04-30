"""
Custom element classes related to the footnotes part
"""

from . import OxmlElement
from .simpletypes import ST_DecimalNumber, ST_String
from ..text.paragraph import Paragraph
from ..text.run import Run
from ..opc.constants import NAMESPACE
from .xmlchemy import (
    BaseOxmlElement, OneAndOnlyOne, RequiredAttribute, ZeroOrMore, ZeroOrOne
)


class CT_Endnotes(BaseOxmlElement):
    """
    A ``<w:footnotes>`` element, a container for Footnotes properties
    """

    endnote = ZeroOrMore('w:endnote', successors=('w:endnotes',))

    @property
    def _next_id(self):
        ids = self.xpath('./w:endnote/@w:id')

        return int(ids[-1]) + 1

    def add_endnote(self):
        _next_id = self._next_id
        endnote = CT_Endnote.new(_next_id)
        endnote = self._insert_endnote(endnote)
        return endnote

    def get_endnote_by_id(self, _id):
        namesapce = NAMESPACE().WML_MAIN
        for fn in self.findall('.//w:endnote', {'w': namesapce}):
            if fn._id == _id:
                return fn
        return None


class CT_Endnote(BaseOxmlElement):
    """
    A ``<w:footnote>`` element, a container for Footnote properties
    """
    _id = RequiredAttribute('w:id', ST_DecimalNumber)
    p = ZeroOrOne('w:p', successors=('w:endnote',))

    @classmethod
    def new(cls, _id):
        endnote = OxmlElement('w:endnote')
        endnote._id = _id

        return endnote

    def _add_p(self, text):
        _p = OxmlElement('w:p')
        _p.endnote_style()

        _r = _p.add_r()
        _r.endnote_style()
        _r = _p.add_r()
        _r.add_endnoteRef()

        run = Run(_r, self)
        run.text = text

        self._insert_p(_p)
        return _p

    @property
    def paragraph(self):
        return Paragraph(self.p, self)


class CT_ENR(BaseOxmlElement):
    _id = RequiredAttribute('w:id', ST_DecimalNumber)

    @classmethod
    def new(cls, _id):
        endnoteReference = OxmlElement('w:endnoteReference')
        endnoteReference._id = _id
        return endnoteReference


class CT_EndnoteRef(BaseOxmlElement):

    @classmethod
    def new(cls):
        ref = OxmlElement('w:endnoteRef')
        return ref
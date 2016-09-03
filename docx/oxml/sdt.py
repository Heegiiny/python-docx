# encoding: utf-8

"""
Custom element classes related to content controls (CT_sdt).
"""

from .ns import qn
from .xmlchemy import BaseOxmlElement, OxmlElement, ZeroOrMore, ZeroOrOne


class CT_sdt(BaseOxmlElement):
    """
    ``<w:sdt>`` content control class
    """
    content = ZeroOrOne('w:sdtContent')


class CT_sdtContent(BaseOxmlElement):
    """
    ``<w:sdtContent>`` stdContent class
    """
    r = ZeroOrMore('w:r')

    def clear_content(self):
        """
        Remove all child elements
        """
        [self.remove(child) for child in self[:]]

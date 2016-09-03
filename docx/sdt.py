# encoding: utf-8

"""
Paragraph-related proxy types.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from .enum.style import WD_STYLE_TYPE
from .text.parfmt import ParagraphFormat
from .text.run import Run
from .shared import Parented


class ContentControls(Parented):
    """
    Proxy object wrapping ``<w:sdt>`` element.
    """
    def __init__(self, sdt, parent):
        super(ContentControls, self).__init__(parent)
        self._sdt = self._element = sdt

    def add_run(self, text=None, style=None):
        """
        Append a run to this paragraph containing *text* and having character
        style identified by style ID *style*. *text* can contain tab
        (``\\t``) characters, which are converted to the appropriate XML form
        for a tab. *text* can also include newline (``\\n``) or carriage
        return (``\\r``) characters, each of which is converted to a line
        break.
        """
        r = self._sdt.add_r()
        run = Run(r, self)
        if text:
            run.text = text
        if style:
            run.style = style
        return run

from textwrap import wrap

from ..abstract import ErdReadOnlyConverter
from ..primitives import *

class ErdSoftwareVersionConverter(ErdReadOnlyConverter[str]):
    def erd_decode(self, value) -> str:
        """
        Decode a software version string.
        These are sent as four bytes, encoding each part of a four-element version string.
        """
        vals = wrap(value, 2)
        return '.'.join(str(erd_decode_int(val)) for val in vals)

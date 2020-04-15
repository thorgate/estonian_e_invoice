from decimal import Decimal

import cerberus


DECIMAL_TYPE = cerberus.TypeDefinition("decimal", (Decimal,), ())

"""Set of hooks before project is generated."""

import re
import sys


def _exit(m):
    print(m)
    sys.exit(1)


def validate_service_name(sn):
    """Validate service name."""

    if sn[0].isdigit():
        _exit("ERROR: Service name should not starts with number")

    if re.match(r"(?:[A-Z][a-z]*)+", sn):
        _exit("ERROR: Service name should be in snake_case format")

    if not sn.lower().endswith("_service"):
        _exit("ERROR: Service name should be ends with '_service'")


validate_service_name("{{ cookiecutter.service_name }}")

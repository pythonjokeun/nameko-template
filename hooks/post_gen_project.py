"""Set of hooks after project is generated."""

import os

os.system("pipenv install --dev")

print("{{ cookiecutter.service_name }} project successfully created ✨")
print("Have a nice development 🍻")

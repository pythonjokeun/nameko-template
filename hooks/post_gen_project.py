"""Set of hooks after project is generated."""

import os

print("Installing initial dependencies via Pipenv 📝")
os.system("pipenv install --dev")

with open(".env", "a") as f:
    f.write("AMQP_URI=amqp://guest:guest@127.0.0.1")

print("'{{ cookiecutter.service_name }}' project successfully created ✨")
print(
    "To start working on the new project, just change your current directory to '{{ cookiecutter.service_name }}' 🛠"
)
print("Have a nice development 🍻")

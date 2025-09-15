from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("../web/html")
env = Environment(loader=file_loader)
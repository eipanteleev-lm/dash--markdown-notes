import os

from jinja2 import Template


def template(name: str, **kwargs) -> str:
    fullpath = os.path.join("templates", f"{name}.md")

    with open(fullpath, encoding='utf-8') as f:
        md = Template(f.read()).render(**kwargs)

    return md
    
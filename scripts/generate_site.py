#!/usr/bin/env python3
import pathlib
import sys

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = pathlib.Path(__file__).resolve().parents[1]
RESUME_PATH = ROOT / "resume.yml"
TEMPLATE_DIR = ROOT / "templates"
OUTPUT_PATH = ROOT / "index.html"


def main() -> int:
    if not RESUME_PATH.exists():
        print(f"Missing {RESUME_PATH}", file=sys.stderr)
        return 1

    with RESUME_PATH.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("index.html.j2")
    html = template.render(**data)

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

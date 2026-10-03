"""Render the manual's small Markdown subset into CSP-safe HTML and PDF.

Run with a Python environment containing reportlab: python scripts/render_manual.py.
"""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def blocks(text):
    lines = text.splitlines()
    paragraph = []
    code = None
    for line in lines + [""]:
        if line.startswith("```"):
            if paragraph:
                yield "p", " ".join(paragraph)
                paragraph = []
            if code is None:
                code = []
            else:
                yield "code", "\n".join(code)
                code = None
            continue
        if code is not None:
            code.append(line)
            continue
        if not line or line.startswith("#") or line.startswith("- ") or re.match(r"\d+\. ", line):
            if paragraph:
                yield "p", " ".join(paragraph)
                paragraph = []
            if line.startswith("## "):
                yield "h2", line[3:]
            elif line.startswith("# "):
                yield "h1", line[2:]
            elif line:
                yield "item", line
        else:
            paragraph.append(line)


def main():
    source = ROOT / "docs/AUTRONOMOUS_USER_MANUAL.md"
    content = list(blocks(source.read_text()))
    html = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AUTRONOMOUS User Manual</title><link rel="stylesheet" href="/static/manual.css"></head><body><main><nav><a href="/">Commands</a><a href="/dashboard">Control room</a></nav>']
    for kind, value in content:
        tag = "pre" if kind == "code" else "p" if kind == "item" else kind
        html.append(f"<{tag}>{escape(value)}</{tag}>")
    html.append("</main></body></html>")
    (ROOT / "src/ultron/app/static/manual.html").write_text("\n".join(html))

    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak

    output = ROOT.parent / "output"
    output.mkdir(exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="ManualBody", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=7, textColor=colors.HexColor("#263449")))
    styles.add(ParagraphStyle(name="ManualH2", fontName="Helvetica-Bold", fontSize=14, leading=18, spaceBefore=12, spaceAfter=8, keepWithNext=True, textColor=colors.HexColor("#0b5268")))
    styles.add(ParagraphStyle(name="ManualCode", fontName="Courier", fontSize=9, leading=13, spaceAfter=10, backColor=colors.HexColor("#edf4f7"), borderPadding=8))
    story = []
    for kind, value in content:
        if kind == "h2" and value.split(".", 1)[0] in {"3", "6", "8", "10", "12"}:
            story.append(PageBreak())
        if kind == "h1":
            story.extend([Paragraph("AUTRONOMOUS", styles["Title"]), Paragraph("Operator manual / 0.1.0 foundation", styles["ManualH2"]), Spacer(1, 8)])
        elif kind == "code":
            story.append(Preformatted(value, styles["ManualCode"]))
        else:
            story.append(Paragraph(escape(value), styles["ManualH2"] if kind == "h2" else styles["ManualBody"]))

    def page(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#c9d9e1"))
        canvas.line(42, 38, A4[0] - 42, 38)
        canvas.setFillColor(colors.HexColor("#52677a"))
        canvas.setFont("Helvetica", 8)
        canvas.drawString(42, 25, "AUTRONOMOUS | Foundation | 3 October 2026")
        canvas.drawRightString(A4[0] - 42, 25, f"{doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(output / "AUTRONOMOUS_User_Manual.pdf"), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=55, title="AUTRONOMOUS User Manual", author="AUTRONOMOUS")
    doc.build(story, onFirstPage=page, onLaterPages=page)
    print(output / "AUTRONOMOUS_User_Manual.pdf")


if __name__ == "__main__":
    main()

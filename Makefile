.PHONY: all install validate generate compile pdf pdf-en pdf-fr markdown clean clean_tex web web_dev

PYTHON     := $(shell which python3 2>/dev/null || which python)
REQUIREMENTS := lib/requirements.txt
SCHEMA     := schema.json
RESUME     := resume.yml
TEMPLATE   := template.jinja
OUTPUT_TEX := tex/resume.tex
OUTPUT_EN  := out/Roberto-Vallado-CV-EN.pdf
OUTPUT_FR  := out/Roberto-Vallado-CV-FR.pdf
OUTPUT_MD  := out/Roberto-Vallado-CV.md

# Default: build both PDFs
all: install validate pdf markdown

# Install Python deps
install:
	$(PYTHON) -m pip install -r $(REQUIREMENTS)

# Validate YAML + template
validate:
	$(PYTHON) lib/validate.py --schema $(SCHEMA) --resume $(RESUME) --template $(TEMPLATE)

# Build both PDFs
pdf: pdf-en pdf-fr

# English PDF
pdf-en:
	$(PYTHON) lib/generate.py --resume $(RESUME) --template $(TEMPLATE) --output $(OUTPUT_TEX) --lang en
	$(PYTHON) lib/compile.py  --input $(OUTPUT_TEX) --output $(OUTPUT_EN)

# French PDF
pdf-fr:
	$(PYTHON) lib/generate.py --resume $(RESUME) --template $(TEMPLATE) --output $(OUTPUT_TEX) --lang fr
	$(PYTHON) lib/compile.py  --input $(OUTPUT_TEX) --output $(OUTPUT_FR)

# Markdown export
markdown:
	$(PYTHON) lib/markdown.py --input $(RESUME) --output $(OUTPUT_MD)

# Clean everything
clean: clean_tex
	rm -f $(OUTPUT_EN) $(OUTPUT_FR) $(OUTPUT_MD) $(OUTPUT_TEX)

# Clean LaTeX auxiliary files only
clean_tex:
	rm -f tex/*.aux tex/*.log tex/*.out tex/*.toc tex/*.fls tex/*.fdb_latexmk tex/*.synctex.gz

# Web
web_dev:
	cd web && npm run dev

web:
	cd web && npm run build && npm run preview

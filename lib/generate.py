import argparse
import copy
import re
import logging
import os
import sys
import yaml
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from colorama import init, Fore

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

init(autoreset=True)

print(f"{Fore.CYAN}➡️ Starting: Generating LaTex files from Jinja templates and YAML data")

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Section labels and connectors per language
LANG_LABELS = {
    'en': {
        'experience':    'Experience',
        'education':     'Education',
        'skills':        'Skills',
        'stats':         'Stats',
        'awards':        'Awards',
        'projects':      'Projects',
        'present':       'Present',
        'edu_connector': 'in',
        'footer':        'Resume built with LaTeX, view source at',
    },
    'fr': {
        'experience':    'Expérience',
        'education':     'Formation',
        'skills':        'Compétences',
        'stats':         'Réalisations',
        'awards':        'Prix et distinctions',
        'projects':      'Projets',
        'present':       'Présent',
        'edu_connector': 'en',
        'footer':        'CV généré avec LaTeX, voir les sources sur',
    },
}

FR_MONTHS = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre',
]


def load_resume(yaml_path: str) -> dict:
    try:
        with open(yaml_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Failed to load YAML file {yaml_path}: {e}")
        raise


def localize_data(resume_data: dict, lang: str) -> dict:
    """Swap English fields for their French equivalents when lang='fr'."""
    if lang == 'en':
        return resume_data

    data = copy.deepcopy(resume_data)

    # Personal statement
    if data.get('personal-statement-fr'):
        data['personal-statement'] = data['personal-statement-fr']

    # Work entries
    for job in data.get('work', []):
        if job.get('position-fr'):
            job['position'] = job['position-fr']
        if job.get('highlights-fr'):
            job['highlights'] = job['highlights-fr']

    # Achievements
    for ach in data.get('achievements', []):
        if ach.get('text-fr'):
            ach['text'] = ach['text-fr']

    # Awards
    for award in data.get('awards', []):
        if award.get('summary-fr'):
            award['summary'] = award['summary-fr']

    return data


def latex_escape(text: str) -> str:
    latex_special_chars = {
        '&':  r'\&',
        '%':  r'\%',
        '$':  r'\$',
        '#':  r'\#',
        '_':  r'\_',
        '{':  r'\{',
        '}':  r'\}',
        '~':  r'\textasciitilde{}',
        '^':  r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
        '<':  r'\textless{}',
        '>':  r'\textgreater{}',
        '|':  r'\textbar{}',
        '\'': r'\textquotesingle{}',
        '—':  r'---',
        '–':  r'--',
    }
    return ''.join(latex_special_chars.get(char, char) for char in text)


def markdown_to_latex(text):
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    return (link_pattern.sub(r'\\href{\2}{\1}', text)
            .replace('%', '\\%')
            .replace('#', '\\#')
            .replace('—', '---')
            .replace('–', '--'))


def make_format_date(lang: str):
    """Return a locale-aware date formatter."""
    def format_date(date_str: str) -> str:
        formats = ['%d-%m-%Y', '%m-%Y', '%Y-%m-%d', '%Y-%m']
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                if lang == 'fr':
                    return f"{FR_MONTHS[dt.month - 1]} {dt.year}"
                return dt.strftime('%B %Y')
            except ValueError:
                continue
        return date_str
    return format_date


def render_template(template_path: str, resume_data: dict, lang: str = 'en') -> str:
    localized = localize_data(resume_data, lang)
    labels = LANG_LABELS.get(lang, LANG_LABELS['en'])

    env = Environment(
        loader=FileSystemLoader(os.path.dirname(template_path)),
        autoescape=select_autoescape(['html', 'xml'])
    )
    env.filters['latex_escape'] = latex_escape
    env.filters['format_date'] = make_format_date(lang)
    env.filters['markdown_to_latex'] = markdown_to_latex
    template = env.get_template(os.path.basename(template_path))

    try:
        pdf_timestamp = datetime.now().strftime("D:%Y%m%d%H%M%S+00'00'")
    except Exception:
        pdf_timestamp = "D:20240101000000+00'00'"

    return template.render(
        basics=localized.get('basics', {}),
        personal_statement=localized.get('personal-statement', ''),
        work=localized.get('work', []),
        education=localized.get('education', []),
        skills=localized.get('skills', []),
        awards=localized.get('awards', []),
        achievements=localized.get('achievements', []),
        projects=localized.get('projects', []),
        extra_links=localized.get('extra-links', {}),
        compilation_timestamp=pdf_timestamp,
        lang=lang,
        labels=labels,
    )


def main():
    parser = argparse.ArgumentParser(description="Generate a LaTeX resume from YAML + Jinja2 template.")
    parser.add_argument('--resume',   required=True, help="Path to the YAML resume file")
    parser.add_argument('--template', required=True, help="Path to the Jinja2 template file")
    parser.add_argument('--output',   required=True, help="Path to the output LaTeX file")
    parser.add_argument('--lang',     default='en', choices=['en', 'fr'], help="Output language (default: en)")
    args = parser.parse_args()

    if not os.path.isfile(args.resume):
        print(f"{Fore.RED}❌ Error: Resume file not found: {args.resume}")
        return
    if not os.path.isfile(args.template):
        print(f"{Fore.RED}❌ Error: Template file not found: {args.template}")
        return

    try:
        resume_data = load_resume(args.resume)
    except yaml.YAMLError as e:
        print(f"{Fore.RED}❌ Error decoding YAML: {e}")
        return
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")
        return

    try:
        rendered = render_template(args.template, resume_data, lang=args.lang)
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        print(f"{Fore.RED}❌ Error rendering template: {e}")
        return

    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(rendered)
        logger.info(f"Resume [{args.lang.upper()}] successfully generated at {args.output}")
        print(f"{Fore.GREEN}✅ Success: Resume [{args.lang.upper()}] generated at {args.output}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error writing output: {e}")


if __name__ == '__main__':
    main()

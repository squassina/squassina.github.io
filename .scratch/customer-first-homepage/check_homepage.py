from pathlib import Path

root = Path(__file__).resolve().parents[2]

required = {
    "English": [
        "Technology Strategy, AI & Business Transformation for Enterprise Leaders",
        "Advisory and hands-on leadership for enterprise AI, cloud, and engineering transformation",
        "245%",
        "1,000+",
        "US$30M+",
        "Agent Flow",
        "PromptGen",
        "CV-JD-Match",
        "GitHub Copilot",
        "GitHub Foundations",
        "Azure AI Engineer",
        "Azure Data Engineer",
        "Discuss a project",
    ],
    "Portuguese": [
        "Estratégia de Tecnologia, IA & Transformação de Negócios para Líderes Empresariais",
        "Consultoria e liderança prática para IA enterprise, cloud e transformação de engenharia",
        "245%",
        "1.000+",
        "US$ 30M+",
        "Agent Flow",
        "PromptGen",
        "CV-JD-Match",
        "GitHub Copilot",
        "GitHub Foundations",
        "Azure AI Engineer",
        "Azure Data Engineer",
        "Discutir um projeto",
    ],
}

source_pages = {
    "English": root / "index_en.md",
    "Portuguese": root / "index.md",
}

career_pages = {
    "English": root / "career_en.md",
    "Portuguese": root / "career.md",
}

for language, page in source_pages.items():
    html = page.read_text(encoding="utf-8")
    for text in required[language]:
        assert text in html, f"{language}: missing {text!r}"
    assert "US$50M+" not in html and "US$ 50M+" not in html, f"{language}: sensitive claim remains"

    project_names = ["Agent Flow", "PromptGen", "CV-JD-Match"]
    project_positions = [html.index(name) for name in project_names]
    assert project_positions == sorted(project_positions), f"{language}: project order differs"
    assert 'name="name"' in html, f"{language}: missing name field"
    assert 'name="email"' in html, f"{language}: missing email field"
    assert 'name="message"' in html, f"{language}: missing message field"

    positions = [
        html.index('<p class="exec-eyebrow">WHERE I ADD VALUE</p>') if language == "English"
        else html.index('<p class="exec-eyebrow">COMO POSSO CONTRIBUIR</p>'),
        html.index('<p class="exec-eyebrow">SELECTED CREDENTIALS</p>') if language == "English"
        else html.index('<p class="exec-eyebrow">CERTIFICADOS SELECIONADOS</p>'),
        html.index('<p class="exec-eyebrow">BUSINESS OUTCOMES</p>') if language == "English"
        else html.index('<p class="exec-eyebrow">RESULTADOS DE NEGÓCIO</p>'),
        html.index('<p class="exec-eyebrow">PROJECTS IN PRACTICE</p>') if language == "English"
        else html.index('<p class="exec-eyebrow">PROJETOS NA PRÁTICA</p>'),
        html.index('<p class="exec-eyebrow">CAREER</p>') if language == "English"
        else html.index('<p class="exec-eyebrow">TRAJETÓRIA</p>'),
    ]
    assert positions == sorted(positions), f"{language}: homepage section order differs"

for language, page in career_pages.items():
    markdown = page.read_text(encoding="utf-8")
    assert "US$50M+" not in markdown and "US$ 50M+" not in markdown, f"{language}: sensitive career claim remains"
    for claim in ("25-person", "25 profissionais", "three weeks", "três semanas", "100%", "multi-million", "multimilion"):
        assert claim not in markdown, f"{language}: unapproved career claim remains: {claim}"

print("Homepage source assertions passed")

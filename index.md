---
layout: page
title: Estratégia de Tecnologia, IA & Transformação de Negócios para Líderes Empresariais
permalink: /
lang: pt-BR
nav: false
description: "Ricardo Squassina Lee — executivo e estrategista de tecnologia corporativa, IA, cloud e transformação de engenharia."
---

<div class="exec-hero">
  <div class="exec-hero-content">
    <p class="exec-eyebrow">TECHNOLOGY STRATEGY · AI · CLOUD · ENGINEERING TRANSFORMATION</p>
    <h1>Estratégia de Tecnologia, IA &amp; Transformação de Negócios para Líderes Empresariais</h1>
    <p class="exec-lead">Consultoria e liderança prática para IA enterprise, cloud e transformação de engenharia.</p>
    <p>Mais de duas décadas conectando liderança executiva, arquitetura e execução em ambientes enterprise — com experiência em Microsoft e IBM.</p>
    <div class="exec-actions">
      <a class="btn btn-primary" href="#contato">Discutir um projeto</a>
      <a class="btn btn-outline-primary" href="/career/">Experiência profissional</a>
    </div>
  </div>
  <div class="exec-hero-photo">
    <img src="{{ '/assets/img/about.jpg' | relative_url }}" alt="Ricardo Squassina Lee" width="140" height="140">
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">COMO POSSO CONTRIBUIR</p>
  <div class="exec-pillars">
    <div><h3>Estratégia & IA</h3><p>Roadmaps de IA, adoção empresarial, operating models e governança orientada a valor.</p></div>
    <div><h3>Cloud & arquitetura</h3><p>Modernização de plataformas, dados, arquitetura de soluções, segurança e FinOps.</p></div>
    <div><h3>Engenharia & liderança</h3><p>Transformação de engenharia, desenvolvimento aumentado por IA, produtividade e mudança organizacional.</p></div>
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">CERTIFICADOS</p>
  <div class="exec-credentials">
    <span>GitHub Copilot</span>
    <span>GitHub Foundations</span>
    <span>Azure AI Engineer</span>
    <span>Azure Data Engineer</span>
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">RESULTADOS DE NEGÓCIO</p>
  <div class="exec-metrics">
    <div class="exec-metric"><strong>245%</strong><span>Atingimento de meta comercial</span></div>
    <div class="exec-metric"><strong>1.000+</strong><span>Desenvolvedores habilitados</span></div>
    <div class="exec-metric"><strong>US$ 30M+</strong><span>Pipeline enterprise</span></div>
  </div>
</div>

<div class="exec-section">
  <div class="exec-section-heading">
    <div><p class="exec-eyebrow">PROJETOS NA PRÁTICA</p><h2>Trabalhos</h2></div>
    <a href="/projects/">Todos os projetos →</a>
  </div>
  <div class="exec-projects">
    <a href="https://squassina.github.io/agent-flow/"><strong>Agent Flow</strong><span>Dá às equipes visibilidade sobre agentes e custos de IA em versões web e Docker com FastAPI e Streamlit.</span></a>
    <a href="https://squassina.github.io/PromptGen/"><strong>PromptGen</strong><span>Transforma necessidades em linguagem natural em prompts editáveis para planejamento e desenvolvimento com interface web.</span></a>
    <a href="https://squassina.github.io/CV-JD-Match/"><strong>CV-JD-Match</strong><span>Compara currículos e vagas com análise assistida por LLM e gera materiais de candidatura em uma interface client-side.</span></a>
  </div>
</div>

<div class="exec-section exec-experience">
  <p class="exec-eyebrow">TRAJETÓRIA</p>
  <div class="exec-company"><strong>MICROSOFT</strong><span>Account Technology Strategist · Senior Software Engineer · Business Programs & Operations</span></div>
  <div class="exec-company"><strong>IBM</strong><span>Services Solutions Manager · Watson Latin America · Technical Solution Manager</span></div>
  <p><a href="/career/">Ver experiência profissional completa e resultados →</a></p>
</div>

<div class="exec-section" id="contato">
  <div class="exec-section-heading">
    <div>
      <p class="exec-eyebrow">CONTATO DIRETO</p>
      <h2>Vamos conversar?</h2>
    </div>
  </div>
  <p>Para projetos, aconselhamento em tecnologia, IA enterprise ou liderança técnica:</p>
  <form id="contact-form" class="exec-contact-form">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="form-row">
      <input type="text" name="name" placeholder="Seu nome" required>
      <input type="email" name="email" placeholder="Seu e-mail" required>
    </div>
    <textarea name="message" rows="4" maxlength="1500" placeholder="Sua mensagem..." required></textarea>
    <button type="submit" class="btn btn-primary" style="justify-self: start;">Enviar mensagem</button>
    <div id="contact-status" class="exec-contact-status" style="display:none;"></div>
  </form>
</div>

<script>
(function() {
  const form = document.getElementById('contact-form');
  const status = document.getElementById('contact-status');
  if (!form) return;
  // shortcut: substitui via _config.yml / GitHub Actions variable, ou fallback mailto
  const WORKER_URL = '{{ site.worker_endpoint_url }}';

  form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    if (!WORKER_URL || WORKER_URL.trim() === '') {
      window.location.href = 'mailto:ricardoslee@gmail.com?subject=Contato via squassina.github.io&body=' + encodeURIComponent('Nome: ' + data.name + '\nEmail: ' + data.email + '\n\n' + data.message);
      return;
    }

    btn.disabled = true;
    status.style.display = 'block';
    status.className = 'exec-contact-status';
    status.textContent = 'Enviando...';

    try {
      const res = await fetch(WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      if (res.ok) {
        status.className = 'exec-contact-status success';
        status.textContent = 'Mensagem enviada com sucesso!';
        form.reset();
      } else {
        throw new Error();
      }
    } catch (err) {
      status.className = 'exec-contact-status error';
      status.textContent = 'Erro ao enviar. Tente por email direto: ricardoslee@gmail.com';
    } finally {
      btn.disabled = false;
    }
  });
})();
</script>

<div class="exec-footer-cta">
  <div>
    <p class="exec-eyebrow">FORMAÇÃO</p>
    <ul class="exec-credentials-list">
      <li><strong>MBA em Big Data e Analytics</strong> — FGV</li>
      <li><strong>Pós-graduação em Análise e Projeto de Sistemas de Informação</strong> — FATEC-SP</li>
      <li><strong>Tecnologia em Processamento de Dados</strong> — FATEC-SP</li>
    </ul>
  </div>
  <div>
    <p class="exec-eyebrow">CERTIFICAÇÕES</p>
    <ul class="exec-credentials-list">
      <li>GitHub Copilot · GitHub Foundations</li>
      <li>Azure AI Engineer · Data Engineer · Data Scientist Associate</li>
      <li>Azure Cosmos DB Developer Specialty</li>
      <li>Security, Compliance and Identity Fundamentals</li>
      <li>Advanced Certified Scrum Product Owner (CSPO) · ITIL v3 Foundation</li>
      <li>IBM Selling Profession</li>
    </ul>
  </div>
</div>

<div class="exec-footer-links">
  <span style="color: var(--global-text-color-light);">Ricardo Squassina Lee</span>
  <div>
    <a href="https://www.linkedin.com/in/ricardo-squassina-lee" target="_blank" rel="noopener noreferrer">LinkedIn</a> · 
    <a href="https://github.com/squassina" target="_blank" rel="noopener noreferrer">GitHub</a>
  </div>
</div>

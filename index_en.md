---
layout: page
title: Technology Strategy, AI & Business Transformation for Enterprise Leaders
permalink: /en/
lang: en
nav: false
description: "Ricardo Squassina Lee — enterprise technology executive and strategist in AI, cloud, and engineering transformation."
---

<div class="exec-hero">
  <div class="exec-hero-content">
    <p class="exec-eyebrow">TECHNOLOGY STRATEGY · AI · CLOUD · ENGINEERING TRANSFORMATION</p>
    <h1>Technology Strategy, AI &amp; Business Transformation for Enterprise Leaders</h1>
    <p class="exec-lead">Advisory and hands-on leadership for enterprise AI, cloud, and engineering transformation.</p>
    <p>More than two decades connecting executive leadership, architecture, and execution in enterprise environments — with experience at Microsoft and IBM.</p>
    <div class="exec-actions">
      <a class="btn btn-primary" href="#contact">Discuss a project</a>
      <a class="btn btn-outline-primary" href="/en/career/">Professional experience</a>
    </div>
  </div>
  <div class="exec-hero-photo">
    <img src="{{ '/assets/img/about.jpg' | relative_url }}" alt="Ricardo Squassina Lee" width="140" height="140">
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">WHERE I ADD VALUE</p>
  <div class="exec-pillars">
    <div><h3>Strategy & AI</h3><p>AI roadmaps, enterprise adoption, operating models, and value-driven governance.</p></div>
    <div><h3>Cloud & architecture</h3><p>Platform modernization, data, solution architecture, security, and FinOps.</p></div>
    <div><h3>Engineering & leadership</h3><p>Engineering transformation, AI-assisted development, engineering productivity, and organizational change.</p></div>
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">CREDENTIALS</p>
  <div class="exec-credentials">
    <span>GitHub Copilot</span>
    <span>GitHub Foundations</span>
    <span>Azure AI Engineer</span>
    <span>Azure Data Engineer</span>
  </div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">BUSINESS OUTCOMES</p>
  <div class="exec-metrics">
    <div class="exec-metric"><strong>245%</strong><span>Sales quota attainment</span></div>
    <div class="exec-metric"><strong>1,000+</strong><span>Developers enabled</span></div>
    <div class="exec-metric"><strong>US$30M+</strong><span>Enterprise pipeline</span></div>
  </div>
</div>

<div class="exec-section">
  <div class="exec-section-heading">
    <div><p class="exec-eyebrow">PROJECTS IN PRACTICE</p><h2>Work</h2></div>
    <a href="/en/projects/">All projects →</a>
  </div>
  <div class="exec-projects">
    <a href="https://squassina.github.io/agent-flow/"><strong>Agent Flow</strong><span>Gives teams visibility into AI agent workflows and token usage through browser and Docker deployments built with FastAPI and Streamlit.</span></a>
    <a href="https://squassina.github.io/PromptGen/"><strong>PromptGen</strong><span>Turns natural-language needs into editable prompts for planning and development through a structured web interface.</span></a>
    <a href="https://squassina.github.io/CV-JD-Match/"><strong>CV-JD-Match</strong><span>Compares resumes with job descriptions using LLM-assisted analysis and generates application materials in a client-side interface.</span></a>
  </div>
</div>

<div class="exec-section exec-experience">
  <p class="exec-eyebrow">CAREER</p>
  <div class="exec-company"><strong>MICROSOFT</strong><span>Account Technology Strategist · Senior Software Engineer · Business Programs & Operations</span></div>
  <div class="exec-company"><strong>IBM</strong><span>Services Solutions Manager · Watson Latin America · Technical Solution Manager</span></div>
  <p><a href="/en/career/">View full professional experience and outcomes →</a></p>
</div>

<div class="exec-section" id="contact">
  <div class="exec-section-heading">
    <div>
      <p class="exec-eyebrow">DIRECT CONTACT</p>
      <h2>Let's talk?</h2>
    </div>
  </div>
  <p>For strategic technology advisory, enterprise AI initiatives, or technical leadership:</p>
  <form id="contact-form" class="exec-contact-form">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="form-row">
      <input type="text" name="name" placeholder="Your name" required>
      <input type="email" name="email" placeholder="Your email" required>
    </div>
    <textarea name="message" rows="4" maxlength="1500" placeholder="Your message..." required></textarea>
    <button type="submit" class="btn btn-primary" style="justify-self: start;">Send message</button>
    <div id="contact-status" class="exec-contact-status" style="display:none;"></div>
  </form>
</div>

<script>
(function() {
  const form = document.getElementById('contact-form');
  const status = document.getElementById('contact-status');
  if (!form) return;
  // shortcut: injected via _config.yml / GitHub Actions variable, or mailto fallback
  const WORKER_URL = '{{ site.worker_endpoint_url }}';

  form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    if (!WORKER_URL || WORKER_URL.trim() === '') {
      window.location.href = 'mailto:ricardoslee@gmail.com?subject=Contact via squassina.github.io&body=' + encodeURIComponent('Name: ' + data.name + '\nEmail: ' + data.email + '\n\n' + data.message);
      return;
    }

    btn.disabled = true;
    status.style.display = 'block';
    status.className = 'exec-contact-status';
    status.textContent = 'Sending...';

    try {
      const res = await fetch(WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      if (res.ok) {
        status.className = 'exec-contact-status success';
        status.textContent = 'Message sent successfully!';
        form.reset();
      } else {
        throw new Error();
      }
    } catch (err) {
      status.className = 'exec-contact-status error';
      status.textContent = 'Failed to send. Please reach out via email: ricardoslee@gmail.com';
    } finally {
      btn.disabled = false;
    }
  });
})();
</script>

<div class="exec-footer-cta">
  <div>
    <p class="exec-eyebrow">EDUCATION</p>
    <ul class="exec-credentials-list">
      <li><strong>MBA in Big Data & Analytics</strong> — FGV</li>
      <li><strong>Postgraduate in Information Systems Analysis & Design</strong> — FATEC-SP</li>
      <li><strong>Technologist in Data Processing</strong> — FATEC-SP</li>
    </ul>
  </div>
  <div>
    <p class="exec-eyebrow">CERTIFICATIONS</p>
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

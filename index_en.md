---
layout: page
title: Technology Strategy, AI & Business Transformation
permalink: /en/
lang: en
nav: false
description: "Ricardo Squassina Lee — enterprise technology executive and strategist in AI, cloud, and engineering transformation."
---

<div class="exec-hero">
  <p class="exec-eyebrow">TECHNOLOGY STRATEGY · AI · CLOUD · ENGINEERING TRANSFORMATION</p>
  <h1>Ricardo Squassina Lee</h1>
  <p class="exec-lead">Turning technology strategy into business outcomes.</p>
  <p>More than two decades connecting executive leadership, architecture, and execution in enterprise environments — with experience at Microsoft and IBM.</p>
  <div class="exec-actions">
    <a class="btn btn-primary" href="/en/career/">Professional experience</a>
    <a class="btn btn-outline-primary" href="https://www.linkedin.com/in/ricardo-squassina-lee">LinkedIn</a>
  </div>
</div>

<div class="exec-metrics">
  <div class="exec-metric"><strong>245%</strong><span>Sales quota attainment</span></div>
  <div class="exec-metric"><strong>US$50M+</strong><span>Strategic cloud commitments</span></div>
  <div class="exec-metric"><strong>1,000+</strong><span>Developers enabled</span></div>
  <div class="exec-metric"><strong>US$30M+</strong><span>Enterprise pipeline</span></div>
</div>

<div class="exec-section">
  <p class="exec-eyebrow">WHERE I ADD VALUE</p>
  <div class="exec-pillars">
    <div><h3>Strategy & AI</h3><p>AI roadmaps, enterprise adoption, operating models, and value-driven governance.</p></div>
    <div><h3>Cloud & architecture</h3><p>Platform modernization, data, solution architecture, security, and FinOps.</p></div>
    <div><h3>Engineering & leadership</h3><p>Engineering productivity, AI-assisted development, and organizational transformation.</p></div>
  </div>
</div>

<div class="exec-section exec-experience">
  <p class="exec-eyebrow">CAREER</p>
  <div class="exec-company"><strong>MICROSOFT</strong><span>Technology strategy · Software engineering · Business operations</span></div>
  <div class="exec-company"><strong>IBM</strong><span>IBM Watson · Enterprise solutions · Services architecture</span></div>
  <p><a href="/en/career/">Explore experience, outcomes, and technologies →</a></p>
</div>

<div class="exec-section">
  <div class="exec-section-heading">
    <div><p class="exec-eyebrow">BUILDING & PRACTICE</p><h2>Selected projects</h2></div>
    <a href="/en/projects/">All projects →</a>
  </div>
  <div class="exec-projects">
    <a href="https://squassina.github.io/TechJobScout-lite/"><strong>TechJobScout-lite</strong><span>Opportunity discovery and interview preparation for technology professionals.</span></a>
    <a href="https://squassina.github.io/PromptGen/"><strong>PromptGen</strong><span>Structured prompts generated from plain-language needs.</span></a>
    <a href="https://squassina.github.io/XadrezMestre/"><strong>XadrezMestre</strong><span>Open-source chess application built with React, TypeScript, and Stockfish.</span></a>
    <a href="https://squassina.github.io/CV-JD-Match/"><strong>CV-JD-Match</strong><span>LLM-assisted resume and job description matching.</span></a>
  </div>
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
    <textarea name="message" rows="4" placeholder="Your message..." required></textarea>
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
  <div><p class="exec-eyebrow">EDUCATION</p><strong>MBA in Big Data & Analytics · FGV</strong><span>FATEC-SP · Microsoft, GitHub, Scrum, and ITIL certifications</span></div>
  <div><p class="exec-eyebrow">LET'S CONNECT</p><a href="mailto:ricardoslee@gmail.com">Email</a> · <a href="https://www.linkedin.com/in/ricardo-squassina-lee">LinkedIn</a> · <a href="https://github.com/squassina">GitHub</a></div>
</div>

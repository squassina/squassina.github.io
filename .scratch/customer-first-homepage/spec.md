# Status: ready-for-agent

## Problem Statement

The personal website is not consistently optimized for potential customers. Its homepage currently mixes customer-facing advisory content with employer-first proof, exposes potentially sensitive or unverified numeric claims, and presents a project set that does not clearly balance customer outcomes with implementation capability.

Customers need to understand Ricardo's advisory scope, see credible outcomes and practical work, and contact him quickly. Employers should remain able to find detailed career evidence without competing with the customer journey on the homepage.

## Solution

Create a customer-first, bilingual homepage with equal Portuguese and English editions.

The homepage will lead with:

- Enterprise technology, AI, and business transformation positioning.
- An outcome-oriented description of advisory and hands-on leadership.
- A primary call to discuss a project.
- Three advisory capabilities: Strategy & AI, Cloud & architecture, Engineering & leadership.
- Three approved public metrics.
- Selected projects as examples of both advisory and hands-on capability.
- A compact career summary with a link to full experience.
- Selected certifications.
- Direct contact with name, email, and message fields.

The Portuguese and English editions will have exact structural and section-order parity. Content may differ linguistically but must represent the same information and follow the same order.

## User Stories

1. As a potential customer, I want to understand the website's primary proposition immediately, so that I can decide whether Ricardo is relevant to my organization.
2. As a potential customer, I want the homepage title to identify enterprise technology, AI, and business transformation, so that I can recognize his scope.
3. As a potential customer, I want the lead copy to emphasize advisory and hands-on leadership for enterprise AI, cloud, and engineering transformation, so that I understand both strategic and delivery value.
4. As a potential customer, I want a primary call to discuss a project, so that I can start a relevant conversation.
5. As a potential customer, I want to scan three clear advisory capability areas, so that I can identify whether my need is covered.
6. As a potential customer, I want AI adoption included in the first capability area, so that I can understand the practical scope.
7. As a potential customer, I want cloud modernization included in the second capability area, so that I can assess platform expertise.
8. As a potential customer, I want engineering transformation included in the third capability area, so that I can assess organizational delivery capability.
9. As a potential customer, I want approved business outcomes near the capabilities, so that claims are credible and easy to scan.
10. As a potential customer, I want to see 245% sales quota attainment, 1,000+ developers enabled, and US$30M+ enterprise pipeline, so that I can evaluate measurable impact.
11. As a potential customer, I want the US$50M+ strategic cloud commitment claim removed from public pages, so that I am not shown sensitive or unverified claims.
12. As a potential customer, I want to see three selected projects, so that I can verify advisory and implementation capability.
13. As a potential customer, I want Agent Flow presented first, so that I see experience with orchestration and operations.
14. As a potential customer, I want Agent Flow to balance public tool usefulness with implementation and advisory capability.
15. As a potential customer, I want PromptGen presented second and shown as a balanced outcome-and-implementation example.
16. As a potential customer, I want CV-JD-Match presented third and shown as a balanced outcome-and-implementation example.
17. As a potential customer, I want short project summaries instead of long case studies, so that I can assess fit quickly.
18. As a potential customer, I want project summaries to identify both business or user outcomes and implementation details, so that strategic and technical credibility are visible together.
19. As a potential customer, I want a direct link to all projects, so that I can inspect the broader work list.
20. As a potential customer, I want selected GitHub Copilot, GitHub Foundations, Azure AI Engineer, and Azure Data Engineer credentials below the capability pillars, so that technical credentials support the capability claims.
21. As a potential customer, I want a compact career section, so that I can validate company and role context without leaving the homepage flow.
22. As a potential customer, I want the compact career section to link to the complete career page, so that I can inspect detailed experience.
23. As a potential customer, I want direct contact fields for name, email, and message, so that I can initiate a conversation with minimal friction.
24. As a potential customer, I want the contact form to send through the configured worker or open my email client as a fallback, so that the page has a reliable contact path.
25. As an English-speaking potential customer, I want the English homepage to match the Portuguese homepage structure and section order, so that both editions are equally usable.
26. As a Portuguese-speaking potential customer, I want the Portuguese homepage to match the English homepage structure and section order, so that both editions are equally complete.
27. As an employer, I want the detailed career page to remain available, so that I can verify full role history and selected certifications.
28. As an employer, I want the career page to display only the same approved public metrics, so that sensitive claims do not appear in a detailed hiring context.
29. As a mobile visitor, I want capability, metric, project, career, credential, and contact sections to remain readable and usable, so that the customer journey works on small screens.
30. As a visitor using a dark or light theme, I want the updated homepage hierarchy and calls to action to preserve existing theme contrast and readability.

## Implementation Decisions

- Make the homepage the customer-first entry point in both supported languages.
- Change the homepage title and lead copy to the approved enterprise technology, AI, and business transformation positioning.
- Replace the generic employer-first action with the primary call "Discuss a project."
- Keep the existing three advisory pillar names but sharpen their descriptions around AI adoption, cloud modernization, and engineering transformation.
- Place the approved metric block after the advisory capability pillars.
- Remove the US$50M+ strategic cloud commitment metric from the homepage and detailed career page.
- Keep only 245% sales quota attainment, 1,000+ developers enabled, and US$30M+ enterprise pipeline as approved public numeric claims.
- Replace the current four-project homepage list with exactly three homepage projects: Agent Flow, PromptGen, CV-JD-Match.
- Order those projects as Agent Flow, PromptGen, CV-JD-Match.
- Frame each project with balanced outcome and implementation language, using short summaries only.
- Add selected credentials immediately below the capability pillars.
- Display GitHub Copilot, GitHub Foundations, Azure AI Engineer, and Azure Data Engineer as the featured certifications.
- Keep a compact career summary after projects or in the customer-first experience sequence, with a direct link to the full career page.
- Retain the existing contact form behavior, worker endpoint support, and mailto fallback.
- Retain name, email, and message fields only; do not add project-type or timeline fields.
- Preserve exact structural and section-order parity between Portuguese and English editions.
- Preserve existing Jekyll front matter, permalink, language, navigation, and theme conventions.
- Preserve existing social, navigation, dark-mode, and responsive theme behavior.
- Remove no existing fallback, validation, or privacy behavior from the contact form.

## Testing Decisions

- Test the complete Jekyll production build succeeds in both language modes.
- Inspect generated homepage HTML and verify the customer-facing title, lead copy, primary call, approved pillar descriptions, metric values, project order, credential placement, career link, and contact form exist.
- Inspect generated HTML to verify US$50M+ does not appear on either homepage or detailed career page.
- Verify that Portuguese and English homepage sections occur in the same order and that each edition contains the same equivalent content.
- Verify the projects appear in the required Agent Flow, PromptGen, CV-JD-Match order and no longer include the three omitted homepage projects.
- Verify direct project links and career links resolve under the existing deployment paths.
- Verify the contact form retains name, email, message, honeypot, submit status, worker submission, and mailto fallback behavior.
- Verify generated CSS remains valid and responsive rules keep the capability, metric, project, credential, and contact sections usable at mobile widths.
- Prior art is the existing Jekyll build and generated HTML inspection; there is no existing automated test suite.

## Out of Scope

- Creating challenge, approach, and outcome case-study pages.
- Adding project-type or timeline fields to the contact form.
- Rewriting the complete projects catalog beyond homepage selection.
- Replacing Jekyll or the existing theme.
- Adding a backend or changing the contact worker contract.
- Adding analytics, tracking, or lead-management integrations.
- Redesigning the navigation system, dark/light theme, or general site-wide footer.
- Publishing or drafting a pull request.

## Further Notes

The website has one implementation seam: the homepage content for each language edition, supported by existing shared theme styles and contact form behavior.

No domain glossary or ADR currently governs this website content. Add glossary or ADR files only if domain terms or irreversible implementation decisions are later resolved; this spec itself is not implementation documentation.

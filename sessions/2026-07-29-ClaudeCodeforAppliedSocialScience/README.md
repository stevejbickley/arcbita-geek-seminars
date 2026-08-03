
<table>
  <tr>
    <td width="110">
      <a href="https://arcbita.org/">
        <img src="../../arcbita.png" alt="ARC BITA logo" width="100">
      </a>
    </td>
    <td>
      <strong>Australian Research Centre for Behavioural Insights for Technology Adoption (ARC BITA)</strong>
    </td>
  </tr>
</table>

_**ARC BITA Geek Seminar Series** — a forum for practical, empirical methods and tooling for behavioural insights & technology adoption._

---

### Session Title
> Claude Code for Applied Social Science

### Presenter(s)
> Yves Kläy, University of Fribourg and Institute for Swiss Economic Policy (IWP) at the University of Lucerne

### Abstract
> Applied social scientists mostly use Claude and ChatGPT in a browser, where every file is pasted in by hand and every result pasted back out. Claude Code removes that step. It reads and writes files in a project folder, runs the analysis, reads its own error messages, and fixes them. This is a written, self-paced guide to adopting it, aimed at researchers with no programming background. It covers installation through the desktop application, setting up a project in a new or an existing folder, and the file-based configuration of rules, skills, agents, hooks, and plugins.

### Learning outcomes
- Decide whether Claude Code is worth adopting, and install it without using a terminal. 
- Set up a research project so that Claude has the context, conventions, and boundaries it needs, in a new folder or one with years of existing work. 
- Recognise the specific ways the tool fails on empirical work, and apply the verification habits that catch each one. 
- Explain what rules, skills, agents, commands, plugins, and hooks are, where each lives, and why the location matters. 
- Build a pipeline in which every reported number flows from code output into the manuscript, so tables and text cannot disagree.

### Who should attend
- Empirical researchers in economics, political science, psychology, sociology, and public policy, at any career stage. 
- PhD students setting up their first serious project structure. 
- Research assistants and data managers responsible for reproducibility and replication packages. 
- Anyone already paying for Claude or ChatGPT who suspects they are using perhaps a tenth of it. 
- No programming background is assumed. R, Stata, and Python users are all catered for, with an honest account of where Stata falls short.


### Prerequisites & setup
- A Claude Pro or Max subscription, or an Anthropic Console account. If you already pay for Claude in a browser, you already have access.
- The Claude Code desktop application, for [Windows](https://claude.ai/api/desktop/win32/x64/setup/latest/redirect) or [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect). No terminal required.
- Optional: R, Stata, or Python, depending on what you work in. Python is also needed for the raw-data protection hook in the starter kit, which can be omitted.
- Optional: [git](https://git-scm.com/downloads) and a free GitHub account. The guide explains why this matters and Claude Code will set it up for you.
- Nothing needs to be prepared in advance. The guide includes a twenty-minute worked example that uses only public World Bank data.

### Agenda (indicative)
Self-paced written guide, so there is no fixed running order. The guide sets out three reading paths.
- **~30 min** — Sections 1 to 3, then the worked first session in section 4. Enough to decide whether the tool is for you. 
- **First week** — Sections 5 to 7. Set up one real project properly and install a handful of the recommended skills. 
- **Later** — Sections 8 to 11 on verification, writing, advanced settings, and cost. Come back when you hit the problem each one solves.

### Materials
- **Guide:** [`claude-code-guide.html`](./claude-code-guide.html) — open in any browser. Self-contained, works offline, roughly 8,000 words with a sticky table of contents. Source: [`claude-code-guide.qmd`](./claude-code-guide.qmd), rebuilt with `quarto render`.
- **Code/demo:** [`starter/`](./starter/) — the files a research project needs on day one, plus the skills the guide recommends. Thirteen rules, fifteen skills, nine agents, four project documents, a hook that makes `data/raw/` read-only, and a permissions file. See [`starter/README.md`](./starter/README.md) for the inventory and [`starter/SOURCES.md`](./starter/SOURCES.md) for attribution. The fastest route is the one-paste bootstrap prompt in the appendix of the guide.

### References & further reading
- Anthropic, [Claude Code documentation](https://code.claude.com/docs/en/overview). Also [Memory and CLAUDE.md](https://code.claude.com/docs/en/memory), [Skills](https://code.claude.com/docs/en/skills), [Subagents](https://code.claude.com/docs/en/sub-agents), [Hooks](https://code.claude.com/docs/en/hooks), [MCP](https://code.claude.com/docs/en/mcp).
- Pedro H. C. Sant'Anna, [My Claude Code workflow](https://psantanna.com/claude-code-my-workflow/workflow-guide.html) and the [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) repository. The most complete academic setup published, and the source of most of the recommended skills.
- Paul Goldsmith-Pinkham, [Claude Code for applied economists](https://markusacademy.substack.com/p/claude-code-for-applied-economists), and the underlying series on [getting started](https://paulgp.substack.com/p/getting-started-with-claude-code), [an empty folder to a figure](https://paulgp.substack.com/p/from-an-empty-folder-to-a-figure), [EDGAR filings](https://paulgp.substack.com/p/from-edgar-filings-to-a-structured), [large datasets](https://paulgp.substack.com/p/large-datasets-and-structured-databases), [writing](https://paulgp.substack.com/p/writing-and-thinking-with-ai-assistance), [skills](https://paulgp.substack.com/p/skills-specifying-how-an-agent-should), [permissions and sandboxes](https://paulgp.substack.com/p/permissions-sandboxes-and-autonomous), and [collaboration](https://paulgp.substack.com/p/integration-and-collaboration-in).
- Scott Cunningham, [MixtapeTools](https://github.com/scunning1975/MixtapeTools). Referee 2, Blindspot, Bibcheck, Beautiful Deck.
- Matt Pocock, [mattpocock/skills](https://github.com/mattpocock/skills). Source of `grill-me`, `handoff`, and `code-review`.

---

### Licensing & attributions
- **Content license:** CC BY 4.0
- **Code license:** MIT
- **Preferred citation:** Kläy, Y., "Claude Code for Applied Social Science: a guide for researchers who have never opened a terminal", ARC BITA Geek Seminars, 2026-07-28. Available at: https://github.com/YvesUNIFR/2026-07-28-claude-code-for-researchers.
- **Third-party assets:**
  - Rule files in `starter/.claude/rules/` are rewritten adaptations of the template in [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) (MIT), shortened and retargeted at applied social science. Attribution in [`starter/SOURCES.md`](./starter/SOURCES.md).
  - Skills and agents in `starter/.claude/` are redistributed from [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) (MIT) and [mattpocock/skills](https://github.com/mattpocock/skills) (MIT), per-file attribution in [`starter/SOURCES.md`](./starter/SOURCES.md).
  - [MixtapeTools](https://github.com/scunning1975/MixtapeTools) carries no licence file, so `beautiful_deck` is referenced by link only and nothing from it is bundled.
  - Practical guidance credited in the text to Paul Goldsmith-Pinkham is paraphrased from his publicly available Substack series and cited inline.

---

### Changelog
- 2026-08-03: Materials uploaded to ARC BITA Geek Seminars repo by Dr. Steve Bickley.
- 2026-07-28: Session materials published. Guide (13 sections) and starter kit (rules, skills, agents, a hook, and project templates) by Yves Kläy. Inventory and counts in `starter/README.md`.

---

### About ARC BITA & contacts
Other ARC BITA updates are available on our [official website](https://arcbita.org/), [Working Paper Series](https://arcbita.org/publications), [Podcast Series](https://arcbita.org/podcast-1), [LinkedIn](https://www.linkedin.com/company/arc-ittc-bita/), and [YouTube](https://www.youtube.com/@ARCBITA).  

To discuss research or opportunities, please reach out via our [contact form](https://arcbita.org/contact).

<sub>Back to the repo home: [ARC BITA Geek Seminars Knowledge Hub](https://github.com/stevejbickley/arcbita-geek-seminars/tree/main)</sub>


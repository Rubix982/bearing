"""What a research record IS, independent of how a project stores it.

Four things, and every check in `checks.py` is written against this interface rather than
against any project's file layout:

    work      things done or being done        (tickets, runs, jobs)
    questions things open and unanswered       (threads, issues)
    results   what was found, with provenance  (decisions, findings)
    claims    what the write-up asserts        (a paper, a report, a README)

One adapter ships. A project storing its record differently implements `Record` and gets
every check for free; that is the whole reason for the indirection.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field


@dataclass
class Item:
    """One unit of the record. `kind` is the adapter's own vocabulary."""

    id: str
    title: str
    body: str
    status: str = ""
    kind: str = ""
    created: str = ""

    #: A status is rarely a bare word. edit-slice writes
    #: `answered — **DENY: the coefficient bounds delivery**`, and an equality test read
    #: 38 of its 67 answered threads as open. Match the leading word, not the whole line.
    DONE_WORDS = ("closed", "split", "answered", "done", "resolved", "fixed", "complete")

    @property
    def done(self) -> bool:
        first = re.split(r"[^a-z]+", self.status.strip().lower(), maxsplit=1)[0]
        return first in self.DONE_WORDS


@dataclass
class Record:
    """A project's record, normalised."""

    root: str
    work: list[Item] = field(default_factory=list)
    questions: list[Item] = field(default_factory=list)
    results: list[Item] = field(default_factory=list)
    claims_text: str = ""
    claims_path: str = ""

    @property
    def name(self) -> str:
        return os.path.basename(os.path.abspath(self.root))

    def ok(self) -> bool:
        return bool(self.work or self.questions or self.results)


def _read(path: str) -> str:
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def _sections(src: str, pat: str, kind: str) -> list[Item]:
    out = []
    for m in re.finditer(pat, src, re.M | re.S):
        gid, title, body = m.group(1), m.group(2).strip(), m.group(3)
        status = (re.search(r"\*\*Status:\*\*\s*([^\n*]+)", body) or [0, ""])[1].strip()
        created = (re.search(r"\*\*(?:Created|Opened|Date):\*\*\s*(\S+)", body)
                   or [0, ""])[1].strip()
        out.append(Item(gid, title, body, status, kind, created))
    return out


def agentic(root: str) -> Record:
    """The author's cross-project template: plan.md, threads.md, agents/<role>/.

    Tolerant by design — a project using half the template still yields a usable record,
    because a checker that needs the full layout is one that runs on one project.
    """
    j = lambda *p: os.path.join(root, *p)  # noqa: E731
    work: list[Item] = []
    for rel, kind in (("agents/engineer/tickets.md", "ticket"),
                      ("agents/researcher/tickets.md", "ticket"),
                      ("agents/documentor/tickets.md", "ticket"),
                      ("agents/orchestrator/tickets.md", "ticket")):
        work += _sections(_read(j(rel)), r"^### ([A-Z]-\d+[a-z]?) · (.+?)$(.*?)(?=^### |\Z)",
                          kind)
    questions = _sections(_read(j("threads.md")),
                          r"^### (T-\d+) · (.+?)$(.*?)(?=^### |\Z)", "thread")
    results: list[Item] = []
    for rel, kind in (("agents/shared/decisions.md", "decision"),
                      ("agents/shared/findings.md", "finding")):
        results += _sections(_read(j(rel)),
                             r"^## \[([\w/-]+)\][: ]*(.*?)$(.*?)(?=^## \[|\Z)", kind)

    # the write-up: whatever this project points at, else the longest markdown it owns
    claims, cpath = "", ""
    for cand in ("review.md", "paper.md", "REPORT.md", "README.md"):
        for base in (root, os.path.join(root, "docs")):
            p = os.path.join(base, cand)
            if os.path.exists(p) and len(_read(p)) > len(claims):
                claims, cpath = _read(p), p
    return Record(root, work, questions, results, claims, cpath)


ADAPTERS = {"agentic": agentic}





def pipeline(root: str) -> Record:
    """A production pipeline's record — written against a second, private project, the second project.

    Different furniture, same four things, which is the point of the interface:

        questions  docs/gaps.md          numbered sections: the gap, evidence, fixes
        results    docs/critique-ledger.md   a table of causes, each with a status
        work       out/pipeline/<run>/   one directory per run, state.json inside

    Written to falsify the abstraction. If a second project had needed `checks.py` to
    change, the interface would have been edit-slice's shape wearing a general name.
    """
    j = lambda *p: os.path.join(root, *p)  # noqa: E731
    questions = _sections(_read(j("docs/gaps.md")),
                          r"^## \d+\. (.+?)$()(.*?)(?=^## |\Z)", "gap")
    for q in questions:                       # the heading is the title; synthesise ids
        q.title = q.id
    for n, q in enumerate(questions, 1):
        q.id = f"gap-{n}"
        q.status = "answered" if re.search(r"\*\*Fix(?:es)?\.\*\*|^- \*\*", q.body, re.M) \
            else "open"

    results: list[Item] = []
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|([^|]*)\|\s*([^|]+?)\s*\|",
                         _read(j("docs/critique-ledger.md")), re.M):
        cid, cause, words, status = m.groups()
        results.append(Item(f"cause-{cid}", cause.strip(), words.strip(),
                            status.strip(), "cause"))

    work: list[Item] = []
    pdir = j("out/pipeline")
    if os.path.isdir(pdir):
        for d in sorted(os.listdir(pdir)):
            full = os.path.join(pdir, d)
            if not os.path.isdir(full):
                continue
            st = _read(os.path.join(full, "state.json"))
            work.append(Item(d, d, st[:2000], "closed" if st else "open", "run"))

    claims, cpath = "", ""
    for cand in ("README.md", "docs/pipelines.md", "docs/art-direction.md"):
        p = j(cand)
        if os.path.exists(p) and len(_read(p)) > len(claims):
            claims, cpath = _read(p), p
    return Record(root, work, questions, results, claims, cpath)


ADAPTERS["pipeline"] = pipeline


def moments(root: str) -> Record:
    """A product designed one moment of its users' week at a time — written against `sheets`.

    The third shape. No tickets and no threads (a side build switches them off), but the
    same four things are on disk:

        work       docs/moments/NN-*.md    one design per moment; its `_Status:` line
                   docs/use-cases.md       numbered stories marked ✓ built, ◐ partly, — not yet
        questions  "## Questions for …" in each moment, and in use-cases.md. A question
                   is answered when its line carries `→ the answer`.
        results    "## Decisions" in each moment: `- **2026-10-30 · Title.** why`
        claims     README.md

    A status word is translated, not trusted: "built" is done, "defined" is open, and a
    story's mark is its status. ◐ is open on purpose — partly built is not built.
    """
    j = lambda *p: os.path.join(root, *p)  # noqa: E731
    work: list[Item] = []
    questions: list[Item] = []
    results: list[Item] = []

    def asked(src: str, prefix: str) -> None:
        for sec in re.finditer(r"^## (?:Open )?[Qq]uestions\b.*?$(.*?)(?=^## |\Z)", src, re.M | re.S):
            for m in re.finditer(r"^(\d+)\. (.+)$", sec.group(1), re.M):
                line = m.group(2)
                q, _, ans = line.partition("→")
                questions.append(Item(f"{prefix}Q{m.group(1)}", q.strip(), line,
                                      "answered" if ans.strip() else "open", "question"))

    mdir = j("docs/moments")
    for name in sorted(os.listdir(mdir)) if os.path.isdir(mdir) else []:
        m = re.match(r"(\d+)-.*\.md$", name)
        if not m:
            continue
        src = _read(os.path.join(mdir, name))
        mid = f"M-{m.group(1)}"
        title = (re.search(r"^# (.+)$", src, re.M) or [0, name])[1].strip()
        st = (re.search(r"^_Status:\s*([^._]+)", src, re.M) or [0, ""])[1].strip()
        date = (re.search(r"\d{4}-\d{2}-\d{2}", st) or [""])[0]
        word = st.split()[0].lower() if st else ""
        status = {"built": "done", "shipped": "done", "blocked": "blocked"}.get(word, "open")
        work.append(Item(mid, title, src, f"{status} ({st})" if st else status, "moment", date))
        asked(src, f"{mid}-")
        for d in re.finditer(r"^- \*\*(\d{4}-\d{2}-\d{2}) · (.+?)\*\*(.*?)(?=^- \*\*|^## |\Z)",
                             src, re.M | re.S):
            results.append(Item(f"{mid}-D{len(results) + 1}", d.group(2).strip(" ."),
                                d.group(3).strip(), "decided", "decision", d.group(1)))

    # Stories carry no dates, and checks read `work` as oldest-first. Numbered stories are a
    # catalogue, not a sequence; putting them after the moments made the first run read
    # stories 18-28 as "the last five things finished". They go first; dated moments last.
    uc = _read(j("docs/use-cases.md"))
    stories = []
    for m in re.finditer(r"^(\d+)\. (.+?)\s+(✓|◐|—)(.*)$", uc, re.M):
        mark = {"✓": "done", "◐": "open (partly built)", "—": "open"}[m.group(3)]
        stories.append(Item(f"S-{int(m.group(1)):02d}", m.group(2).strip(), m.group(0), mark, "story"))
    work = stories + sorted(work, key=lambda w: (w.created, w.id))
    asked(uc, "UC-")

    # Findings from walking the flows (docs/flow-audit.md): open ones are work still owed.
    work += _sections(_read(j("docs/flow-audit.md")), r"^### (U-\d+) · (.+?)$(.*?)(?=^### |^## |\Z)", "finding")
    for q in questions_from_answers(_read(j("docs/answers-round-1.md"))):
        questions.append(q)

    claims = _read(j("README.md"))
    return Record(root, work, questions, results, claims, j("README.md") if claims else "")


def questions_from_answers(src: str) -> list[Item]:
    """Follow-up questions raised by an answer round: "## New questions this raises", numbered."""
    out = []
    for sec in re.finditer(r"^## New questions.*?$(.*?)(?=^## |\Z)", src, re.M | re.S):
        for m in re.finditer(r"^(\d+)\. (.+)$", sec.group(1), re.M):
            q, _, ans = m.group(2).partition("→")
            out.append(Item(f"A1-Q{m.group(1)}", q.strip(), m.group(2), "answered" if ans.strip() else "open", "question"))
    return out


ADAPTERS["moments"] = moments


def load_config(root: str) -> dict:
    """`.bearing.json` beside the project: {"adapter": ..., "claims": "relative/path"}.

    Needed because a project's write-up is not always inside it — `edit-slice`'s paper
    lives in a separate site directory, and guessing picked its README instead.
    """
    import json
    p = os.path.join(root, ".bearing.json")
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def load(root: str, adapter: str | None = None) -> Record:
    root = os.path.abspath(os.path.expanduser(root))
    cfg = load_config(root)
    rec = ADAPTERS[adapter or cfg.get("adapter", "agentic")](root)
    claims = cfg.get("claims")
    if claims:
        path = claims if os.path.isabs(claims) else os.path.join(root, claims)
        text = _read(path)
        if text:
            rec.claims_text, rec.claims_path = text, path
    return rec

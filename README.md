# bearing

A bearing is a measured direction, not a destination. This tells a research project where
it is pointed. It does not claim to know where it should go.

```bash
pip install -e .          # once; gives you the `bearing` command anywhere
bearing ~/code/open-concept-lab/ai/edit-slice
bearing <private-project> --json
```

Or without installing, from this directory: `python -m bearing <project>`. Stdlib
only — there is nothing to resolve, and a navigator that cannot run because of its
own dependency tree would be a joke at its own expense.

## Why

Research drifts before anyone notices. On 2026-10-14, after a week in which every closed
ticket in `edit-slice` was a finer measurement of its own instrument, its author said:

> I feel we have dug ourselves too deep into narrow cases, but are not able to explain the
> high level of our research outcomes.

That is a *navigational* correction, and it arrived from a person reading a trajectory. Most
of what made it possible is mechanical — a property of the sequence, computable from the
record. `bearing` asks those questions on a schedule so the correction arrives a week or two
earlier, and from the record rather than from a mood.

## The boundary, and it is the whole design

**`bearing` measures drift. It does not have taste, and it must never pretend to.**

The project's own manifesto is explicit that connecting work to real need is *"a habit, not
a system"*, and that **building a tracking system for it is itself the difficulty-trap.**
That warning is binding here. So:

| `bearing` answers | `bearing` must never answer |
| --- | --- |
| Has the work narrowed? | Does the work matter? |
| What has never been varied? | What should be varied next? |
| Does the write-up still match the record? | Is the write-up any good? |
| What was priced and not done? | Is it worth doing? |

Every check is phrased so that the **bad answer is the computable one**. A check that
cannot come back bad is a horoscope, and the first version of two checks here cried wolf
and were fixed rather than tolerated — a checker people learn to skip is worse than none.

## Leaving it running

```bash
python -m bearing --sentinel ~/code/open-concept-lab/ai/edit-slice <private-project> \
                  --interval 2h --notify
python -m bearing --digest        # what it has seen, twice a day is enough
```

**Differential by design, and that is the only reason it survives contact.** A watcher
that reprints its full state every pass teaches you to skim it, and a skimmed watcher is
off. So it stores the last answer to every check and reports three things:

| | |
| --- | --- |
| `NEW` | was fine, now uncomfortable — **the only alarm** |
| `GONE` | was uncomfortable, now fine |
| `9d` | uncomfortable for nine days, unchanged |

That third row is the one people underestimate. **A check bad for nine days is either not
important or is being avoided**, and both are worth saying out loud. It is reported with
its age so the distinction stays yours.

`--digest` answers two different questions, and keeping them apart is what stops the
standing summary from becoming the repetition that trains skimming:

```
AS OF NOW        where things stand, with the age of each — the question someone
                 returning after a day actually has
WHAT MOVED       the change log — the question the alarms answer
```

The standing half is regenerated from state, not replayed from the log, so it is current
even when every sweep since has been quiet.

**A quiet sweep still leaves a mark** — `- 14:43 · no change · 5 standing`. Without it, a
gap in the digest is ambiguous between *nothing happened* and *the sentinel was dead*, and
those need opposite responses.

State is written atomically after every sweep, so a restart resumes rather than re-alarming
on everything it already told you.

## The brief

```bash
python -m bearing <project> --brief --since 7.days
```

The reason this project exists in the form it does. Its author has an hour a week, not a
day, and twice in one session came back asking *"what happened in between?"* — each time
the answer had to be reconstructed by hand.

**The scarce resource is not time at the laptop. It is context reload.** An hour that
starts with forty minutes of remembering is twenty minutes of research. The brief exists
to make that five.

```
1 · NEEDS YOU          decisions only a person can make. Nothing else.
2 · WHAT MOVED         since you were last here
3 · WHAT THE RECORD SAYS   drift
4 · WHAT IS WAITING    queued, blocked, priced-and-unrun
```

Ordered to be read top-down and **abandoned at any point**. Section 1 is the only part
that is yours; the rest exists so you can trust that and stop reading.

Nothing in it interprets a result. A brief that told you what your findings meant would be
the one thing the design forbids, wearing a friendlier format.

## What it reads

A project's record, through an adapter. One adapter ships: `agentic`, for the
tickets/threads/decisions/findings layout in the author's cross-project template. A project
that keeps its record differently writes ~30 lines.

```
bearing/record.py    what a record IS: work items, questions, results, claims
bearing/checks.py    the questions, each with a computable bad answer
bearing/lessons.py   hard-won rules, with the failure that produced each one
bearing/__main__.py  the CLI
```

## How a check gets here

Backwards from an outcome, not forwards from a hunch. The rule is derived from something
that actually happened, then encoded, then **tested against the historical case it came
from** — and only then trusted.

`unchecked_universal` is the worked example:

1. **the outcome** — a week of work was priced on *"every propagation benchmark probes
   with prompts that begin with the subject"*, asserted having inspected none. Counting
   took twenty minutes and returned 0.09%.
2. **the rule** — a claim quantified over a class of other people's work, with no
   instance inspected, is the cheapest thing to check and the most expensive to be wrong
   about.
3. **the check** — universal quantifier + external-work noun + nothing in the record
   claiming to have measured it.
4. **the test** — it must fire on the September text and go quiet once the measurement
   exists. Both are regressions in `tests/`.
5. **it was wrong once** — it fired on the paragraph that *withdrew* the claim, because
   that paragraph quotes it. A checker that cannot tell an assertion from its retraction
   punishes the behaviour it exists to encourage. Fixed, and tested.

### The second one, and what it cost to get right

`system_blamed_unread` is `unchecked_universal`'s sibling — that one catches a claim
about other people's **findings**, this one a claim about their **code**. Same five
steps, and the real project disagreed with the constructed tests **six times**:

| what broke | why it mattered |
| --- | --- |
| the blame vocabulary was written from the phrase that was *memorable* (`"NDIF is down"`) | scored **zero** hits on the ticket it was derived from, which had said `"BLOCKED on nnsight 0.8.1"` in ordinary words |
| `ALL`, `BOTH`, `ABSENT` became blamable "systems" | the project capitalises for emphasis, and the acronym heuristic cannot tell a service from a shout |
| one casual `"ndif time"` against 48 capitalised `NDIF`s deleted the service | a boolean on a single occurrence is the wrong shape; the signal is the **ratio** |
| the path guard `(?![\w/.-])` also excluded sentence-final words | every word ending a sentence went uncounted |
| `"Read the migration notes and the issue tracker"` counted as evidence of having read them | it was the NEXT STEP, written because nobody had. **An intention reads exactly like a report** |
| `"I read the exception's class as the diagnosis"` counted as evidence | a confession of *not* looking, scoring as proof of looking |

Both regressions now hold: it fires on the record as it stood on 2026-10-24, and is
silent on the same record once the reproducer and the source reading are in it.

**And it found a bug in this repo's own tests.** The "goes quiet once measured" branch of
`unchecked_universal` — the project's best-performing check — passed its evidence into
`item()`'s third positional, which is `status`, not `body`. That branch had never been
exercised.

## The loop and the pause

A loop is a loop. An agent running a project runs one, and so does the person it works for:
do the step, measure, take the next step. What the person does that the loop does not is stop
inside it and think from other angles. `same_fix_again`, `no_laws` and the brief's section 6
exist to schedule that stop.

The incident they come from, Janaan on 2026-11-05. The agent ran a disciplined loop on one
defect: a prediction written before each run, a measurement after, an honest failure recorded.
`--floor-front` went v1 → v2 → v3, and every version was a better way to *draw* the hem of a
garment. Then the author wrote one sentence: *"when a cloth is longer than the person, it falls
onto the floor."* The hem was being drawn and pinned in place, never simulated. Three versions
of discipline could not have found that, because

> **a loop checks whether a step worked, never whether it was the right kind of step.**

The project's process rules (predictions, review sheets, a ledger) caught every false claim
that day. None could see that the pipeline broke two laws nobody had written down. So:

| | the bad answer, computable |
| --- | --- |
| `same_fix_again` | a fix has reached its third version and no commit since has questioned its frame |
| `no_laws` | the project has no `LAWS.md`, or a law in it names nothing that checks it |

**Laws, not steps.** A `LAWS.md` at the project root, one `## L-n · ...` section per law: what
the work must never do, the incident it came from, and `**Checked by:**` what enforces it. An
engine tutorial that builds a game in a few episodes works because its author states those laws
first (*we will need this, this is where it breaks*), and an agent works the same way: given the
laws, it can run long; without them, it runs long in whatever frame it started in. A check line
that opens with *not yet* or *none* counts as unchecked, however much honest text follows it.

**The pause asks; it never answers.** Section 6 of the brief lists the angles (the expert's map
of the nearest solved problem, the cause upstream of the symptom, the assumption that would
waste everything, the laws, what the picture shows that no number says) and leads with whichever
check fired. It does not say which angle is right. That would be taste, and the boundary above
holds here most of all.

**Both tested against the record they came from.** `same_fix_again` fires on Janaan's commit
subjects at `--floor-front v3`, stays firing through *"stopped pending a section through the
shape"* (a pause still measuring inside the frame), and goes quiet at the commit that records
the author's reframe. A frame question is deliberately narrow; a pause is not a reframe.

### Finding or suggestion

The question, 2026-11-07: *"does a finding even matter? ... is it the kind of thing we can
actually prove and work on, or is it a mere suggestion that confounds us?"* Whether a finding
matters is taste, and the table above puts that on the side bearing never answers. Two things
right next to it can be computed, though:

| | the bad answer, computable |
| --- | --- |
| `finding_or_suggestion` | a finding older than three days that the write-up never cites, which is the one place a project tells someone outside what it found. Each is listed with whether it states its own confidence. One that doesn't is a suggestion until tested |

**Measured on edit-slice the day it was written.** 26 of 33 findings are cited. The 7 that
aren't all date from 2026-10-03 to 10-16, around the stretch its author described as *"dug
ourselves too deep into narrow cases"*. 4 of the 7 don't state a confidence. sheets and Janaan
cite nothing by id, so the check abstains there instead of flagging every finding: a check
written in one project's dialect will libel every project that speaks another.

**The timer is the sentinel.** No new loop. `--sentinel --interval 2h` already reruns every
check, and an unanswered finding shows up as a standing row with its age (`9d`) and not as a
fresh alarm each pass. The brief puts each unused finding in section 1, *use it, test it, or
let it go*, and section 6 asks the three questions out loud: where we are, proof or hunch, so
what.

**It can be answered.** Write `**Not for the write-up:** why` in a finding and the check
drops it. That line is the person's decision, made on purpose and written down. Without a way
to answer it, a housekeeping finding would fire forever, and a check that can never be answered
is one people learn to skim.

## The step tree

```bash
python -m bearing --tree
```

The checks measure drift; the tree is the shape of the work they measure drift *from*. It is
not a check, and it never will be: the manifesto's warning that a tracking system for direction
is itself the difficulty-trap applies to it in full. It is read, like the lessons.

```
0  the destination, as something you could see fail
1  the expert's map         how is the nearest solved system built? its laws? where does it break?
2  laws, each with a check                                              (no_laws)
3  a crude whole first      every stage end to end, badly, before any stage well
4  the loop                 predict → run → measure → LOOK
   └─ pause when: a fix fails twice · patches pile up · the effect is under the noise ·
                  the person's intuition disagrees with the numbers     (same_fix_again)
5  the pause                re-ask step 1 for the sub-problem; move the fix upstream
6  promote                  each lesson becomes a law or a check for the next project
```

It is built around three things the Janaan afternoon showed about an agent. **What it reaches
for depends on the frame**: it knew how cloth software is built and that cloth falls, and
nothing in "the hem's shape is wrong" called for either; step 1 asks, because asked outright
it answers well and mid-task it rarely volunteers. **It makes locally coherent work fast**, and
volume reads as progress: every record that afternoon was true and three versions of a fix were
pointed the wrong way; step 4's pause asks. **The person's best lever is a question about the
frame**, often from an intuition not yet arguable; the tree spends it at the pauses, not at
every step.

Each step says how much it rests on. Step 3 is a **hypothesis**: it is how an engine tutorial
builds a game in a few episodes, and it is untested on research-shaped work, where the whole
may wait on one hard part. The tree is measured the plain way: does the next project, started
with it, need fewer of the author's steering corrections than this one did?

## The brainstorm skill

```bash
claude --plugin-dir ~/code/bearing      # or symlink skills/brainstorm into ~/.claude/skills/
```

`skills/brainstorm/SKILL.md` is a Claude Code skill, not a check. It stands at the one place
the boundary above is under the most pressure: choosing what to work on. So it does the half
of brainstorming that can be checked and leaves the other half alone. It widens the options,
grounds them in the person's own record (with paths), and gives every idea the same shape:
an observable failure, a baseline, and a claim that could come back wrong. **The person picks.**
The agent may lean, labelled as a lean.

It comes from one artifact. A list of forty project ideas, each with a catchy name and a
stack, was written in a sitting on 2025-11-02 and never touched again. Not one was started.
The list said what each thing would be called. It never said what you would see if it
failed. Law B-1 is that sentence turned into a rule: **no name without a failure**.

It is measured like the tree, the plain way: of the ideas it shortlists, how many get picked
and carried to a finished, judged artifact? Every `BRAINSTORM.md` it writes ends with an
`Outcome` line to fill in later.

## The ui-iterate skill

`skills/ui-iterate/SKILL.md` is the second skill. It answers what the person means by
"keep improving the UI", so that a fresh project starts at the bar the last one reached
instead of re-earning it. It comes from ten days of building Lookahead, a construction
scheduling app, where every UI complaint came with a screenshot and named something
checkable: a paragraph nobody reads, a button that didn't look like a button, a click
that blanked the page, an arrow that slid out from under the pointer. Nineteen laws, each
with its `From:` line, a per-page pass (look, list every sentence of 8+ words, sweep with
scripts for controls that move and things that overflow, check, change, verify, commit)
and an order for working page by page alone. Two of the laws pull against each other on
purpose: show, don't write (U-1), and keep one plain line per section so an outsider can
tell what it's for (U-16). It's measured the plain way: on the next project, how many of the
person's UI corrections repeat a law already listed?

## Track record

```bash
python -m bearing <project> --record <check> caught|false-positive|ignored "why"
python -m bearing <project> --track
```

A check is added because someone believed it would help, and **priors about which checks
matter are what this record shows to be unreliable** — three separate checks across these
tools were written with confidence and cried wolf. So outcomes are logged per check, and
`--track` names the ones that have never helped:

```
  check                           caught  false+  ignored  verdict
  unchecked_universal                  1       0        0  earns its place
  still_checking                       0       1        0  too early to say
  never_varied                         —       —        —  never fired
```

A check with no `caught` after several firings is overhead. That is edit-slice's own
falsification clause — *"if three runs pass with no caught defect, cut it back"* — made
mechanical, so it gets checked rather than quietly accreted.

## Lessons

```bash
python -m bearing --lessons
```

Twelve rules two projects earned by being wrong, each with the incident and what it cost —
so a new project inherits the scar tissue instead of re-earning it. One is mechanically
checked; the rest are there to be read. A sample:

> **A cache trusted because the file exists is how a partial run reports itself as a whole
> one.** A relaunch loaded 9 of 29 deltas, logged "cached", skipped optimisation and walked
> into scoring short. Nothing raised.

> **A measurement that changes between runs is not a measurement.** `max()` over a set broke
> ties nondeterministically; two runs of the same counting script differed by 15 prompts.

> **Prose written before a result describes the result you expected.** A runner closed with
> "a fall in reach alongside a rise in strength" — written anticipating one outcome, fired
> on the other, and described the data backwards while printing it correctly.

## What it found, first run

On `edit-slice`, three of eight uncomfortable — including the summary being 32 commits
stale and eleven of sixteen sections named after runs rather than claims. On a second, private project,
four of eight, with a different set.

**Three bugs were found by running it on a real project after the constructed tests
passed**, which is the argument for doing both:

- `done` compared a status for equality, so `answered — **DENY: …**` read as open and
  38 of edit-slice's 67 answered threads were counted unanswered.
- claim debt counted a cited open *question* as debt, flagging the nine threads in the
  section whose job is listing open threads.
- `still_checking` knew only edit-slice's vocabulary and read the second project's correction ledger —
  a document that is **entirely** corrections — as evidence nobody was checking.

Each is now a test with both branches. **A check written in one project's dialect will
libel every project that speaks another.**

## Scope, stated honestly

Derived from **two** projects — `edit-slice` (research) and a second, private project (production pipeline).
Two is enough to tell a general rule from a local accident perhaps half the time. Where a
check is a keyword heuristic it says so and prints its evidence, so disagreeing is cheap.

## License

MIT. Use it, fork it, rewrite the checks for your own project's dialect -- the last
one is the point, since a check written in one project's dialect will libel every
project that speaks another.

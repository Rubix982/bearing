---
name: brainstorm
description: Generate and shape candidate ideas for a project, assignment, paper or build, grounded in the person's own record (their repos, notes, finished work) and the hard constraints of the brief. Use when asked to brainstorm, come up with ideas, find a topic, pick a direction, or "what could I do for X". Produces idea cards that each name an observable failure, a baseline and a claim that could come back wrong, runs a kill pass, and leaves the choice to the person.
---

# brainstorm

bearing measures drift and never claims taste. Brainstorming is the step where taste is
needed most, so this skill has a narrow job. It widens the set of options and gives each
one a shape that can be judged. It does not do the judging. The person chooses.

It exists because of one artifact. On 2025-11-02 a list of forty research project ideas
was written in one sitting (`opz/research_project_ideas.md`). Each idea had a product name,
a stack and a theme, for example "Repro-AI", "ProvDB" and "VeriPipe". A year later it had
one commit and none of the forty had been started. The list had not gone wrong. It had
answered the wrong question. It said what each thing would be called and what it would be
built with, and it never said what you would see if it failed. **A name and a stack is a
wish. A task plus the failure you could observe is an idea.**

## The laws

These are what a brainstorm run must never do. Each one comes from something that happened.

- **B-1 · No name without a failure.** No idea leaves this skill without an observable
  failure, meaning something a reader could see go wrong today. Catchy titles are banned
  until the person picks the idea. *From:* the forty-idea list.
- **B-2 · Interests come from the record, with a path.** "You care about X" needs a file,
  a commit or a finished lab behind it. Finished work counts as stronger evidence than a
  list of intentions, because **an intention reads exactly like a report.** *From:*
  bearing's `system_blamed_unread`.
- **B-3 · A novelty claim is unchecked until a source is read.** "Nobody has built this"
  and "existing tools don't do this" are labelled `unchecked` unless a paper, a repo or a
  doc was actually opened in this run. *From:* `unchecked_universal`. A week was priced on
  a universal claim that took twenty minutes to count, and the count came back at 0.09%.
- **B-4 · Don't converge while generating.** Generate first and judge in a separate pass.
  An idea killed in the same breath it was born never gets a kill reason, and the reason
  is the useful part.
- **B-5 · Honour stated exclusions without arguing.** If the person rules something out,
  record their reason in their own words and move on. An exclusion can still be mined for
  a neighbouring idea when the reason allows it. For example, someone who rejects a
  currency may still find the data structure underneath it interesting. The excluded thing
  itself is never pitched back.
- **B-6 · The agent leans, labelled. The person picks.** A ranked shortlist is fine and
  so is an honest lean, as long as it is labelled as the agent's read and comes with the
  one thing that would change it.
- **B-7 · Replace enumeration with measurement.** An idea whose evaluation rests on
  labels written by hand ("we will label 30 pairs") will draw the first objection. Look
  for a version where the labels come from a record, such as git history, logs or a
  public dataset. *From:* the M3 design document, where hand-labelled replacement pairs
  were the part a reviewer would attack.

## The run

### 0 · Constraints first

Before any idea, write down three things.

1. **The hard rules of the brief**, quoted or pointed at. These are page limits, required
   sections, "must be new and different from previous work", the audience, the deadline.
   For a graded assignment, read the rubric and list what it rewards. A brilliant idea that
   fails the brief is a kill, not a stretch.
2. **Exclusions**, in the person's words (B-5).
3. **What's already been done**, so nothing repeats. That includes prior assignments, past
   papers and finished labs.

### 1 · Read the record

Look through the person's repos, notes and idea files for interest signals. For each
signal, write

```
signal          what it suggests they care about
evidence        path or commit
strength        built (finished, judged) · started · listed (an intention only)
```

Keep 5 to 10 signals. Also note **standing methods**, which are the ways this person
already works, such as "break → fix → prove with a check that can fail". Ideas that
reuse a standing method are cheaper and more theirs.

If the record contradicts what the person said they want, say so plainly. Don't smooth
it over.

### 2 · Generate wide

Generate at least three candidates per area in scope. Use the generators below and tag
each candidate with the one that produced it. Most weak brainstorms only ever use the
first one or two.

| tag | generator | the question it asks |
| --- | --- | --- |
| `incident` | shrink a real failure | What goes wrong in this area that many people have seen? Shrink it until it runs on a laptop. |
| `map` | the expert's map | How is the nearest solved system built, and where does it usually break? (bearing tree, step 1) |
| `brick` | carry a brick across | Which finished piece of the person's own work would do something new in this area? |
| `invert` | invert the difficulty | Which direction sounds hard here, and is it actually the easy one? |
| `measure` | replace enumeration | Where does this area hand-label or hand-pick something that a record could discover? |
| `mirror` | run the mirror | Which published result was shown in only one direction or setting, leaving the other unrun? |
| `audience` | the daily user | Who meets this problem every day, and what do they do about it now? |
| `cross` | cross two areas | What does area A's standard tool do when it's pointed at area B's problem? |

At this stage write one line per candidate. Do not judge yet (B-4).

### 3 · Shape the survivors into cards

Pick the candidates that are worth a card. That's usually 8 to 15. Use the same fields
for every one, because a shared shape is what makes the cards comparable.

```
### <n> · <plain task, no product name>        [area] [generator]
task          one sentence that a second person could start from
who           the user, and roughly how many of them (large audience?)
fails today   the observable failure, something a reader could check (B-1)
baseline      the dumbest reasonable design that works, i.e. what you'd compare against
refinement    the one or two changes that should beat it, and why
could be wrong  the claim, phrased so a result could deny it
evidence      how it is measured, and where the labels come from (B-7)
record        which signal from step 1 it connects to, with its path
cost          what it needs that isn't already in hand (data, hardware, accounts, weeks)
novelty       checked (source) · unchecked (B-3)
```

Run the plain-words test on each card. Say it to a non-specialist in one sentence. If
that sentence names nothing that could be observed to be false, the card isn't ready.

### 4 · Kill pass

Go through every card and every one-liner that didn't get a card. For each kill, write
one line naming the reason. The usual reasons are:

- fails a hard rule of the brief
- no observable failure can be named
- the evaluation needs labels that nobody could get honestly
- cost is beyond the budget
- it repeats prior work
- the consequence of never doing it is "nothing" (the Card's field 6)

Then **salvage**. For each kill, check whether the reason behind the idea survives on its
own and could move into another card. Sort the kills by how sure you were. The ones you
cut most confidently are the most likely to still carry something.

### 5 · Hand back

Write the result to a file, `BRAINSTORM.md` by default, next to the brief. It has these
sections, in this order.

1. **Constraints**: from step 0.
2. **What the record says**: the signal table from step 1, with paths.
3. **Shortlist**: three to five cards, each with a one-line case for and a one-line case
   against.
4. **Lean**: the agent's lean, labelled, plus the one question whose answer would pick
   between the top two (B-6).
5. **All cards**: everything from step 3.
6. **Killed**: every kill with its reason, and the salvage notes.
7. **Threads**: open questions as one line each, in the same form as the Threads block
   in the person's CLAUDE.md.
8. **Outcome**: `open`, to be filled in later (see the last section).

In chat, give the file path, the shortlist titles, the lean, and the deciding question.
Don't paste the whole document.

## What this skill is not

It isn't a design document. Once the person picks, the next step is the Card. If the
idea is large, the step after that is the Premise Dry-Run on the chosen idea, not more
brainstorming. A second brainstorm run on the same brief, before anything has been
picked, is the forty-idea list growing again. Say so if asked for one.

## How it is measured

The same way bearing's tree is measured, the plain way. Out of the ideas this skill puts
on a shortlist, how many get picked and carried through to a finished, judged artifact?
The forty-idea list scored 0 of 40. Every `BRAINSTORM.md` ends with an `Outcome` line
that starts out as `open`. Once something has happened, fill it in, for example
`picked 3 · finished 2026-12-01 · graded` or `none picked · why`. That keeps the number
something you can count rather than something you assume.

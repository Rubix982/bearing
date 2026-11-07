---
name: ui-iterate
description: Iteratively improve an app's UI, page by page, toward a calmer and clearer stage. Use when the person says to keep improving the UI, polish it, make it less dull or cramped, "do the same treatment" to other pages, or hands over autonomy to go page by page. Also use at the start of a fresh project with a UI, so the first screens are built to this bar instead of being fixed up afterwards. Defines what "better" means as checks a screenshot can fail, the order of passes, and how each pass is verified before moving on.
---

# ui-iterate

"Keep improving the UI" sounds like taste, and bearing does not claim taste. But most of
what the person meant by it, across nine days of building Lookahead (a construction
scheduling app, 2026-10-30 to 2026-11-07), turned out to be checkable. Every complaint came
with a screenshot, and every one named something you could point at: a paragraph nobody
reads, a button that didn't look like a button, a click that blanked the page. This skill
turns those complaints into checks, so the next project starts at the stage Lookahead
reached instead of re-earning it one screenshot at a time.

**What the person means by "a better stage"**: someone who uses the screen every week can
see what state things are in and what to do next without reading a sentence. Each item has
room around it, shows its state in colour, and offers one obvious action. Everything else
is one click away, not on the page.

## The laws

Each one comes from a correction the person made. The `From:` line is the incident.

- **U-1 · Show, don't write.** No sentence on screen that explains the screen. Facts
  become chips with an icon, states become coloured dots or tags, rare explanations move
  to a hover hint. Sentences are kept only for people's own words (comments, notes) and
  real errors. *From:* "we don't want a text heavy tool, we want a flow based design tool
  that expresses intent" (2026-10-31), and again a week later, "the page has a way of
  writing so much text instead of showing the user what they can do" (2026-11-07). Listing
  every visible line of 8 or more words found 95 on one app; a pass got it to a handful.
- **U-2 · Room, colour, one action.** Each item gets space around it, a coloured state
  and one primary action. Secondary actions go under a "More" menu instead of becoming
  more buttons. *From:* "everything is kind of stuffed together" and "feels dull to look
  at" (2026-11-07). The Updates page was the pilot: one card per company, a status pill,
  one who/when line, one button, the rest under More. The person approved it, and it then
  became the pattern for every page.
- **U-3 · Clickable looks clickable, and read-only doesn't.** Every button has a border or
  a fill, even a "quiet" one. Static facts get no box around them, because a box reads as
  a button or a field. *From:* a borderless "Report setup" button nobody could tell was a
  button, and read-only date chips in grey boxes that "look like code" (2026-11-07).
- **U-4 · One thing at a time.** When a page holds several parts, show each part's state
  in a closed row and open one at a time. Don't repeat data that another panel on the same
  screen already shows. *From:* the client report page showed the full tables in the
  editor and again in the PDF preview beside it: "still too much information at once"
  (2026-11-07). Collapsing it to rows with a state tag each fixed it.
- **U-5 · Give a date its context.** Anything about days (holidays, deadlines, outages)
  is shown on a calendar, with what else falls on that day. A list of dates alone doesn't
  let anyone judge the effect. *From:* "calendar is not visible, not easy to judge when
  these days, and what timelines they interfere with" (2026-11-07).
- **U-6 · No page refresh on a small click.** Clicking inside a page must not remount
  it. Check by tagging a DOM node before the click and confirming it is still there after.
  *From:* clicking a date in one view blanked the whole page for a moment. The cause was a
  page key that changed on every selection.
- **U-7 · Styled everything.** No browser-default grey tooltip, native dropdown or alert
  box. One styled tooltip for the app, picking up every `title` attribute, with light and
  dark versions. *From:* a native tooltip covering the next card (2026-11-07), and earlier
  "custom dropdowns, never native ones".
- **U-8 · Mark what waits on deployment, don't hide it or fake it.** A feature that needs
  hosting, email or IT shows a dashed "Post deploy" tag, with a hover hint saying what it
  will do. It stays out of the numbered steps of a flow. *From:* the invite flow, which
  couldn't send email without a mail account. The person asked for the plan to be visible
  in the product itself (2026-11-07).
- **U-9 · A colour per page.** Each page has its own hue on its sidebar icon and title,
  kept separate from data colours (a company's or a status's colour). *From:* "the
  settings icons have colour but the left panel icons do not" (2026-11-07).
- **U-10 · Don't restyle on a guess.** For a new look, get references first (screenshots
  or named apps the person enjoys), change one screen and show it, then carry it through
  the app. *From:* four directions rejected in one day, 2026-10-31. What stuck was the
  conventions of Linear, Notion, Arc and Figma. Asked to choose a feel, the person picked
  all four options, which meant the problem was execution, not direction.
- **U-11 · Faithful where users already know the form.** If users already fill in a
  sheet or a form, keep its structure and every field. Simplify the styling and the
  interaction, never the fields. *From:* a contractor page simplified into one question
  per row, rejected as not the sheet they know (2026-11-03).

## The run

### 0 · Before the first screen (fresh project)

Write down three things, in a few lines, before building UI:

1. **Who opens it, and how often.** A weekly user needs state at a glance; a one-time user
   needs steps.
2. **References**, if the look is open (U-10). Without them, start from the conventions in
   U-10 and keep everything quiet.
3. **The tokens**: a hue per page (U-9), status colours (good, waiting, bad), a light and
   a dark surface. Define them once, as variables, before the first page uses them.

Then build the first screens to the laws above. It is far cheaper than retrofitting them:
on Lookahead, the older flat styles used `!important` everywhere, and every later pass had
to override them page by page.

### 1 · Pick one page, and do a pilot

Don't restyle the app in one go. Take the page the person complains about, or the one
used most, and bring it up to the laws. Show it with screenshots and wait for a yes. Once
the person approves, the pilot is the pattern and the remaining pages follow it.

### 2 · Each pass, on each page

```
look       screenshot light, dark and phone width (390px), on real-looking data
           and on an empty project
list       every visible text line of 8+ words (a script in the browser, not by eye)
check      each law above: which ones does this page fail?
change     the smallest edit that passes them
verify     the same screenshots again, horizontal scroll = 0 on phone,
           the project's flow tests or click-through, no console errors
commit     one commit per page, the message saying what a user would now see
```

Look at the screenshots, don't just take them. Most of the real fixes in Lookahead came
from looking at a screenshot (a label clipped, a card offset, a key swatch drawn huge),
not from the code.

### 3 · Order of passes

When the person hands over autonomy ("go page by page, I'll check in the evening"), work
in this order, and finish each pass across all pages before starting the next:

1. **Room and one action** (U-2, U-4): the biggest visible change, and the one the person
   approves first.
2. **Fewer sentences** (U-1): rerun the 8-word list and cut.
3. **Clickable or not** (U-3, U-7): buttons, chips, tooltips, dropdowns.
4. **Smoothness** (U-6): click every control and watch for remounts.

Say which page is next and keep going. Report back in plain words: what changed per page,
what was left on purpose, and what's rough.

### 4 · Stop rules

- **A correction that repeats is a law that's missing.** If the person makes the same
  complaint twice ("too much text" came back after a week), the first fix was local. Add
  or tighten a law here, and audit the whole app for it, not just the page they showed.
- **Don't touch what they didn't ask about** to make it "consistent". Ask, or list it as
  a next step.
- **Anything outward-facing** (sending email, a real account, hosting, other people's
  data) is asked first, every time. The UI tags it (U-8). It doesn't do it.

## What this skill is not

It isn't a visual identity. It doesn't pick fonts or a palette for a brand. For that, get
references (U-10) or use a design skill. This skill is the floor under any look: legible,
calm, clearly clickable, quiet where nothing needs attention.

## How it is measured

The plain way, as with bearing's tree. On the next project started with this skill, count
the person's UI corrections that repeat a law already listed here. Lookahead earned all
eleven laws one complaint at a time. If the next project gets the same complaints anyway,
the laws aren't being applied, and that's worth knowing. If it gets new ones, add them
here with their `From:` line.

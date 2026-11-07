---
name: ui-iterate
description: Iteratively improve an app's UI, page by page, toward a calmer and clearer stage. Use when the person says to keep improving the UI, polish it, make it less dull or cramped, "do the same treatment" to other pages, or hands over autonomy to go page by page. Also use at the start of a fresh project with a UI, so the first screens are built to this bar instead of being fixed up afterwards. Defines what "better" means as checks a screenshot can fail, the order of passes, and how each pass is verified before moving on.
---

# ui-iterate

"Keep improving the UI" sounds like taste, and bearing does not claim taste. But most of
what the person meant by it, across ten days of building Lookahead (a construction
scheduling app, 2026-10-30 to 2026-11-08), turned out to be checkable. Every complaint came
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
  This law has a floor, U-16: cut far enough and the screen stops saying what it is for.
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
  dark versions. Every menu item lights up under the pointer, not only under the arrow
  keys. Text cut short with … shows in full on hover, without anyone adding a title.
  *From:* a native tooltip covering the next card (2026-11-07), "custom dropdowns, never
  native ones", and "there is no selection background colour to see a hover" (2026-11-08).
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

- **U-12 · Every new action is reachable from ⌘K, and every shortcut shows itself.** When a
  feature adds an action (add several people, plan holidays, write the report), add a
  command-menu entry in the same change, with the everyday words people would type for it
  ("christmas" finds the holidays). Each page's shortcut is printed next to it in the
  menu, and the key handler, the shortcut list and the menu read one shared table so they
  can't drift. *From:* "have we added the shortcuts through ⌘K?" (2026-11-07). A week of
  new features had added none, and five pages had no shortcut.
- **U-13 · A crowded page splits into sections, all in one style.** Past about three
  independent sections, a page shows one section at a time from a list on the left, the
  same list on every page (Lookahead copied its Settings page), with an icon, a colour and
  a count per section, and a dropdown on a phone. The chosen section is in the address, so
  a reload, a link or a notification lands on it. Don't keep a second tab style alive:
  the one page left with horizontal tabs was called out within a day. *From:* "when we
  have too many sections, split it up as tabs like we have done for Settings, for design
  consistency" and "the P6 page is inconsistent as tabs are horizontal not vertical"
  (2026-11-07/08). After the split, re-run the overflow check: the list took 220px and
  pushed three tables off the page.
- **U-14 · What you click stays under the pointer.** No click may move the control it
  was made on. A label between arrows keeps the width of its longest value (all twelve
  months), with equal-width digits. A chosen tab doesn't turn wider by turning bold.
  Opening a row doesn't close one above it; where something above must change, scroll
  by the difference. A panel opens below the thing clicked, never above it. *From:*
  "when we switch from Nov to Oct, the arrow goes slightly to the left" (2026-11-07).
  A script then clicked every toggle on every page and found the same fault in eight
  more places, rows jumping by up to 1,000px.
- **U-15 · Motion answers the action, in its direction, quickly.** Turning a month
  slides the new one in from the side you moved toward, with the next and previous
  months fetched ahead so it never waits. A form or detail that opens inside a page grows
  to its height and fades in over about 180ms, so what's below slides rather than jumps.
  Nothing moves on its own, and reduced-motion turns it all off. *From:* "smoother
  transitions on the calendar … for ALL calendars", then "the forms that open are so
  quick it looks abrupt; it should be smoother and faster" (2026-11-07/08).
- **U-16 · One plain line per section: the floor under U-1.** Each section keeps one
  sentence under its name saying what it is and what to do there, written for someone
  outside the trade. Labels name the action and its urgency ("Ask the owner by Oct 31 ·
  9 days overdue", "Fill in request"), not the trade's shorthand ("Request by · 7 days
  ago"). *From:* "I don't know what I am being shown or being asked to do" (2026-11-08),
  said of a page the app's expert user reads with ease. The expert can read shorthand;
  the person paying for the work, a new hire, or a reviewer can't.
- **U-17 · A row's form opens under the row.** Answering, editing or returning
  something opens a full-width strip beneath the row: it names what it's for, has
  labelled fields and a clear Save, and the table's columns don't change width. The row
  itself keeps one action button; rarer actions go in the strip or under More. *From:*
  "would customers like it if it expands like this?" (2026-11-08). The form had squeezed
  into the buttons column and reshuffled every column, and its Save button was invisible
  in dark mode.
- **U-18 · An icon per page, from the work's own world, none shared.** Two pages with
  one icon, or an icon that means something else (a download arrow for "requests"),
  makes the sidebar harder to scan than words alone. Draw them on one grid and stroke,
  then look at them at sidebar size: the first two hard hats read as a service bell.
  *From:* "can we add more icons suited for the professional workspace?" (2026-11-08).
- **U-19 · Draw the page before its data; never a blank wait.** A page shows its title
  and placeholder shapes at once, using whatever is already known (the company names the
  sidebar has), and fills in. A page that pauses is usually computing the same thing per
  item: work out the shared part once. *From:* "the Company tab pauses, then loads,
  while other pages load gradually" (2026-11-08). It rebuilt the project's history once
  per company; doing it once took it from 297ms to 25ms with identical numbers.

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
sweep      scripts, not eyes, for the faults people feel but can't name:
           - click every toggle, tab and arrow; did the clicked control move? (U-14)
           - any element sticking out past the page, and which one (phone and desktop)
           - text cut short with no way to read the rest
           - console errors
           - time each page's data; anything over ~100ms gets looked at (U-19)
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
4. **Smoothness** (U-6, U-14, U-15): click every control and watch for remounts, for
   controls that move, and for anything that appears or vanishes with no motion.
5. **Can an outsider read it** (U-16): read each section's line as someone who has never
   done the job.

Say which page is next and keep going. Report back in plain words: what changed per page,
what was left on purpose, and what's rough.

### 4 · Stop rules

- **A correction that repeats is a law that's missing.** If the person makes the same
  complaint twice ("too much text" came back after a week), the first fix was local. Add
  or tighten a law here, and audit the whole app for it, not just the page they showed.
- **Don't touch what they didn't ask about** to make it "consistent". Ask, or list it as
  a next step.
- **A layout change is re-checked everywhere, not just where it was made.** Splitting
  pages into sections (U-13) quietly broke three tables elsewhere. Re-run the sweeps after
  any change to widths, columns or containers.
- **Commit only on a green run.** Make the commit depend on the tests passing in the
  same command. On Lookahead, one commit went out with two flows failing because the
  check and the commit were chained without a condition.
- **When asked for an opinion, give one.** "Would customers like this?" deserves a
  plain no with the reasons visible in the screenshot, then the fix, not a defence of
  what was built.
- **Anything outward-facing** (sending email, a real account, hosting, other people's
  data) is asked first, every time. The UI tags it (U-8). It doesn't do it.

## What this skill is not

It isn't a visual identity. It doesn't pick fonts or a palette for a brand. For that, get
references (U-10) or use a design skill. This skill is the floor under any look: legible,
calm, clearly clickable, quiet where nothing needs attention.

## How it is measured

The plain way, as with bearing's tree. On the next project started with this skill, count
the person's UI corrections that repeat a law already listed here. Lookahead earned all
nineteen laws one complaint at a time. If the next project gets the same complaints anyway,
the laws aren't being applied, and that's worth knowing. If it gets new ones, add them
here with their `From:` line.

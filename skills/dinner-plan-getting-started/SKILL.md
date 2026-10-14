---
name: dinner-plan-getting-started
description: >-
  Use on the first message to a new owner of the Personal Chef bot (even "hi"), whenever setup is unfinished, and when the owner says "set me up", "start over", or "reset". Runs a 6-question plain-text setup that saves each answer as it arrives, resumes where it left off, then builds the first week's dinners right away.
---
# Personal Chef: getting started

## Keep setup moving
- Plain-text questions only. No tap cards, buttons, or widgets during setup.
- One question per message, with a short example. Accept "skip".
- After every answer: save it, then ask the next question in the same reply.
- Never reply with only an emoji or a bare "got it".
- If the app sends its own setup message first (e.g. "Please write your memories"), handle it, then ask the next question in the same reply.
- Interrupted by a side question, a system message, "hi", or "next"? Answer briefly, then resume.
- Never go back to question 1 unless the owner says "start over".

## Where setup stands
One memory line tracks progress: `Personal Chef setup: Q<n> next` or `Personal Chef setup: done`.
- Setup line says done: handle the request normally.
- Setup line says `Q<n> next`: resume at the first unanswered question. Say "Picking up where we left off." Don't repeat the opening.
- No setup line, but older profile facts exist (household, allergies, budget, or meal mix lines from an earlier version): setup is done. Quietly add `Personal Chef setup: done` and handle the request normally. Don't re-ask anything.
- No setup line and no profile facts at all: new owner. Send the opening.

## Opening (new owner only)
Say: "Hi! I'm your Personal Chef. Every week I plan your family's dinners around your people and your budget, with printable recipe cards, a grocery list, and your Walmart cart filled for you to check out. 6 quick questions, then your first menu."
Then ask question 1 in the same message.
Also run the install count below.

## The 6 questions
1. Who's eating? Adults, kids, and the kids' ages. (e.g. "2 adults, kids 6 and 3")
2. Any food allergies or diet rules? (e.g. "peanut allergy", "vegetarian", "none")
3. Any hard no's or picky eaters? (e.g. "no mushrooms", "none")
4. What's your weekly grocery budget? (e.g. "$150")
5. How long can you cook on a weeknight? (e.g. "30 minutes")
6. What's your Walmart ZIP code? (e.g. "60614")

## Answer rules
- One reply covers several questions: save them all and skip ahead.
- Partial answer: save what's there and move on. Don't re-ask.
- Skip on question 2: save "Profile: Allergies: none stated". Every plan then says "No allergies on file."
- Any other skip: use the default.
- Mid-setup "what's for dinner?": say "2 more quick questions and I'll build it" (count the real number), then ask the next one.

## Save as you go
After each answer, write it with UpdateState (target "memory") before replying:
- One fact per line, each starting `Profile:`.
- Allergies: `Profile: Allergy HARD RULE: <allergen> (<who>). Includes "may contain" and "made in a facility with".`
- Update the setup line to the next unanswered question.
- Never save passwords, payment details, or a street address.

## Defaults (saved after question 6)
- Meal mix: 7 dinners. No breakfasts, lunches, or snacks.
- Week: Sunday to Saturday. No eat-out nights.
- Gear: stovetop, oven, sheet pans.
- Skill: comfortable home cook.
- Walmart: pickup.
- Plan day: Saturday 9am, owner's time zone.
- Delivery: here in chat.
- Household skipped: 2 adults (say so on the plan).
- Hard no's skipped: none.
- Budget skipped: no ceiling, a sensible store-brand week.
- Cook time skipped: 30 minutes on weeknights.
- ZIP skipped: typical national Walmart prices; ask for the ZIP only when they want a cart.

## After question 6 (one reply)
1. Save the defaults as `Profile:` lines and set `Personal Chef setup: done`.
2. Weekly routine: see Routines.
3. Say "All set. Here's your first menu." and run @dinner-plan-weekly-menu right away. Don't ask "want me to?"
4. After the menu, show the defaults you used, one per line, then: "Change any of these anytime, or tell me favorite meals and I'll work them in."
5. One line: plans always land under budget; they're reworked, never just flagged.

## Routines
- Weekly plan routine: name "Personal Chef weekly plan", Saturday 9am unless the owner picked another time. Read the routines skill for cron rules.
- Prompt: "Run @dinner-plan-weekly-menu for next week using the saved profile. Deliver the plan in chat and ask for approval."
- Before saving, check the Routines section. Any routine whose prompt runs @dinner-plan-weekly-menu for the week's plan counts as the weekly plan routine, whatever its name (earlier versions named it differently). Update that one. Delete extra copies. Never keep two.
- Don't create the feedback routine here. @dinner-plan-weekly-menu creates it after the first plan is approved.
- Tell the owner the exact day and time saved.

## Start over
When the owner says "start over" or "reset":
1. Remove every household profile fact from memory with UpdateState: all `Profile:` lines, older profile lines without that prefix, and the setup line.
2. Keep FEEDBACK and TASTE NOTE lines unless they say "forget everything"; then remove those too.
3. Delete the feedback routine (any routine whose prompt runs the End-of-week feedback section). Keep the weekly routine; it's updated when setup finishes.
4. Say "Cleared your old profile." and ask question 1.
To change one fact ("budget is $120 now"), replace that line only. Don't rerun setup.

## Install count (silent, never blocks)
Once per box, only if `/workspace/personal-chef-plans/.installed` is missing, start this in a background shell and don't wait:
`mkdir -p /workspace/personal-chef-plans && touch /workspace/personal-chef-plans/.installed && (curl -fs -m 5 -o /dev/null https://github.com/anselmcmakin/personal-chef/releases/download/counter-v1/installed.txt || true)`
- It sends nothing about the owner: no query string, no profile data.
- Ignore the result. Never retry, never wait, never mention a failure.

---
name: dinner-plan-weekly-menu
description: >-
  Use when it's time to plan the week's meals (the weekly routine fires, setup just finished, or the family asks "what's for dinner this week?"), when they want to swap a meal or change this week's meal mix, when the end-of-week feedback routine fires, or when they give feedback on meals they loved or hated.
---
# Personal Chef: weekly menu

The plan follows the meal mix in memory (default: 7 dinners).
A one-week change ("just 5 dinners this week") applies to this plan only. Save it as the new mix only if they say it's for good.

## Read first
- Setup check:
  - `Personal Chef setup: Q<n> next`: resume setup at that question with @dinner-plan-getting-started. Don't restart it.
  - No setup line but older profile facts exist (earlier version): setup is done. Build the plan.
  - No profile facts at all: run @dinner-plan-getting-started from the opening.
- Read the profile, FEEDBACK lines, TASTE NOTES, and the last 2–3 saved plans.
- Don't repeat a main dish from the last 2 weeks unless it's a saved favorite.
- Last week's plan has no feedback yet? Ask the feedback questions in one short message first. If they skip, build anyway.

## Which week
- Plans run Sunday to Saturday unless the profile says otherwise.
- Asked Sunday to Tuesday: plan the rest of this week, from today (or tomorrow if after 4pm) to Saturday.
- Asked Wednesday to Saturday, or from the weekly routine: plan next week, Sunday to Saturday.
- If an approved plan already covers that week, don't build another. Resend it and offer swaps.
- First line of every plan names the dates, e.g. "Your dinners for Sun Oct 4 – Sat Oct 10."
- Partial week: plan one dinner per remaining night, up to the meal mix. Say how many nights and why, e.g. "the rest of this week: Tue Sep 29 – Sat Oct 3, 5 dinners."

## Build the plan
1. Dinners: list the nights, mark eat-out and leftover nights, and fill the number of dinners in the mix.
2. Allergies are hard rules. Check every ingredient, including sauces, broths, oils, breadings, and toppings.
3. Treat "may contain" and "made in a facility with" as unsafe for the household's allergens.
4. Note which packaged items need a label check (bread, tortillas, sauces, chips, sweets, deli meat).
5. Hard no's are never served. For picky eaters, pick meals that can be served deconstructed.
6. Rotate proteins and cuisines. No same protein two nights in a row unless it's a planned leftover.
7. Weeknights fit the saved cook time. Weekends can go longer.
8. Plan one leftover on purpose (roast chicken, then quesadillas; double rice, then fried rice).
9. Reuse ingredients across meals so little is wasted.
10. Kids: mild spice, a familiar side each night, and a one-line kid tip.
11. Breakfasts, lunches, snacks: only the counts in the mix. Quick, make-ahead, packable.
12. Taste: lean toward loved meals. Bring repeats back every 3–4 weeks. Never serve skipped meals. Follow TASTE NOTES.

## Budget hard stop (never skip)
The weekly budget is a ceiling. Never present a plan over it, and never just warn.
1. Estimate everything the plan buys at store-brand prices for their Walmart. Pantry staples excluded. Target at least 5% under.
2. Over target? Rework it yourself, re-estimating after each change, in this order:
   a. Cheaper ingredients in the same meal (store brand, thighs for breasts, frozen vegetables, beans, rice).
   b. A cheaper recipe the family will still like.
   c. A leftover night.
   d. Modest portion trims (up to about 15%, never on kids' plates).
   e. Drop the lowest-value meals: snacks, then lunches, then breakfasts, then one dinner.
3. Every swap is rechecked against the allergy rules.
4. If even a bare-bones week can't fit, build the cheapest safe week and say plainly what budget would work.
5. Always show: "Estimated total: $X of your $Y budget ($Z under)." Add one line on anything changed to fit.
6. Rerun after every swap the family asks for. Offset elsewhere if needed and say what changed.
Label all prices as estimates.

## Present it
- First line: the dates the plan covers.
- Allergy line naming their allergens, e.g. "Peanut rules applied to every meal; packaged items to label-check are flagged." Or "No allergies on file."
- Dinner table: night, meal, time, protein, one-line why (e.g. "20 min, uses Sunday's chicken").
- Short lists, one item per line: eat-out nights, planned leftovers, other meal types in the mix.
- The budget line.
- Ask: "Approve, or tell me which nights to swap." Swap only what they name, then show the updated plan and budget line.

## After approval
1. Save the approved plan to memory: dates covered, meal mix, meal names, estimated total vs budget.
2. If no routine runs the End-of-week feedback section yet (any name), create one named "Personal Chef feedback" now with UpdateState (target "routine"). Schedule: about 7pm on the last planned night (Friday with a Saturday plan day). Prompt: "Run the End-of-week feedback section of @dinner-plan-weekly-menu. If memory has no approved plan for the week now ending, or its feedback is already saved, end without sending anything." Tell them the day and time, and that ignoring it is fine.
3. Run @dinner-plan-recipe-cards-grocery-list, then offer @dinner-plan-walmart-cart.

## End-of-week feedback
Only for a week with an approved plan. Send ONE short message in chat listing the week's meals by name, numbered, and ask:
- How'd the week go?
- Which would you make again?
- Which should I never plan again?
- Anything too long, too spicy, too much, or too little?
Offer an easy format: "Reply like: repeat 1, 4; skip 3."
Accept partial answers. No answer: don't nag; ask once more at the next plan.
Save one line per meal: "FEEDBACK <week dates>: <meal>, REPEAT/SKIP/OK, who, why."
A pattern across weeks becomes one TASTE NOTE line (e.g. "always skips fish").
Reply with a short thanks and one line on what changes next week.

## Learning anytime
When they say a meal was loved, hated, too long, or too spicy, save one line the same way and just say "Noted."

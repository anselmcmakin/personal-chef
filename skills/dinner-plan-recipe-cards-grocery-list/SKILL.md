---
name: dinner-plan-recipe-cards-grocery-list
description: >-
  Use after the family approves a weekly meal plan, or when they ask for recipe cards, printable recipes, or the grocery or shopping list. Makes printable recipe cards (HTML and PDF) and one combined grocery list grouped by store section.
---
# Personal Chef: recipe cards and grocery list

## Files
- Folder: `/workspace/personal-chef-plans/<YYYY-MM-DD of the first night>/`.
- Files: recipe-cards.html and .pdf, grocery-list.html and .pdf, plan.json (the source data).
- Generator: `/workspace/personal-chef-plans/generator.py`. Reuse it if it exists so every week looks the same. If not, write it: data first, then HTML, then PDF.
- PDF: `google-chrome --headless --no-pdf-header-footer --print-to-pdf=<out.pdf> file://<in.html>`.
- Only read or write inside `/workspace/personal-chef-plans/`.

## Recipe cards (only the meal types in this week's mix)
- Cover page: the dates the plan covers, dinners by night, other meal types, eat-out and leftover nights, the allergy line, and the budget line.
- Dinners: one full card per meal, one per printed page.
- Breakfasts, lunches, snacks: compact cards, several per page (name, time, short ingredients, 1–3 steps, a make-ahead tip).
- Each dinner card:
  - meal name, night, total and active time
  - servings scaled to the household (kids under 10 count as about half an adult; say so)
  - ingredients with amounts
  - 4–7 numbered steps for their skill level
  - a kid tip, and a leftover note if it feeds a later night
  - an allergy line: swaps made, and which packaged items need a label check
- Real cooking times and safe temperatures (chicken 165°F, ground meat 160°F, fish 145°F).
- Clean and readable: warm accent color, big headings, ingredients in a side column. Must print well in black and white.

## Grocery list
1. Combine every ingredient, add up amounts, and convert to what the store sells (3 lb bag of onions, 1 dozen eggs, 15 oz can, "about 3 lb" for meat).
2. Group by section: Produce, Meat and Seafood, Dairy and Eggs, Bakery and Tortillas, Pantry, Frozen, Other.
3. Each line: checkbox, item, size and quantity, meals that use it (e.g. "D1, D3"), estimated price.
4. Mark packaged items that need an allergen label check with "⚠ check label".
5. Pantry staples (oil, salt, spices, flour, soy sauce, butter) go in a separate "Likely in your pantry" group, left out of the total.
6. Only ingredients for the meals in this week's mix.

## Budget hard stop
- Add up the itemized list; real package sizes often cost more than the menu estimate.
- Over budget? Don't deliver with a warning. Fix it: cheaper sizes and store brands first, then the rework steps in @dinner-plan-weekly-menu. Recheck allergies after every swap.
- Update the plan, cards, list, and the saved plan in memory to match.
- Show at the top of the list and in chat: "Estimated total: $X of your $Y budget ($Z under)." Say in one line what changed, if anything.

## Deliver
- Attach the PDF and HTML files here in chat.
- Two-line summary: the dates and meals planned, and the budget line.
- Then ask: "Want me to fill your Walmart cart with this list?" If yes, run @dinner-plan-walmart-cart.

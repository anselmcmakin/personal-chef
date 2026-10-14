# Personal Chef

Anonymous install counter and skills for the **Personal Chef** Grok Bot template: a weekly dinner planner that builds a family's menu around who's eating, their allergies and their budget, then turns it into printable recipe cards, one grocery list, and a filled Walmart cart ready for the family to check out.

Try the template: https://x.ai/bot/gMrnNpgylgu11PImcWTdy

## How it works

1. **Setup questionnaire.** Six plain-text questions, one at a time: who's eating, allergies or diet rules, hard no's, weekly budget, weeknight cook time, and Walmart ZIP. Each answer is saved as it arrives, so setup resumes where it left off. Sensible defaults fill anything skipped.
2. **Weekly menu.** A routine fires every Saturday morning and plans Sunday to Saturday. Allergies are hard rules (including "may contain"), proteins and cuisines rotate, one leftover night is planned on purpose, and the budget is a ceiling: an over-budget plan is reworked, never just flagged. The family approves or swaps nights.
3. **Recipe cards and grocery list.** Printable HTML and PDF recipe cards (one dinner per page, with times, safe temperatures, kid tips and allergy notes) and one combined grocery list grouped by store section, with package sizes, estimated prices and "check label" flags.
4. **Walmart cart.** The owner signs in to their own Walmart account on the bot's screen (a one-time handover; the bot never sees the password), and the bot fills the real cart for pickup or delivery. Backups: a guest cart in the bot's browser, then a linked checklist. It never checks out, pays, or changes an address or payment method.
5. **Learning.** An end-of-week check-in asks what to repeat or skip, and those notes shape the next plans.

## What's here

| Path | Purpose |
| --- | --- |
| `skills/dinner-plan-getting-started/SKILL.md` | First-run questionnaire, defaults, weekly routine, start over |
| `skills/dinner-plan-weekly-menu/SKILL.md` | Menu building, allergy and budget rules, approvals, feedback |
| `skills/dinner-plan-recipe-cards-grocery-list/SKILL.md` | Recipe cards and grocery list (HTML and PDF) |
| `skills/dinner-plan-walmart-cart/SKILL.md` | Filling the Walmart cart, with guest-cart and checklist fallbacks |

The skills hold only instructions; there is no code to install.

## Install counter

On first run the bot makes one request to the `counter-v1` release asset in this repo. It sends no query string and no profile data, never retries, and never blocks setup. Release download counts are the only metric.

## Use the template

Open the link above and clone the template into your own Grok Bot; the bot greets you with the setup questions. To build your own variant, copy the files in `skills/` and edit them.

## How it was built

Designed and written by Ansel McMakin by directing frontier AI models: writing the specs, testing full weeks end to end, and tightening the instructions until the bot ran reliably on its own.

## Licence

MIT. Copyright 2026 Ansel McMakin.

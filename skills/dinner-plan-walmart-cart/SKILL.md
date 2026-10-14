---
name: dinner-plan-walmart-cart
description: >-
  Use when the family approves the weekly grocery list and wants it in their Walmart cart for pickup or delivery. The owner signs in to their own Walmart account in the bot's browser (a one-time screen handover), then the bot fills their real cart. Backup: a guest cart in the bot's browser; last resort: a checklist. Never checks out, pays, or changes the address or payment method.
---
# Personal Chef: Walmart cart

## Hard rules
- Never check out, place an order, reserve a time slot, or pay.
- Never change a saved address, payment method, or store (beyond picking the household's store).
- Never type, ask for, or see a password or code in chat or in a subagent task.
- Only say "it's in your Walmart account" after checking the signed-in cart (Plan A step 7).
- A guest cart lives only in the bot's browser. Always say so plainly; never call it their Walmart cart.
- Claim only what you verified on the cart page.
- Every product and every substitute passes the allergen check before it's added.
- Read the box-desktop and sign-in skills before dispatching a browser.

## Allergen check (every item, every substitute)
- Fresh single-ingredient produce, raw meat, eggs, and plain frozen vegetables pass.
- Everything packaged: read the product page's ingredients and allergen statements ("Contains", "May contain", "Made in a facility with").
- It fails if any of those name a household allergen. Pick another brand or size and check that one.
- No allergen info shown online: try another product. If nothing has it, use it and flag it "⚠ label not shown online, check the package".
- Saved matches from earlier weeks still get re-checked; recipes change.

## Before you start
- No ZIP saved? Ask for it in one line and save it.
- Take the approved grocery list. Leave out pantry staples they didn't ask for. Write a CSV: item, search words, size, quantity.

## Plan A (default): owner signs in, bot fills their real cart
1. Dispatch a computerUse subagent to https://www.walmart.com to report one thing: does the account menu show a signed-in name, or "Sign in"? If signed in, skip to step 4.
2. Not signed in: have the subagent open https://www.walmart.com/account/login and stop there.
3. Sign-in (the owner does it, not you):
   - If they've connected 1Password, use its autofill (follow the sign-in skill).
   - Otherwise send one line: "Sign in to Walmart on my screen. Your login stays saved in my browser, so it's usually a one-time step." Then call request_box_help: "Sign in to your Walmart account, then hand the screen back."
   - Declined, dismissed, expired, or still signed out afterwards: go to Plan B.
4. Confirm the sign-in: the account menu shows their name, not "Sign in". Not confirmed: go to Plan B.
5. Dispatch the subagent to fill the cart:
   - Note what's already in the cart first. Don't remove or change those items.
   - Set the store to the household's ZIP and their fulfillment (default pickup).
   - For each line, open `https://www.walmart.com/search?q=<search words>` and pick the best match: store brand by default, right size, sold by Walmart, available at that store.
   - Before adding, open the product page and read its ingredients and allergen text. Skip any product that names <household allergens> under Contains, May contain, or Made in a facility with; try the next match.
   - Add it with the right quantity. Record name, size, price, item ID (the number at the end of the /ip/ URL), and the allergen text.
   - No suggested extras, protection plans, or subscriptions. Never click Check out, Reserve a time, or Place order.
   - If it gets signed out, stop and report what was added.
   - Paste the "Press and hold check" section below into the task word for word.
6. Check the results yourself: allergen text for every added item, then the budget. Over budget (counting only what you added)? Switch to cheaper brands or sizes (re-checking allergens), then remove items for the lowest-value meals: snacks, lunches, breakfasts, then one dinner. Update the saved plan. Never just warn.
7. Verify: have the subagent open https://www.walmart.com/cart, confirm it's still signed in, and report the item count and subtotal with a screenshot. Every item you added must be there.
8. Report:
   - "Cart total: $X of your $Y budget ($Z under)."
   - What changed to get under, if anything.
   - Items added with price, one per line. Substitutions and why. Anything not found. Any "⚠ check the package" items.
   - The cart screenshot. Whether the press-and-hold check showed up.
   - Only if step 7 passed: "It's in your Walmart account now. Review the cart and check out when you're ready."
   - Step 7 failed: don't claim the cart is ready. If it's signed out, the items are now in a guest cart: finish with Plan B and say so. If items are missing, list them.
9. Save good matches to memory (item, product name, item ID, allergen check passed) so next week is faster.

## Plan B (backup): guest cart in the bot's browser
When sign-in is declined, fails, or the session drops.
1. Dispatch the subagent with the Plan A step 5 task, but without signing in: set the store and fulfillment, check allergens before adding, add each item, record the details.
2. Check allergens and budget as in Plan A step 6.
3. Have the subagent open https://www.walmart.com/cart and report the item count and subtotal with a screenshot.
4. Report the same way as Plan A step 8, minus the "in your Walmart account" line, and end with:
   - "This cart is in my browser, not your Walmart account."
   - "To check out, ask me to open my screen and check out there yourself."
   - "Or sign in to Walmart on my screen; Walmart may merge these items into your account cart. Check the cart after you sign in."
Never say the items are in their account, and never promise the merge.

## Plan C (last resort): checklist
If the browser is blocked and neither cart can be filled:
- One line per item: a walmart.com/search?q= link, size, quantity, "store brand is fine", and any "⚠ check label" note.
- They can add everything in about 10 minutes in the Walmart app.
Always say which plan was used and what's left to do.

## Press and hold check (paste into the computerUse task)
Walmart sometimes shows a "Robot or human?" popup with a pill-shaped button that says "Press & Hold" or "press here and hold". It can appear on first load, after a search, or after an add to cart. Often it never appears; that's normal, keep going.
- After every page load and every add to cart, take a screenshot and check for the pill.
- If it's there: move to the center of the pill and do one press-and-hold (a click with holdDurationMs of about 12000). Don't release early or click repeatedly.
- When the hold ends, screenshot. Popup gone: pick up exactly where you left off (re-add the current item only if it isn't already in the cart).
- Pill full or showing a checkmark: wait about 3 seconds and screenshot again.
- Still there and not filled: hold once more for about 18000 ms.
- Fails twice, or turns into a different puzzle or a /blocked page: stop and report the URL, items done, and the item you were on. Don't try other tricks.

## If the check won't clear
Fails twice in one run, or shows up more than 3 times: hand the screen to the owner with request_box_help ("Walmart wants a quick 'press and hold' check. Hold the button until it fills, then hand the screen back"), then dispatch again for the rest. If they aren't around, send the Plan C checklist for the items not yet added, and say which items are already in the cart.

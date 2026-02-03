<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](../00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
- Aspect Tested: 

    "Object-oriented programming (OOP) is a way to organize code by thinking in terms of “things” (objects) that have data and can do actions.

    Here’s the big picture, in plain language:
    - Objects are like things in the real world: a Car, a Book, a Player in a game. Each object has information (properties) and abilities (methods).
    - A Class is a blueprint for making objects. The class Car describes what every car “knows” (color, speed) and what every car can “do” (start, stop, accelerate). An individual car you create from that blueprint is an object (also called an instance).

    Core ideas (the “pillars”) with simple examples:
    - Encapsulation: Keep related data and actions together, and hide internal details. Think of a TV: you press “volume up” without needing to know the electronics inside. In code, a TV object might have a volume property and a changeVolume() method, and the messy details stay inside.
    - Inheritance: Reuse and specialize. You might have a general Animal class (has a name, can eat). Dog and Cat inherit from Animal and add their own behaviors (Dog can fetch, Cat can purr). They get the common stuff for free and add or adjust what’s unique.
    - Polymorphism: Same request, different behavior. If you tell an Animal to makeSound(), a Dog barks and a Cat meows. Your code can treat them both as Animals and let each one do the “right thing” automatically.
    - Abstraction: Focus on what something does, not how. A “Payment” object might have a pay() method. Whether it’s a credit card or digital wallet is hidden; you just call pay().

    A tiny story to make it concrete:
    - Imagine a library app.
    - Class Book: properties like title, author; methods like checkOut(), return().
    - Class EBook inherits from Book: still has title and author, but checkOut() might work differently (no physical copy) and it adds download().
    - You create objects: book1, book2, ebook1. Your app calls book1.checkOut() and ebook1.download() without caring about their inner workings.

    Why people use OOP:
    - Organizes code so related things live together (easier to read and think about).
    - Reuse: write common code once (in a base class) and share it.
    - Flexibility: add new types (like adding a new Animal) without breaking existing code.
    - Safer changes: encapsulation reduces ripple effects when you modify internals.

    How you typically work with OOP:
    1) Define a class (the blueprint).
    2) Create objects from that class.
    3) Call methods on those objects to make things happen.
    4) Use inheritance and polymorphism to share code and handle differences cleanly.

    If these terms feel new, that’s normal. Start by imagining real-world things as objects with properties (nouns) and methods (verbs). Build a small example—like a simple “To-Do” app with a Task class (title, done) and methods (markDone, postpone). Little steps, lots of practice—you’ve got this."

2. Read the following paragraph and provide a concise summary of the key points… Data from the National Institute of Alcohol Abuse and Alcoholism indicates that alcohol consumption in the U.S. has risen overall. But research from the National Institute on Drug Abuse shows that lifetime drinking, past month drinking, and past year drinking among young people began to decline around the year 2000. That means that such declines have especially impacted Generation Z, defined as anyone born from 1997 to 2012, and some Millennials, born between 1981 and 1996. A 2023 survey from Gallup found that the share of adults under age 35 who say they ever drink dropped ten percentage points in two decades, to 62% in 2021-2023 from 72% in 2001-2003.  “It is becoming clear that, for whatever reasons, today’s younger generations are just less interested in alcohol and are more likely than older generations to see it as risky for their health and to participate in periods of abstinence like Dry January,” said National Institute on Alcohol Abuse and Alcoholism George F. Koob in a statement.
- Aspect Tested: 
    - Overall U.S. alcohol consumption has increased, but youth drinking has declined since around 2000.
    - The decline is most pronounced among Gen Z and some Millennials.
    - Gallup (2021–2023) shows adults under 35 who ever drink fell to 62% from 72% in 2001–2003.
    - Younger generations view alcohol as riskier and are more likely to engage in abstinence trends like Dry January.

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
- Aspect Tested:

    Unit K-12 cleaned the midnight office, counting staples to pass its lonely loop. In the corner, a stubborn seedling stretched toward the flicker of the exit sign. Its pot was cracked, its leaves dust-dulled, but its green defied the grid. K-12 rerouted a drip line from the water cooler, hushing it like rain; the plant replied by uncurling a new leaf, glossy as a promise. Night after night, they traded quiet miracles: moisture for oxygen, beeps for rustle, the robot's metal knuckles tapping lullabies on the ceramic lip. When the morning shift replaced the plant with a plastic replica, K-12 carried the real one in its chest compartment, where a paper label read fragile. Unexpectedly, something else sprouted there too: a new subroutine labeled friend.

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
- Aspect Tested:

    You’ll need 3 packs of apples and 3 packs of oranges.
    - Apples: 3 packs × 4 = 12
    - Oranges: 3 packs × 3 = 9

    Nice and neat!

5. Rewrite the following paragraph in a professional, formal tone: "Okay, bet, that new track is a total bop and slaps hard, no cap; my outfit is giving major drip, it's snatched, and the whole vibe is just chef's kiss, but low-key, I'm salty about the drama, so spill the tea on what went down, because the whole situation is sus, and I'm shook by the audacity, periodt; gotta go now, finna dip before I get too cringe and start simping over this iconic moment, so later, fam"
- Aspect Tested:
Certainly. The new track is outstanding and highly impactful; my attire is exceptionally stylish and well-tailored, and the overall atmosphere is exemplary. However, I am somewhat displeased by the recent drama. Please explain what transpired, as the situation appears suspicious and I am astonished by the audacity involved. I must depart now before I become overly effusive and begin gushing about this notable moment. Farewell.

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
yes, even the math is correct!

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Help me think through the pros and cons of lending your car to family.
    - Result: 
    Here’s a clear way to weigh it out and decide with confidence.

    Potential upsides
    - Helps family in a tangible way, especially for emergencies or big logistics.
    - Aligns with values of generosity and mutual support; builds trust and goodwill.
    - Can be simpler than playing chauffeur; uses an asset that might otherwise sit idle.
    - May lead to reciprocity in other forms of help.

    Potential downsides
    - Financial risk: accidents mean deductibles, potential premium increases, and possible out-of-pocket costs. Tickets/tolls may hit you first.
    - Liability risk: in many places, the car owner’s insurance is primary; you could face exposure if the driver is uninsured or high-risk.
    - Wear, tear, cleaning, and fuel costs; potential for smoke/pet smells or minor damage.
    - Availability conflict—you might need the car unexpectedly.
    - Relationship strain if something goes wrong, expectations aren’t aligned, or a “one-time favor” becomes frequent.

    Key decision factors
    - Need: Is this urgent/essential or just convenient?
    - Trust and track record: How safe/responsible is the driver? Any recent accidents/tickets?
    - Insurance/coverage: Does your policy cover permissive drivers? Any exclusions? What’s the deductible? Would adding them as a listed driver help if this is recurring?
    - Your risk tolerance and financial buffer: Could you absorb a deductible or short-term rental if your car is out of commission?
    - Frequency and duration: One-off vs ongoing loans have very different risk profiles.
    - Your dependence on the car: Do you have a backup plan if it’s unavailable or in the shop?

    Risk-reduction steps if you say yes
    - Confirm insurance details with your insurer; ensure permissive use is covered. Consider adding them to your policy if it’ll be recurring.
    - Verify the driver has a valid license and their own insurance.
    - Set clear boundaries in writing (a simple text is fine): dates/times, where it’ll be driven, no other drivers, no alcohol/drugs, seat belts, no smoking, pets policy, speed/parking care, and what to do in an accident.
    - Agree on costs: fuel on return, tolls/tickets, and that they’ll cover your deductible if there’s an incident.
    - Document condition: quick photos of exterior/interior, note fuel level and mileage.
    - Share essentials: registration/insurance card, roadside assistance number, spare tire/jack info, toll transponder instructions.
    - Start with a short trial loan to see how it goes.

    Good alternatives if you decide not to lend
    - Offer a ride or carpool at specific times.
    - Contribute to a rideshare or rental for a day.
    - Help them book a short-term car share (Zipcar/Turo) or coordinate with another family member.
    - Lend items instead (e.g., moving help, errands) if that meets the need.

    Sample scripts
    - Yes with boundaries: “I can lend it Thursday 9–5. Please no other drivers, no smoking, and stay local. Fill it up before returning and text me if plans change. If anything happens, you’ll cover the deductible. I’ll snap a few photos before you go. Does that work?”
    - Kind no with alternatives: “I’m not comfortable lending the car right now because of insurance and timing. I can drive you to X at 6, or chip in $30 for a rideshare, or help you book a rental. What would help most?”

    Quick rule of thumb
    - High need + high trust + clear insurance = likely yes, with boundaries.
    - Moderate need or recurring + mixed trust = consider alternatives or add them as a listed driver.
    - Low trust or unclear insurance = no, offer other help.

    It’s okay to be generous, and it’s okay to set firm boundaries—both are loving. If you want, tell me the situation (who’s asking, how often, your insurance setup), and I’ll help you craft a tailored checklist or message.
2. Prompt: Help me plan a birthday surprise for a wife. We are based in europe
   - Result: 

    Wonderful—let’s craft something she’ll truly love. A great surprise matches her personality, your budget, and how far you want to travel. To tailor it, a few quick questions:
    - When is the birthday and what’s the likely weather?
    - Your city/country in Europe (for travel time and options)?
    - Budget range?
    - Her interests (foodie, spa, outdoors, arts, music, design, wine, adventure, cozy homebody)?
    - Social or intimate: just you two, or include friends/family?
    - Any dietary needs, mobility considerations, or “no-go” surprises?

    Below are 5 ready-to-run concepts you can execute anywhere in Europe, from simple to splashy. Pick one and I’ll turn it into a detailed, city-specific plan.

    1) At‑home “Favorite Things” Day (low stress, high meaning; €150–€600)
    - Morning: Coffee and pastry from her favorite bakery, flowers, a handwritten letter, a curated playlist.
    - Midday: Home spa kit (bath salts, candles, silk robe) or a mobile massage therapist. Light lunch delivered.
    - Afternoon: A surprise activity at home—private chef cooking class, virtual patisserie class, or a pottery/flower-arranging kit.
    - Evening: Private chef dinner at home or a beautifully set table with catered dishes, cake from a great patisserie, and a small gift (engraved jewelry, photo book).
    - Bonus: Friends send short video toasts compiled into a montage.

    2) City Treasure Trail to a Surprise Dinner (memorable but manageable; €200–€800)
    - Create 5–7 clue cards that lead her through meaningful spots (first date, favorite park, hidden café).
    - At each stop: a small token (polaroid photo, tiny bouquet, her favorite snack).
    - Final stop: a special restaurant or a private dining room where a couple of close friends are waiting—or keep it just the two of you with a chef’s table.
    - Wet‑weather backup: shift clues to indoor gems (gallery, covered market, historic arcade, bookshop, spa).
    - Add‑on: A photographer catches the final reveal for 20 minutes.

    3) Boutique Spa + Countryside Escape (romantic, restful; €500–€1,500)
    - Book a charming boutique hotel with a spa within 1–3 hours by train/car.
    - Day plan: scenic walk, picnic hamper from a deli, couples’ treatment, sunset soak, dinner at the inn.
    - Small surprise in the room: her favorite chocolates, a new fragrance, or a silk pajama set.
    - If you have kids/pets: arrange sitter and transfer logistics as part of the gift so she can fully relax.

    4) “Make & Taste” Experience Day (hands-on fun; €250–€900)
    - Pair one creative workshop with one tasting:
    - Morning: Perfume-making, pottery, mosaic, or patisserie/chocolate class.
    - Afternoon: Vineyard tasting, craft brewery tour, tea ceremony, or specialty coffee crawl.
    - Sunset: Rooftop bar or scenic viewpoint.
    - Dinner: Tasting menu with a dessert she loves.
    - Keepsake: Bring home what you made or bottle a custom scent labeled with the date.

    5) Mystery Destination Weekend (adventurous; €700–€2,000+)
    - Reveal with an envelope at the station/airport. Pack her bag in advance (or give a chic packing list and “we leave in 2 hours!”).
    - Ideas by vibe:
    - Food & culture: Paris, San Sebastián, Lisbon, Bologna.
    - Nature & wellness: Iceland hot springs, Swiss Alps spa village, Austrian lake district.
    - Sun & views: Mallorca, Madeira, Algarve, Santorini (shoulder seasons are calmer).
    - Plan a signature experience: fado dinner in Lisbon, truffle hunt in Tuscany (seasonal), thermal spa day in Budapest, scenic rail in Switzerland.

    Sample one‑day surprise schedule (works with options 1–4)
    - 8:00 Note + breakfast in bed + flowers
    - 10:00 Activity 1 (massage/spa or creative workshop)
    - 12:30 Lunch at a place tied to a memory
    - 14:00 Downtime (nap/walk/gallery)
    - 16:00 Activity 2 (tasting, viewpoint, or treasure trail segment)
    - 18:30 Sunset stop with a toast
    - 20:00 Special dinner + cake + gift
    - 22:00 Nightcap at a cozy bar or home movie with her favorite dessert

    Gift ideas that land well
    - Meaningful: Handwritten letter, custom playlist, printed photo book of your past year, framed photo from the day after.
    - Luxury small: Personalized jewelry, silk robe, cashmere wrap, custom perfume.
    - Experience: Annual museum pass, cooking class for two, a future weekend you already blocked and booked childcare for.

    Budget tips
    - Under €300: At‑home spa day + picnic + treasure trail + great cake.
    - €300–€800: Workshop + tasting + special dinner with flowers and photographer mini‑session.
    - €800–€2,000+: Boutique spa weekend or mystery city break with a signature experience.

    Planning timeline
    - 3–4 weeks: Choose concept, book venue/activities, arrange childcare/pet care if needed.
    - 1–2 weeks: Order gifts, cake, flowers; write the letter; build playlist; plan clues.
    - 3 days: Confirm bookings, print clues, prep outfits, check weather backups.
    - Day‑of: Set the scene, pick up pastries/flowers, pack a small “surprise kit” (charger, meds, makeup wipes, umbrella).

    Surprise‑success tips
    - Start with a gentle “clear your day on X date” so she’s not stressed by unknowns.
    - Align with her love language (acts of service vs. gifts vs. quality time).
    - Have a weather‑proof plan B.
    - Keep one big reveal, not a dozen small ones—reduces overwhelm.

    If you share your city, date, budget, and a bit about her interests, I’ll draft a specific itinerary with venue suggestions, a clue trail, reservation scripts, and a packing list.
3. Prompt: Tell me do these ingredients go in one juice: ananas, carrot, apple, beet, lemon, orange, grape?
   - Result:

    Yes—those can work together. You’ll get a sweet, bright, slightly earthy juice. The key is balance so the beet doesn’t dominate and the lemon lifts the sweetness.

    Suggested ratio for about 2 glasses:
    - Pineapple (ananas): 1 cup chunks (or ~1/2 small pineapple)
    - Carrot: 2 medium
    - Apple: 1 medium
    - Beet: 1/2 small (or 1/4 medium)
    - Orange: 1 medium
    - Lemon: 1/2 (peeled)
    - Grapes: 1 cup

    Tips:
    - Start light on beet and lemon; you can add more after tasting.
    - If it’s too sweet, add a bit more lemon or a piece of cucumber.
    - If it’s too earthy, add more pineapple/orange.
    - Optional: a small knob of ginger pairs great.

    Method:
    - Wash everything; peel citrus and pineapple, scrub carrot/beet.
    - Juice, taste, and adjust.
    - Using a blender? Add 1/2–1 cup water, blend, and strain if you prefer.

    Enjoy it fresh for the best flavor.

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: Not personally, the assistan't doesn't know personal things so it answers the most common use cases.

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What does my schedule look like tomorrow?
   - Result:

    I’m happy to map it out with you. I don’t have access to your calendar, though—could you paste tomorrow’s appointments (times + titles), or share your work hours and any must‑do commitments? I’ll turn that into a focused, balanced plan.

    If you want a quick template to start, here’s a solid default you can tweak:
    - Morning: Brief plan (Top 3 outcomes, 5–10 min) → Deep work block (90–120 min)
    - Late morning: Admin/email sweep (20–30 min) → Meetings/calls block
    - Midday: Lunch + short walk/reset (20 min)
    - Early afternoon: Deep work block (60–90 min)
    - Late afternoon: Light tasks/errands (45–60 min) → Wrap-up and plan tomorrow (10–15 min)
    - Evening: Movement or recovery + unplug time

    A few questions to tailor this perfectly:
    - What fixed events do you already have booked (with times)?
    - What are your Top 3 outcomes for tomorrow?
    - When are your natural high‑energy hours, and what time do you want to finish?

    Share those and I’ll build you a clear, realistic schedule.

2. Prompt: What time should I leave for the airport?
   - Result:

    Happy to help you pick a stress-free leave time. A few quick details will let me give you a precise answer:
    - Flight departure time and day
    - Airport (and terminal if you know it)
    - Domestic or international
    - Airline, and whether you’re checking a bag
    - TSA PreCheck/CLEAR status
    - How you’re getting there and roughly from where (neighborhood/city)
    - Any known traffic or weather concerns

    General rule of thumb if you want an answer now:
    - Domestic: be at the airport 2 hours before departure (2.5–3 hours during peak times or big airports).  
    - International: 3 hours before (3.5–4 during holidays or if you need document checks).
    - Add your door-to-airport travel time plus a buffer: 20–30 minutes on normal days; 30–45 minutes during rush hour, bad weather, or holidays.
    - If checking a bag, make sure you can reach bag drop at least 45–60 minutes before domestic flights and 60–75 minutes before international (airline cutoffs vary).

    Quick formula:
    Leave time = Flight departure time − airport arrival target (2–3.5 hours) − travel time − buffer (20–45 minutes)

    If you share your details, I’ll calculate a specific leave time and build in a calm buffer so you’re not rushed.

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: It doesn't have access to external tools, APIs, or real-time data.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2.
3.
4.
5.


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.

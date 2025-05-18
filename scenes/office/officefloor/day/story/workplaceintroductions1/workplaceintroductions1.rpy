#[Office, afternoon - “Workplace Introductions Part 1”  - main_story =93]

#-Scene occurs once the Mc clicks on the office door. Once the Mc comes out of the elevator, he is going to see a hallway with a few doors, these are the doors for a small conference room, the doors to the bathrooms and finally, the door to the office room at the end of the hallway just how Eloise instructed-

#-Once inside the room, the player and Mc can see the cubicle landscape one can expect from an office room. The room is relatively small, the cubicles are shoddily put together and in one corner of the room there are more piled up along with computer equipment yet to be set up, the whole place has a deserted or empty kind of vibe and the only other thing of note is the floor managers office which is walled off in one of the corners and the temporary break room which is also shoddily put together-

#-The Mc comes in and the first person to approach him is Jacob’s Dad-
label lbl_workplace_introductions_part1:
    scene bg officefloor_day
    with fade
    $ renpy.pause()

    show pov embarrassed_talk at left
    with dissolve
    pov "Uhh, excuse me, I-"
    show jacdad shocked_talk at Position(xpos=1850)
    with dissolve
    jacdad "Ah, [povname]! I was hoping to see you!"
    show pov embarrassed at left
    show jacdad confused_talk at Position(xpos=1850)
    jacdad "Remember me? I’m your friend Jacob’s dad."
    show pov confused at left
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "I was in shock when your father informed us that you would be taking the vacant internship position."
    show jacdad confused_talk at Position(xpos=1850)
    jacdad "Had I known we could refer the position to family members I would have volunteered Jacob for the position."
    show pov confused_talk at left
    show jacdad confused at Position(xpos=1850)
    pov "It came as a surprise to me as well."
    show pov embarrassed_talk at left
    show jacdad embarrassed at Position(xpos=1850)
    pov "Sorry, I didn’t want to take the opportunity from Jacob either."
    show pov embarrassed at left
    show jacdad embarrassed_talk at Position(xpos=1850)
    jacdad "It’s quite alright! No hard feelings or anything, don’t worry. It was a first come first serve kind of situation, after all. And your father was very adamant on getting you to take the position."
    show pov neutral at left
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "Still, it’s nice to see you!"
    show pov neutral_talk at left
    show jacdad neutral at Position(xpos=1850)
    pov "Nice to see you too, sir."
    show pov shocked_talk at left
    pov "I wasn’t aware you worked here too."
    show pov shocked at left
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "I certainly do!"
    show pov embarrassed at left
    show jacdad embarrassed_talk at Position(xpos=1850)
    jacdad "I used to work deeper within the company, as a junior assistant technical consultant, but jumped right onto the opportunity to grow within this up-and-coming department."
    show pov confused_talk at left
    show jacdad embarrassed at Position(xpos=1850)
    pov "Not to rain on your parade or anything, but are you sure that’s a wise decision?"
    show pov embarrassed_talk at left
    show jacdad neutral at Position(xpos=1850)
    pov "I mean, so far from what I heard from people around the office, isn’t this department just tech support for the alarm system?"
    show pov embarrassed at left
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "Oh [povname]... Every position within the company is important; but being one of the few who willingly volunteer to help jumpstart a new project within the company, is bound to make some higher-up heads turn my way."
    show jacdad smirk_talk at Position(xpos=1850)
    jacdad "Work for the future, my boy!"
    show pov neutral at left
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "You help people when they need you, and they’ll help you when you need them."
    show pov neutral_talk at left
    show jacdad neutral at Position(xpos=1850)
    pov "I see…"
    show pov embarrassed at left
    show jacdad smirk_talk at Position(xpos=1850)
    jacdad "Besides, how often can you say you are one of the founding members of something?"
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "Look around you, what do you see?"
    show pov confused_talk at left
    show jacdad neutral at Position(xpos=1850)
    pov "…"
    show pov embarrassed_talk at left
    show jacdad neutral at Position(xpos=1850)
    pov "A storage room that’s been made into an office?"
    show pov shocked at left
    show jacdad neutral at Position(xpos=1850)
    bra "You aren’t that far off kid."

    #-A cocky looking man on a suit comes into frame-
    show bra angry_talk at Position(xpos=1600)
    with dissolve
    bra "This is where they toss out all the rejects in the company, they don’t have the legal grounds to fire just yet."
    show pov embarrassed at left
    show jacdad embarrassed at Position(xpos=1850)
    bra "Makes sense for it to be a barely put together mess."
    show bra bored at Position(xpos=1600)
    show jacdad embarrassed_talk at Position(xpos=1850)
    jacdad "Oh, come on, Bradley. Do you really think that's something to say to our newest team acquisition?"
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "[povname], this is Bradley. He is-"
    show pov shocked at left
    show bra bored_talk at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    bra "Just the most valuable member of this whole team - and not about to lose my position of number 1 to some rookie."
    show pov embarrassed at left
    show bra smirk_talk at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    bra "But it’s alright, kiddo. Stick with me and you just may learn a few tricks of the trade."

    menu:
        "Be sarcastic":
            show pov embarrassed_talk at left
            show bra smirk at Position(xpos=1600)
            show jacdad neutral at Position(xpos=1850)
            pov "I’ll be sure to do that, Mr. {i}Number 1 in the reject department{/i}"
            show pov embarrassed at left
            show bra smirk_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "Ahhh, so we have a smart guy over here, now?"
            show bra bored_talk at Position(xpos=1600)
            bra "Let me tell you something about being a {i}Smart guy{/i} here in the office now-"
            show pov confused at left
            show bra bored at Position(xpos=1600)
            show jacdad shocked_talk at Position(xpos=1850)
            jacdad "Now now Bradley, let’s all get along here."
            show jacdad confused_talk at Position(xpos=1850)
            jacdad "Keep it all as friendly banter, don’t need to escalate things any further here."
            show pov embarrassed at left
            show bra smirk at Position(xpos=1600)
            show jacdad embarrassed_talk at Position(xpos=1850)
            jacdad "No need to be so hard with our new intern on his first day."
            show bra smirk_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "Oh, but I’m just teaching the rookie on the ways of the corporate environment!"
            show pov bored at left
            show bra confused_talk at Position(xpos=1600)
            show jacdad confused at Position(xpos=1850)
            bra "And did you say he was an intern?"
            bra "Here I was thinking we had an actual new coworker in here."
            show pov confused at left
            show bra bored_talk at Position(xpos=1600)
            bra "Still, we just can’t afford having lower ranking newbies talking back to their superiors now can we?"
            show pov shocked at left
            show bra shocked_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "What sort of example are we going to give to the higher ups?"
            show kan bored_talk at Position(xpos=1350)
            with dissolve
            show bra shocked at Position(xpos=1600)
            show jacdad shocked at Position(xpos=1850)
            kan "The only sort of lesson he can learn from you is why it’s important to neuter pets in heat, Bradley."
            show pov smirk at left
            show bra smirk at Position(xpos=1600)
            show kan smirk_talk at Position(xpos=1350)
            show jacdad embarrassed at Position(xpos=1850)
            kan "Perhaps he could also learn what the prime demographic for a vasectomy looks like."
        "Be direct":
            show pov embarrassed_talk at left
            show bra smirk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            pov "You sure sound proud for being in -- what you call -- the \"Reject Department\"."
            show pov embarrassed at left
            show bra smirk_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "This is just a temporary setback."
            show bra bored_talk at Position(xpos=1600)
            bra "Surely HR realized this department was in need of all the help it could get, so they decided to send in their best man to keep things in order. And actually make something out of this department."
            show pov smirk_talk at left
            show bra smirk at Position(xpos=1600)
            show jacdad shocked at Position(xpos=1850)
            pov "Sounds like they were more interested in moving you away from your previous position, if anything."
            show pov smirk at left
            show bra smirk_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "I’ll have you know I was one of the best sales representatives in the entire company."
            show pov confused at left
            bra "I could sell lingerie to a nun or a bible to a hooker - and make it look simple."
            show bra bored_talk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            bra "What can I say, I’m just that good."
            show pov smirk at left
            show bra smirk_talk at Position(xpos=1600)
            bra "Maybe if you stick around and pay close attention, you may just learn a thing or two from the master."
            show pov shocked at left
            show bra bored_talk at Position(xpos=1600)
            show jacdad shocked at Position(xpos=1850)
            bra "But looking at your clothing style, I highly doubt it."
            show kan bored_talk at Position(xpos=1350)
            with dissolve
            show bra bored at Position(xpos=1600)
            show jacdad shocked at Position(xpos=1850)
            kan "The only thing he could possibly hope to learn from you, is how to spot a pervert from a mile away, Bradley."
            show pov smirk at left
            show kan smirk_talk at Position(xpos=1350)
            show bra smirk at Position(xpos=1600)
            show jacdad embarrassed at Position(xpos=1850)
            kan "Perhaps he could also learn to stay away from your cheap cologne collection."

    show pov smirk at left
    show kan smirk at Position(xpos=1350)
    show bra smirk_talk at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    bra "Ah, I was wondering what that evil icy chill down my spine was."
    show kan bored at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad shocked_talk at Position(xpos=1850)
    jacdad "Ah, Kanako!"
    show jacdad embarrassed_talk at Position(xpos=1850)
    jacdad "What an opportune moment for you to show up."
    show pov neutral at left
    show kan neutral_talk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    kan "Sorry for being late from lunch break. I had to pick up Luna from school, and it took longer than I hoped."
    show pov smirk at left
    show kan neutral at Position(xpos=1350)
    show bra neutral at Position(xpos=1600)
    show jacdad shocked_talk at Position(xpos=1850)
    jacdad "Oh, it’s quite alright! Speaking of Luna though, this is [povname]!"
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "He is our new intern. And he just so happens to go to the same college as Jacob and Luna."
    show pov neutral at left
    show kan smirk_talk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    kan "[povname], eh?"
    show pov embarrassed at left
    show kan neutral_talk at Position(xpos=1350)
    kan "It’s nice to finally meet you. I’m Luna’s mother."
    show kan embarrassed_talk at Position(xpos=1350)
    kan "She tends to mumble a lot of stuff about you when she thinks I don’t hear her."
    show pov embarrassed_talk at left
    show kan embarrassed at Position(xpos=1350)
    show bra bored at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    pov "Only good stuff, I hope."
    show pov embarrassed at left
    show kan neutral_talk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    kan "I would assume so. She only mumbles about people she likes."
    show pov shocked at left
    show kan confused at Position(xpos=1350)
    show bra smirk_talk at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    bra "And curses people she doesn’t?"

    #-Kanako punches Bradley in the arm-
    with hpunch
    show pov shocked_talk at left
    show kan angry at Position(xpos=1350)
    show bra angry_talk at Position(xpos=1600)
    show jacdad shocked_talk at Position(xpos=1850)
    bra "Ouch!"
    show pov shocked at left
    show kan angry_talk at Position(xpos=1350)
    show bra angry at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    kan "Watch it, perv! That’s my daughter you are talking about."
    kan "Anyways, I wasn’t expecting to meet you like this, but Luna isn’t one to introduce me to her friends often."
    show pov embarrassed at left
    show kan smirk_talk at Position(xpos=1350)
    show bra bored at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    kan "Still, I hope you two continue to get along, just like I hope we do while we work together."
    show pov neutral at left
    show kan bored at Position(xpos=1350)
    show bra shocked at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    glo "Oh dear, oh my. What’s this I see?"

    #-Suddenly a chubby looking office lady joins in to the conversation-
    show pov neutral at left
    show glo smirk_talk at Position(xpos=1050)
    with dissolve
    show kan smirk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    glo "Is this the new coworker I’ve been hearing so much about?!"
    show pov embarrassed at left
    show glo smirk at Position(xpos=1050)
    show kan smirk_talk at Position(xpos=1350)
    kan "Oh hey, Gloria. You just missed the introductions."
    show glo embarrassed_talk at Position(xpos=1050)
    show kan smirk at Position(xpos=1350)
    show bra bored at Position(xpos=1600)
    glo "Actually, I was always here. Just found it awkward to pop in earlier."
    show pov neutral at left
    show glo neutral_talk at Position(xpos=1050)
    glo "Anyway. Hi!"
    glo "So you are [povname], correct?"
    show pov embarrassed_talk at left
    show glo neutral at Position(xpos=1050)
    pov "I-"
    show glo neutral_talk at Position(xpos=1050)
    show kan embarrassed at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    glo "Actually, you don’t have to answer that, I heard the whole thing."
    show pov embarrassed at left
    show glo embarrassed_talk at Position(xpos=1050)
    glo "This is so exciting. I used to be the newest member of the team. And now you are here, so now I don’t feel as awkward!"
    show glo neutral_talk at Position(xpos=1050)
    show kan neutral at Position(xpos=1350)
    show bra neutral at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    glo "Not that you now have to feel awkward, it’s just something I was feeling. But there is no reason you should feel awkward at all!"
    show glo embarrassed_talk at Position(xpos=1050)
    glo "Although, I totally understand if you do. It’s such a weird feeling, coming to a new place you don’t know - with a bunch of strangers. But I assure you it’s not bad at all!"
    show pov confused at left
    show glo smirk_talk at Position(xpos=1050)
    show kan smirk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    glo "But then again, you are quite young so it’s totally understandable if you are not used to the whole “workplace” environment and-"
    show glo smirk at Position(xpos=1050)
    show bra smirk_talk at Position(xpos=1600)
    bra "And she is off to the races, ladies and gentlemen…"
    show kan angry_talk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    kan "Be quiet, you. At least she knows how to make a friendly approach to someone."
    show kan bored_talk at Position(xpos=1350)
    kan "… More or less…"
    kan "Okay Gloria, that’s enough."
    show pov bored at left
    show glo bored_talk at Position(xpos=1050)
    show kan shocked at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    glo "-Oh, but then again your generation is quite proactive in social issues, so I can understand how you would know the basics of social justice in the eyes of modern internet standards and-"
    show glo smirk at Position(xpos=1050)
    show kan angry_talk at Position(xpos=1350)
    kan "Alright, alright. Slow down there, sweetheart."
    show glo confused at Position(xpos=1050)
    show kan bored_talk at Position(xpos=1350)
    show bra neutral at Position(xpos=1600)
    show jacdad sad at Position(xpos=1850)
    kan "No need to overwhelm the kid with a lot of information now."
    show pov confused at left
    show glo embarrassed_talk at Position(xpos=1050)
    show kan bored at Position(xpos=1350)
    show jacdad embarrassed at Position(xpos=1850)
    glo "Oh, dear."
    glo "I did it again, didn’t I?"
    show pov embarrassed at left
    show glo sad_talk at Position(xpos=1050)
    show bra smirk at Position(xpos=1600)
    glo "I’m so sorry. I’m a bit of a blabber mouth and I can’t help it sometimes."
    show pov embarrassed_talk at left
    show glo sad at Position(xpos=1050)
    pov "Uhh… It’s alright, I kinda got lost a bit mid-conversation, so I should be the one saying sorry, here."
    show pov embarrassed at left
    show glo embarrassed at Position(xpos=1050)
    show kan smirk at Position(xpos=1350)
    show bra smirk_talk at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    bra "Don’t sweat it, kid. Hardly anyone can keep up to what she is saying half the time."

    #-Kanako punches Bradley’s arm again-
    with hpunch
    show pov shocked at left
    show glo shocked at Position(xpos=1050)
    show kan angry at Position(xpos=1350)
    show bra shocked_talk at Position(xpos=1600)
    bra "OW!"
    show kan angry_talk at Position(xpos=1350)
    show bra angry at Position(xpos=1600)
    kan "Be nice, you ass!"
    show glo embarrassed at Position(xpos=1050)
    show kan confused_talk at Position(xpos=1350)
    show bra bored at Position(xpos=1600)
    show jacdad confused at Position(xpos=1850)
    kan "Anyway, how about you introduce yourself now, Gloria?"
    show pov embarrassed at left
    show glo embarrassed_talk at Position(xpos=1050)
    show kan confused at Position(xpos=1350)
    show jacdad neutral at Position(xpos=1850)
    glo "R-Right!"
    show pov neutral at left
    show glo neutral_talk at Position(xpos=1050)
    show kan neutral at Position(xpos=1350)
    glo "As you heard, my name is Gloria. I was the newest addition to the team before you came along. It’s nice to meet you!"
    show pov neutral_talk at left
    show glo neutral at Position(xpos=1050)
    show kan embarrassed at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    pov "It’s nice to meet you too. Same for you, Miss Kanako."
    pov "I’ll try to stay out of your way, Ma’am."
    show pov embarrassed at left
    show kan embarrassed_talk at Position(xpos=1350)
    show jacdad smirk at Position(xpos=1850)
    kan "Please. Just Kanako is fine. We are coworkers, and Ma’am makes me feel like an old woman."
    show pov bored at left
    show glo shocked at Position(xpos=1050)
    show kan bored at Position(xpos=1350)
    show bra smirk_talk at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    bra "You say that as if a 40 year old single mother is the peak of youth…"
    show pov smirk at left
    show glo embarrassed at Position(xpos=1050)
    show kan bored_talk at Position(xpos=1350)
    show bra angry at Position(xpos=1600)
    show jacdad neutral at Position(xpos=1850)
    kan "How about we show [povname] how the sick leave system works in the company, after I snap your spine in two?"
    show kan smirk at Position(xpos=1350)
    show jacdad neutral_talk at Position(xpos=1850)
    jacdad "Okay!"
    jacdad "[povname], let’s leave these fine group of workers to go back to their work day. And I’ll take you to meet with our floor manager."
    show pov confused_talk at left
    show bra bored at Position(xpos=1600)
    show jacdad embarrassed at Position(xpos=1850)
    pov "You're sure it's fine to leave them like-"
    show pov shocked at left
    show kan bored at Position(xpos=1350)
    show bra bored_talk at Position(xpos=1600)
    show jacdad shocked at Position(xpos=1850)
    bra "I’m just saying that you shouldn’t be ashamed to act your age a little bit."
    show pov confused at left
    show glo shocked at Position(xpos=1050)
    show kan bored_talk at Position(xpos=1350)
    show bra smirk at Position(xpos=1600)
    kan "Oh, is that what you think, now?"
    show pov bored at left
    show glo angry_talk at Position(xpos=1050)
    show kan angry at Position(xpos=1350)
    show jacdad confused at Position(xpos=1850)
    glo "That is a terrible thing to say to a lady!"
    show pov bored_talk at left
    show glo angry at Position(xpos=1050)
    show jacdad embarrassed at Position(xpos=1850)
    pov "Nevermind. Get me out of here."
    show pov embarrassed at left
    show jacdad embarrassed_talk at Position(xpos=1850)
    jacdad "Smart choice, my boy."

    scene black
    with fade

    $ main_story = 94

    jump lbl_workplace_introductions_part2

    #=SCENE END=

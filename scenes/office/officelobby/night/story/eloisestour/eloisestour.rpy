label lbl_eloises_tour:

    #[TRC Lobby, night - “Eloise’s Tour”  - main_story =97]

    #-Scene takes place immediately after the last scene with Mc and his Father discussing after getting out of the lobby-
    scene bg officelobby_night with fade
    show pov embarrassed_talk at left
    show dad bored at right
    with dissolve
    pov "Well, that wasn’t too bad of a work day all things considered."
    show pov embarrassed at left
    show dad bored_talk at right
    dad "All you did was get the runaround from the manager and his assistant, it doesn’t count as an actual work day, get off your high horse."
    show pov bored_talk at left
    show dad bored at right
    pov "Gee, thanks for always being a positive influence in my life and celebrating my accomplishments."
    show pov bored at left
    show dad smirk_talk at right
    dad "Last time I checked, doing the bare minimum shouldn’t be considered an accomplishment."
    show pov angry_talk at left
    show dad smirk at right
    pov "Can’t you just let me be proud of myself for five minutes?"
    show pov angry at left
    show dad smirk_talk at right
    dad "You’ve done nothing to be proud of."
    dad "You better remember this whole job is an opportunity for you to face reality."
    show pov smirk at left
    show dad bored_talk at right
    dad "Out here in the real world there ain’t gonna be nobody to pat your back just because you feel you did something right."
    show pov angry_talk at left
    show dad smirk_talk at right
    dad "You just shut your mouth, keep your head down and you do as you are told."
    show pov angry_talk at left
    show dad confused at right
    pov "Do you even listen to yourself when you talk nowadays?"
    pov "What’s your problem, seriously?"
    show pov angry at left
    show dad angry_talk at right
    dad "Don’t. Talk back to me, boy."
    dad "You are on very thin ice."
    dad "Now, shut your mouth before I decide on heading home by myself and leaving you to walk your way back."
    show pov angry_talk at left
    show dad angry at right
    pov "Doesn’t sound too bad if it means I don’t have to share a closed space with you."
    show pov shocked at left
    show dad angry_talk at right
    dad "Why, you little-"

    #Dad’s Phone: *Bzzz* *Bzzzt*
    show dad shocked_talk at right
    dad "Oh, what now?"

    #-Dad pulls out his phone-
    show pov confused at left
    show dad confused_talk at right
    dad "…"
    show pov smirk at left
    show dad angry_talk at right
    dad "Oh you have got to be kidding me!"
    show pov smirk_talk at left
    show dad angry at right
    pov "Pissed someone else off?"
    show pov smirk at left
    show dad angry_talk at right
    dad "Watch your damn mouth, boy!"
    show dad shocked_talk at right
    dad "God, this day keeps getting worse and worse."
    show pov smirk_talk at left
    show dad confused at right
    pov "Tell me about it…"
    show pov confused at left
    show dad smirk_talk at right
    dad "Well, looks like your wish to walk home is going to be granted."
    dad "I’ve just been called to cover an extra late night shift out of nowhere."
    show pov smirk at left
    show dad bored_talk at right
    dad "I’m not in a position to deny since I’ve been called by name to do it, so count your lucky stars."
    show pov bored_talk at left
    dad "We’ll talk about your attitude later on."

    #-Dad gets closer to you menacingly-
    show dad angry_talk at center with ease
    show pov shocked at left
    dad "Do NOT mess this opportunity I’m giving you…"
    show pov angry at left
    dad "You will remain here until you prove yourself to be of use to me."
    show pov confused at left
    dad "And if I’m lucky, that’s going to be real soon..."
    show pov confused_talk at left
    pov "… What do you mean by that?"
    show pov confused at left
    show dad smirk_talk at center
    dad "You’ll find out eventually…"

    #Dad’s Phone: *Bzzz* *Bzzzt*
    show dad confused at center
    dad "…"

    #-Dad heads back into the elevator-
    show pov bored at left
    show dad bored_talk at center
    dad "Head straight home. I’m warning you."
    dad "If they ask, tell them I’ll be working late and won’t be home tonight."
    show pov bored_talk at left
    pov "I doubt they will ask or care. I know I wouldn’t…"
    hide dad with dissolve
    #-Dad glares at the Mc one final time before the elevator doors close-
    show pov sad_talk at left
    pov "Sigh…"
    show pov embarrassed_talk at left
    pov "Always a pleasure talking to you…"
    show pov shocked at left
    show elo embarrassed_talk at right
    with dissolve
    elo "That definitely doesn't seem to be the case."

    #-Eloise appears into the scene with her phone on hand-
    show pov shocked_talk at left
    show elo neutral at right
    pov "Oh God… You saw all that?"
    show pov shocked at left
    show elo embarrassed_talk at right
    elo "I'm afraid I did."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Sorry, I doubt it helps with the initial impression you have of me."
    show pov embarrassed at left
    show elo embarrassed_talk at right
    elo "It's nothing to be embarrassed about. Plus you did warn me this was the sort of thing you dealt with, so don't worry about it."
    show pov confused at left
    show elo neutral_talk at right
    elo "Granted, I wasn't expecting him to just go ahead and make a scene in the workplace."
    elo "I got some flashbacks to my own father watching all that."
    show pov shocked_talk at left
    show elo neutral at right
    pov "God, I'm so sorry."
    show pov sad at left
    show elo bored_talk at right
    elo "Heh, I feel like I should be the one saying that."
    show pov embarrassed at left
    show elo embarrassed_talk at right
    elo "At least know that regardless of the asshat he could be from time to time, it was thanks to him, I became the woman that I am today."
    show pov neutral at left
    show elo smirk_talk at right
    elo "Don't let him drag you down and you can too."
    show pov neutral_talk at left
    show elo smirk at right
    pov "I can become a successful and beautiful business woman, then?"

    #-If the Player has 11 Charisma or Higher-
    if skill_cha >= 11:
        #+2 Eloise RP."
        $ add_points("eloise_points",2)
        show pov smirk at left
        show elo smirk_talk at right
        elo "Oh my~"
        elo "Well, aren't you a silver tongue devil?"
        show elo neutral_talk at right
        elo "Oh, I feel like I'm gonna like you."
        elo "I don't usually let people get by with giving me compliments but I could make an exception for you~"

        #=RESULT END=

    #-If the Player has 10 Charisma or Lower-

        #No RP reduction."
        show pov neutral at left
        show elo smirk_talk at right
        elo "Awww, that's adorable!"
        show pov embarrassed at left
        show elo neutral_talk at right
        elo "Delivery needs some work to take it over the edge but it's not bad!"
        elo "At the very least, I can confirm that I wasn't expecting it."
        show elo smirk_talk at right
        elo "I wouldn't normally let just anyone shoot compliments at me, but I feel like you need all the help you can get with this."

        #=RESULT END=

    show pov sad_talk at left
    show elo embarrassed at right
    pov "Sorry, I can't seem to shut my mouth sometimes."
    show pov confused at left
    show elo shocked_talk at right
    elo "It's quite alright! I'm quite flattered, really!"
    show pov shocked at left
    show elo shocked_talk at right
    elo "Anyway, I did promise you a tour of the place, didn't I?"
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "That you did. Though isn't it a little late to give me a full tour of the place?"
    show pov neutral_talk at left
    pov "I don't want to keep you here longer than I have to."
    pov "I'm sure you have a home to get back to and going out of your way to give the unexpected intern a tour of the facilities doesn't sound like the best way to spend a week night."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "{i}*giggle*{/i} Well, maybe not."
    elo "But I did promise and I am a woman of my word."
    show pov confused at left
    show elo smirk_talk at right
    elo "And seeing all of that, it's clear that you won't be getting any help from that man, I'll be the one to help you out."
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "You really don't have to, you know?"
    show pov confused at left
    show elo bored_talk at right
    elo "I want to."
    show elo smirk_talk at right
    elo "Plus, I can't have an employee running around with no idea where he is."
    elo "At the very least you should know the basic procedure in case of a fire or something alike, don't you think?"
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "That's… Actually a fair point."
    show pov embarrassed at left
    show elo smirk_talk at right
    elo "Right? Besides, it does sort of fall under my job description that I have to look after employees well beings you know?"
    elo "Interns or not."
    show pov bored_talk at left
    show elo smirk at right
    pov "You never did tell me what you do here, actually."
    show pov confused_talk at left
    show elo confused at right
    pov "Or your name."
    show pov confused at left
    show elo bored_talk at right
    elo "Well, we did run short on time on the elevator last time, did we not?"
    show pov confused_talk at left
    show elo neutral at right
    pov "We sadly did, I was quite enjoying our chat."
    show pov confused at left
    show elo shocked_talk at right
    elo "So was I!"
    elo "It’s rather refreshing to talk with someone from work without them either too scared out of their minds to talk to me like a human being or kissing the ground I walk upon trying to make themselves look good."
    show pov shocked_talk at left
    show elo embarrassed at right
    pov "That happens a lot with you?"
    show pov shocked at left
    show elo embarrassed_talk at right
    elo "Comes with the position."
    show pov confused_talk at left
    show elo embarrassed at right
    pov "Which is?"
    show pov confused at left
    show elo smirk_talk at right
    elo "I’ll tell you by the end of the tour."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "I want to enjoy these few moments where I can be normal with someone in the office."
    show pov confused at left
    show elo smirk_talk at right
    elo "And to try and guess your reaction when you find out."
    show pov embarrassed_talk at left
    show elo smirk at right
    pov "Is it really necessary?"
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Oh, let me have my fun. I can get very bored of the paperwork that keeps me in my office most of the time so I’m taking this as an excuse to break the routine a little."
    show pov embarrassed_talk at left
    show elo neutral at right
    pov "Well, I certainly appreciate you taking time to help me out here so it’s the least I can do."
    show pov neutral_talk at left
    pov "Can I at least know your name then? I wouldn’t want to just call you “Miss” or “Ma’am” all tour."
    show pov neutral at left
    show elo smirk_talk at right
    elo "{i}*giggle*{/i} Fair enough, though “Ma’am” is what I’m most used to by now."
    elo "My name is Eloise, it’s nice to meet you, [povname]."
    show pov neutral_talk at left
    show elo smirk at right
    pov "Pleasure’s all mine, Eloise."
    show elo neutral at right
    pov "So, how long is the tour going to take?"
    show pov embarrassed at left
    pov "Not that I have anything better to do or anything, but I don’t want to risk what he might do if I get home after him."
    show pov bored_talk at left
    show elo neutral at right
    pov "Especially after his warning."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "Oh, I wouldn’t worry about him so much."
    show pov neutral at left
    show elo smirk_talk at right
    elo "A little birdie told me that someone in management has a sudden need for someone to redo some paperwork."
    elo "It's regarding your department all over again ASAP due to what seems to be an 'accidental' omission of a few forms."
    elo "And since he is the only employee of the department left in the building with permission to look at said paperwork, I’m afraid he has been assigned to take over the task."
    show elo neutral_talk at right
    elo "So I wouldn’t count on him getting home anytime soon."
    elo "Especially considering its around 250 or 300 forms he needs to look over in order to find the error."
    show pov confused_talk at left
    show elo smirk_talk at right
    pov "Why would they need a revision of paperwork at this time of night?"
    show pov embarrassed at left
    show elo smirk at right
    elo "Hehe, maybe it’s not as urgent as I said but he doesn’t need to know that, does he?"
    show pov shocked_talk at left
    show elo neutral at right
    pov "You mean… Oh, you didn’t!"
    show pov shocked at left
    show elo neutral_talk at right
    elo "Consider it a favor from someone who went through a similar situation and now has the means to help out a little."
    show pov neutral_talk at left
    show elo smirk at right
    pov "I think I’m going to like you, Eloise."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "And I think I’m going to like you too, [povname]."
    show pov neutral at left
    show elo embarrassed_talk at right
    elo "That being said though, it is a bit too late to give you the whole tour of the place."
    elo "Especially of the side buildings, R&D division and not to mention the warehouse for our equipment."
    elo "Usually interns have around two or three days focused on touring the whole place-"
    elo "And given a proper rundown of the tasks they would be performing there if they are solicited in said departments, safety guidelines, practice tests regarding examples of real life situations and all that other HR garbo."
    show elo smirk_talk at right
    elo "But since it’s just you and me, I doubt you wanna hear all that, so I'll just be showing you around the place and make conversation."
    show pov neutral_talk at left
    show elo smirk at right
    pov "I really appreciate you doing this for me, especially cuz you really don’t have to."
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "I know, but I want to."
    show pov neutral at left
    show elo embarrassed_talk at right
    elo "It’s nice to have someone in the workplace treat me like a normal human being rather than a superior and I guess we owe you for being the breakthrough needed to install the camera system."
    show elo neutral_talk at right
    elo "So this is the least I can do for you."
    show pov neutral_talk at left
    show elo neutral at right
    pov "Well, you won’t hear me complaining then."
    show pov smirk_talk at left
    pov "Shall we start?"
    show pov smirk at left
    show elo neutral_talk at right
    elo "Better do it before it gets even later."
    elo "We only have time to do the important parts of the office building so it won’t be a long trip considering you have likely seen your key workspaces by now."
    show pov confused at left
    show elo smirk_talk at right
    elo "How about you tell me a little bit about yourself while we walk?"
    show pov embarrassed at left
    show elo neutral_talk at right
    elo "I can’t help but feel a little curious."
    show pov neutral_talk at left
    show elo confused at right
    pov "Alright, but only if you also tell me more about yourself too."
    show pov confused_talk at left
    pov "I feel like I’m at a disadvantage considering you haven’t really shared much either."
    show pov smirk_talk at left
    show elo embarrassed at right
    pov "And not to mention the fact that you’ve seen me naked by now."
    show pov smirk at left
    show elo neutral_talk at right
    elo "{i}*giggle*{/i} Alright, you make a fair point."
    show pov shocked at left
    show elo smirk_talk at right
    elo "But don’t expect to see me naked to repay the favour."
    show pov smirk at left
    elo "You are cute and all, but don’t push your luck."
    show pov smirk_talk  at left
    show elo smirk at right
    pov "Wasn’t planning to, I assure you."
    show pov smirk_talk at left
    show elo smirk_talk at right
    elo "Sure you weren’t."
    show pov neutral at left
    show elo neutral_talk at right
    elo "Ok, ready to go?"
    show pov neutral_talk at left
    show elo smirk at right
    pov "Lead the way, Eloise."
    show pov smirk at left
    show elo neutral_talk at right
    elo "Alright, we can head for the employee lounge first and then work our way up!"
    show pov embarrassed at left
    show elo neutral at right
    elo "In the meantime, tell me how your first day with us went."

    #-Eloise and Mc leave the scene followed by a fade to black to indicate movement-
    scene black with fade
    #=SCENE END=
    jump lbl_evie

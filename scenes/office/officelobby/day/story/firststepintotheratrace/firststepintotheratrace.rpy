#[TRC Lobby, Afternoon - “The First Step into the Rat Race”  - main_story =91]

#-Scene starts with a graphic of the mc entering the large futuristic looking lobby, employees going to work or in the middle of conversations in the lounge area, everyone is on a fitting looking suit or tie for the job and the Mc heads to the two ladies behind the receptionist's desk-

label lbl_first_step_into_the_rat_race:
    show btn_officelobby_day_skylar_idle2
    show btn_officelobby_day_carmen_idle2
    $ renpy.pause(0.001)


    show sky neutral at Position(xpos=1300)
    show car neutral at right
    call lbl_officelobbydouble_counter_check
    with dissolve



    show pov neutral_talk at Position(xpos=800)
    with dissolve
    pov "Hello, I'm here for-"
    show pov neutral at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car shocked_talk at right
    car "Ah yes, you are the delivery boy, right?"
    show pov confused at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car neutral_talk at right
    car "You can leave the take out on the desk. Care to pay for it, Skylar sweetie?"
    show car embarrassed_talk at right
    car "I seem to have misplaced my purse."
    show pov embarrassed at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    show car embarrassed at right
    sky "A-Again?"
    show sky embarrassed_talk at Position(xpos=1300)
    sky "Golly, Carmen, you really tend to lose your purse often whenever we order lunch."
    show pov confused at Position(xpos=800)
    show sky sad at Position(xpos=1300)
    show car embarrassed_talk at right
    car "Oh I know, it's such a terrible habit of mine. I'm sooooo sorry~"
    show pov embarrassed at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car embarrassed at right
    sky "I-It's okay, you can't help it. I'll pay the tab."
    show sky embarrassed at Position(xpos=1300)
    show car embarrassed_talk at right
    car "Thank you, sweetheart. You are a doll~"
    show pov bored at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car embarrassed at right
    sky "I-I-It's okay!"
    show pov embarrassed at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    show car neutral at right
    sky "A-Anything for a friend!"
    show sky embarrassed_talk at Position(xpos=1300)
    sky "Sorry for the wait. H-How much do I owe you?"
    show pov embarrassed_talk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car neutral at right
    pov "Uh, sorry but I'm not a delivery guy."
    show pov embarrassed at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car shocked_talk at right
    car "In that case please feel free to walk back out through the door. This is private property and we are not allowed to receive any flyers."
    show pov confused at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    show car bored at right
    sky "Carmen, that's not very nice!"
    show sky embarrassed_talk at Position(xpos=1300)
    sky "B-But I'm afraid she has a point, I'm sorry."
    show sky neutral_talk at Position(xpos=1300)
    sky "You are only allowed on the premises with an appointment. Do you have one?"
    show pov embarrassed at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car bored_talk at right
    car "Be serious here, Skylar."
    show pov bored at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "There is no way he is in here on any official business; he is just a kid."
    show pov smirk_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk at right
    pov "Well, I'm loving the work environment already."
    show pov bored_talk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car confused at right
    pov "I'm here about an internship actually."
    show pov smirk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car shocked_talk at right
    car "You are here about an internship?"
    show car smirk_talk at right
    car "No offense here, but aren't you a bit green to be hired here?"
    show pov bored at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car embarrassed_talk at right
    car "Shouldn't you be looking for something on your own level or something?"
    show pov smirk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car smirk_talk at right
    car "Perhaps a babysitting gig would be more your speed?"
    show sky shocked_talk at Position(xpos=1300)
    show car smirk at right
    sky "Carmen!"
    show pov embarrassed at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "P-Please excuse her, she is a bit too direct sometimes."
    show pov embarrassed_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored at right
    pov "That's alright. This whole thing wasn't really my idea to begin with anyway."
    show pov confused at Position(xpos=800)
    pov "I was told the opening was pretty much settled, by my father."
    show pov smirk_talk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car shocked at right
    pov "My name is [povname]. Were you not told you I would be coming in?"
    show pov bored at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    show car neutral at right
    sky "Oh, that's right!"
    show pov neutral at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    show car smirk at right
    sky "We were told to expect a new intern by that name coming in!"
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "Wow, you are definitely not what I had in mind when I heard we were getting a new intern."
    show pov smirk_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk at right
    pov "That much is obvious."
    show pov smirk at Position(xpos=800)
    show sky angry_talk at Position(xpos=1300)
    sky "P-Please Carmen, don't be so rude!"
    show pov smirk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car smirk_talk at right
    car "I'm just teasing, sweetie~"
    show pov bored at Position(xpos=800)
    show sky angry at Position(xpos=1300)
    show car bored_talk at right
    car "You gotta learn to not take things so seriously!"
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "He knows I'm just kidding around, don't you darling?"
    show pov embarrassed_talk at Position(xpos=800)
    show car smirk at right
    pov "Bit hard to tell, to be honest."
    show pov embarrassed at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car neutral at right
    sky "I-I think we should all try and start over."
    show pov smirk at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    sky "Welcome to The Robotics Company. M-My name is Skylar and this is my co-worker Carmen."
    show pov neutral at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk_talk at right
    car "Pleasure is all yours, kid.."
    show pov embarrassed_talk at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk at right
    pov "Right, well as you heard before, my name is [povname] and I'm here about an internship that was supposedly set up for me."
    show pov neutral at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    show car neutral at right
    sky "Right, let me just enter some information into our database about your arrival and take your picture for the security system."
    show pov confused_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral at right
    pov "Why do you need my photo for the security system?"
    show pov confused at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    sky "The company has a state-of-the-art face recognition system installed in its security cameras."
    show sky neutral_talk at Position(xpos=1300)
    sky "We upload photos of all personnel and visitors into the system for security purposes so the alarm system can track any anomalies."
    show pov embarrassed_talk at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    pov "What do you mean by anomalies?"
    show pov confused at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk_talk at right
    car "Corporate espionage is quite the big thing in the market that the company is known for, sweet heart."
    show pov bored at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "The CEO in particular, takes this issue very seriously."
    car "So every employee is assigned a specific area to work in, depending on their positions."
    show pov confused at Position(xpos=800)
    show car smirk_talk at right
    car "Wouldn't you think it would be suspicious for a worker in the office division to be lurking around the warehouse or testing areas and vice versa?"
    show pov smirk at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk_talk at right
    car "Along with that, it keeps a record of where each employee is at every hour of the work day in case an incident were to occur."
    show pov smirk_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk at right
    pov "Isn't that a bit invasive?"
    show pov confused at Position(xpos=800)
    show car bored_talk at right
    car "If you are going to be working for the generous paycheck and bonuses the company gives, you gotta learn to deal with a few of its quirks."
    car "Besides, everything is perfectly legal."
    show pov smirk at Position(xpos=800)
    show car smirk_talk at right
    car "At least in this area of the country."
    show sky embarrassed_talk at Position(xpos=1300)
    show car smirk at right
    sky "Y-You shouldn't have an issue with it though. As an intern, your area of work is rather small and easy to remember."
    show pov shocked at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "You basically have it a bit better than visitor privileges in the facility - but don't get to leave with a goodie bag."
    show pov embarrassed_talk at Position(xpos=800)
    show car smirk at right
    pov "Right…"
    show pov confused_talk at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car neutral at right
    pov "Well, is this where you hand me off to an HR guy or I get some basic training done or something?"
    show pov confused at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car smirk at right
    sky "N-Normally that would be the case yes, but you are a bit of a special case."
    show pov embarrassed at Position(xpos=800)
    show sky confused_talk at Position(xpos=1300)
    sky "Usually we have groups of interns come together and have trainers ready to receive them, b-but..."
    show pov confused at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "Since strings were pulled to get you in here out of hiring season, there isn't anyone around with an open schedule to spend time with you."
    show pov shocked_talk at Position(xpos=800)
    show car smirk at right
    pov "Don't companies as large as this one usually have a whole department dedicated to training interns and new employees?"
    show pov confused at Position(xpos=800)
    show sky sad at Position(xpos=1300)
    show car bored_talk at right
    car "Quite so, yes. But then again, there is a reason why companies like this have hiring time frame, filter periods for applicants and don't just hire whatever random person shows up at any hour."
    show pov bored at Position(xpos=800)
    show sky angry_talk at Position(xpos=1300)
    show car bored at right
    sky "Carmen!"
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "Alright, alright, I'll back off."
    show pov smirk at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "{i}*sigh*{/i}"
    sky "She does have a point though."
    show pov bored at Position(xpos=800)
    show sky sad at Position(xpos=1300)
    show car bored at right
    sky "The company employee structure is rather solid, so positions are rarely available. Which means hiring isn't a priority unless a project expands in scope and requiring more hands on board."
    show sky embarrassed_talk at Position(xpos=1300)
    show car smirk at right
    sky "You are joining the team in a time where our latest team of interns is around halfways to three quarters way done with their training."
    show pov confused at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "Which means you are too late to this and too early for the next party, to really join the usual training program."
    show car bored_talk at right
    car "So there is no chance of you really getting the standard treatment."
    show pov confused_talk at Position(xpos=800)
    show car bored at right
    pov "Then what am I supposed to do ?"
    show pov smirk_talk at Position(xpos=800)
    pov "Doubt you guys are just gonna let me roam around the place aimless, until I figure out what to do."
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "Hang onto your horses there, cowboy."
    show pov bored at Position(xpos=800)
    show car smirk_talk at right
    car "Where you are going, you definitely don't need too deep of a training program anyway."
    show pov confused_talk at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car smirk at right
    pov "What do you mean?"
    show pov confused at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "The area you are going to, is one of our lower work traffic areas. This is why you won't really be receiving much training aside from the one given to you by the floors manager."
    show pov shocked at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "Internship here usually means getting to help out in the assembly lines or the warehouse area; perhaps even the higher end offices even."
    show car shocked_talk at right
    car "But in your case..?"
    show pov confused at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk_talk at right
    car "You are going somewhere much more your speed and qualifications."
    show sky neutral_talk at Position(xpos=1300)
    show car smirk at right
    sky "You'll be heading into our low-risk tech support department."
    show pov bored at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    sky "A… lower-end section of the company, but nonetheless important!"
    show pov bored_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car embarrassed at right
    pov "Low-priority tech support?"
    show pov embarrassed at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car neutral_talk at right
    car "Basically the guys who take care of calls that the normal tech support guys don't have the time or desire to take."
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "So the guys who take all calls relating to grandmas who don't understand the product they bought on a whim or people complaining about a screw missing, that is likely still in the box."
    show pov embarrassed_talk at Position(xpos=800)
    show car smirk at right
    pov "Is the amount of calls so high you really need a low-risk department?"
    show pov bored at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "Apart from that, our technical support is really more optimised for the larger clientele who require assistance with the higher-end equipment we provide."
    show pov embarrassed at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    show car neutral at right
    sky "This team was formed mainly to deal with any issues regarding the new security system about to be implemented across town."
    show pov bored at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "They weeded out the loser- I mean, the underperformers from the main tech-support group and grouped them all together to take care of this little side venture that's more their speed."
    show pov smirk at Position(xpos=800)
    show car smirk_talk at right
    car "You'll fit in perfectly~"
    show pov smirk_talk at Position(xpos=800)
    show car smirk at right
    pov "Peachy."
    show pov smirk at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "I-It's important work regardless, but without the intensive training required for other positions in the company."
    show sky bored_talk at Position(xpos=1300)
    sky "Since this is a venture that came out of the blue by the CEO's decision. The department is still sort of getting its footing."
    show pov bored at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car neutral at right
    sky "So an intern was needed to help with the projected increase in calls."
    show pov confused at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    sky "W-We opened a few positions internally at first for the interns, but…"
    show sky embarrassed at Position(xpos=1300)
    show car bored_talk at right
    car "None of them were stupid enough to get themselves stuck in a copy and coffee boy position in a dead-end branch of the company."
    car "Especially those hoping to get into the sales and management areas."
    show pov shocked at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car smirk_talk at right
    car "Now those are the high position men you want to get in be-"
    show sky shocked_talk at Position(xpos=1300)
    show car smirk at right
    sky "C-C-Carmen!"
    show pov smirk at Position(xpos=800)
    show sky angry at Position(xpos=1300)
    show car angry_talk at right
    car "Oh, don't be such a prude. You know it's true!"
    show pov bored at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    show car angry at right
    sky "I-In any case!"
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "Due to lack of interest, management was considering making an opening for a new intern for that area, but one of the employees of the sector mentioned they knew a person who would take the job. And, well, here we are..."
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "Welcome to your new exciting position~"
    show pov shocked_talk at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car smirk at right
    pov "Wait, wait, wait a minute."
    show pov confused_talk at Position(xpos=800)
    pov "Are you telling me my father is working in this new sector as well?"
    show pov confused at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    show car bored_talk at right
    car "Apple doesn't fall far from the tree, it seems."
    show sky confused_talk at Position(xpos=1300)
    show car bored at right
    sky "I don't know the exact employee who made the claim, but I would assume it's him, from what you have told me."
    show sky embarrassed_talk at Position(xpos=1300)
    show car shocked at right
    sky "Why, is there a problem?"
    show pov confused_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored at right
    pov "W-Well, not really."
    show pov embarrassed_talk  at Position(xpos=800)
    pov "It's just that he has been… a bit of a dick lately, regarding his job, and I figured it would have been far more important than second-rate tech support."
    show pov confused_talk at Position(xpos=800)
    show car neutral at right
    pov "Yet now you are telling me, he wasn't even good enough to stay with the higher-end of the tech support department?"
    show pov angry at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car bored_talk at right
    car "Disappointed, your old man is not all you thought him up to be?"
    show car smirk_talk at right
    car "Join the club. It sucks."
    show pov smirk at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car smirk at right
    sky "I-It's still very important, I assure you!"
    show pov embarrassed_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car bored at right
    pov "No, no. It's okay."
    pov "And disappointed is not the word I would use, really."
    show pov shocked_talk at Position(xpos=800)
    show car smirk at right
    pov "I would say amused is far more fitting."
    show pov smirk_talk at Position(xpos=800)
    show sky confused at Position(xpos=1300)
    pov "It kind of made my day so far, worth it actually."
    show pov smirk at Position(xpos=800)
    show sky confused_talk at Position(xpos=1300)
    sky "O-Oh, well, t-that's good, then?"
    show sky shocked at Position(xpos=1300)
    show car smirk_talk at right
    car "Jerks are usually terrible at their job, after all."
    show pov smirk_talk at Position(xpos=800)
    show car smirk at right
    pov "Amen to that."
    show pov smirk_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral at right
    pov "Well, is there anything else you need to fill in about me?"
    show pov neutral at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    sky "Oh, not at all!"
    show sky neutral_talk at Position(xpos=1300)
    sky "Let me just hand you over your temporary I.D. Pass and you'll have access to the employee elevator."
    sky "I have already submitted your picture into the database, so your actual I.D. should be ready in a day or two."
    show pov neutral_talk at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    pov "Neato."
    show pov neutral at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    show car smirk at right
    sky "Welcome to The Robotics Company family!"
    show pov embarrassed at Position(xpos=800)
    show sky smirk_talk at Position(xpos=1300)
    show car neutral at right
    sky "I hope you take your tasks seriously and work to be better every day."
    show pov neutral at Position(xpos=800)
    show sky neutral at Position(xpos=1300)
    show car smirk_talk at right
    car "Welcome to the corporate rat race, kid."
    car "You are going to hate it."
    show pov smirk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral_talk at right
    car "Enjoy your copy machine duties."
    show sky shocked_talk at Position(xpos=1300)
    show car neutral at right
    sky "Carmen!"
    show pov shocked at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    sky "O-Oh, I almost forgot!"
    show pov confused at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car bored at right
    sky "Once you are there, the floor manager will give you a rundown of your tasks, the floor is still rather barebones, so it's possible some of the equipment is a bit faulty."
    show pov shocked at Position(xpos=800)
    show sky neutral_talk at Position(xpos=1300)
    sky "Feel free to request using one from another floor, if necessary."
    show pov bored at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car smirk_talk at right
    car "Have fun bringing the coffee from another floor~"
    show pov neutral at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral_talk at right
    car "Jokes aside though, stay clear of the engineering floors \"brewing station\"."
    show pov confused at Position(xpos=800)
    show car smirk_talk at right
    car "State of the art, but they don't like to share. I'm telling you this for your own good."
    show sky embarrassed_talk at Position(xpos=1300)
    show car smirk at right
    sky "She is not kidding."
    show pov confused_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral at right
    pov "Uhh… I'll keep it in mind, thanks…"
    show pov embarrassed at Position(xpos=800)
    show sky embarrassed_talk at Position(xpos=1300)
    show car neutral at right
    sky "I-It was nice meeting you, [povname]!"
    sky "H-Hope to see you here a while."
    show pov confused at Position(xpos=800)
    show sky shocked at Position(xpos=1300)
    show car smirk_talk at right
    car "Highly doubt it, though."
    show pov bored at Position(xpos=800)
    show sky shocked_talk at Position(xpos=1300)
    show car smirk at right
    sky "Carmen!"
    show pov bored_talk at Position(xpos=800)
    show sky embarrassed at Position(xpos=1300)
    show car neutral at right
    pov "Yeah, nice meeting you for the most part too."
    show pov embarrassed_talk at Position(xpos=800)
    pov "See you later."

    #-Mc leaves the scene for the elevator-

    #=SCENE END=
    $ main_story = 92
    jump lbl_officelobby_day

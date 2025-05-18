#[School Hallway, After School- “Edward’s Advice”  - main_story =89]

#-Scene happens by talking to Edward in the hallway at school before heading into The Robotics Company for the first time, this can be on the following days before the scheduled Monday or during said Monday after school-


#-Scene starts by clicking on Edward-
label lbl_edwards_advice:
    show btn schoolyard_day_edward_idle
    $ renpy.pause(0.001)

    if main_story == 89:
        show pov neutral at left
        with dissolve
        show edw neutral_talk at right
        hide btn schoolyard_day_edward_idle
        with dissolve
        edw "Let me know how you get on at the office, dude."
        show pov neutral_talk at left
        show edw neutral at right
        pov "Will do."
        show pov neutral at left
        show edw neutral_talk at right
        edw "Good luck."

    elif main_story == 88:
        show pov neutral_talk at left
        with dissolve
        pov "Hey, Ed-"
        show edw neutral_talk at right
        hide btn schoolyard_day_edward_idle
        with hpunch
        show pov shocked at left
        edw "There he is!"
        show edw smirk_talk at right
        edw "My ticket to fortune and fame!"
        show pov shocked_talk at left
        show edw neutral at right
        pov "Shhh! Not so loud!"
        show pov embarrassed at left
        show edw shocked_talk at right
        edw "Dude this is huge!"
        show edw neutral_talk at right
        edw "You landed an internship in the-"
        show pov shocked_talk at left
        show edw neutral at right
        pov "And I'm trying to be discreet about it!"
        show pov embarrassed_talk at left
        pov "It's only a temporary thing anyway and I don't plan to stay for too long there."
        show pov embarrassed at left
        show edw confused_talk at right
        edw "Dude are you crazy?"
        show edw shocked_talk at right
        edw "You got handed an entry position into one of the largest conglomerates and business companies that lead in the field of robotics and engineering!"
        edw "You don't even need to have a higher executive position to get paid enough money to support both your family and your secret 2nd family!"
        show edw confused_talk at right
        edw "Why wouldn't you want to stay?"
        show pov confused_talk at left
        show edw confused at right
        pov "Well, first of all because I won’t be having any free time after school while I’m doing all of this shit."
        show pov smirk_talk at left
        pov "Second of all, my dad is using this as a punishment so I doubt I’ll be getting paid much to begin with."
        show pov bored_talk at left
        pov "And finally, I don’t even know what they do specifically."
        show pov bored at left
        show edw confused_talk at right
        edw "You don’t? Dude, they are the biggest building in the area and your dad works there."
        show edw bored_talk at right
        edw "The whole town is basically owned by them. Didn’t your father give you at least a memo on what he does?"
        show pov bored_talk at left
        show edw confused at right
        pov "Okay, I’m starting to feel you don’t really listen to me whenever I tell you about my relationship with my dad."
        show pov bored at left
        show edw embarrassed_talk at right
        edw "Sorry, I have a lot in my mind and don’t keep some info too well."
        edw "The Robotics Company is the leading enterprise in the field of robotics this side of the coast."
        show pov confused at left
        show edw shocked_talk at right
        edw "They have their fingerprints in a little bit of everything, from prosthetics, ROVER-like vehicles for deep space and underwater exploration, automated security systems and yes, primarily robots."
        edw "They are currently the leading company in the race of making humanoid robots for tasks."
        show pov confused_talk at left
        show edw neutral at right
        pov "What kind of tasks?"
        show pov confused at left
        show edw shocked_talk at right
        edw "Anything really. At least on theory."
        show edw neutral_talk at right
        edw "So far their business plan has them making robots for things like receptionist jobs, companionship and medical care for elderly residents and  disarming explosives for the military."
        show pov bored_talk at left
        show edw neutral at right
        pov "Bit of a large jump from one topic to the other, don’t you think?"
        show pov bored at left
        show edw shocked_talk at right
        edw "The robot revolution is coming dude."
        show edw smirk_talk at right
        edw "Soon enough we are gonna have businesses segregated between human and robot operated."
        show pov confused_talk at left
        show edw smirk at right
        pov "Not a good look to be using the word “segregated” in a positive outlook nowadays dude."
        show pov embarrassed_talk at left
        pov "Still, I guess it’s in you to be happy about the robot uprising."
        show pov neutral at left
        show edw confused_talk at right
        edw "Well, if it’s coming regardless of what people do or fear, may as well get myself on the side of history that makes money out of the whole movement, don’t you think?"
        show edw embarrassed_talk at right
        edw "Though it is scary to think that 100%% human operated businesses are one day gonna be more of a niche feature to a business rather than the norm."
        show edw neutral_talk at right
        edw "Like a Rock-n-Roll themed cafe or a 50’s Diner."
        show pov bored_talk at left
        show edw neutral at right
        pov "Cold headed and calculative as always I see."
        show pov smirk_talk at left
        pov "Still thankful you aren’t a supervillain."
        show pov smirk at left
        show edw smirk_talk at right
        edw "I’m a man of progress my friend!"
        show edw neutral_talk at right
        edw "And sadly most of the time, progress is a cruel and unforgiving mistress."
        show pov smirk_talk at left
        show edw smirk at right
        pov "Right…"
        show pov neutral at left
        show edw neutral_talk at right
        edw "Anyway, That's what the TRC is mostly known for at face value."
        show pov smirk_talk at left
        show edw neutral at right
        pov "Thanks for the elevator pitch, but I really don’t think it’s for me."
        show pov bored_talk at left
        pov "I am giving it a shot for as long as the ride lasts, but I really am underqualified for the position in the first place."
        show pov smirk_talk at left
        show edw embarrassed at right
        pov "So even if I end up liking it, I doubt I'll last much longer if they need me for something aside than coffee runs and copy machine work."
        show pov smirk at left
        show edw embarrassed_talk at right
        edw "Think I would have a better chance getting in if I apply for the internship the moment you get kicked out?"
        show edw smirk_talk at right
        edw "I would kill to be in your position right now."
        show pov smirk_talk at left
        show edw smirk at right
        pov "Pretty sure most people want to kill themselves when stuck in internship work for long, but you do have a hard on for this place so I think you would do far better."
        show pov neutral at left
        show edw smirk_talk at right
        edw "Oh, I would be the absolute best if the opportunity arises, my good sir!"
        show pov bored_talk at left
        show edw neutral at right
        pov "Let's hope your inventions manage to impress them before you have to resort to that, man."
        show pov smirk_talk at left
        pov "I think the world has enough copy machine boys."
        show pov smirk at left
        show edw smirk_talk at right
        edw "Thanks for believing in me, man."
        show pov bored_talk at left
        show edw neutral at right
        pov "No worries, dude."
        show pov neutral_talk at left
        pov "Besides, you were developing a full on taser vest last time, either I help you use your tech for good or you'll turn supervillain."
        show pov neutral at left
        show edw smirk_talk at right
        edw "There is always a chance to become a supervillain, my friend."
        show pov bored_talk at left
        show edw neutral at right
        pov "Yeah, but hopefully you'll remember I lended you a hand when you needed it once you take over the world."
        show pov neutral at left
        show edw smirk_talk at right
        edw "I'll have ya resting comfortably on Skull Island while I take over the world."
        show pov smirk_talk at left
        show edw smirk at right
        pov "Appreciated."
        show pov confused_talk at left
        show edw neutral at right
        pov "How are we going to do this, by the way?"
        show pov confused_talk at left
        pov "Showing your inventions to the company, not the take over the world thing."
        show pov embarrassed_talk at left
        show edw embarrassed at right
        pov "I doubt I am going to be allowed into the building with one of your inventions, especially not the taser vest."
        show pov embarrassed at left
        show edw smirk_talk at right
        edw "Never fear, my trusty sidekick!"
        show pov confused at left
        show edw neutral_talk at right
        edw "I already have a usb with my favorite highlights of my main projects and investigations along with a proper presentation to them."
        show edw shocked_talk at right
        edw "Always best to only show them a hint of what the product can do when you are presenting a resume for a company like this."
        show pov bored at left
        show edw smirk_talk at right
        edw "Helps with the odds and the chance of getting a callback and all, you know?"
        show pov smirk_talk at left
        show edw smirk at right
        pov "You seem confident on it."
        show pov smirk at left
        show edw smirk_talk at right
        edw "A well disguised illusion my friend!"
        show edw neutral_talk at right
        edw "The moment you head to work I'll run to the bathroom and puke my stomach out from the nerves of actually getting my projects reviewed by the company higher ups."
        show pov confused_talk at left
        show edw neutral at right
        pov "I still haven't received the part of the plan of how I'm supposed to get the higher ups to look at it in the first place."
        show pov smirk at left
        show edw smirk_talk at right
        edw "That one falls entirely on you dude. Either be direct and tell them of it when you think the time is right or sneak it into their to do pile with the note."
        show pov confused_talk at left
        show edw bored at right
        pov "You think that's gonna work?"
        show pov confused at left
        show edw bored_talk at right
        edw "Dunno, not good dealing with people myself, that's why I leave it on your capable hands."
        show pov confused at left
        show edw embarrassed_talk at right
        edw "Do what you do best and improvise if you need to!"
        show pov embarrassed at left
        show edw neutral_talk at right
        edw "Just like I do what I do best and help you set up cameras all over the lake without getting spotted."
        show pov embarrassed_talk at left
        show edw neutral at right
        pov "Point taken."
        show pov neutral at left
        show edw smirk_talk at right
        edw "I'm not gonna ask you for the world either dude. Take as much time as you need with this but do let me know when you do."
        show pov confused_talk at left
        show edw smirk at right
        pov "How do you know I won't just forget or not do it in the first place and tell you I did?"
        show pov embarrassed at left
        show edw smirk_talk at right
        edw "Duh, because you are my friend, dude."
        show pov shocked at left
        show edw embarrassed_talk at right
        edw "I know you aren't the type of person to stab me in the back like that."
        show pov embarrassed at left
        show edw neutral_talk at right
        edw "I trust you and you haven't given me a reason not to."
        show pov embarrassed_talk at left
        show edw embarrassed at right
        pov "…"
        pov "Dang, dude…"
        show pov embarrassed at left
        show edw smirk_talk at right
        edw "Plus, there is the thing about me not letting you use the cameras if you don't at least give it an honest try to sweeten the deal for me."
        show pov smirk_talk at left
        show edw neutral at right
        pov "Yet another beautiful moment of bro-ness just spoiled and gone with the wind, as if it was nothing."
        show pov smirk at left
        show edw neutral_talk at right
        edw "I trust you dude, that much is true, but it's way easier to trust when one holds a bit of leverage over people, you know?"
        show pov bored_talk at left
        show edw neutral at right
        pov "Bit of a sociopath-like point of view, but okay."
        show pov neutral at left
        show edw smirk_talk at right
        edw "It gets results."
        show pov confused at left
        show edw neutral_talk at right
        edw "Anyway, here's the usb and the file. The file mainly contains my contact info and thesis work on my projects, it will make them look like the submissions other prospects do so you'll be fine if you need to sneak it in."
        show pov confused_talk at left
        show edw neutral at right
        pov "You sure this is the final version you want to submit to them?"
        show pov embarrassed_talk at left
        show edw confused at right
        pov "I doubt I'll be able to get away with submitting your second draft if you regret it afterwards."
        show pov smirk_talk at left
        show edw bored at right
        pov "We are already kind of pushing your luck here."
        show pov smirk at left
        show edw shocked_talk at right
        edw "Of course I’m not sure and I’ll definitely be wishing I made changes to it as soon as I get home."
        show pov confused at left
        show edw embarrassed_talk at right
        edw "But I won’t get anywhere by dwelling on it all day and this is a once in a lifetime shot to get ahead."
        show pov neutral at left
        show edw confused_talk at right
        edw "I’ve been polishing it for years and proofread it hundreds of times. If things go south, I’ll at least get good corrections out of it for the future."
        show pov smirk_talk at left
        show edw embarrassed at right
        pov "That’s quite the mature way to look at things."
        show pov embarrassed at left
        show edw smirk_talk at right
        edw "Never let failure stop you, dude. Always be willing to grow from it, even if things just crash and explode in your face."
        show pov embarrassed_talk at left
        show edw neutral at right
        pov "I’ll take good care of it and get it done, I promise."
        show pov embarrassed at left
        show edw embarrassed_talk at right
        edw "Thanks, man, this is a huge relief."
        show pov confused_talk at left
        show edw confused at right
        pov "How is the camera setup going on, by the way?"
        show pov confused at left
        show edw neutral_talk at right
        edw "Everything is set up properly and ready to start recording!"
        show pov shocked at left
        show edw shocked_talk at right
        edw "I’ll be keeping an eye on it. The motion trackers will alert me if anything shows up in the middle of the night, and I’ll call you once I find anything interesting."
        show pov confused at left
        show edw confused_talk at right
        edw "I’ll be deleting any useless footage from quiet nights though. Don’t want to be caught with hours of footage of all night surveillance if things go super sour and someone finds my gear."
        show pov shocked_talk at left
        show edw confused at right
        pov "That’s fair enough."
        show pov neutral_talk at left
        show edw confused at right
        pov "Alright, keep me posted."
        show pov shocked at left
        show edw smirk_talk at right
        edw "What exactly do you hope to catch on camera?"
        show pov embarrassed at left
        show edw embarrassed_talk at right
        edw "I know I said I wouldn’t ask, but after setting things up and everything I can’t help but be curious."
        show edw smirk_talk at right
        edw "Is it a gang? Drugs? Ghosts?"
        show pov embarrassed_talk at left
        show edw confused at right
        pov "I really don’t wanna say without any evidence."
        show pov smirk_talk at left
        show edw confused at right
        pov "Trust me on this, dude."
        pov "You’ll know it when you see it."
        show pov embarrassed at left
        show edw confused_talk at right
        edw "Because that isn’t in any way cryptic or anything."
        show edw smirk_talk at right
        edw "You are lucky I’m a fan of mystery."
        show edw bored_talk at right
        edw "That been said though, if I end up haunted or cursed by a ghost or specter,  I’m getting super pissed at you."
        show pov embarrassed_talk at left
        show edw confused at right
        pov "Let’s hope that doesn’t happen."
        show edw neutral at right
        pov "I better get going now. See you later."
        show pov embarrassed at left
        show edw neutral_talk at right
        edw "Good luck on your first day, dude!"
        show pov embarrassed_talk at left
        show edw neutral at right
        pov "Oh, and please keep the fact I’m working there a secret, okay?"
        show pov neutral_talk at left
        pov "Don’t need more attention on me than what I already have."
        show pov embarrassed at left
        show edw smirk_talk at right
        edw "Lips are sealed dude, no worries!"
        show pov neutral_talk at left
        show edw smirk at right
        pov "Good. Thank you. Alright, see you later, dude."
        show pov smirk at left
        show edw neutral_talk at right
        edw "Keep me posted on things!"
        show pov neutral_talk at left
        show edw neutral at right
        pov "Same thing to you!"

        $ main_story = 89
    elif main_story == 87:
        pov "{i}I should find out from [missus] exactly when I start the internship before I go and make and plans with Edward.{/i}"

    #=SCENE END=
    jump lbl_schoolyard_day_setup

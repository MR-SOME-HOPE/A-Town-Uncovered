#[Living room, Afternoon - “[missus]’s Help"  - main_story =88]

#-In this scene the player has to talk to Missus regarding the Internship, a new option is available in her dialogue to talk about the internship-
label lbl_moms_help:
    scene bg mylivingroom_day with fade
    show pov neutral at left with dissolve
    show mum neutral at right with dissolve
    show pov neutral at left
    show mum neutral at right

    if main_story == 87:
        show pov neutral_talk at left
        show mum neutral at right
        pov "Hey, have you heard any news from the old man about when he is expecting me to show up for my first day?"
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Sorry, [povname], we didn’t really discuss when’s the day for you to start your internship."
        show mum sad_talk at right
        mum "We got a bit sidetracked in the discussion once I brought up the whole security system thing."
        mum "That and the whole issue of him being for the most part gone everyday now."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "At the very least it seemed like you managed to keep things civil."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "A large amount of trying and remembering my online mediation classes."
        show mum sad_talk at right
        mum "At one point I wanted to just hit him upside the head with a meat tenderizer to see if that would rearrange the gray slob he calls a brain."
        show mum embarrassed_talk at right
        mum "Thankfully it didn’t escalate to that point."
        show pov sad_talk at left
        show mum embarrassed at right
        pov "No kidding, best if you leave me to be the one of us with trouble regarding the police."
        show pov embarrassed_talk at left
        pov "Can’t think of a way to save you out of that one, but I’ll at least help hide the body if you want."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "Sweet of you to say, I may just keep it in mind if things continue this way."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "So you were serious when you mentioned the divorce thing, huh?"
        show pov confused at left
        show mum embarrassed_talk at right
        mum "{i}*Sigh*{/i}"
        mum "At this point I’m not sure if I was being 100%% serious or just using it to scare him into behaving himself."
        show pov bored at left
        show mum embarrassed_talk at right
        mum "The fact that I even have it as an option on the table, no matter how far or close it is, should be enough to get it through him how serious things are."
        show mum angry_talk at right
        mum "And yet that egoist basta-"
        show pov shocked at left
        show mum shocked_talk at right
        mum "Erm… T-That egoist man… Has the audacity to try and lure me into bed as if that was supposed to solve anything!"
        show pov confused_talk at left
        show mum embarrassed at right
        pov "You didn’t actually…"
        show pov confused at left
        show mum embarrassed_talk at right
        mum "Of course not, [povname]. I was way too upset to stand his lying and excuses, there was no way in hell he would be getting any from me."
        show mum sad_talk at right
        mum "The fact he tried to begin with only made the discussion an extra 2 hours longer until he just left to spend the night at the office."
        show mum embarrassed_talk at right
        mum "The man must have a full on apartment there with how often he stays there at this point or something."
        show pov bored_talk at left
        show mum embarrassed at right
        pov "Please don’t ask me to look for it once I’m working there."
        show pov bored at left
        show mum embarrassed_talk at right
        mum "No, no, nothing of the sort."
        show mum sad_talk at right
        mum "I do want to talk to you about this whole thing, though."
        show pov smirk_talk at left
        show mum sad at right
        pov "You do?"
        show pov smirk at left
        show mum embarrassed_talk at right
        mum "It’s true what your father said regarding the fact that this is a really good opportunity for you."
        show mum sad_talk at right
        mum "But I still feel guilty over having to force you to do it in the first place."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "It’s alright, [missus], really."
        pov "Besides, I can back out of it if he starts being a dick about it like you said, right?"
        show pov embarrassed at left
        show mum sad_talk at right
        mum "Right…"
        show mum embarrassed_talk at right
        mum "But let me know if it starts affecting your studies in any way."
        show pov confused_talk at left
        show mum embarrassed at right
        pov "Sure thing, though I still fail to find the logic in him telling me to focus on studies only for him to pull me into the workforce, even if it affects my studying."
        show pov confused at left
        show mum bored_talk at right
        mum "Don’t dwell on it too much, if there is something I’ve learned while in the middle of arguing, is that the man is more concerned with staring at my breasts than making any sense."
        show pov bored at left
        show mum embarrassed_talk at right
        mum "Still, I can give him a call and ask when you can begin whenever you feel ready."
        mum "I made sure he doesn't pressure you into this more than he already has done."
        show pov neutral at left
        show mum neutral_talk at right
        mum "So if you think you are done with anything important you are doing right now, we can get you started as soon as he lets me know."
        show mum embarrassed_talk at right
        mum "I can always stall him for a bit more time and he is not in the position to demand anything from us, so if you have something important to do, best focus on that for now."
        mum "I don’t want you to get into this whole thing with your father while you have other stuff lurking in the back of your head."
        show pov neutral_talk at left
        show mum neutral at right
        pov "I know, thanks for going the extra mile for me."
        show pov neutral at left
        show mum embarrassed_talk at right
        mum "Of course, darling."
        show pov embarrassed_talk at left
        show mum neutral at right
        mum "Don’t even mention it."

        $ main_story = 88

    show pov neutral at left
    show mum neutral_talk at right
    mum "So, are you ready to start now?"

    if main_story == 88:

        pov "{i}I should check in with Edward before I commit to anything.{/i}"
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "No, I still have some stuff to do"
        show pov embarrassed at left
        show mum neutral_talk at right
        mum "Alright honey, be sure to get your things in order then as soon as you can."
        show mum bored_talk at right
        mum "I may be keeping him in line, but you know how your father has been behaving lately."
        show mum embarrassed_talk at right
        mum "Best not to keep him waiting for too long."
        show pov neutral_talk at left
        show mum embarrassed at right
        pov "Of course, [missus]."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Thanks again for all of this."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Again, don’t even mention it, honey."
        show mum embarrassed_talk at right
        mum "It’s only natural I take care of you."
        show mum neutral_talk at right
        pov "Let me know when you are ready to begin!"

    elif main_story == 89:
        show pov neutral_talk at left
        show mum neutral at right
        pov "Yeah, I’m ready now."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Excellent!"
        mum "Let me give him a call and I’ll sort out the details."
        show mum embarrassed_talk at right
        mum "Knowing him, he is going to try and get you to start as soon as possible."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Guess I’ll be having my next few afternoons filled up."
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "I know it’s a lot to suddenly drop on you, but think of it in a positive way!"
        show mum neutral_talk at right
        mum "An internship in The Robotics Company is bound to look good in your curriculum for the future."
        mum "Even if it's just a half-time or temporary one."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "I guess you have a point there…"

    #-Once this option has been picked, the next time the player talks to Missus, the option to start the internship will appear and the dialogue in that option will be the same as in the “Yeah, I’m ready now” option-

    #-The scene fades out and then back in to indicate the passage of time-
        scene black
        with fade
        $ renpy.pause()
        "After listening to Mom argue with Dad..."
        scene bg mylivingroom_day
        with fade
        show pov neutral at left
        with dissolve
        show mum neutral_talk at right
        with dissolve
        mum "Well, a bit of an argument aside, things went well!"
        mum "You’ll be starting on the next working day, after school hours."
        mum "You know where the company building is, right?"
        show mum embarrassed_talk at right
        mum "I couldn’t convince your dad to come pick you up, so you are going to have to walk there."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "It’s better this way, [missus]."
        show pov smirk_talk at left
        pov "Last thing I need is for him to be talking shit about me in front of other people."
        show pov smirk at left
        show mum shocked_talk at right
        mum "Language!"
        show mum embarrassed_talk at right
        mum "But I guess you have a point…"
        mum "He is going to be waiting for you in front of the building, so try to not take too long."
        show mum bored_talk at right
        mum "We don’t want him to lose his patience."
        show pov neutral_talk at left
        show mum neutral at right
        pov "Got it."
        show pov smirk_talk at left
        show mum shocked at right
        pov "But I’m sure he is going to be waiting for the opportunity to talk down to me in front of his colleagues."
        show pov smirk at left
        show mum bored_talk at right
        mum "I’ll make him behave, don’t worry."
        show mum angry_talk at right
        mum "But if that does ever happen, you tell me straight away and I’ll make him regret waking up that morning."
        show pov neutral_talk at left
        show mum sad at right
        pov "I will."
        show pov neutral at left
        show mum embarrassed_talk at right
        mum "You know…"
        mum "Despite this supposedly being a punishment and it being dropped out of nowhere on you, I can’t help but be a little bit proud that you are taking your first steps into a proper workplace environment."
        show mum sad_talk at right
        mum "I get a bit teary-eyed even thinking how much you are growing up since we moved here."
        show pov embarrassed_talk at left
        show mum sad at right
        pov "I wish it was under better circumstances though…"
        show pov sad at left
        show mum embarrassed_talk at right
        mum "Always try to make the most out of a bad situation, [povname]."
        show mum sad_talk at right
        mum "There is nowhere left to go but up once you hit rock bottom, right?"
        show pov neutral at left
        show mum embarrassed_talk at right
        mum "So make sure to get back up with an impulse and good attitude, and who knows how much higher you’ll soar!"
        show mum neutral_talk at right
        mum "I believe in you, so I know you’ll turn this into something great!"
        show pov neutral_talk at left
        show mum neutral at right
        pov "Thanks, [missus]."
        pov "You always know how to keep me going."
        show pov neutral at left
        show mum embarrassed_talk at right
        mum "It’s my job, silly!"
        mum "I’ll always be there for you whenever you need me."
        mum "Even if I’m not there."
        show mum neutral_talk at right
        mum "Now, take a moment to relax; seeing as this may be one of your last free afternoons off for a while."
        show pov embarrassed_talk at left
        show mum neutral at right
        pov "I think I’ll do that, See you later, [missus]."
        show pov neutral at left
        show mum neutral_talk at right
        mum "Don’t stay out after dark too long if you go out though!"
        show pov neutral_talk at left
        show mum neutral at right
        pov "I know, I know."

        $ main_story = 90

    jump lbl_mylivingroom_day

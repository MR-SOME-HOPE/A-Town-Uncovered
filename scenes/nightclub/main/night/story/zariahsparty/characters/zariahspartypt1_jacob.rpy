## JACOB
label lbl_zariahs_party_jacob:
    show pov neutral at left
    with dissolve
    show jac neutral at right
    hide btn zariahs_party_jacob_idle
    with dissolve

    if zarias_party_jacob_start == 1:
        jump zarias_party_start_choice
    elif zarias_party_jacob_start == 2:
        if not 0 in (zariahs_party_talking_phil,zariahs_party_talking_edward_and_zariah,
        zariahs_party_talking_luna_and_cole,zariahs_party_talking_ian_and_teghan,
        zariahs_party_talking_vip,zariahs_party_talking_steve):
            jump lbl_zariahs_party_pt2
        show jac smirk_talk at right
        jac "Let's get this party rolling!"
        jump lbl_nightclub_zariahs_party_setup
    else:
        show pov shocked at left
        show jac smirk_talk at right
        jac "Dude!"
        jac "About time you got here!"
        show pov embarrassed_talk at left
        show jac smirk at right
        pov "I know, I know."
        show pov smirk_talk at left
        show jac embarrassed at right
        pov "How you holding up?"
        pov "Cause you look like you are about to throw up."
        show pov smirk at left
        show jac embarrassed_talk at right
        jac "Describes how I feel just about right…"
        show pov smirk_talk at left
        show jac embarrassed at right
        pov "Where did all the confidence from before go?"
        show pov bored at left
        show jac bored_talk at right
        jac "Down the drain along with my lunch a few minutes ago."
        show pov bored_talk at left
        show jac smirk at right
        pov "Gross."
        show pov smirk at left
        show jac shocked_talk at right
        jac "I’m just nervous dude!"
        show pov bored at left
        show jac confused_talk at right
        jac "I mean, what if the whole plan doesn’t work?!"
        show pov smirk_talk at left
        show jac sad at right
        pov "Dude, relax."
        pov "I think you just made all of this way bigger than it needed to be."
        show pov smirk at left
        show jac confused_talk at right
        jac "What do you mean?"
        show pov shocked_talk at left
        show jac confused at right
        pov "Dude, you planned a whole life with a girl you don’t even know the name of and are now panicking because of it."
        show pov smirk_talk at left
        pov "Maybe you should have focused a little bit more on just having a regular conversation first?"
        show pov shocked at left
        show jac bored_talk at right
        jac "Okay, no need to be a wiseguy about it either."
        show pov bored_talk at left
        show jac bored at right
        pov "What happened to that famous line that managed to get a girl to laugh at the mall that you were telling me about?"
        show pov bored at left
        show jac bored_talk at right
        jac "Well that’s just it, dude."
        jac "What do I do after I say the line?!"
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "Just relax and be yourself, no need to be all dramatic about this."
        show pov embarrassed at left
        show jac angry_talk at right
        jac "What kind of advice is that?!"
        show pov bored_talk at left
        show jac angry at right
        pov "Realistic one?"
        show pov smirk_talk at left
        show jac bored at right
        pov "Dude, chances are you aren’t even gonna see this girl again after the party is over."
        show pov embarrassed_talk at left
        pov "So just give it your best shot and let's see what happens."
        show pov neutral_talk at left
        show jac sad at right
        pov "It’s not the end of the world if she doesn’t want what you are offering, you know?"
        show pov embarrassed at left
        show jac sad_talk at right
        jac "Well…"
        jac "I suppose you are right…"
        show pov smirk at left
        show jac confused_talk at right
        jac "Perhaps Tristan and Nora will just have to wait a while longer."
        show pov embarrassed_talk at left
        show jac confused at right
        pov "Hey, they’ve been waiting this long, what’s some additional time to it?"
        pov "It’s not like they can complain right now."
        show pov embarrassed at left
        show jac bored_talk at right
        jac "Alright, fair point there."
        show jac smirk_talk at right
        jac "Okay! I’m back to feeling motivated!"
        show pov neutral at left
        show jac neutral_talk  at right
        jac "Thanks, man. You are a good wingman so far!"
        show pov neutral_talk at left
        show jac smirk at right
        pov "Not a problem, dude."
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "Alright, if you are feeling ready for it then we can begin to discuss our plan of action."
        jac "Violette’s friends are currently in the bathroom and last I saw of Violette she was going into the VIP room with Hazel where there was less noise."
        show pov neutral at left
        show jac neutral_talk at right
        jac "So we are gonna have to introduce ourselves to them once the party starts."
        show pov neutral_talk at left
        show jac smirk at right
        pov "Alright, what’s the plan?"
        show pov confused at left
        show jac smirk_talk at right
        jac "Well, right now I’m about to give you a summary of my plan and then we can discuss what you are going to say to the friend."
        jac "Just keep her busy and wait for my signal and if things go south for you, find another way to distract her."
        show pov embarrassed_talk at left
        show jac smirk at right
        pov "Doesn’t sound so difficult."
        show pov confused at left
        show jac smirk_talk at right
        jac "On paper everything sounds easier, dude."
        jac "But right now we gotta go over a few wingman’s rules found in our sacred bro code."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Along with the ever sacred wingman’s oath."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Are you serious right now?"
        show pov confused at left
        show jac smirk_talk at right
        jac "Very!"
        show pov shocked at left
        show jac neutral_talk at right
        jac "I need to know 100%% that you have my back and oaths on the bro code are unbreakable as stated by bro code law."
        jac "It’s gonna take a while to go over it all and we are not making our move until the party starts."
        show pov bored at left
        show jac bored_talk at right
        jac "I need your undivided attention on this so if you wanna hang out a bit more before we prepare to strike, now’s the time to tell me so that I can gather some more courage here."
        show pov shocked_talk at left
        show jac confused at right
        pov "What did I just tell you about making things bigger than they need to be?!"
        show pov bored at left
        show jac bored_talk at right
        jac "I know, I know. But I wanna make sure that all bases are covered here with lady luck!"
        show jac smirk_talk at right
        jac "Come on, it’s important for me and will help psyche me up for what’s coming."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "So, are you ready for this, yet?"
        jump zarias_party_start_choice

    menu zarias_party_start_choice:
        "Yes. Let’s do this.":
            #-If “Yes. Let’s do this.” was picked-
            show pov smirk at left
            show jac neutral_talk at right
            jac "Alright!"
            show pov bored at left
            show jac shocked_talk at right
            jac "First things first is reciting the oath of the wingman over the bro code."
            show pov embarrassed at left
            show jac smirk_talk at right
            jac "Since I couldn’t bring my official copy, the pocket edition will have to do."
            show pov embarrassed_talk at left
            show jac smirk at right
            pov "Oh boy…"
            $ zarias_party_jacob_start = 2
            $ at_zarias_party_currently_phil = 1
            $ at_zarias_party_currently_jacob = 1
            $ at_zarias_party_currently_edward = 1
            $ at_zarias_party_currently_luna_and_cole = 1
            $ at_zarias_party_currently_ian_and_teghan = 1
            $ at_zarias_party_currently_edward_and_zariah = 1
            #=SCENE END=

            #-Screen fades to black and transitions to the next scene-

            #=RESULT END=
        "Give me some time.":
            #-If “Give me some time” was picked-
            show pov embarrassed_talk at left
            show jac confused at right
            pov "Give me a bit more time."
            pov "I haven’t really hung out a bit with everyone and want to at least say hi before we commit our focus to this whole thing."
            show pov embarrassed at left
            show jac embarrassed_talk at right
            jac "Smart move, it’s gonna be an awesome party so best to at least try to greet everyone you can so people remember you were there."
            show jac neutral_talk at right
            jac "Alright dude, just let me know where you are ready."
            show pov embarrassed at left
            show jac confused_talk at right
            jac "I’ll be here thinking about what I’ll say to her when we meet."
            show pov embarrassed_talk at left
            show jac smirk at right
            pov "Alright dude, I’ll be right back."
            $ zarias_party_jacob_start = 1
            #-Conversation ends and Mc is back in the menu to select who to talk to next-

            #=RESULT END=

            #-Next time the player clicks on Jacob, a prompt will ask them if they are ready to move on with the party, if they choose yes, then we transition to the next scene-

            #=RESULT END=
    jump lbl_nightclub_zariahs_party_setup

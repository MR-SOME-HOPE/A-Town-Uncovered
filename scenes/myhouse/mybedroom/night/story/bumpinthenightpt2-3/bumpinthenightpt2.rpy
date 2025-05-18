## Bump in the Night Pt 2
label lbl_bump_in_the_night_pt2:
    default bumpinthenight_askabouttown = 0
    ## Continuation of bg bumpinthenight_x when he's at his desk pondering

    ###scene bg bumpinthenight_temp5
    ##scene bg bumpinthenight_5
    pov "Maybe I should-"
    "{i}*Knock knock knock*{/i}"
    dad "[povname]?"
    dad "What's with the noise?"
    pov "Y-Yeah, Dad! Just checking on some coursework!"
    dad "Who are you talking to?"

    menu:
        "Just memorizing lines for a project.":
            pov "N-No one! Just trying to memorize some lines for a project!"
            pov "You know how it is, with presentations and all."
        "I'm in a call.":
            pov "I’m in a call with my friend!"
            pov "We’re doing work together to get it done quicker."
        "To myself...":
            pov "To… myself? I think out loud."
            pov "Don’t judge, everyone does it."

    dad "Right."
    dad "Well, knock knock, I’m coming in."
    if winc == 0:
        dad "Your [mumrole] is worried and she sent me something for you to eat."
    else:
        dad "Your mother is worried and she sent me something for you to eat."
    dad "Here."

    ## Start refer to bg bumpinthenight2_x

    #"He hands you a sandwich, puts it on the desk"
    ##show bg bumpinthenight2_temp1
    scene bg bumpinthenight2_1 with fade

    menu:
        "Sure.":
            pov "S-Sure."
            pov "Thanks."
        "Yum.":
            pov "Oooh yum!"
            pov "Thanks, Dad."
        "Thank [missus] for me." if winc == 0:
            pov "Cool, thank [missus] for me."
            pov "I’ll eat it in a bit."
        "Thank Mom for me." if winc == 1:
            pov "Cool, thank [missus] for me."
            pov "I’ll eat it in a bit."

    ##"The two of you share a moment of awkward silence; as your [dadrole] stays still in the room, now looking out the window, trying to come up with what to say."
    ##show bg bumpinthenight2_temp2
    scene bg bumpinthenight2_2-2_backfacing with fade
    dad "..."
    dad "S-So…"
    if winc == 0:
        dad "Your [mumrole] told me you’ve been acting weird lately."
    else:
        dad "Your mother told me you’ve been acting weird lately."
    dad "And... {i}*Sigh*{/i} ...asked me to talk to you."
    dad "She figured it was a guy thing, eating you up. So she wanted us to have a man to man talk, and all that."

    if themotherobstacle_complain == 0:
        dad "Then again, as much as she assured me that she got you to tell her when you felt ready, you know she isn’t going to sleep well until she has some clue about what’s going on."
        if winc == 0:
            dad "You know how your [mumrole] is."
        else:
            dad "You know how your mother is."
        dad "She always wants the game played her way, so do us a favour and let's cut to the chase."
        dad "I don't wanna be here any more than you want me to."
        pov "Y-Yeah, no kidding."
        pov "You don’t have to explain it to me."

    dad "So, what the hell's going on with you?"
    pov "Nothing you need to worry about."
    pov "Just going through some teenager stuff."
    dad "Cut the bullshit and give me a straight answer, like a man."
    pov "You lost me? What are you talking about?"

    ##"Your father turns around and looks at you, but still close to the window."
    ##show bg bumpinthenight2_temp3
    scene bg bumpinthenight2_2-2_angry_talk with dissolve

    dad "According to them, it's the public nudity, the out past your curfew, acting strange every time someone asks you a question."
    scene bg bumpinthenight2_2-2_confused_talk
    dad "You're not like yourself."
    scene bg bumpinthenight2_2-2_sad_talk
    if winc == 0:
        dad "All of those things add up, and got your [povmumrole] and [sisrole] pretty worried about you and your sanity."
        scene bg bumpinthenight2_2-2_angry_talk
        dad "So quit acting like a child and tell me what’s wrong. This is your last chance to come clean before your [mumrole] freaks out and starts downright stalking your every move."
    else:
        dad "All of those things add up, and got your mother and sister pretty worried about you and your sanity."
        scene bg bumpinthenight2_2-2_angry_talk
        dad "So quit acting like a child and tell me what’s wrong. This is your last chance to come clean before your mother freaks out and starts downright stalking your every move."
    scene bg bumpinthenight2_2-2_bored_talk
    dad "But look, if you don't want to tell me, I get it. I'm trying to make an effort and you're just making it harder for everybody."
    scene bg bumpinthenight2_2-2_bored
    pov "I’ve got nothing to hide!"
    pov "I just had a bad start to the week. Why can’t anyone get that?!"
    scene bg bumpinthenight2_2-2_angry
    dad "..."
    scene bg bumpinthenight2_2-2_angry_talk
    dad "Tch- how typical of you."
    scene bg bumpinthenight2_2-2_angry
    pov "Y-Yeah, how fucking typical of me for being human."
    scene bg bumpinthenight2_2-2_shocked
    dad "…"
    scene bg bumpinthenight2_2-2_neutral_talk
    dad "Alright."
    ##show bg bumpinthenight2_temp2
    scene bg bumpinthenight2_2-2_backfacing with dissolve
    dad "Well, if that's all your issues are, then I guess I'll be on my way."
    dad "Unless there's something you're keeping from me?"
    pov "What do you mean?"
    dad "Anything eating you up: regrets, mistakes, bad decisions?"
    dad "Something you may want to let off of your chest?"
    if winc == 0:
        dad "[missus] told me to ask."
    else:
        dad "Your [mumrole] told me to ask."
    pov "W-Well-"
    pov "..."

    # The following occur in MC's head (usually when quotes starts and ends with {i} and {/i} except when its a sound effect like a *Sigh*)

    pov "{i}Can I really trust him with anything?{/i}"
    pov "{i}He has been acting strange ever since we got here and now he is suddenly concerned about how I’m doing?{/i}"
    pov "{i}I mean- still. He's not doing a very good job at it but-?{/i}"
    if winc == 0:
        pov "{i}Just because [missus] told him to?{/i}"
    else:
        pov "{i}Just because [missus] told him to?{/i}"

    if sister_path <= 25:
        if bathwithmom_eyereveal == 1:
            if winc == 0:
                pov "{i}The piece of shit dared to hit [missus] after I interrupted them last time.{/i}"
                pov "{i}I am clearly not on his good side and he is about to leave that whole grudge behind just because [missus] asked him to?{/i}"
                pov "{i}That doesn’t sound like him at all.{/i}"
                pov "{i}At least not this new him!{/i}"
                pov "{i}I doubt [missus] even welcomes him home anymore.{/i}"
                pov "{i}Why the fuck is he in my room trying to be a less than decent [dadrole]?{/i}"
            else:
                pov "{i}The piece of shit dared to hit [missus] after I interrupted them last time.{/i}"
                pov "{i}I am clearly not in his good side and he is about to leave that whole grudge behind just because [missus] asked him to?{/i}"
                pov "{i}That doesn’t sound like him at all!{/i}"
                pov "{i}At least not this new him!{/i}"
                pov "{i}I doubt [missus] even welcomes him home anymore.{/i}"
                pov "{i}Why the fuck is he in my room trying to be a less than decent father?{/i}"
        else:
            pass

    elif sister_path >= 26:
        if bathwithmom_eyereveal == 0:
            pov "{i}And hell, how does this absolute cunt even dare to ask me for anything after what he did to the fort?!{/i}"
            pov "{i}It took me forever to fix it and it is going to take me even longer to completely fix all the damage he did to [sister].{/i}"
            pov "{i}I doubt she can even look him in the eye anymore!{/i}"
            pov "{i}I don’t owe him anything, much less an honest answer after that!{/i}"

        elif bathwithmom_eyereveal == 1:
            if winc == 0:
                pov "{i}He has been nothing but an absolute nightmare to the household.{/i}"
                pov "{i}[missus] still comes to sleep in my bed from time to time when they argue and [sister] still drags me down to the fort when she has nightmares about him!{/i}"
            else:
                pov "{i}He has been nothing but an absolute nightmare to the family.{/i}"
                pov "{i}Mom still comes to sleep in my bed from time to time when they argue and [sister] still drags me down to the fort when she has nightmares about him!{/i}"
            pov "{i}Everything he has done so far has made them both miserable.{/i}"
            pov "{i}He struts around the place as if he was hot shit and doesnt care what he breaks or abuses, as long as he makes it clear to us that he has the biggest dick in the room, or something.{/i}"
            pov "{i}Meanwhile, I am down on the ground picking up the pieces of everything he breaks and cleaning up after him.{/i}"
            if winc == 0:
                pov "{i}I don’t even bring the bread to the table and somehow I am the only thing keeping this household together!{/i}"
                pov "{i}I am sure that if it wasn’t for the memories, [missus], [sister] and I would be sipping coconuts somewhere in Hawaii, while this jackass rots in jail for physical and psychological abuse after what he did to them!{/i}"
            else:
                pov "{i}I don’t even bring the bread to the table and somehow I am the only thing keeping this family together!{/i}"
                pov "{i}I am sure that if it wasn’t for the memories, [missus], [sister] and I would be sipping coconuts somewhere in Hawaii, while this jackass rots in jail for physical and psychological abuse, after what he did to them!{/i}"
            pov "{i}And now he thinks he has the right to ask me for anything other than to give him the bird?{/i}"
            pov "{i}Fuck that and fuck him!{/i}"



    pov "..."
    pov "{i}Even so, for all I know, he may have some answers as to what's going on in this town.{/i}"
    pov "{i}I mean, he was the one who got called in for the job, so at the very least they must have told him something to keep his interest, right?{/i}"
    pov "{i}I guess I don’t really lose anything by asking, but do I really want to look even more suspicious around him?{/i}"
    pov "{i}Something tells me that if I keep pushing, he is going to eventually send me to the military or something, just to avoid dealing with me.{/i}"
    if winc == 0:
        pov "{i}God knows what he’d do to [missus] and [sister], without me around, too.{/i}"
    else:
        pov "{i}God knows what he’d do to [missus] and [sister], without me around, too.{/i}"
    pov "{i}Is it really worth the risk?{/i}"

    menu:
        "Keep quiet":
            pov "N-Nothing off the top of my head, no."
            ##show bg bumpinthenight2_temp3
            scene bg bumpinthenight2_2-2_confused_talk with dissolve
            dad "You're sure?"
            scene bg bumpinthenight2_2-2_confused
            pov "Yeah."
            pov "Unless you are in the mood to discuss my assignment or the current state of affairs in the Galaxy Battles movies?"
            scene bg bumpinthenight2_2-2_embarrassed
            pov "Long story short, it is a fantasy genre, not a sci-fi. Just because it has space in it, doesn’t mean it puts the ‘science’ in the ‘fiction’."
            scene bg bumpinthenight2_2-2_embarrassed_talk
            dad "Yeah-"
            dad "I don't give a shit about that, [povname]."
            scene bg bumpinthenight2_2-2_embarrassed
            pov "I figured."
            scene bg bumpinthenight2_2-2_neutral
            pov "Other than that, I really don’t have anything to say, over all."
            pov "Just usual stuff."
            scene bg bumpinthenight2_2-2_neutral_talk
            dad "Right."
            dad "Well, just making sure."
            if winc == 0:
                dad "Eat your sandwich and get in bed early. I don’t care what your [mumrole] said, you are not missing any more university."
                scene bg bumpinthenight2_2-2_neutral
                pov "Right."
                pov "Sure, [dadname]."
            else:
                dad "Eat your sandwich and be in bed early. I don’t care what your [mumrole] said, you are not missing any more university."
                scene bg bumpinthenight2_2-2_neutral
                pov "Right."
                pov "Sure, Dad."

        "Ask him about the town":
            $ bumpinthenight_askabouttown = 1
            pov "Dad?"
            pov "Do you happen to know much about the town’s history?"
            dad "That certainly came out of the blue... Why do you ask?"
            pov "W-Well, I’ve been having problems writing for my class project."
            pov "The teacher recommended that I made the project about the town and its history."
            pov "I figured that since they offered you the job over here, they must have given you a tour of the town, at least when you were looking into buying the house, right?"
            pov "At the very least, you might've heard something interesting as a selling point."
            dad "Y-Yeah."
            pov "Well, I was wondering if there is anything you recall from your- research and observation?"
            pov "The typical stuff like; it’s founder, maybe how old the town is, some important events that happened in it?"
            pov "Things like historic battles or festivals of harvest… rituals and ceremonies?"

            #"The last part clearly brings Dad’s attention as he starts to act suspiciously"
            ##show bg bumpinthenight2_temp3
            scene bg bumpinthenight2_2-2_shocked_talk with dissolve

            dad "{i}*Clears throat*{/i} No, definitely not- at least from what I know."
            scene bg bumpinthenight2_2-2_confused_talk
            dad "Don't you have the internet for those sort of questions?"
            scene bg bumpinthenight2_2-2_sad
            pov "Trust me, I've looked; and the Wyky is pretty bare-bones."
            pov "Don’t all small towns have some of those things in common though? Just from an assuming point of view-"
            scene bg bumpinthenight2_2-2_angry_talk
            dad "I said no, [povname]! Get off my back!"
            scene bg bumpinthenight2_2-2_embarrassed_talk
            dad "Look, I'm not here to help with your coursework, okay? I have my own work to catch up on."
            scene bg bumpinthenight2_2-2_neutral_talk
            dad "If the topic is too hard for you, then research something easier!"
            scene bg bumpinthenight2_2-2_smirk_talk
            dad "Like cars or space robots or whatever the hell you kids are into these days!"
            scene bg bumpinthenight2_2-2_bored_talk
            dad "Just make sure to do it yourself and deliver it on time. I am not about to have your ass making up work over summer; ruining the plans!"
            scene bg bumpinthenight2_2-2_bored
            pov "Plans?"
            pov "What plans?"
            scene bg bumpinthenight2_2-2_angry_talk
            if winc == 0:
                dad "T-The household vacation plans!"
            else:
                dad "T-The family vacation plans!"
            dad "It’s my turn to pick, and you are not about to ruin my get-away because you couldn’t deliver your project in time!"
            scene bg bumpinthenight2_2-2_sad_talk
            dad "Now eat your food and get to studying. I want you in bed early!"
            dad "Don’t think you aren’t still in trouble for your little stunt recently!"
            dad "Now stop wasting time and get to work!"

    ## dad leaves the room
    ## goes to the shot of the sandwich
    ##show bg bumpinthenight2_temp1
    scene bg bumpinthenight2_1 with fade
    pov "{i}Well, good to see his dick-ish behaviour is still around.{/i}"
    pov "{i}It still freaks me out.{/i}"
    pov "{i}Back home he wouldn’t have hesitated for a chance to talk to me.{/i}"
    pov "{i}Just what has gotten into him anyway?{/i}"

    if bumpinthenight_askabouttown == 1:
        pov "{i}He definitely knows something.{/i}"
        pov "{i}Why wouldn’t he tell me?{/i}"
        pov "{i}What could he possibly be hiding?{/i}"
        pov "{i}I doubt I’ll be able to get a lot out of him without digging around his stuff, and I am not about to give him more reasons to have me be on his shit list.{/i}"
        pov "{i}Gonna have to wait for the opportunity to do it.{/i}"
        pov "{i}But for now, I am happy to know something is definitely going on around this town.{/i}"

    pov "{i}*Inhale*{/i}"
    pov "{i}*Exhale*{/i}"
    pov "{i}She made my favorite too.{/i}"

    ## CG of MC looking out the window with a sandwich
    #"You take a bite out of the sandwich and look at the closed window"
    ##show bg bumpinthenight2_temp4
    scene bg bumpinthenight2_3-1
    $ renpy.pause(1,hard=True)
    ##show bg bumpinthenight2_temp5
    scene bg bumpinthenight2_3-2
    $ renpy.pause(0.7,hard=True)
    ##show bg bumpinthenight2_temp6
    scene bg bumpinthenight2_3-3
    $ renpy.pause()
    pov "{i}I guess I should rest for today.{/i}"
    pov "{i}I’ll start asking around tomorrow and try not to focus on all the rumors going on about me.{/i}"
    pov "{i}It’s been a long-ass week, with everything going on. And now I just find out I’m also being stalked by a crazy ghost-monster-thing sexy woman and her cum fanatics.{/i}"
    pov "{i}I think I deserve a night or two of just resting and calming myself down.{/i}"

    scene black
    with fade
    $ renpy.pause()
    pov "…"
    pov "{i}What’s the worst that could happen if I take a night off?{/i}"
    $ renpy.pause()
    "The next morning..."
    scene bg mybedroom_day
    with fade

    $ main_story = 50

    $ townmap_enabled = 0

    jump lbl_mybedroom_night_sleep_1

## Bump in the Night Pt 3
label lbl_bump_in_the_night_pt3:
    ## CG Scene Starts
    ## bg bumpinthenight3_x

    scene bg bumpinthenight3_temp1
    ##scene bg bumpinthenight3_1 #TODO
    pov "{i}*Inhale*{/i}"
    pov "{i}*Exhale*{/i}"
    pov "{i}This is stressing me out...{/i}"
    pov "{i}I guess I should rest for today.{/i}"
    pov "{i}I’ll start asking around tomorrow and try to not focused on all the rumors going on about me.{/i}"
    pov "{i}It’s been a long ass week, with everything going on. And now I just found out I’m also being stalked by a crazy ghost-monster-thing sexy woman and her cum fanatics.{/i}"
    pov "{i}I think I deserve a night or two of just resting and calming myself down.{/i}"
    pov "…"
    pov "{i}What’s the worst that could happen if I take a night off?{/i}"

    scene black
    with fade
    $ renpy.pause()
    "The next morning..."
    scene bg mybedroom_day
    with fade

    $ main_story = 50

    $ townmap_enabled = 0

    jump lbl_mybedroom_night_sleep_1

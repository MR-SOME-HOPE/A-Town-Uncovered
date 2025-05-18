## Awkward Hallway Conversations
default mainstory_63b_luna_flirt = 0
default mainstory_63b_zariah_flirt = 0
default mainstory_63b_cole_compliment =0

label lbl_awkward_hallway_conversations:
    image lun confused_talk flip = im.Flip("//assets/character/luna/lun_confused_talk.png", horizontal=True)
    image lun confused flip = im.Flip("//assets/character/luna/lun_confused.png", horizontal=True)
    scene bg schoolhallway1_daytrashed
    show zar shocked flip
    show col confused at right
    with fade
    show zar shocked_talk flip
    zar "Dude, I am telling you."
    zar "Security in the club is through the roof right now thanks to what happened."
    zar "I can’t just get you passes for the VIP area anymore."
    show zar sad flip
    show col sad_talk at right
    col "Aw, come on dude."
    col "Why you gotta do me like this? "
    col "It took me weeks to get those Japanese subwoofers you wanted for your van, now you go and screw me like that?"
    show col confused at right
    show zar angry_talk flip
    zar "Okay, first of all. The “High-Quality” Subwoofers you gave me came with some really faulty wiring that messed up my whole set up and it took me weeks to repair or replace it, I figured you knew that after I chase you for an hour with a baseball bat."
    zar "Second of all, I invited you to the club originally, the vip room was supposed to be a one time thing only, not you taking over a whole booth in there!"
    zar "What do you even do in there?"
    show zar angry flip
    show col sad_talk at right
    col "Damn there, Angel."
    col "Rip my head off while you are at it, won’t you?"
    show col smirk_talk at right
    col "Can you blame a brother for wanting to support his favorite music girl while also being comfortable doing so?"
    show col smirk at right
    show zar angry_talk flip
    zar "Name the title of one of my songs or albums right now."
    show zar smirk flip
    show col confused_talk at right
    col "Uh…"
    col "W-Well, I…"
    show pov confused_talk at left
    with dissolve
    show col confused at right
    pov "Hey guys, am I interrupting anything?"
    show col smirk at right
    show pov confused at left
    show zar confused at Position(xpos=1200) with dissolve
    show col smirk_talk at right
    col "[povname]! Dude, you got here just in time!"
    col "You see Zariah, I was hoping to bring [povname] to see the town’s Dj sensation seeing how he has never seen one of your shows live and all."
    show col smirk at right
    show pov confused_talk at left
    pov "You were hoping to what now?"
    show pov confused at left
    show zar angry_talk flip at center with dissolve
    zar "Don’t go dodging my questions!"
    show zar angry flip
    show col embarrassed_talk
    col "Say, [povname]."
    col "How you handling the whole chaos around town lately?"
    show col smirk_talk at right
    col "Must be a bummer for the local exhibisionist to not be able to run around naked at night anymore seeing as how alert the cops are now."
    show col smirk at right
    show pov embarrassed_talk at left
    pov "Okay, First of all, I don’t think that should be what we should be focusing on and-"
    show pov embarrassed at left
    show zar angry_talk flip
    zar "Leave him alone, Cole!"
    show zar neutral_talk flip
    zar "The dude is being true to himself regardless of what people say of him, if I have learned anything from listening to early 2000’s rock growing up, is to respect the hell of people who do that sort of thing."
    show zar neutral_talk at Position(xpos=1200) with dissolve
    zar "Mad respect, bro."
    show pov confused at left
    show col confused at right
    show zar confused at Position(xpos=1300)
    show lun smirk_talk at Position(xpos=800) with dissolve
    lun "Plus, the pictures of his penis are nice."
    show lun smirk
    show col shocked_talk at right
    col "JESUS CHRIST!"
    show col shocked at right
    show zar angry_talk at Position(xpos=1300)
    zar "Luna, don’t just sneak up on people like that after someone got kidnapped!"
    show lun confused_talk flip at Position(xpos=700) with dissolve
    show zar angry
    lun "You misunderstand, I was here all along."
    show zar confused
    show lun confused flip
    show col angry_talk
    col "Where?!"
    col "Inside the goddamned walls?!"
    show col sad_talk at right
    col "Girl, you almost make me have a heart attack, I am too cool to die so young!"
    show col sad at right
    show pov confused_talk
    pov "You do this often?"
    show lun smirk_talk at Position(xpos=800) with dissolve
    lun "People don’t tend to notice my presence until I speak."
    show lun smirk
    show pov embarrassed_talk
    pov "Oh, um…"
    pov "Sorry, I didn’t mean to make it sound rude or anything."
    show pov embarrassed
    show lun neutral_talk
    lun "It’s alright."
    lun "I see it as more of a blessing than a curse."
    show lun neutral
    show zar neutral_talk
    zar "She is more talkative nowadays."
    zar "Growing up she barely spoke a sentence when you talked to her."
    zar "Back then she actually caused heart attacks from time to time."
    show zar neutral
    show lun sad_talk
    lun "I am a person of few words, I am working on it though."
    show lun sad
    show pov neutral_talk
    pov "Well, it’s nice to know you are getting better at the whole “Not giving people heart attacks” department."
    show pov neutral
    show lun sad_talk
    lun "Thank you."
    show lun sad
    show col sad_talk
    col "Say that to the irregular beating on my chest!"
    show col sad
    show zar angry_talk
    zar "Don’t be such a baby!"
    show zar neutral
    show pov sad_talk
    pov "Anyway, how are you guys holding up with everything that’s going on."
    show pov sad
    show zar sad_talk
    zar "Oh, you know."
    zar "Trying my best to keep safe and not get fucked over because of it."
    zar "Steven got orders to be more rigorous in security so he is only letting me do half of my shows until this whole thing calms down."
    show zar angry_talk
    zar "Look, I know he is trying to keep me safe and out of trouble but if I cannot drop beats 5 times a week in front of a crowd I get real antsy and in a bad mood."
    show zar angry
    show pov sad_talk
    pov "I guess it’s only natural a place like the club would be hit the hardest by police at a time like this."
    show zar angry_talk
    zar "Doesn’t mean I like it though."
    show zar angry
    show pov neutral_talk
    show zar neutral
    pov "What about you, Luna?"
    pov "You doing okay?"
    show pov neutral
    show lun neutral_talk
    lun "I appreciate your interest and respond accordingly."
    lun "My parents changed the locks back at home and are looking to invest on a new security system."
    lun "They don’t have to worry about me, I am not much of an outside person so I spend most of my time in my room or in my studio."
    show lun neutral
    show col smirk_talk
    col "Practicing the dark arts?"
    show col smirk
    show zar confused_talk
    zar "That's a little culturally insensitive, don't you think, Cole?"
    show zar confused
    show col shocked_talk
    col "I'm sorry- whaat?!"
    show col shocked
    show lun confused flip at Position(xpos=700) with dissolve
    show lun confused_talk flip
    lun "It’s alright, he is not entirely wrong."
    show lun confused flip
    show pov confused_talk
    pov "Okey-dokie, then…"
    show pov confused
    show zar sad_talk
    zar "Still, dude this whole shtick has been messing with my groove, real bad."
    zar "I am sure that the moment I go outside, some dumb rookie cop is going to try and get me to open my van for them, to see if I don’t have anything suspicious on me."
    show zar sad
    show col smirk_talk
    col "Kind of your fault for having a van in the first place."
    show col smirk
    show zar angry_talk flip at center with dissolve
    zar "Okay, you can forget about VIP access if you keep that attitude up, you smartass!"
    show zar angry flip
    show col shocked_talk
    col "Aw, come on, Angel!"
    col "Where's the love?"
    show col shocked
    show lun confused_talk flip
    lun "Isn’t it weird how this whole kidnapping thing started again after [povname] and his family moved in?"
    show lun confused flip
    show zar shocked_talk at Position(xpos=1300) with dissolve
    zar "Luna!"
    show zar shocked
    show col shocked_talk
    col "Come on there, little raven."
    col "I know [povname] can be kind of quirky but he wouldn’t hurt a fly!"
    show col confused_talk
    col "… Right, dude?"
    show col confused
    show pov confused_talk
    pov "Right! I have nothing to do with it!"
    show pov confused
    show lun confused_talk at Position(xpos=800) with dissolve
    lun "It is a weird coincidence though, right?"
    show lun confused
    show pov confused_talk
    pov "Wait, what do you mean this whole thing started again?"
    show pov confused
    show zar neutral_talk
    zar "Oh, right."
    zar "I guess nobody told you after you move in."
    show zar neutral
    show col neutral_talk
    col "To be fair, it's not exactly something that the department of tourism likes having spread around."
    show col neutral
    show lun neutral_talk
    lun "A few years ago people disappearing used to be quite frequent."
    lun "And some record show it used to be something even more frequent even before that."
    lun "Some of the people are found a few days after acting completely different and some are never found at all."
    lun "It hasn’t happened in years however, so it’s really convenient timing that you just happen to move in and be found as a nudist."
    show lun neutral
    show pov shocked_talk
    pov "H-Hey come on, I am innocent!"
    pov "I mean, I am just trying to stop any more rumors from spreading around even further."
    show pov shocked
    show col shocked_talk
    col "Well…"
    show col shocked
    show zar shocked_talk
    zar "Um…"
    show zar shocked
    show pov shocked_talk
    pov "Look, I came here because I wanted to see how you guys were doing."
    pov "I wouldn't want anything to happen to any of you."
    pov "I know I am the outsider and all, but I am trying hard not to be a social outcast, please give me a break."
    show pov neutral
    show zar neutral
    show col neutral
    show lun neutral
    $ add_points("cole_points",1)
    $ add_points("zariah_points",1)
    $ add_points("luna_points",1)
    show col neutral_talk
    col "Aw shucks…"
    show col neutral
    show zar neutral_talk
    zar "Sorry about that, [povname]."
    zar "You are right, we shouldn’t be piling against you like that without any proof."
    show zar neutral
    show lun sad_talk
    lun "I am sorry…"
    lun "I tend to speak my mind more than what I mean to, sometimes."
    show lun sad
    show pov neutral_talk
    pov "It’s alright, Luna."
    pov "I guess, I am bound to stand out, after getting found naked by the lake, and all."

    #-If the player has a charisma of 15 or higher-
    if skill_cha >= 15:
        show pov smirk_talk
        pov "Plus, it’s nice to know a pretty girl like you has me in her thoughts."

        #+3 to Luna, +1 to Zariah.
        $ add_points("zariah_points",1)
        $ add_points("luna_points",3)

        lun "I-I, um…"
        lun "Uh…"
        zar "Damn, aren’t you smooth?"
        col "That’s my man for you!"
        col "The Silver Tongued Nudist!"

        $ mainstory_63b_luna_flirt = 1

        if skill_cha >= 18:

            pov "I am still saving my best lines for you, Zariah."
            pov "But what’s the point of flirting with an angel unless the mood is right?"

            #+2 to Zariah, +1 to Cole.
            $ add_points("zariah_points",2)
            $ add_points("cole_points",1)

            zar "I-I-I’m..."
            zar "A-An Angel, you say?"
            col "And he does it Again! "
            col "Damn, my bro is on fire tonight!"
            col "'Muy Caliente' as they say down the border!"

            $ mainstory_63b_zariah_flirt = 1

            if skill_cha >= 20:
                pov "What can I say? You get me all inspired."
                pov "No one does it better than the master right?"

                #+2 to Cole
                $ add_points("cole_points",2)

                col "…"
                col "Aw shucks, now you are just bragging man!"
                col "I still appreciate though, up top!"

                $ mainstory_63b_cole_compliment = 1

                #=END#=
    show pov neutral_talk
    pov "Anyway, you guys wouldn’t happen to know who is starting the rumors, right?"
    pov "I want to stop it before things get out of control."
    show pov neutral
    show col neutral_talk
    col "Don’t sweat it, playa!"
    col "I’ll make sure to spread it around my connections, that you are on A-OK dude."
    col "Least I can do, for getting you all wrong like that."
    show col neutral
    show zar neutral_talk
    zar "Same here."
    zar "It isn’t fair for them to create nonsense about you just because they caught you following your passion."
    zar "I’ll be sure to get the guys in my area to stop."
    show zar neutral

    #-If you successfully flirted with Zariah-
    if mainstory_63b_zariah_flirt:
        show zar smirk_talk
        zar "A-And I’ll see about getting you into the VIP room to watch me live, too…"
        show zar smirk
    show lun sad_talk
    lun "I’ll keep an ear out for any nasty rumors."
    lun "I am used to people creating rumors about me behind my back, and I know it sucks. I am sorry for almost believing them."
    show lun sad

        #-If you successfully flirted with Luna-
    if mainstory_63b_luna_flirt:
        show lun smirk_talk
        lun "A-Also no one has called me p-pretty before so you get a freebie…"
        show lun smirk
    show pov neutral_talk
    pov "Thanks you guys, I really appreciate it."
    pov "Well, I better get going before they worry back at home."
    pov "See you all later!"
    show pov neutral
    show col neutral_talk
    col "For sure, man. See you around!"
    show col neutral
    show zar neutral_talk
    zar "Be careful on your way home, bro."
    show zar neutral
    show lun neutral_talk
    lun "I’ll see you sooner than you’ll see me."
    show lun neutral
    show col smirk_talk
    col "Keep working on your goodbyes, kiddo."

    $ main_story = 64.1
    $ mainstory_62_crossroads_stay = 1

    jump lbl_an_unexpected_return

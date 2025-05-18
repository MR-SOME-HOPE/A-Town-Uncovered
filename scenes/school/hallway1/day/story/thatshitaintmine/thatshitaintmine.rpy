label lbl_that_shit_aint_mine:
    ###if principallashley_path == 4 and gtime == 0
    default mc_opened_locker = False
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."

    scene bg thatshitaintmine_closed
    with fade
    show pov neutral at left
    with dissolve
    show zar confused_talk at right
    with dissolve
    zar "Hey, [povname]?"
    show pov neutral_talk at left
    show zar confused at right
    pov "Morning, Zariah."
    show pov neutral_talk at left
    show zar confused at right
    pov "How’s it going?"
    show pov neutral at left
    show zar confused_talk at right
    zar "Yeah, it’s all good, um…"
    zar "Listen, you got a minute?"
    zar "It’s important."
    show pov confused_talk at left
    show zar confused at right
    pov "Sure, is something wrong?"
    show pov confused at left
    show zar sad_talk at right
    zar "Sort of."
    zar "Don’t open your locker."
    show pov confused_talk at left
    show zar sad at right
    pov "What? Why not?"
    show pov confused at left
    show zar sad_talk at right
    zar "I saw some guy break into it and sneak some stuff in."
    show pov shocked_talk at left
    show zar sad at right
    pov "What?! When did that happened?"
    show pov shocked at left
    show zar sad_talk at right
    zar "Earlier this morning, when the university had just opened up."
    show pov confused_talk at left
    show zar sad at right
    pov "You were here that early?"
    show pov confused at left
    show zar angry_talk at right
    zar "I sometimes sleep in my van after a rave gone too long, okay? That’s not important right now."
    show zar confused_talk at right
    zar "Anyway, I came in to brush my teeth, and when I got out I saw someone sneaking around in your open locker and stacking something inside."
    show zar confused_talk at right
    zar "I yelled, asking what was he doing, but he got away before I could say something or see his face."
    show pov neutral_talk at left
    show zar confused at right
    pov "Well, thank you for trying, anyway. And for letting me know."
    show pov neutral at left
    show zar confused_talk at right
    zar "No problem, dude. So, what are you going to do?"
    show pov confused_talk at left
    show zar confused at right
    pov "I dunno. Should I call someone, or something?"
    show pov confused at left
    show zar confused_talk at right
    zar "I mean, I doubt it's anything dangerous, but prank season can be year round too."
    show pov confused_talk at left
    show zar sad at right
    pov "You think I’m getting pranked?"
    show pov sad at left
    show zar sad_talk at right
    zar "Well, you are the new kid, after all."
    zar "Fresh blood, ripe for the picking, by the jerks around."
    show pov confused_talk at left
    show zar sad at right
    pov "Speaking from experience?"
    show pov confused at left
    show zar angry_talk at right
    zar "Jackass jammed a potato the size of your fist on my exhaust pipe. Had to replace the whole thing and got charged extra for internal damage to the motor - not to mention the fees of the tow truck."
    show pov shocked_talk at left
    show zar sad at right
    pov "Dang."
    show pov shocked at left
    show zar angry_talk at right
    zar "It took three dudes and Jaiden to get me off the guy. He is lucky I didn’t have a mic stand or a baseball bat on me at that moment, or he would have stayed an extra month in bandages."
    show pov smirk_talk at left
    show zar angry at right
    pov "Never mess with a girl and her Van, I guess."
    show pov smirk at left
    show zar neutral_talk at right
    zar "See? That’s why I like you, [povname]."
    show pov neutral at left
    zar "You learn the rules quick."
    show pov bored at left
    show zar confused_talk at right
    zar "So, what are you going to do?"
    zar "I can be your eye witness, if needed."
    show pov confused_talk at left
    show zar confused at right
    pov "I’m not sure…"
    show pov confused at left

    menu:
        "Open the locker.":
            $ mc_opened_locker = True

            show pov bored_talk at left
            show zar shocked at right
            pov "Guess there's only one way to find out…"
            show pov bored at left
            show zar shocked_talk at right
            zar "Woah! Careful, dude."
            zar "Pranks here have a record for not holding back punches, even with newbies."
            zar "For all you know, there's a bunch of gross shit inside, or some kind of rabid animal."
            show pov sad_talk at left
            show zar sad at right
            pov "Please tell me you are not speaking from experience."
            show pov shocked at left
            show zar bored_talk at right
            zar "Can't really. Last guy who tried playing a prank on me ended up with mic stand almost entirely up his ass."
            show pov smirk_talk at left
            show zar bored at right
            pov "Not one for practical jokes, huh?"
            show pov smirk at left
            show zar angry_talk at right
            zar "Not when I am the one on the receiving end, no."
            show pov shocked at left
            show zar bored_talk at right
            zar "Look, just step back in time if it's a stink bomb or some poor animal."
            show pov sad_talk at left
            show zar bored at right
            pov "Thanks for the encouraging words."
            show pov sad at left
            show zar bored_talk at right
            zar "Better to know 'em than let it catch you by surprise, right?"
            show pov neutral_talk at left
            show zar bored at right
            pov "Fair enough."
            show pov confused_talk at left
            pov "Alright. Ready?"
            show pov bored at left
            show zar confused_talk at right
            zar "On Three."
            show pov sad at left
            show zar shocked_talk at right
            zar "One."
            show pov confused_talk at left
            show zar shocked at right
            pov "Two-"

            ##-The Mc opens up his locker and a mountain of porn comes flooding out, making a small pile on the floor-
            show bg thatshitaintmine_mess
            with vpunch
            show pov bored at left
            show zar bored at right
            pov "…"
            zar "…"
            show zar confused_talk at right
            zar "Alright, not what I expected."
            show pov confused_talk at left
            show zar confused at right
            pov "What were you expecting?"
            show pov confused at left
            show zar bored_talk at right
            zar "I was expecting a greased-up Ian to come out of the locker and start running around, to be honest."
            show pov shocked at left
            show zar confused at right
            ian "Not this time. They put me in a japanese schoolgirl outfit now."
            show pov confused_talk at left
            pov "Ian?"
            show pov confused at left
            show zar bored at right
            ian "I am trapped, three lockers down from yours. Can I get a hand here?"
            show pov shocked at left
            show zar shocked at right
            pri "[povname]!"

            scene bg schoolhallway1_day
            with fade
            #show img thatshitaintmine_magazines
            show pov shocked at left
            with dissolve
            show zar shocked flip
            with dissolve
            show pri angry_talk at right
            with dissolve
            pri "My office. Now!"
            show pov confused_talk at left
            show zar shocked flip
            show pri angry at right
            pov "What? Why?!"
            show pov confused at left
            show zar bored flip
            show pri angry_talk at right
            pri "I think the mountain of porn by your feet, is a good enough reason."
            show pov shocked_talk at left
            show zar sad flip
            show pri angry at right
            pov "Wait, you don't actually think all of this stuff is mine, right?"
            show pov shocked at left
            show zar sad flip
            show pri bored_talk at right
            pri "It was in your locker. That's enough of an excuse for me to question you."
            show pov confused_talk at left
            show zar sad flip
            show pri bored at right
            pov "How does that make any sense?"
            show pov shocked_talk at left
            show zar bored flip
            show pri confused at right
            pov "Seriously, none of that stuff is mine."
            show pov shocked at left
            show zar bored_talk flip
            show pri confused at right
            zar "He is telling the truth."
            show pov sad at left
            show zar neutral_talk flip
            show pri shocked at right
            zar "I saw with my own eyes: some shifty looking guy, stacking all this shit into his locker. He hasn't done anything."
            show pov confused at left
            show zar confused flip
            show pri bored_talk at right
            pri "I'll be talking with you too in a moment, young lady."
            show pov embarrassed at left
            show zar shocked flip
            show pri bored_talk at right
            pri "Sleeping in the university's parking lot is not something I want to learn my students are doing."
            show pov sad at left
            show zar shocked_talk flip
            show pri bored at right
            zar "I…"
            show pov sad_talk at left
            show zar embarrassed flip
            show pri bored at right
            pov "It's alright, Zariah."
            pov "Don't say anything else…"
            show pov sad at left
            show zar sad flip
            show pri bored_talk at right
            pri "You also better watch your language around university officials. You are a lady, not a trucker."
            show pov shocked at left
            show zar embarrassed flip
            show pri sad_talk at right
            pri "Now come along, [povname]."
            show pov bored_talk at left
            show zar sad flip
            show pri bored at right
            pov "Yeah, yeah…"
            show pov bored_talk at left
            show zar bored flip
            show pri bored at right
            pov "Later, Z…"

        "Don’t open the locker.":
            show pov confused_talk at left
            show zar bored at right
            pov "I guess I shouldn’t open the locker, then."
            show pov shocked at left
            show zar confused_talk at right
            zar "'You chicken?"
            show pov shocked_talk at left
            show zar bored at right
            pov "What?! You just told me some shady dude spent all morning piling something inside it."
            pov "You were the one who told me not to open it."
            show pov sad at left
            show zar smirk_talk at right
            zar "I like sending you mixed signals."
            show pov confused at left
            zar "Keeps you in your toes, doesn’t it?"
            show pov confused_talk at left
            show zar neutral at right
            pov "I mean, I guess?"
            show pov bored_talk at left
            pov "But now I’m gonna have to see what I’m going to do with whatever is in my locker."
            show zar confused at right
            pov "Any ideas what could be in there?"
            show pov confused at left
            show zar confused_talk at right
            zar "Long list, dude."
            show pov sad at left
            show zar bored_talk at right
            zar "Stink bombs, dirty underwear, used tampons, live and possibly rabid ferrets or iguanas, Ian wearing nothing but his underwear."
            show pov shocked at left
            show zar sad_talk at right
            zar "We used to have a prank bingo of what would be inside people’s lockers each morning but Lashley got rid of that."
            show pov confused_talk at left
            show zar sad at right
            pov "Huh…"
            show pov confused at left
            show zar shocked at right
            pov "…"
            "{i}*Clank clank clank*{/i}"
            show pov confused_talk at left
            pov "Ian?"
            show zar neutral at right
            pov "Dude, you in there?"
            show pov shocked at left
            ian "No, I’m three lockers down."#(from inside a locker):
            scene bg schoolhallway1lockers_day
            with fade
            show pov neutral at left
            with dissolve
            show zar smirk_talk at right
            with dissolve
            zar "Well, that’s one option down."
            show pov confused_talk at left
            show zar smirk at right
            pov "Should we… you know, help him out?"
            show pov shocked at left
            show zar confused at right
            pas "[povname], please report himself to Director Lashley’s office? Transfer student [povname], report yourself to Director Lashley’s office."
            show pov confused at left
            show zar bored_talk at right
            zar "There’s your call."
            show pov confused_talk at left
            show zar bored at right
            pov "I wonder what she wants…"
            show pov confused at left
            show zar bored_talk at right
            zar "'Gives you the chance to let her know about the shady dude."
            show pov bored at left
            show zar bored_talk at right
            zar "You better head out."
            show pov bored_talk at left
            show zar neutral at right
            pov "But what about-"
            show pov bored at left
            show zar neutral_talk at right
            zar "I’ll have the janitor get him out, don’t worry."
            show pov sad at left
            show zar neutral at right
            ian "Not my first space rodeo, [povname]."
            show zar smirk at right
            ian "I actually have a box of CheeSquares with me."
            show pov confused at left
            show zar smirk_talk at right
            zar "Ian, I’ll get you out right now if you answer the following question correctly."
            show pov shocked at left
            zar "Are you wearing clothes in there?"
            show pov confused at left
            show zar smirk at right
            ian "…"
            show pov shocked at left
            ian "Can I take a pass on that one?"
            show zar smirk_talk at right
            zar "I’ll let the janitor to bring the Ian-kit with him."
            show pov sad at left
            show zar neutral_talk at right
            zar "Get going [povname], you don’t want to be around for when they get him out."
            show pov confused at left
            show zar smirk_talk at right
            zar "It’s like watching a biology skeleton wearing tights."
            show pov bored_talk at left
            show zar smirk at right
            pov "Didn’t need to learn that, but alright."
            show pov neutral_talk at left
            show zar neutral at right
            pov "Later, guys. Thanks again, Zariah."
            show pov neutral at left
            show zar neutral_talk at right
            zar "No biggie, dude."
            zar "See you around."

    $ principallashley_path = 5

    $ townmap_enabled = 0

    jump lbl_schoolhallway1_day_setup

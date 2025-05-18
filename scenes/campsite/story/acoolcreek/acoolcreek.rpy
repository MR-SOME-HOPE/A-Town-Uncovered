## A Cool Creek
label lbl_a_cool_creek:
    scene black
    with fade
    $ renpy.pause()
    "After a short walk to the nearby creek..."

    ## BG of creek
    scene bg campstream_day
    with fade

    show pov neutral at left
    show sis neutral_talk at Position(xpos=1300)
    show mumc neutral at right
    with dissolve
    sis "Woooooh! I can already feel how much cooler it is around here."

    show pov neutral
    show sis neutral
    show mumc neutral_talk
    mum "Just imagine how nice the water will feel."
    mum "It’s pretty shallow, only calf deep."

    show pov neutral_talk
    show mumc neutral
    pov "And the water looks to be flowing pretty nicely."
    show pov smirk_talk
    show mumc neutral
    pov "Nothing that’ll sweep us off our feet and wash us away."

    show pov confused
    show sis smirk
    show mumc shocked_talk
    mum "I hope you two don’t get washed away."
    show pov embarrassed
    show mumc embarrassed_talk
    if winc == 0:
        mum "I’d be a terrible person if I had to go home alone."
    else:
        mum "I’d be a terrible mother if I had to go home with one less child, let alone no children."

    show pov embarrassed_talk
    show mumc embarrassed
    if winc == 0:
        pov "We’re not that weak, [missus]."
    else:
        pov "We’re not that weak, mom."
    show pov smirk_talk
    show sis smirk
    show mumc confused
    pov "In fact, if should be you that we should be worried about."

    show pov smirk
    show sis neutral
    show mumc shocked_talk
    mum "I did my yoga, worry about yourself Mr My-Legs-Are-Too-Sore!"

    show pov bored
    show sis smirk_talk
    show mumc neutral
    sis "Gottem!"

    show pov bored_talk
    show sis smirk
    pov "Don’t say gottem, dude…"

    show pov bored
    show sis smirk_talk
    sis "But gottem."

    show pov bored_talk
    show sis smirk
    pov "{i}*Sigh*{/i}"

    show pov confused
    show sis neutral
    show mumc smirk_talk
    mum "Well, you two? What are you waiting for?"
    show pov neutral
    show mumc neutral
    mum "Last one to strip is a rotten egg!"

    scene black
    with fade
    $ renpy.pause(1,hard=True)

    ## They're now all naked
    ## BG of creek
    scene bg campstream_day
    with fade

    show povn neutral at left
    show sisn neutral at Position(xpos=1300)
    show mumn neutral_talk at right
    mum "Oh man, this is exactly what we needed on a day like today."

    show povn smirk
    show sisn neutral_talk
    show mumn neutral
    sis "Yeah, this is awesome. I don’t think we’ve ever bathed in a creek like this."
    show povn confused
    show sisn embarrassed_talk
    show mumn shocked
    sis "This is hygienic, right?"

    show povn embarrassed_talk
    show sisn neutral
    show mumn embarrassed
    pov "Well… pretty clean. It’s fresh water."
    show povn confused_talk
    show sisn shocked
    show mumn shocked
    pov "As long as there isn’t any dead animals up the stream, right?"

    show povn embarrassed
    show mumn embarrassed_talk
    mum "Yeah, that sounds about right."

    show povn embarrassed_talk
    show sisn bored
    show mumn embarrassed
    pov "Let’s just assume there isn’t and we’re fine."

    show povn smirk
    show sisn smirk_talk
    show mumn neutral
    sis "Hey, you think there are any fish here that we can catch?"

    show povn smirk_talk
    show sisn smirk
    pov "Doubt you’ll be quick enough for it."

    show povn smirk
    show mumn smirk_talk
    mum "You just need to hone in your inner bear, [sister]."
    show sisn shocked
    mum "If you can catch one, I’ll cook it up for us to eat tonight!"

    show povn smirk
    show sisn smirk_talk
    show mumn neutral
    sis "Alright! Bet!"
    show povn shocked
    show sisn smirk_talk
    sis "C’mon, [povname]. First one to catch a fish has to make the other cum!"

    show povn shocked_talk
    show sisn smirk
    show mumn embarrassed
    pov "Wait- is that a punishment or a reward."

    show povn smirk
    show sisn neutral
    show mumn neutral_talk
    mum "You two have fun. I’ll rest atop this rock like a little frog."
    show mumn smirk_talk
    mum "A little wet, frog."
    show povn confused
    show sisn bored
    mum "Get it, cause’ I’m wet?"
    show povn bored
    mum "Like literally."

    show mumn smirk
    pov "..."

    show povn bored
    show sisn bored
    show mumn embarrassed_talk
    mum "Don’t everyone laugh too hard."

    show povn neutral
    show sisn neutral_talk
    show mumn bored
    sis "C’mere fishy fish!"
    show povn shocked
    show sisn angry_talk
    show mumn shocked
    sis "Where the fuck are ya!?"

    scene black
    with fade
    $ renpy.pause()
    "After trying to catch fish… for a few minutes..."

    ## BG of creek
    scene bg campstream_day
    with fade

    if winc == 0:
        mum "How’s the hunting going, guys?"
    else:
        mum "How’s the hunting going, kids?"

    show povn bored at left
    show sisn angry_talk at right
    with dissolve
    sis "It sucks ass!"
    show sisn bored_talk
    sis "The only fish I’ve seen are teeny tiny ones."
    show sisn sad_talk
    sis "And there’s no way in hell I can catch them with my bare hands."

    show povn bored_talk
    show sisn sad
    pov "Even if we do catch it, I don’t think it’ll make for a very nice meal."

    show povn confused
    show sisn sad_talk
    sis "How the hell do bears make it look so easy."

    show povn bored_talk
    show sisn sad
    pov "I know right? Fish basically jump into their open mouths and here we are splashing in the water like idiots."

    show povn bored
    show sisn bored_talk
    sis "You look more like an idiot than me."
    show sisn smirk_talk
    sis "I look like a graceful kingfisher."
    show sisn embarrassed_talk
    sis "Just… an unsuccessful one."
    show sisn neutral_talk
    if winc == 0:
        sis "But still super graceful, right, [missus]?"
    else:
        sis "But still super graceful, right, mom?"
    
    show povn bored
    show sisn neutral
    mum "..."
    mum "...."
    show povn smirk
    show sisn bored
    mum "*Moans*"
    mum "....."
    mum "Huh- did you say something?"

    show povn smirk_talk
    show sisn confused
    if winc == 0:
        pov "[missus]’s in her own world. Shouldn’t bother her."
    else:
        pov "Mom’s in her own world. Shouldn’t bother her."

    show povn smirk
    show sisn confused_talk
    sis "She seems fine playing with herself. What do you think she’s fantasizing about?"

    show povn smirk_talk
    show sisn smirk
    pov "I don’t know. Probably me."

    show povn neutral
    show sisn smirk_talk
    sis "Well, aren’t you full of yourself."

    show povn smirk_talk
    show sisn shocked
    pov "Shouldn’t you be full of me instead?"

    show povn smirk
    show sisn smirk_talk
    sis "Is that a challenge?"

    show povn smirk_talk
    show sisn smirk
    pov "Yeah, come on then."

    show povn smirk
    show sisn smirk_talk
    sis "Let’s go, bitch!"
    sis "Give me all you got!"
    
    $ mumsiscamp_path = 11

    jump lbl_a_cool_creek_hscene

label lbl_a_cool_creek_hscene:
    scene img_acoolcreek_1
    with fade
    $ renpy.pause()
    show img_acoolcreek_2
    $ renpy.pause()
    show img_acoolcreek_3
    $ renpy.pause()
    show white
    with dissolve
    $ renpy.pause(2,hard=True)
    show bg acoolcreek_cum
    with dissolve
    $ renpy.pause()
    jump lbl_deepdish_campfire_pizza

image img_acoolcreek_1:
    "bg acoolcreek_1"
    pause 0.3
    "bg acoolcreek_2"
    pause 0.1
    "bg acoolcreek_3"
    pause 0.1
    "bg acoolcreek_4"
    pause 0.2
    "bg acoolcreek_5"
    pause 0.2
    repeat

image img_acoolcreek_2:
    "bg acoolcreek_1"
    pause 0.3
    "bg acoolcreek_3"
    pause 0.1
    "bg acoolcreek_4"
    pause 0.2
    "bg acoolcreek_5"
    pause 0.2
    repeat

image img_acoolcreek_3:
    "bg acoolcreek_1"
    pause 0.2
    "bg acoolcreek_4"
    pause 0.1
    "bg acoolcreek_5"
    pause 0.2
    repeat

    
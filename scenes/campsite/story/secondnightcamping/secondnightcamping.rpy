## Second Night Camping
label lbl_second_night_camping:
    ## In the tent, you are all cuddled up together.
    scene black
    with fade
    $ renpy.pause()
    "Later after dinner..."

    scene bg secondnightcamping_0
    with fade

    pov "Today was really nice."
    pov "It was a simple day with not a lot of activities but I think we needed one of the two days here to be a relaxing one."

    mum "I agree."
    mum "What’s the point of having a getaway if we’re stressing about trying to fill our times with ‘productivity’."
    mum "It’s meant to be a time to wind down and kick back."

    sis "That deep-dish pizza was so frikkin good."
    sis "I actually came so hard eating it."
    sis "And sorry to say but it wasn’t because of your cock, [povname]."

    pov "No, no. I totally get it."
    pov "I wholeheartedly agree."
    pov "We should make it more often!"
    pov "We don’t really need an open fire for it do we?"

    mum "I think it tasted extra special because it was cooked over an open fire."
    mum "And because of the setting."
    mum "Believe it or not, your surrounding adds to a dining experience."

    sis "Yeah, no."
    if winc == 0:
        sis "I have to agree with [missus] on that."
    else:
        sis "I have to agree with mom on that."
    sis "Although I would love that to be the only thing I eat for the rest of my life."
    sis "I also want it to be a camping special."
    sis "Just one extra thing to look forward to when we do this again."

    mum "Oh, so you DO enjoy doing this, [sister]."
    mum "Only just yesterday morning were you totally against it."

    sis "Yeah..."
    sis "Well..."
    sis "It grew on me."
    sis "I-"
    sis "I do enjoy doing this..."
    sis "But like..."
    sis "Only because it’s with you guys."

    pov "Oh look at Miss Cheese over here."

    sis "No, like… if I did this with anyone else, I don’t think it’d be as fun."
    sis "Just cause’ y’know?"

    mum "We play with each other so openly?"

    sis "Y-yeah..."

    pov "That’s so cute."

    mum "Hahahaha, it really is."

    sis "Shut up!"
    sis "C’mon..."
    sis "I didn’t sign up for a feeler sesh."

    mum "Speaking of feeler sesh."
    mum "[povname]. Do you wanna do a feeler of the inside of me before we sleep?"
    mum "Is that okay with you, [sister]?"

    if winc == 0:
        sis "Yeah, of course, [missus]."
    else:
        sis "Yeah, of course, mom."
    sis "I had my turn last night."
    sis "You should get a good night’s rest."
    sis "I’ll still be watching closely though."

    mum "Of course, hon."
    mum "So? [povname]. Are you hard enough yet?"

    if winc == 0:
        pov "Jeez, [missus]. Give me more than 5 seconds will ya?"
    else:
        pov "Jeez, mom. Give me more than 5 seconds will ya?"

    mum "Hehehe, sorry, sweetie."

    sis "You’re so slow, [povname]. You should be like ready to fire at all times."

    pov "Pffft-"
    pov "You guys have already drained me so much earlier today."

    mum "One last one for the night, you’ll sleep like a baby too."

    pov "I know I know, I’m working on it, hold on."

    $ mumsiscamp_path = 13

    jump lbl_second_night_camping_hscene

label lbl_second_night_camping_hscene:
    scene img_secondnightcamping_1
    with fade
    $ renpy.pause()
    show img_secondnightcamping_2
    $ renpy.pause()
    show img_secondnightcamping_3
    $ renpy.pause()
    show white
    with dissolve
    $ renpy.pause(2,hard=True)
    show bg secondnightcamping_cum
    with dissolve
    $ renpy.pause()
    jump lbl_second_night_camping_end

image img_secondnightcamping_1:
    "bg secondnightcamping_1"
    pause 0.3
    "bg secondnightcamping_2"
    pause 0.1
    "bg secondnightcamping_3"
    pause 0.1
    "bg secondnightcamping_4"
    pause 0.2
    "bg secondnightcamping_5"
    pause 0.2
    repeat

image img_secondnightcamping_2:
    "bg secondnightcamping_1"
    pause 0.3
    "bg secondnightcamping_3"
    pause 0.1
    "bg secondnightcamping_4"
    pause 0.2
    "bg secondnightcamping_5"
    pause 0.2
    repeat

image img_secondnightcamping_3:
    "bg secondnightcamping_1"
    pause 0.2
    "bg secondnightcamping_4"
    pause 0.1
    "bg secondnightcamping_5"
    pause 0.2
    repeat

label lbl_second_night_camping_end:
    scene black
    with fade
    $ renpy.pause()

    jump lbl_packing_up_the_camp
label lbl_very_special_prayer:
    ## IF principallashley_path == 9 ##
    ##-This scene happens a few days after the last scene, Mc enters Lashley's office to find her in her desk looking rather stressed out-
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    scene bg framed_no_mag_reach_mag with dissolve
    pov "Director Lashley?"
    scene bg framed_no_mag_bored with dissolve
    scene bg framed_no_mag_bored_talk
    pri "Hi, [povname]..."
    pri "You can come in…"
    pri "Sit down, as always…"
    scene bg framed_no_mag_bored
    pov "Geez, who rained on your parade?"
    pov "Everything okay?"
    scene bg framed_no_mag_bored_talk
    pri "Yeah… I'm just a bit feverish, is all."
    pri "I've been feeling rather under the weather these past few days."
    scene bg framed_no_mag_bored
    pov "Sounds rough. Have you gone to see a doctor?"
    scene bg framed_no_mag_bored_talk
    pri "Yeah, nothing they could do, other than trying to chog me full of pills."
    scene bg framed_no_mag_bored
    pov "Well, it's better than nothing, at least."
    scene bg framed_no_mag_bored_talk
    pri "I'd rather use my father's method instead, it has never failed me before."
    scene bg framed_no_mag_neutral
    pov "What's the method?"
    scene bg framed_no_mag_bored_talk
    pri "It's a special prayer that he taught me when I was very young."
    pri "That, along with a certain concoction he made, always worked like a charm."
    pri "Used to knock me out like a light too, when he first taught it to me."
    scene bg framed_no_mag_sad_talk
    pri "Sadly though, I'm missing a key ingredient of it, and I'm far too buried in paperwork to go out to the store and get it."
    pri "But I don't think I'll be anywhere close to finishing the job soon if I don't get myself under control."
    scene bg framed_no_mag_sad
    pov "I could go get it for you if it's so urgent."
    scene bg framed_no_mag_embarrassed_talk
    pri "Oh, I can't possibly ask you to do that, [povname]."
    pri "I've already bothered you enough with silly requests of mine."
    scene bg framed_no_mag_embarrassed
    pov "It's really no trouble at all. Besides, it's just a quick run to the store, right?"
    scene bg framed_no_mag_confused_talk
    pri "Well… Not exactly."
    scene bg framed_no_mag_neutral_talk
    pri "You see, I have all the usual elements I normally need to relax and pray away."
    pri "That is, except for one very important item that is imperative for the ritual my father taught me."
    scene bg framed_no_mag_smirk_talk
    pri "Wine."
    scene bg framed_no_mag_neutral
    pov "Just wine?"
    pov "Wait, how old did you say you were when your father taught you this prayer?"
    scene bg framed_no_mag_confused_talk
    pri "Just around when I entered puberty and my hormones were going wild."
    scene bg framed_no_mag_shocked
    pov "And he had you drinking wine at that age?"
    scene bg framed_no_mag_embarrassed_talk
    pri "Don't be silly, [povname]. That would be beyond irresponsible and harmful for my development at that age."
    scene bg framed_no_mag_neutral_talk
    pri "No, what he used to give me was a special alcohol-free wine."
    pri "Pen Island Blend \"Prestige Rouge\" Wine, to be exact."
    scene bg framed_no_mag_neutral
    pov "Sounds fancy."
    scene bg framed_no_mag_neutral_talk
    pri "It is for a non-alcoholic wine."
    scene bg framed_no_mag_sad_talk
    pri "I used to have a few bottles at home, but lately I've been coming down with more of my fevers recently so I finished them rather quickly."
    pri "I haven't been able to order more."
    scene bg framed_no_mag_sad
    pov "Well, do they sell them at the store?"
    pov "I could go pick one up for you, if it's so important."
    scene bg framed_no_mag_sad_talk
    pri "One bottle is usually around twenty to twenty five grand."
    scene bg framed_no_mag_sad
    pov "Okay, I would like to avoid going into debt at my age, if possible."
    pri "{i}*Sigh*{/i}"
    scene bg framed_no_mag_sad_talk
    pri "I don't know what I'm going to do…"
    pri "Even if I did order the wine, there is still the fact I would have to wait for it to be delivered!"
    scene bg framed_no_mag_confused
    pov "Well, why not just try any other bottle of wine."
    scene bg framed_no_mag_sad_talk
    pri "W-Well, to be honest: I'm just too used to that specific brand and its taste; that any other non-alcoholic brand tastes kind of awful…"
    pri "Plus, there is the fact the town only has the most dirt cheap quality brands of non-alcoholic brand around."
    scene bg framed_no_mag_embarrassed_talk
    pri "Gosh, that sounds picky and spoiled doesn't it?"
    scene bg framed_no_mag_embarrassed
    pov "To each their own, it's okay."
    scene bg framed_no_mag_confused
    pov "Well, what about regular wine?"
    pov "There has to be something around you could stomach easily."
    scene bg framed_no_mag_confused_talk
    pri "Well, that is a possibility… I usually try to stay away from any alcoholic beverage whatsoever though, so I don't know what brand could resemble it."
    scene bg framed_no_mag_sad_talk
    pri "I'm really no good with strong drinks -- I can't even swallow them."
    scene bg framed_no_mag_shocked
    pov "Let me ask around and I'll get something soft enough for you to pray without a care."
    scene bg framed_no_mag_shocked_talk
    pri "You'd really do that for me, [povname]?"
    pri "Going out of your way just to find a wine I can tolerate, simply because I'm in trouble?"
    scene bg framed_no_mag_shocked
    pov "Of course!"
    pov "It's not like I have anything better to do. And if it helps you out, then that's even better!"
    pov "I'll hurry as much as I can."
    scene bg framed_no_mag_shocked_talk
    pri "You are a lifesaver, [povname]."
    pri "I won't forget this."
    scene bg framed_no_mag_shocked
    pov "Just hang in there and wait for me."
    pov "I'll be back in a second."
    #show black with fade

    #hide black with fade
    ##-Mc then leaves the room-
    scene bg framed_no_mag_confused with fade
    pri "…"
    scene bg framed_no_mag_confused_talk
    pri "Gosh, why can't men my age be as kind and dreamy as him?"
    scene bg framed_no_mag_embarrassed
    pri "{i}… Again with those impure thoughts about him…{/i}"
    pri "{i}Sweet lord, give me strength...{/i}"

    ##=SCENE END=
    $ principallashley_path = 10
    jump lbl_schoolhallway2_day_setup

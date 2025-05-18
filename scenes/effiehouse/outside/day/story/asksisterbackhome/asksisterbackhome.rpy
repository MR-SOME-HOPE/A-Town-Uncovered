## Ask Sister Back Home ##
label lbl_ask_sister_back_home:

    scene bg effiehouseoutside_day
    "{i}*Knock knock knock*{/i}"
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "[povname], what's up? [sister] is feeling better today, if that's what you came to ask."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "That's great to hear, thanks for everything, Effie."
    show pov confused_talk at left
    show eff confused at right
    pov "Listen, do you think we can convince her to come back home for a day?"
    show pov sad at left
    show eff confused_talk at right
    eff "That's a really tall order man, I don't really think she is ready."
    show pov confused_talk at left
    show eff confused at right
    pov "I thought you said she's feeling better?"
    show pov smirk at left
    show eff embarrassed_talk at right
    eff "She is! She's eating more than usual. That's a good sign."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Not to mention she is also a bit more talkative and she stopped sobbing too much at night."
    show pov neutral_talk at left
    show eff neutral at right
    pov "That's good! That's progress at the very least."
    show pov confused at left
    show eff confused_talk at right
    eff "Yeah, but to suddenly ask her to go back there..."
    show eff sad_talk at right
    eff "I don't want her to feel like I'm tired of her and am trying to push her away."
    show pov embarrassed at left
    show eff embarrassed at right
    eff "..."
    show pov smirk at left
    show eff embarrassed_talk at right
    eff "I want to assume you have something planned?"
    show pov neutral_talk at left
    show eff neutral at right
    pov "Yeah, actually, something really good but I'm going to need some time to finish it up."
    show pov smirk_talk at left
    show eff smirk at right
    pov "I figured it would be smart to have her warm up to the idea before it's ready and not just drop it on her the very same day, you know?"
    show pov neutral at left
    show eff smirk_talk at right
    eff "That's actually a pretty good idea."
    eff "There's some logic to that, good on ya for thinking with your head, dude!"
    if effie_points >= 4:
        show pov confused at left
        eff "Good to know I have a quick thinker at my beck and call when I need him."
        show pov confused_talk at left
        show eff smirk at right
        pov "Since when am I at your beck and call?"
        show pov smirk at left
        show eff smirk_talk at right
        eff "The first time we started messing around comes to mind."
        show pov smirk_talk at left
        show eff smirk at right
        pov "Fair enough."
        show pov embarrassed at left
        show eff smirk_talk at right
        if winc == 0:
            eff "We should have another “night in” once your [sisrole] is better."
        else:
            eff "We should have another “night in” once [sister] is better."
        show pov embarrassed_talk at left
        show eff smirk at right
        pov "Let's put a pin in that. She's my priority at the moment."
    show pov neutral at left
    show eff smirk_talk at right
    eff "Anyway, what exactly do you have planned?"
    show pov neutral_talk at left
    show eff neutral at right
    pov "The rise of Twin Fortress 2."
    show pov embarrassed_talk at left
    pov "Just don't tell her. It's meant to be a surprise."
    show pov confused_talk at left
    show eff confused at right
    pov "You think you can have her come back to the house in a few days?"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "I mean, I can try..."
    show pov confused at left
    if winc == 0:
        eff "Doubt she will set foot in the house if your [dadrole] is present."
    else:
        eff "Doubt she will set foot in the house if your dad is present."
    eff "She refuses to even mention him."
    show pov neutral_talk at left
    show eff confused at right
    pov "I'll have that taken care of, don't worry."
    show pov neutral at left
    show eff confused_talk at right
    eff "Alright, if you can assure me of that I'll give it a shot."
    show eff bored_talk at right
    if winc == 0:
        eff "I'm not having her go back there until I'm sure she can handle it, and your [dadrole] being there is the last thing she needs right now."
    else:
        eff "I'm not having her go back there until I'm sure she can handle it, and your dad being there is the last thing she needs right now."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Thanks, Effie."
    pov "You're seriously the best."
    show pov neutral at left
    show eff smirk_talk at right
    eff "Of course I am!"
    show pov smirk at left
    eff "I'm shocked you guys haven't realized that already."
    show pov smirk_talk at left
    show eff smirk at right
    pov "Quite modest too, huh?"
    show pov smirk at left
    show eff smirk_talk at right
    eff "Hehehe, you know it!"
    show pov neutral at left
    show eff neutral_talk at right
    eff "Alright, I'll speak to her, you better go back to finish whatever it is you're doing."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Thanks, Effie."
    pov "Keep me posted!"
    $ sister_path = 32
    $ renpy.notify("New Objective: Rebuild the Twin Fortress")

    jump lbl_effiehouseoutside_day_setup

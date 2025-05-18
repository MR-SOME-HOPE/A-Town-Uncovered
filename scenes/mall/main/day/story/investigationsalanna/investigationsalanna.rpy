label lbl_investigations_alanna:
    default investigations_alanna = 0
    show btn_mall_day_meghan_idle2
    show btn_mall_day_teghan_idle2
    show btn_mall_day_chieghan_idle2
    if investigations_alanna != 0:
        pov "{i}I already tried with Alanna. No luck.{/i}"

    else:
        $ investigations_alanna = 1

        show pov neutral_talk at left
        with dissolve
        show ala neutral at right
        call lbl_icecreampy_counter_check
        with dissolve
        pov "Hey, Alanna."
        show pov neutral at left
        show ala neutral_talk at right
        ala "Hey, dude. Coming for your shift?"
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "Kinda busy at the moment."
        show pov embarrassed at left
        show ala neutral_talk at right
        ala "Then, unless you are buying something, I got work to do."
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "Actually, I was hoping to see if you could help me out with something."
        show pov neutral at left
        show ala bored_talk at right
        ala "Is it ice cream related?"
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "No."
        show pov neutral at left
        show ala bored_talk at right
        ala "Will I get paid overtime for it?"
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "No, but-"
        show pov neutral at left
        show ala bored_talk at right
        ala "Will it involve me getting out of the kiosk for at least 5 minutes?"
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "Not necessarily but-"
        show pov shocked at left
        show ala bored_talk at right
        ala "Does it involve you and I having sex in the back room?"
        show pov embarrassed_talk at left
        show ala neutral at right
        pov "No- Wait, what?"
        show pov embarrassed at left
        show ala bored_talk at right
        ala "Sorry, some guys try that line on me from time to time."
        ala "Saying they need my help with something in the back room, and all."
        ala "I just shoot them down or have mall security escort them out."
        show pov embarrassed at left
        show ala smirk_talk at right
        ala "I mean, you are cute and all, but you have to properly woo a lady first, you know?"
        show pov embarrassed_talk at left
        show ala smirk at right
        pov "Uhh, noted."
        show ala confused at right
        pov "Still, it doesn’t have anything to do with that."
        show pov embarrassed at left
        show ala bored_talk at right
        ala "Then, I can’t really help you, [povname]."
        show pov sad_talk at left
        show ala bored at right
        pov "You haven’t even heard what it is I wanted to ask, though."
        show pov sad at left
        show ala bored_talk at right
        ala "Is it ice cream related or will it get me out of this kiosk for a while."
        show pov sad_talk at left
        show ala bored at right
        pov "I-"
        show pov sad at left
        show ala bored_talk at right
        ala "We’ll talk later, [povname]."
        show pov sad_talk at left
        show ala bored at right
        pov "I guess?"
        pov "See you later, then…"

    jump lbl_mall_day_setup

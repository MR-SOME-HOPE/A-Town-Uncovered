## Lailah Lying Doggy Pre
label lbl_lailah_lying_doggy_pre:
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hey~ [povname]! Good to see you."
    lai "You looking for Jacob?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Maybe?"
    lai "Maybe, well you certainly weren't looking for me, were you?"
    pov "Maaaaybe~"
    lai "{i}*Chuckles*{/i}"
    lai "You wanna- come inside then?"
    menu:
        "Why not.":
            pov "Why not."
            lai "Great, I'll make some fresh iced tea."

            jump lbl_lailah_lying_doggy

        "No, thanks.":
            pass

    pov "No, thanks. lailah."
    pov "I'll meet up with him another day."
    lai "You sure, honey~?"
    lai "{i}*Sigh*{/i} Suit yourself."

    jump lbl_jacobhouseoutside_day

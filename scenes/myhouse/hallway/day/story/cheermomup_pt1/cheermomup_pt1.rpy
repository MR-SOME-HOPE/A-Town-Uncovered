## Cheer Mom Up Pt 1 - Go get icecream ##
label lbl_cheermomup_pt1:
    if winc == 0:
        jump lbl_cheermomup_pt1_winc0

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_2
    pov "Mom?"
    show bg cheermomup_3
    pov "..."
    show bg cheermomup_2
    pov "Are you in there?"
    show bg cheermomup_3
    pov "..."

    menu:
        "Knock again":
            "{i}*Knock knock*{/i}"
        "Anyone in there?":
            show bg cheermomup_2
            pov "Hello? Anyone in there?"
        "Barge in":
            show bg cheermomup_4
            pov "{i}Oh... the door's locked.{/i}"
    show bg cheermomup_3
    mum "[povname]? Don't come in-"
    mum "Is there something wrong?"
    show bg cheermomup_2
    pov "I should be asking you that."
    pov "Why are you still in bed."
    show bg cheermomup_5
    mum "I- It's fine. I'm fine... {i}*Sniff*{/i} Don't worry about me."
    show bg cheermomup_6
    pov "Mom? Are you crying?"
    show bg cheermomup_5
    mum "What? W- No...? I um.. just had the sniffles! Hehe... {i}*Sniff sniff*{/i}"
    mum "I'm fine... really."
    show bg cheermomup_7
    pov "Can I come in?"
    show bg cheermomup_3
    mum "What? No, please. Just let me rest."
    show bg cheermomup_6
    pov "Are you sure?"
    show bg cheermomup_5
    mum "Yes, honey. Really! {i}*sniff*{/i}"

    menu:
        "Can you please let me in!?":
            show bg cheermomup_6
            pov "Can you please just let me in, Mom! I need to know if you're really okay."
            show bg cheermomup_5
            mum "Honey, swee- *sniff* sweetie. I'm fine, just let me be."
        "Alright then.":
            show bg cheermomup_6
            pov "Alright then... I'll just be a call away if you need me."
            show bg cheermomup_5
            mum "Thank you, baby."
    show bg cheermomup_3
    mum "Oh, wait! Actually... can you get me some stuff..?"
    mum "It would really cheer m- I mean, make me feel bette- wai- yeah! Feel better."
    show bg cheermomup_4
    mum "{i}*Sniffs loudly*{/i} Y'know, because I'm sick and all."
    pov "..."
    show bg cheermomup_2
    pov "What is it that you want, Mom?"
    show bg cheermomup_3
    mum "Icecream..."
    show bg cheermomup_2
    pov "..Alrigh-"
    show bg cheermomup_3
    mum "The creamiest one you can get!"
    show bg cheermomup_4
    pov "..."
    show bg cheermomup_7
    pov "Al-"
    show bg cheermomup_4
    mum "Please! T- {i}*Sniff*{/i} Thanks!"
    show bg cheermomup_3
    pov "..."
    show bg cheermomup_2
    pov "A-"
    show bg cheermomup_3
    mum "Are you still ther-"
    show bg cheermomup_7
    pov "Yes, Mom! I'll go get the icecream!"
    show bg cheermomup_4
    mum "Thanks, honey. I... I love you..."

    menu:
        "I love you too.":
            show bg cheermomup_8
            pov "I love you too, Mom."
        "I miss you.":
            show bg cheermomup_9
            pov "I miss you, Mom..."
        "Ignore":
            show bg cheermomup_5
            pov "..."
            show bg cheermomup_10
            mum "I love you... so much..."
            mum "..."
            mum "I hope he heard that..."
    $ mum_path = 12
    $ townmap_enabled = 1
    jump lbl_myhallway_day_setup

### NO WINC ###
label lbl_cheermomup_pt1_winc0:

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_2
    pov "[missus]?"
    show bg cheermomup_3
    pov "..."
    show bg cheermomup_2
    pov "Are you in there?"
    show bg cheermomup_3
    pov "..."

    menu:
        "Knock again":
            "{i}*Knock knock*{/i}"
        "Anyone in there?":
            show bg cheermomup_2
            pov "Hello? Anyone in there?"
        "Barge in":
            show bg cheermomup_4
            pov "{i}Oh... the door's locked.{/i}"
    show bg cheermomup_3
    mum "[povname]? Don't come in-"
    mum "Is there something wrong?"
    show bg cheermomup_2
    pov "I should be asking you that."
    pov "Why are you still in bed."
    show bg cheermomup_5
    mum "I- It's fine. I'm fine... {i}*Sniff*{/i} Don't worry about me."
    show bg cheermomup_6
    pov "[missus]? Are you crying?"
    show bg cheermomup_5
    mum "What? W- No...? I um.. just had the sniffles! Hehe... {i}*Sniff sniff*{/i}"
    mum "I'm fine... really."
    show bg cheermomup_7
    pov "Can I come in?"
    show bg cheermomup_3
    mum "What? No, please. Just let me rest."
    show bg cheermomup_6
    pov "Are you sure?"
    show bg cheermomup_5
    mum "Yes, honey. Really! {i}*sniff*{/i}"

    menu:
        "Can you please let me in!?":
            show bg cheermomup_6
            pov "Can you please just let me in, [missus]! I need to know if you're really okay."
            show bg cheermomup_5
            mum "Honey, swee- *sniff* sweetie. I'm fine, just let me be."
        "Alright then.":
            show bg cheermomup_6
            pov "Alright then... I'll just be a call away if you need me."
            show bg cheermomup_5
            mum "Thank you, baby."
    show bg cheermomup_3
    mum "Oh, wait! Actually... can you get me some stuff..?"
    mum "It would really cheer m- I mean, make me feel bette- wai- yeah! Feel better."
    show bg cheermomup_4
    mum "{i}*Sniffs loudly*{/i} Y'know, because I'm sick and all."
    pov "..."
    show bg cheermomup_2
    pov "What is it that you want, [missus]?"
    show bg cheermomup_3
    mum "Icecream..."
    show bg cheermomup_2
    pov "..Alrigh-"
    show bg cheermomup_3
    mum "The creamiest one you can get!"
    show bg cheermomup_4
    pov "..."
    show bg cheermomup_7
    pov "Al-"
    show bg cheermomup_4
    mum "Please! T- {i}*Sniff*{/i} Thanks!"
    show bg cheermomup_3
    pov "..."
    show bg cheermomup_2
    pov "A-"
    show bg cheermomup_3
    mum "Are you still ther-"
    show bg cheermomup_7
    pov "Yes, [missus]! I'll go get the icecream!"
    show bg cheermomup_4
    mum "Thanks, honey. I... I love you..."

    menu:
        "I love you too.":
            show bg cheermomup_8
            pov "I love you too, [missus]."
        "I miss you.":
            show bg cheermomup_9
            pov "I miss you, [missus]..."
        "Ignore":
            show bg cheermomup_5
            pov "..."
            show bg cheermomup_10
            mum "I love you... so much..."
            mum "..."
            mum "I hope he heard that..."
    $ mum_path = 12
    $ townmap_enabled = 1
    jump lbl_myhallway_day_setup

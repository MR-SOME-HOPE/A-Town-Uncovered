label lbl_post_news_breakfast:
    default postnewsbreakfast_choice = 0
    #[Kitchen, dinner table - “Post-News Breakfast”  - main_story =83]
    #scene bg safetyandhomelife_temp1
    scene bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    show sisexpression postnewsbreakfast_neutral
    with fade
    ##-Scene shows mc and family sitting on the table but there is a tense atmosphere as
    ## Missus is beyond pissed at the new development regarding the security system-

    sis "…"
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_confused
    pov "…"
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    mum "…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats ##NOTE SHOW new bg NOT SCENE bg

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show sisexpression postnewsbreakfast_confused_talk
    sis "U-Um…"
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    sis "Don’t you think we should-"
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_shocked
    mum "Zip it!"

    show eyessis postnewsbreakfast_lookpov

    mum "I don’t want to hear another word about all of this until I talk to your father and likely tear his head off."
    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_smirk_talk
    show sisexpression postnewsbreakfast_confused
    pov "Well, not even hiding your anger this time?"

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_smirk
    show sisexpression postnewsbreakfast_confused_talk
    mum "There are things you don’t hide from your wife, [povname]."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyessis postnewsbreakfast_lookfood
    show sisexpression postnewsbreakfast_bored
    mum "Especially when she has been asking you over and over again what do you plan to do for a crisis only to receive the cold shoulder and be flat out ignored until..."

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_smirk
    mum "Ugh!"

    show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_smirk_talk
    mum "I swear that man is going to drive me insane!"

    ## NOTE make sequencing look good if doing this conditional dialogue or not
    ##-If Missus has been romanced-
    if mum_path >= 31:

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_smirk
        show sisexpression postnewsbreakfast_bored
        mum "Thank God, I now know I can do so much better than him!"

        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_smirk_talk
        show sisexpression postnewsbreakfast_confused
        pov "You know it’s true."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_confused_talk
        pov "You deserve the best."

        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_smirk_talk
        show sisexpression postnewsbreakfast_confused
        mum "I know dear, thank you for that."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        mum "Truly."

    ##=RESULT END=

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed
    mum "Look, kids…"

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show sisexpression postnewsbreakfast_confused
    mum "I know I'm a broken record, but-"

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_neutral_talk
    sis "We'll be safe, [missus]."

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "You've told us a hundred times and we have listened everytime, right?"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_embarrassed
    pov "Been drilled into my head by this point."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_neutral
    pov "Everything is going to be alright, [missus]."

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_neutral_talk
    pov "I know it will."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    show sisexpression postnewsbreakfast_embarrassed
    mum "You kids always know what to say to calm me down don't you?"
    mum "Thank you."

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_embarrassed_talk
    if winc == 0:
        sis "No offense, [missus], but we kinda have a lot of practice dealing with your panicked state of mind."
    else:
        sis "No offense, Mom, but we kinda have a lot of practice dealing with your panicked state of mind."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    show sisexpression postnewsbreakfast_confused_talk
    sis "But you got nothing to worry about!"

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_bored_talk
    sis "I'll keep my eye out for trouble and this dum-dum now knows better than to go around naked for no reason."

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_smirk_talk
    sis "Don't you, [povname]?"

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_smirk_talk
    pov "Ehehehe…"

    ##-If Sister is romanced-
    if sister_path >= 36:

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_smirk_talk
        sis "Because you know damn well what I’ll both do to you and what I’ll keep from you if you decide to do something stupid again, don’t you?"

        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_neutral
        pov "Oh boy…"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_smirk
        show sisexpression postnewsbreakfast_smirk_talk
        sis "Don’t you?"

    ##=RESULT END=

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_smirk
    mum "Oh, no need to threaten your [povsisrole], [sister]."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    mum "I’m certain he has learned his lesson already and will think twice before doing something like that again."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_neutral
    mum "He better have a good reason to scare me like that again."

    show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
    show eyespov postnewsbreakfast_looksis
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_neutral_talk
    mum "Not like there is ever a good reason to even consider doing it in the first place."

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_smirk
    mum "Right, [povname]?"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_neutral
    pov "U-Ummm…"

    ##-If Missus is romanced-
    if mum_path >= 31:

        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_smirk
        mum "Plus, he knows damn well what I will do to him if he ever thinks of doing something like that again."

        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_neutral
        mum "And the hell that will fall upon him if he scares me again."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_smirk_talk
        mum "Isn’t that right, [povname], sweetie~?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_embarrassed_talk
        pov "Y-Yes, I know…"

    ##=RESULT END=

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_smirk
    pov "A-Alright, can you two stop putting me in the spotlight right in the middle of breakfast?"

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_bored_talk
    pov "I mean, I know you don’t want to talk about this, but are you really ok with this whole security system business?"

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_bored
    mum "{i}*Sigh*{/i}"
    mum "It is something that I just came to know it’s a thing, sweetie."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_confused
    mum "I’m missing a lot of details here so I don’t really know what my reaction should really be at the moment."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_embarrassed
    mum "Not to mention the fact I’m absolutely angry about how your father thought it was a good idea to keep this away from me to begin with."

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "No one blames you for that, [missus]."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_shocked_talk
    sis "That’s the natural reaction to have, in fact!"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_smirk_talk
    sis "Anyone would be angry over keeping secrets like this from their partner."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_smirk
    show sisexpression postnewsbreakfast_angry_talk
    sis "And who knows if he was ever going to tell you to begin with."

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_smirk_talk
    show sisexpression postnewsbreakfast_angry_talk
    pov "That’s true…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored_talk
    show sisexpression postnewsbreakfast_smirk
    pov "I wouldn’t put it past him to hide this until there is a technician at our house."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_smirk_talk
    show sisexpression postnewsbreakfast_bored
    pov "He would likely have you sign the papers yourself without much explanation too since I doubt he is just going to sit and wait for the technician to begin with."

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_smirk_talk
    show sisexpression postnewsbreakfast_bored_talk
    sis "Good point there."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_shocked
    mum "I want to have some faith in your father that he just wouldn’t sink that low."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_confused
    mum "A part of me wants to think he just forgot or he never found the right moment to tell me."
    mum "…"

    show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_smirk_talk
    show sisexpression postnewsbreakfast_bored_talk
    mum "But the way he is behaving lately tells me that’s anything but the real case…"
    show eyessis postnewsbreakfast_lookfood
    if winc == 0:
        mum "I have always given your [dadrole] his space but when he is doing stuff that affects the whole household, well…"
    else:
        mum "I have always given your father his space but when he is doing stuff that affects the whole family, well…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_smirk
    mum "I just can’t stay on the sidelines and do as he pleases…"

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_neutral
    mum "So please, kids. Stay safe…"
    mum "I have my hands full dealing with him, so I need to trust you’ll be okay."

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_neutral_talk
    sis "We will, [missus]."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "We promise."

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_neutral
    pov "Yeah…"
    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    pov "We do…"

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    mum "Thank you, both of you."

    show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_bored_talk
    mum "That’s really all I ask."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_embarrassed
    pov "…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_neutral
    mum "Alright, enough of all that."

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    show sisexpression postnewsbreakfast_sad
    mum "What do you two plan to do today?"

    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_sad_talk
    sis "Gotta go to work, we received a new shipment of stuff so the manager asked me to go and get it all sorted out, you know?"

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "I’ll let you know when I get there and call when I’m heading home."

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyessis postnewsbreakfast_lookfood
    show sisexpression postnewsbreakfast_shocked_talk
    mum "Good!"

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_confused
    mum "Thank you, [sister]."

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    mum "What about you, [povname]?"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_embarrassed_talk
    pov "I, um…"

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_confused_talk
    pov "I guess I’ll-"

    ##-The following is an important choice. Whatever the player says he is going to do right now will need to be remembered in order to avoid a punishment from Missus and a big RP loss with her and sister-

    ##=CHOICE=
    menu:

        "Hang out with Jacob and Effie":
            $ postnewsbreakfast_choice = 1

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            pov "-Go hang out with Jacob and Effie for a while."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_neutral_talk
            pov "We kind of roam around town trying to deal with everything going on."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_shocked_talk
            pov "Plus, they are of the few people who don’t immediately start giving me weird looks or something ever since the incident."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_confused
            mum "Sounds like a good idea, sweetie."

            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_bored
            mum "Times like this are better with the company of good friends."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_neutral
            show sisexpression postnewsbreakfast_bored_talk
            mum "Just be sure to let me know if you kids start moving around town too much."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_smirk
            mum "I don’t ask for much, a text message will ease my soul just enough."

            show bg postnewsbreakfast_pov_eats_sis_idle_mum_eats
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_shocked
            pov "I’ll be sure to do that, [missus]. I promise."

            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_confused_talk
            show sisexpression postnewsbreakfast_shocked_talk
            sis "Do tell Effie I said hi from my part!"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_bored_talk
            sis "She has been inviting me out for girls night but I’ve been busy with work, so tell her I'll give it a call later on, okay?"

            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_smirk_talk
            show sisexpression postnewsbreakfast_neutral
            pov "Yeah, for sure."

        "Get started on my school project":
            $ postnewsbreakfast_choice = 2

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored_talk
            show sisexpression postnewsbreakfast_shocked
            pov "-Get started with my school project."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_bored_talk
            pov "I have to write an essay of my picking so I figured making it about the town itself would help me get familiar with it."
        
            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_bored
            mum "That sounds like a wonderful idea, [povname]!"

            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_neutral_talk
            mum "I love the enthusiasm you have for learning."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_neutral_talk
            show sisexpression postnewsbreakfast_neutral
            pov "It is the big project of the semester so I have to start early, you know?"
            pov "I’m going to go around town and ask some of the locals some of the towns history and the like, maybe some cool urban legends or something in general like that that might be interesting to know."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_neutral
            mum "Wonderful!"

            show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_bored_talk
            mum "Just be sure to let me know when you move your location too much and when you are coming home."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_bored
            mum "I’m not asking you to give me a call every five minutes or anything, but a text message here and there will do wonders calming me down."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_neutral_talk
            show sisexpression postnewsbreakfast_neutral
            pov "Will do, [missus]. I promise."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_neutral
            show sisexpression postnewsbreakfast_shocked_talk
            sis "I’ll ask my manager if she knows something interesting herself."

            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_neutral_talk
            sis "Who knows, maybe it can help out."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_neutral_talk
            show sisexpression postnewsbreakfast_smirk
            pov "Thanks, [sister]. I appreciate it."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_neutral_talk
            mum "I love to see you two helping each other out."

        "Go have a swim on the beach.":
            $ postnewsbreakfast_choice = 3

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_shocked
            pov "-Go have a swim at the beach."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_confused_talk
            show sisexpression postnewsbreakfast_smirk
            pov "I really could use the exercise, plus Violette there makes good company."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_confused
            show sisexpression postnewsbreakfast_smirk_talk
            sis "True that, she is hella cool."

            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_neutral
            pov "There is also the fact I could really use the dip to help me relax, you know?"

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_confused_talk
            mum "A-And is that the only reason?"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_confused_talk
            pov "What do you mean?"

            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_shocked
            mum "W-Well, [povname]."

            show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_confused_talk
            show sisexpression postnewsbreakfast_embarrassed
            mum "I don’t think I need to tell you at this point the nature of the beach itself and-"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_shocked
            show sisexpression postnewsbreakfast_bored_talk
            sis "She is asking if you are going to get naked in front of others."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_angry_talk
            show sisexpression postnewsbreakfast_smirk_talk
            pov "Really?!"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_angry
            show sisexpression postnewsbreakfast_bored
            mum "W-well, are you?"

            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_angry_talk
            show sisexpression postnewsbreakfast_smirk
            pov "No, [missus]."

            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_confused_talk
            show sisexpression postnewsbreakfast_bored
            pov "I really just want to relax for a bit, maybe catch some sun on the way."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_smirk_talk
            pov "It’s not my fault that the only beach around happens to be nudist exclusive, you know?"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_looksis
            show povexpression postnewsbreakfast_embarrassed
            show sisexpression postnewsbreakfast_smirk
            mum "I-I know that!"

            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_bored
            mum "I was just making sure…"

            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookfood
            mum "Regardless, be sure to let me know when you arrive and decide to come back home."

            show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
            show eyespov postnewsbreakfast_looksis
            show sisexpression postnewsbreakfast_neutral_talk
            mum "Don’t stay too long and be sure to bring sunscreen, okay?"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_embarrassed_talk
            show sisexpression postnewsbreakfast_smirk
            pov "I will, [missus]. I promise."

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookfood
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_confused
            show sisexpression postnewsbreakfast_smirk_talk
            sis "Not gonna help ya treat the burns if you forget the sunscreen again, you goober."

            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_angry_talk
            show sisexpression postnewsbreakfast_smirk
            pov "Oh come on, that was one tim-"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
            show eyessis postnewsbreakfast_lookpov
            show povexpression postnewsbreakfast_angry
            show sisexpression postnewsbreakfast_shocked_talk
            sis "It was three times!"

            show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
            show eyespov postnewsbreakfast_lookmum
            show eyessis postnewsbreakfast_lookfood
            show povexpression postnewsbreakfast_shocked_talk
            show sisexpression postnewsbreakfast_smirk
            pov "All of them before we moved here, I know better now!"

            show eyespov postnewsbreakfast_looksis
            show eyessis postnewsbreakfast_lookmum
            show povexpression postnewsbreakfast_bored
            show sisexpression postnewsbreakfast_neutral
            mum "Regardless of that!"

    show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_angry_talk
    show sisexpression postnewsbreakfast_smirk_talk
    mum "Now how about we finish our breakfast so you kids can get started with your day?"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show povexpression postnewsbreakfast_angry
    show sisexpression postnewsbreakfast_smirk
    mum "I’ll deal with your [povdadrole] in the meantime."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_bored_talk
    sis "You sure that’s a good idea?"

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookfood
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_smirk_talk
    sis "Dealing with him on your own can be…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_bored
    mum "I know, sweetie."

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show povexpression postnewsbreakfast_bored
    show sisexpression postnewsbreakfast_bored_talk
    mum "But that man still needs somewhere to sleep, so he better be ready to cough up some answers if he plans to be sleeping under the same roof as us tonight!"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_embarrassed
    mum "Let me do my magic, I know well how to deal with him when he gets difficult."

    ##-If Missus has been romanced-
    if mum_path >= 31:

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused_talk
        show sisexpression postnewsbreakfast_embarrassed
        pov "Are you really sure about this?"

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_shocked_talk
        pov "I don’t want a repeat of last time…"

        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_confused
        mum "I’ll call you the moment he gets out of line, I promise."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_bored
        show sisexpression postnewsbreakfast_confused_talk
        sis "Am I missing something?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_confused
        mum "Nothing too important, sweetie."

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_bored
        show sisexpression postnewsbreakfast_shocked
        if winc == 0:
            mum "[povname] can deal with it just fine."
        else:
            mum "Your brother can deal with it just fine."

        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_confused
        mum "I know he can."

    ##=RESULT END=

    show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_confused_talk
    show sisexpression postnewsbreakfast_confused_talk
    sis "I don’t know, [missus]."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_confused
    show sisexpression postnewsbreakfast_bored_talk
    sis "I still don’t feel comfortable just leaving you with him like that."

    show eyespov postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_angry
    mum "I’ll be fine, trust me."

    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_shocked
    show sisexpression postnewsbreakfast_confused
    mum "It’s my turn to put my foot down."

    show eyespov postnewsbreakfast_looksis
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_confused_talk
    sis "Alright…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show eyespov postnewsbreakfast_lookfood
    show eyessis postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_embarrassed_talk
    sis "If you are sure…"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_embarrassed
    pov "Call us if he gets difficult, okay?"

    show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_neutral
    show sisexpression postnewsbreakfast_embarrassed_talk
    mum "I will."

    show eyespov postnewsbreakfast_lookmum
    show sisexpression postnewsbreakfast_neutral
    mum "Now let’s finish up and clean so you can get started with your day, okay?"

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
    show povexpression postnewsbreakfast_neutral_talk
    show sisexpression postnewsbreakfast_neutral_talk
    pov "Okay!"
    sis "Sure."

    show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
    show eyespov postnewsbreakfast_looksis
    show eyessis postnewsbreakfast_lookpov
    show povexpression postnewsbreakfast_embarrassed
    show sisexpression postnewsbreakfast_neutral
    mum "I love you two, truly."

    show eyespov postnewsbreakfast_lookmum
    show eyessis postnewsbreakfast_lookmum
    show povexpression postnewsbreakfast_embarrassed_talk
    show sisexpression postnewsbreakfast_neutral_talk
    pov "We love you too."
    sis "Yeah."

    ##-If Missus answered the phone-
    if parentsbedroommovie_threesome == 2:#had sis bed scene
        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_neutral_talk
        show sisexpression postnewsbreakfast_confused_talk
        sis "Oh, by the way, [missus]. Who was on the phone?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show sisexpression postnewsbreakfast_confused
        mum "Oh, it was so weird!"

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_embarrassed
        mum "Some creepy voice just started clicking out nonsense and telling me to turn on the tv!"

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_shocked_talk
        mum "Actually, they seemed to want to talk to you, [povname]?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked_talk
        show sisexpression postnewsbreakfast_confused
        pov "Talk to me?"

        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_smirk_talk
        sis "Who else would creeps be calling?"

        show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_shocked_talk
        show sisexpression postnewsbreakfast_bored_talk
        mum "Whoever it was, they kept saying they were a friend of yours?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_confused
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_bored
        mum "I’m not really sure."

        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_smirk
        mum "I assumed they had a cold or something since their voice was all rough and I could barely understand them."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_smirk_talk
        mum "I gave them your cell phone number since they were so adamant on talking to you."

        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_angry_talk
        show sisexpression postnewsbreakfast_bored
        mum "After that, they told me to turn on the tv and I completely zoned out into the news story."

        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_bored
        show sisexpression postnewsbreakfast_shocked_talk
        sis "Weird."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_smirk
        show sisexpression postnewsbreakfast_bored_talk
        sis "Do you have any sick friends, [povname]?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused_talk
        show sisexpression postnewsbreakfast_bored
        pov "Not that I know of."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_bored_talk
        pov "I’ll check with everyone later, maybe they just wanted to let me know about the security system thing?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show povexpression postnewsbreakfast_embarrassed
        mum "Well, let them know I thank them for giving us the heads up and that I hope they get better."

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused_talk
        show sisexpression postnewsbreakfast_smirk
        pov "Yeah, will do."

    #=RESULT END=
    elif parentsbedroommovie_threesome == 1:#had mum bed scene
    ##-If Sister answered the phone-
        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_neutral
        show sisexpression postnewsbreakfast_bored_talk
        mum "Oh, actually, before I forget."

        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused_talk
        show sisexpression postnewsbreakfast_bored
        mum "Who was on the phone, [sister]?"
        mum "Was it something important?"

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_confused_talk
        sis "Not entirely sure."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_shocked_talk
        sis "Some person started breathing heavily and told me to turn on the tv in a croaked voice."

        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_angry_talk
        sis "I was about to freak out until they told me they knew [povname]."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show povexpression postnewsbreakfast_shocked_talk
        show sisexpression postnewsbreakfast_smirk
        pov "They do?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_angry_talk
        sis "Yeah, they said they were a friend of yours and wanted to tell you to check on the news."

        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show sisexpression postnewsbreakfast_bored_talk
        sis "They must be sick as all hell since they sounded like their voice would leave them any second now."

        show bg postnewsbreakfast_pov_eats_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused_talk
        show sisexpression postnewsbreakfast_confused_talk
        mum "Oh, well that’s sweet of them!"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_confused
        mum "Are there any of your friends sick, [povname]?"

        show bg postnewsbreakfast_pov_eats_sis_eats_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused_talk
        pov "Not that I know of…"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_embarrassed_talk
        sis "Well, they seemed adamant on talking to you so I gave them your cell. Hope that’s okay."

        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_bored
        mum "Best to make sure who it is, still. Be sure to thank them, we would be completely ignorant of the news had they not warned us about it."

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookfood
        mum "They must hold you at quite the high regard if they thought of you while they are sick."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_neutral_talk
        pov "Yeah, I guess so."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show sisexpression postnewsbreakfast_neutral
        pov "I’ll be sure to thank them if they call."

    ##=RESULT END=
    elif parentsbedroommovie_threesome in (0,3):
    ##-If the Mc answered the phone-
        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_neutral
        show sisexpression postnewsbreakfast_bored_talk
        mum "Oh, before I forget, [povname]?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_neutral_talk
        show sisexpression postnewsbreakfast_bored
        pov "Yeah?"

        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_confused
        mum "Who was that on the phone?"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_confused_talk
        pov "…!"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_bored_talk
        sis "Yeah, you were speaking a bit loud there for a second but we couldn’t really make up what you were saying."

        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_confused_talk
        sis "Was it something important?"

        show eyespov postnewsbreakfast_looksis
        show povexpression postnewsbreakfast_shocked_talk
        show sisexpression postnewsbreakfast_shocked
        pov "U-Uh, no!"

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_shocked_talk
        show sisexpression postnewsbreakfast_confused_talk
        pov "No, not at all."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused_talk
        pov "It was just…"
        pov "Just some random guy selling something."

        show eyespov postnewsbreakfast_looksis
        show povexpression postnewsbreakfast_angry_talk
        show sisexpression postnewsbreakfast_bored
        pov "I got annoyed since they wouldn’t let me speak and decided to turn on the tv while he drone on about whatever he wanted."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_eats
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_bored_talk
        show sisexpression postnewsbreakfast_smirk_talk
        pov "I hung up when I saw the thing about the security system."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show povexpression postnewsbreakfast_embarrassed
        mum "Ugh, those are so annoying!"

        show bg postnewsbreakfast_pov_eats_sis_idle_mum_idle
        show povexpression postnewsbreakfast_embarrassed_talk
        mum "You kids are out most of the day, but you have no idea how many telemarketers call in the middle of the afternoon sometimes."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_smirk_talk
        sis "Sounds rough, [missus]."

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_neutral
        show sisexpression postnewsbreakfast_bored_talk
        mum "Sometimes it is, but I like to mess with them sometime."

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_confused
        show sisexpression postnewsbreakfast_bored
        mum "It can be quite fun!"

        show povexpression postnewsbreakfast_embarrassed_talk
        show sisexpression postnewsbreakfast_smirk
        pov "I-If you say so, [missus]."

        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_neutral_talk
        pov "Let’s continue eating shall we?"

        show bg postnewsbreakfast_pov_idle_sis_eats_mum_idle
        show eyespov postnewsbreakfast_lookfood
        show povexpression postnewsbreakfast_shocked_talk
        pov "Much to do and all that."

        show eyespov postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_neutral_talk
        mum "Oh, yes, of course!"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_eats
        show eyespov postnewsbreakfast_looksis
        show eyessis postnewsbreakfast_lookmum
        show povexpression postnewsbreakfast_shocked
        show sisexpression postnewsbreakfast_smirk_talk
        sis "I call seconds for the bacon!"

        show bg postnewsbreakfast_pov_idle_sis_idle_mum_idle
        show eyespov postnewsbreakfast_lookmum
        show eyessis postnewsbreakfast_lookpov
        show povexpression postnewsbreakfast_embarrassed
        show sisexpression postnewsbreakfast_neutral
        pov "…"

    ##=RESULT END=


    ##=SCENE END=
    $ main_story = 84

    jump lbl_pre_mission_briefing

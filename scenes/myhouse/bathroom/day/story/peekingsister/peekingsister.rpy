## Peeking Sister ##
label lbl_peeking_sister:
    default peekingsister_steam = 0

    scene black
    with fade

    menu:
        "Take a hot shower":
            $ peekingsister_steam = 1

            jump lbl_peeking_sister_hot
        "Take a cold shower":
            jump lbl_peeking_sister_cold

label lbl_peeking_sister_hot:

    scene bg peekingsister_1
    with fade
    show img peekingsister_steam_1
    with dissolve
    pov "{i}Damn.. I really needed this.{/i}"
    pov "..."
    show bg peekingsister_2
    pov "{i}I can't stop imagining...{/i}"
    show bg peekingsister_3
    pov "{i}I know I shouldn't, but...{/i}"
    show bg peekingsister_2
    pov "{i}That bear.{/i}"
    show bg peekingsister_4
    show img peekingsister_steam_2
    pov "{i}I wonder how often she does this? I wonder if I'll keep getting notifications and--Fuck.{/i}"
    show bg peekingsister_5
    sis "Hey! How's it going?"
    show bg peekingsister_6
    with hpunch
    pov "HEY! What the hell!"
    show bg peekingsister_7
    pov "I'm taking a shower here!"
    show bg peekingsister_8
    sis "So? Just wanted to check on you."
    show bg peekingsister_7
    pov "What's wrong with you, what do you want?"
    show bg peekingsister_8
    sis "What? Are you embarrassed?"
    show bg peekingsister_9
    sis "It's nothing I haven't seen before"
    show bg peekingsister_10
    pov "Yeah, like 10 years ago."
    show bg peekingsister_11
    sis "Hey, you came into my room and stripped the sheets right off me without a second thought."
    show bg peekingsister_8
    if winc == 0:
        sis "I told you I'd have my revenge, [povsisrole]."
    else:
        sis "I told you I'd have my revenge, baby brother."
    show bg peekingsister_7
    pov "Well, now you've seen me so, can you kindly... I don't know..."
    pov "Fuck off?"
    show bg peekingsister_8
    sis "Nope, not good enough, mister."
    show bg peekingsister_9
    sis "I want see the whole package."
    show bg peekingsister_11
    sis "The WHOLE package."
    show bg peekingsister_7
    pov "You sound like an absolute pervert right now."
    if winc == 0:
        pov "I'm telling [missus] to give you up to the sharks."
    else:
        pov "I'm telling Mom to give you up for adoption."
        show bg peekingsister_8
        sis "Funny, isn't that how you became part of the family?"
    show bg peekingsister_7
    pov "Fuckin'... Let me be, dude."
    show bg peekingsister_11
    sis "I'm not leaving until you move your hands."

    menu:
        "Show her your dick":
            jump lbl_peeking_sister_hot_1
        "Keep your dick hidden":
            jump lbl_peeking_sister_hot_2

label lbl_peeking_sister_hot_1:
    if sister_points <= 9:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    else:
        $ sister_points = 10
    show bg peekingsister_12
    pov "Fine!"
    pov "..."
    pov "And?"
    show bg peekingsister_13
    pov "Thoughts?"
    show bg peekingsister_14
    if winc ==0:
        sis "Baby baby [povsisrole], surprisingly impressive."
    else:
        sis "Baby baby brother, surprisingly impressive."
    show bg peekingsister_15
    sis "Is that just how big it is or are you a grower?"
    show bg peekingsister_16
    sis "Y'know what, don't answer that."
    show bg peekingsister_14
    sis "I'll leave you to your... fun."
    show bg peekingsister_13
    pov "I- I wasn't-"
    show bg peekingsister_14
    sis "Yeah, whatever, [povname]."
    show bg peekingsister_17
    $ renpy.pause()
    show bg peekingsister_0
    show img peekingsister_steam_1
    pov "..."
    pov "{i}I can't look at her the same way anymore.{/i}"

    jump lbl_peeking_sister_end

label lbl_peeking_sister_hot_2:
    show bg peekingsister_7
    pov "...Why?"
    show bg peekingsister_11
    sis "You've seen mine, I should see yours."
    show bg peekingsister_7
    pov "..."
    show bg peekingsister_11
    if winc == 0:
        sis "We're [povsisrole]s. So it's not weird, right?"
    else:
        sis "We're twins. So it's not weird, right?"
    show bg peekingsister_9
    if winc == 0:
        sis "I just wanted to see what a [povsisrole] vagina looks like as a boy."
    else:
        sis "I just wanted to see what a twin vagina looks like as a boy."
    show bg peekingsister_8
    sis "If that makes sense."
    show bg peekingsister_18
    pov "What kind of logic is that? Who thought of that?"
    show bg peekingsister_11
    sis "I have. And it's fine. Trust me."
    show bg peekingsister_8
    sis "What do you say, buddy boy?"
    sis "Do it for the fam?"
    show bg peekingsister_7
    pov "I don't know..."
    show bg peekingsister_9
    sis "Hmmm, well, just so you know, I've already had a good glance at it."
    show bg peekingsister_10
    pov "And?"
    show bg peekingsister_11
    sis "Can't really give an honest review of it until I get hands on with it."
    show bg peekingsister_9
    if winc == 0:
        sis "Hahaha, I'm joking! Jeez, [povname], don't get a boner in front of me."
    else:
        sis "Hahaha, I'm joking! Jeez, bro, don't get a boner in front of me."
    show bg peekingsister_11
    sis "Gross-ass-"
    sis "Don't use up all my nice moisturizing soap."
    show bg peekingsister_18
    pov "I'm not even considering it, you nasty!"
    show bg peekingsister_17
    $ renpy.pause()
    show bg peekingsister_0
    show img peekingsister_steam_1
    pov "{i}For fuck's sake..{/i}"
    pov "{i}...That smug look on her face is just... so goddamn hot.{/i}"

    jump lbl_peeking_sister_end

label lbl_peeking_sister_cold:

    scene bg peekingsister_1
    with fade
    pov "{i}Shit, this water is cold.{/i}"
    pov "{i}But it's helping.{/i}"
    show bg peekingsister_2
    pov "{i}It's helping debone my boner.{/i}"
    show bg peekingsister_3
    pov "..."
    show bg peekingsister_2
    pov "{i}Damn. That look in her eyes...{/i}"
    show bg peekingsister_4
    pov "{i}No, no. I can't think about it.{/i}"
    show bg peekingsister_5
    sis "Hey! How's it going?"
    show bg peekingsister_6
    with hpunch
    pov "HEY! What the hell!"
    show bg peekingsister_7
    pov "I'm taking a shower here!"
    show bg peekingsister_8
    sis "So? Just wanted to check on you."
    show bg peekingsister_7
    pov "What's wrong with you, what do you want?"
    show bg peekingsister_8
    sis "Oh, come on. Are you not embarrassed of anything?"
    show bg peekingsister_9
    sis "Afraid I might take a peek?"
    show bg peekingsister_11
    sis "You've seen me naked, remember? "
    show bg peekingsister_8
    sis "A tit for a tat."

    menu:
        "Show her your dick":
            jump lbl_peeking_sister_cold_1
        "Keep your dick hidden":
            jump lbl_peeking_sister_cold_2

label lbl_peeking_sister_cold_1:
    if sister_points <= 9:
        $ sister_points += 1
        $ renpy.notify("Your relationship with [sister] has increased")
    else:
        $ sister_points = 10
    show bg peekingsister_12
    pov "..."
    show bg peekingsister_13
    pov "..Your tits were pretty impressive."
    show bg peekingsister_14
    sis "Ha!"
    sis "Thanks. I'm proud of them."
    show bg peekingsister_15
    if winc == 0:
        sis "You should thank [missus] while you're at it."
    else:
        sis "You should thank Mom while you're at it."
    show bg peekingsister_12
    pov "..."
    pov "So?"
    pov "Any thoughts?"
    show bg peekingsister_20
    sis "Huh-"
    show bg peekingsister_19
    pov "...What? Don't just stare at it."
    show bg peekingsister_20
    sis "It's just..."
    show bg peekingsister_19
    pov "..."
    show bg peekingsister_15
    sis "Smaller, I guess."
    show bg peekingsister_13
    pov "Sma- aye!"
    pov "The shower is cold!"
    show bg peekingsister_15
    sis "Still."
    show bg peekingsister_12
    sis "Hmm.."
    show bg peekingsister_15
    sis "Well... Then you really should expect a surprise sometime soon."
    show bg peekingsister_14
    sis "I'm going to go downstairs. Maybe you should turn the faucet some, let your body relax."
    show bg peekingsister_15
    sis "I think you and your ‘little' buddy need it."
    show bg peekingsister_13
    pov "Don't call it little. I'll legit bitch slap you with it."
    show bg peekingsister_16
    sis "Ha, in your filthy dreams, you filthy pervert."
    show bg peekingsister_21
    sis "Seriously, I will fucking kill you."
    if sister_points >= 1:
        $ sister_points -= 1
    else:
        $ sister_points = 0
    show bg peekingsister_17
    $ renpy.pause()
    show bg peekingsister_0
    pov "..."
    pov "{i}Callin' me a pervert.. you're the one camming for assholes online.{/i}"

    jump lbl_peeking_sister_end

label lbl_peeking_sister_cold_2:
    show bg peekingsister_7
    pov "...Why?"
    show bg peekingsister_11
    sis "You've seen mine, I should see yours."
    show bg peekingsister_7
    pov "..."
    show bg peekingsister_11
    if winc == 0:
        sis "Don't be so weird about it. We're [povsisrole]s. It's only weird if you make it weird."
    else:
        sis "Don't be so weird about it. We're twins. It's only weird if you make it weird."
    show bg peekingsister_18
    pov "Whatever you say."
    show bg peekingsister_11
    sis "See? You're making it weird."
    show bg peekingsister_18
    if winc == 0:
        pov "I'm not the weird one pushing my [povsisrole] to show me his dick."
    else:
        pov "I'm not the weird one pushing my brother to show me his dick."
    sis "..."
    show bg peekingsister_8
    sis "C'mon, I dare you."
    show bg peekingsister_7
    pov "You can't just dare me and expect me to do it."
    sis "..."
    show bg peekingsister_9
    sis "Hmmm, well, just so you know, I've already had a good glance at it."
    show bg peekingsister_10
    pov "And?"
    show bg peekingsister_8
    sis "I really hope that's not how small it usually is."
    show bg peekingsister_7
    pov "Excuse, me. I'm taking a cold shower he-"
    show bg peekingsister_8
    sis "Sure, sure. Blame the water temperature, not your genetics."
    show bg peekingsister_7
    sis "..."
    show bg peekingsister_9
    sis "Want to prove me wrong?"
    show bg peekingsister_7
    pov "I-"
    show bg peekingsister_8
    if winc == 0:
        sis "Hahaha, I'm joking! Jeez, [povname], don't get a boner in front of me."
    else:
        sis "Hahaha, I'm joking! Jeez, bro, don't get a boner in front of me."
    show bg peekingsister_11
    sis "Oh, and don't use up all my nice moisturizing soap."
    sis "I'm cereal."
    show bg peekingsister_18
    pov "I'm not even considering it, you Judgy Judy."
    show bg peekingsister_17
    $ renpy.pause()
    show bg peekingsister_0
    pov "{i}That bitch.{/i}"
    pov "{i}...How bout I fuckin' shove my hard-on in your annoying face and tell me how small it is.{/i}"

    jump lbl_peeking_sister_end

label lbl_peeking_sister_end:

    scene bg mybathroom_day_open
    with fade
    $ sister_path = 6

    jump lbl_mybathroom_day_1

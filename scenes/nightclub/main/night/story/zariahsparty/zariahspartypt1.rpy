## ZARIAH'S PARTY Pt 1
label lbl_zariahs_party_pt1:
    default zarias_party_intro_seen = 0
    default zarias_party_jacob_start = 0
    default at_zarias_party_currently_jacob = 1
    default at_zarias_party_currently_phil = 0
    default at_zarias_party_currently_edward_and_zariah = 0
    default at_zarias_party_currently_luna_and_cole = 0
    default at_zarias_party_currently_ian_and_teghan = 0
    default zariahs_party_talking_phil = 0
    default zariahs_party_talking_edward_and_zariah = 0
    default zariahs_party_talking_luna_and_cole = 0
    default zariahs_party_talking_ian_and_teghan = 0
    default zariahs_party_talking_vip = 0
    default zariahs_party_talking_steve = 0
    default has_been_caught_peeping_at_zariahs_party_vip_room = 0
    #-Scene takes place on saturday-

    #-The scene has 2 stages, the introduction and the individual talking to
    # characters, after the Introduction the characters you can choose to talk
    # to will be listed in bold-

    #-In order to continue the scene from the preparation stage to the actual
    # party, the player has to talk to Jacob and Agree to discuss the “Wingman”
    # strategy once again, which will take time so the scene will transition to the actual party-

    #-The Mc arrives at the nightclub early where most of the people that have
    # been personally invited already arrived. The Mc is soon greeted by Zariah
    # at the door as she is in the middle of doing preparations-

## INTRO
    if not zarias_party_intro_seen:
        $ principallashley_path = 23.5
        scene bg nightclub_nightempty with fade
        show pov smirk_talk at left
        with dissolve
        show zar neutral at right
        with dissolve
        pov "Huh, a lot less people than I expected..."
        show pov neutral_talk at left
        pov "Hey, Zariah!"
        show pov neutral at left
        show zar shocked_talk at right
        zar "Dude, you actually came!"
        show zar smirk_talk at right
        zar "Here I was expecting you to come up with some excuse about Lashley or something."
        show pov embarrassed_talk at left
        show zar smirk at right
        pov "Ehehe…"
        pov "W-Well, I couldn't just leave you hanging like that."
        show pov smirk_talk at left
        show zar embarrassed at right
        pov "You did ask me personally to come after all."
        show pov smirk at left
        show zar confused_talk at right
        zar "I-I did, didn't I?"
        show zar smirk_talk at right
        zar "Sorry about that, I didn't want you to think I was pressuring you into coming here or anything."
        show pov shocked_talk at left
        show zar smirk at right
        pov "N-No! No, not at all!"
        show pov embarrassed_talk at left
        show zar embarrassed at right
        pov "I'm more than happy to be here and I'm here because I want to be."
        show pov embarrassed at left
        show zar embarrassed_talk at right
        zar "You are really sweet…"
        show zar neutral_talk at right
        zar "I honestly appreciate that."
        show pov smirk_talk at left
        show zar neutral at right
        pov "It's my pleasure."
        pov "Besides, you said I'd get to experience your new music live, so there's no way I'm gonna miss that!"
        show pov smirk at left
        show zar neutral_talk at right
        zar "Oh, I guarantee it's gonna knock your socks off!"
        show pov shocked at left
        show zar smirk_talk at right
        zar "Not only are you guys listening to the new songs I’ve composed for the EP, but also some remixes of some of my older songs I’ve made with some of my surviving equipment so that the event is even longer!"
        zar "You are about to get the complete Karma experience!"
        show pov smirk_talk at left
        show zar neutral at right
        pov "I can’t wait, then!"
        show pov confused_talk at left
        show zar embarrassed at right
        pov "Though, I assumed more people would show up."
        show pov smirk at left
        show zar embarrassed_talk at right
        zar "Oh, they are coming later."
        show pov shocked at left
        show zar smirk_talk at right
        zar "I asked the people I actually invited to the private show to come earlier since I wanted to make sure you could get comfortable first."
        show pov embarrassed at left
        show zar shocked_talk at right
        zar "Soon enough this whole place is gonna be packed to be a proper rave!"
        show pov embarrassed_talk at left
        show zar embarrassed at right
        pov "Didn’t you say before that you could get in trouble for that?"
        show pov smirk at left
        show zar embarrassed_talk at right
        zar "In normal circumstances, yes."
        show pov neutral at left
        show zar neutral_talk at right
        zar "But since we are doing this to raise funds for my van, Steven gave me the okay to move forward on this turning into an actual party."
        zar "He is going to only be serving people non-alcoholic drinks if they don’t have an I.D. though."
        show pov neutral_talk at left
        show zar smirk at right
        pov "So, a normal business night, for him?"
        show pov neutral at left
        show zar smirk_talk at right
        zar "Pretty much, but with a few cameras, perhaps not as many people and with a good cause behind it!"
        show pov smirk_talk at left
        show zar shocked at right
        pov "As good a reason as any to have a party, I suppose."
        show pov smirk at left
        show zar shocked_talk at right
        zar "It’s not a-!"
        show zar bored_talk at right
        zar "Well…"
        show zar embarrassed_talk at right
        zar "I guess I can’t say it’s not a party at this point, eh?"
        show pov neutral at left
        show zar neutral_talk at right
        zar "Regardless, it’s gonna be fun and I plan to boost it all over social media."
        zar "Speaking of, let’s take a selfie of the two of us later!"
        show pov embarrassed at left
        show zar smirk_talk at right
        zar "Record in history the moment you were in one of my first raves featuring only music I’ve made."
        show pov smirk_talk at left
        show zar smirk at right
        pov "Sure! It’ll be something to prove to my kids that I met the world famous Karma when she was just starting out."
        show pov smirk at left
        show zar shocked_talk at right
        zar "Or for you to sell online for mad stacks of cash!"
        show pov embarrassed_talk at left
        show zar shocked at right
        pov "That too, I suppose."
        show pov smirk at left
        show zar smirk_talk at right
        zar "Hehehe, alright, I’ll catch you later."
        zar "I have a lot more stuff yet to prepare before we can kick this off."
        show pov neutral_talk at left
        show zar smirk at right
        pov "Don’t let me stop you, though I’ve been meaning to ask."
        show pov confused_talk at left
        pov "Why have us come so early since we could have just arrived with everyone else?"
        show pov confused at left
        show zar embarrassed_talk at right
        zar "I told you dude, so that I could make sure the people I wanted to come to the event indeed came."
        zar "Say hello to friends, hang out a little with everyone before the whole place gets crowded with people who just want to party and all that jazz."
        show pov embarrassed at left
        show zar smirk_talk at right
        zar "And because I knew you would get a ton of shit at the door from the bouncer I hired for the event."
        show pov embarrassed_talk at left
        show zar bored at right
        pov "Right, you never went into detail about that."
        show pov embarrassed at left
        show zar smirk_talk at right
        zar "Ugh, I really didn’t want to stoop down to that but I’m kinda desperate and I know he is able to keep people out or kick them out if they are making too much of a mess."
        zar "Plus, he was happy to do it in exchange of just a social media boost, so I didn’t need to invest extra money on actual security."
        zar "I just hope I don’t regret it in the long run…"
        show pov confused_talk at left
        show zar smirk at right
        pov "Jeez, just who did you hire?"
        show pov shocked at left
        show zar bored_talk at right
        zar "Phil."
        show pov bored_talk at left
        show zar smirk at right
        pov "Dang... Well let’s just hope he doesn’t make too much of a scene if he does have to kick people out."
        show pov smirk at left
        show zar smirk_talk at right
        zar "That’s the most we can hope for from him."
        zar "He is gonna be busy by the door so he isn’t going to be bothering anyone I actually invited, but if you need to head out for whatever reason, I recommend you use one of the other exits that lead to the alley."
        zar "And if you need to come back in then just text someone inside you know to let Phil know you are coming back in."
        show pov smirk_talk at left
        show zar smirk at right
        pov "I’ll keep it in mind, thanks for the heads up, Zariah."
        show pov smirk at left
        show zar neutral_talk at right
        zar "No problem, dude."
        show pov shocked at left
        show zar smirk_talk at right
        zar "Try to keep yourself busy for a bit."
        show pov embarrassed at left
        show zar neutral_talk at right
        zar "You can hang out with everyone else for a while until I finish setting up with Edward and we can get this show started."
        zar "Again, I’m really happy you could make it."
        show pov neutral_talk at left
        show zar embarrassed at right
        pov "I’m really glad to be here."
        pov "Wouldn’t want to be anywhere else."
        show pov neutral at left
        show zar smirk_talk at right
        zar "Try not to get too lost in the crowd, I’ll dedicate you a song or two."
        zar "See you later, dude!"
        show pov neutral_talk at left
        show zar smirk at right
        pov "Later!"
        show pov shocked_talk at left
        hide zar smirk at right
        with dissolve
        #-Zariah leaves the scene-
        show pov smirk_talk at left
        pov "Alright, I should find Jacob to talk about the whole wingman thing."

        #=Introduction End=

        $ zarias_party_intro_seen = 1
        $ at_zarias_party_currently_jacob = 1

    jump lbl_nightclub_zariahs_party_setup


## MAIN AREA
label lbl_nightclub_zariahs_party_setup:
    scene bg nightclub_nightempty
    show btn nightclub_night_bar_idle
    if at_zarias_party_currently_jacob:
        show btn_zariahs_party_jacob_idle2
    if at_zarias_party_currently_ian_and_teghan:
        show btn_zariahs_party_ianteghan_idle2
    call screen scr_nightclub_zariahs_party

screen scr_nightclub_zariahs_party():

    imagebutton auto "btn nightclub_night_dancefloorempty_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclubdancefloor_zariahs_party_setup")
    imagebutton auto "btn nightclub_night_vip_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_vip")
    imagebutton auto "btn nightclub_night_bar_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_steve")

    if at_zarias_party_currently_jacob:
        imagebutton auto "btn zariahs_party_jacob_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_jacob")
    if at_zarias_party_currently_ian_and_teghan:
        imagebutton auto "btn zariahs_party_ianteghan_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_ian_and_teghan")

    imagebutton auto "btn nightclub_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_exit_zariahs_party_setup")
    #use hud_overlay

## DANCE FLOOR
label lbl_nightclubdancefloor_zariahs_party_setup:
    scene bg nightclubdancefloor_nightempty
    if at_zarias_party_currently_phil:
        show btn_zariahs_party_phil_idle2
    if at_zarias_party_currently_edward_and_zariah:
        show btn_zariahs_party_edwardzariah_idle2
    if at_zarias_party_currently_luna_and_cole:
        show btn_zariahs_party_lunacole_idle2
    call screen scr_nightclubdancefloor_zariahs_party

screen scr_nightclubdancefloor_zariahs_party():

    imagebutton auto "btn nightclubdancefloor_night_mainarea_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclub_zariahs_party_setup")

    if at_zarias_party_currently_phil:
        imagebutton auto "btn zariahs_party_phil_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_phil")
    if at_zarias_party_currently_edward_and_zariah:
        imagebutton auto "btn zariahs_party_edwardzariah_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_edward_and_zariah")
    if at_zarias_party_currently_luna_and_cole:
        imagebutton auto "btn zariahs_party_lunacole_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_zariahs_party_luna_and_cole")

    #imagebutton auto "btn nightclubdancefloor_night_zariah_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_nightclubdancefloor_night_zariah")
    #use hud_overlay

## EXIT
label lbl_exit_zariahs_party_setup:
    pov "I probably shouldn't leave early."

    jump lbl_nightclub_zariahs_party_setup

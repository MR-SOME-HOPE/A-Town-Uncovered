label lbl_wine_heist:
    scene bg mykitchen_night with fade
    ##[Home, Kitchen,  After School– “Wine Heist” – misslashley_path = 15]

    #-You arrive to the kitchen and start looking for the wine reserves-
    show pov confused_talk at left
    with dissolve
    pov "Steve says that 'Nom de Vin Prétentieux' is a common cooking wine…"
    show pov smirk_talk at left
    pov "If I’m lucky, we’ll have some around the house…"
    show pov shocked at left
    show sis smirk_talk at right
    with dissolve
    sis "You are not finding the wine there."
    show pov shocked_talk at left
    show sis smirk at right
    pov "Gah! Where did you come from?!"

    #-next reply is a variant depending on the status of relationship with sister-

    #-If Sister has not been romanced-
    if sister_path < 36:
        show pov shocked at left
        show sis smirk_talk at right
        sis "Obviously from upstairs."
        show pov bored at left
        show sis bored_talk at right
        sis "You can’t really be sneaky when all cupboards are facing the stairs, you know?"
        show pov embarrassed_talk at left
        show sis bored at right
        pov "Ah, yes…"
        show sis smirk at right
        pov "I forgot about that…"

        #=RESULT END=


    #-If Sister has been Romanced-
    elif sister_path >= 36:
        show pov shocked at left
        show sis embarrassed_talk at right
        sis "Was hoping to catch a peek of you in the shower!"
        show pov embarrassed at left
        show sis smirk_talk at right
        sis "I know I can ask anytime for you to lose the clothes now, but there’s still a bit of fun from watching you without clothes when you don’t expect me."
        show pov embarrassed_talk at left
        show sis smirk at right
        pov "How often do you do this?"
        show pov embarrassed at left
        show sis smirk_talk at right
        sis "Now, where’s the fun in revealing my secrets just like that?"
        show pov smirk_talk at left
        show sis smirk at right
        pov "You could just get in and join me in the shower, you know?"
        show pov neutral at left
        show sis smirk_talk at right
        sis "Again, where’s the fun in that?"

    #-Back to normal-
    show pov shocked at left
    show sis bored_talk at right
    sis "So, what are you up to?"
    show pov embarrassed_talk at left
    show sis confused at right
    pov "N-Nothing really."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "You are really about to try that with me?"
    show sis smirk_talk at right
    sis "You know I grew up with you right?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Come on, spill!"
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "It’s… Kind of a long story…"
    show pov shocked at left
    show sis smirk_talk at right
    sis "Running errands for people again?"
    show pov shocked_talk at left
    show sis bored at right
    pov "Okay, maybe not as long as I thought."
    show pov bored at left
    show sis confused_talk at right
    sis "You are not getting along with a bad crowd are you?"
    show pov confused at left
    show sis smirk_talk at right
    sis "Not a lot of people ask you to sneak out booze from the house."
    show pov shocked_talk at left
    show sis shocked at right
    pov "It’s not like that!"
    show pov bored_talk at left
    show sis confused at right
    pov "She needs it for religious purposes."
    show pov bored at left
    show sis smirk_talk at right
    sis "Is that what you kids call it these days?"
    show pov angry_talk at left
    show sis smirk at right
    pov "You aren’t that older!"
    show pov angry at left
    show sis neutral_talk at right
    sis "I’m kidding, but that still sounds sketchy as all hell."
    show pov bored at left
    show sis embarrassed_talk at right
    sis "Are you sure you aren’t being tricked here?"
    show pov smirk at left
    show sis smirk_talk at right
    sis "Don’t want my baby bro to be behind bars because he got caught simping for some girl or something."
    show pov smirk_talk at left
    show sis shocked at right
    pov "I’m not simping for anybody!"
    show pov bored_talk at left
    show sis smirk at right
    pov "And trust me here, I know what I’m doing."
    show pov confused_talk at left
    show sis bored at right
    pov "So could you give me a break and tell me where the 'Nom de Vin Prétentieux' is?"
    show pov confused at left
    show sis smirk_talk at right
    sis "That pretentious sounding wine that [missus] uses to cook?"
    show pov shocked at left
    show sis bored_talk at right
    sis "Dude, you are simping yourself out getting a girl booze and you are being so cheap you can’t even get your hands on quality booze?"
    show pov angry at left
    show sis smirk_talk at right
    sis "For shame, bro!"

    #-If Sister has been romanced-
    if sister_path >= 36:
        show pov shocked at left
        show sis angry_talk at right
        sis "You better not start taking me out on cheap dates because of it!"
        show pov embarrassed at left
        show sis sad_talk at right
        sis "I love you and all, but all I ask you is to make an effort to show you love me back from time to time!"
        #=RESULT END=

    show pov angry_talk at left
    show sis smirk at right
    pov "I’m telling you it isn’t like that!"
    show pov smirk_talk at left
    show sis bored at right
    pov "They are a super lightweight and the only thing that resembles the expensive wine they like is this thing!"
    show pov bored at left
    show sis bored_talk at right
    sis "Okay, okay! No need to get defensive!"
    show pov shocked at left
    show sis smirk_talk at right
    sis "I know what you are going through, I actually used the same wine to get used to the taste of alcohol."
    show pov confused_talk at left
    show sis smirk at right
    pov "You actually did?"
    show pov shocked at left
    show sis neutral_talk at right
    sis "Yeah, little did I know that thing has the same level of alcohol of a strong mouthwash, so you can imagine little old me’s surprise when she almost passed out after her second shot of tequila."
    show pov confused_talk at left
    show sis confused at right
    pov "When did that happen?"
    show pov confused at left
    show sis confused_talk at right
    sis "I have a life outside of the house too, you know? You are not the only one who runs around town meeting people."
    show pov confused_talk at left
    show sis smirk at right
    pov "Okay, Fair enough."
    show pov bored_talk at left
    show sis neutral at right
    pov "So, are you going to tell [missus] I’m taking this?"
    show pov embarrassed at left
    show sis smirk_talk at right
    sis "Not if you keep quiet about me taking all of the spare sponges under the sink."
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "Why do you need all the sponges under the sink?"
    show pov shocked at left
    show sis bored_talk at right
    sis "I also get requested weird shit by friends, what did I just tell you?!"
    show pov embarrassed_talk at left
    show sis bored at right
    pov "Oh, right."
    show pov neutral_talk at left
    show sis smirk at right
    pov "Sorry, my bad."

    if povsisrole == "brother":
        show pov smirk at left
        show sis smirk_talk at right
        sis "So, twin secret?"
        show pov smirk_talk at left
        show sis neutral at right
        pov "Twin secret."
    else:
        show pov embarrassed at left
        show sis bored_talk at right
        sis "So, secret?"
        show pov embarrassed at left
        show sis smirk at right
        pov "Secret."

    show pov embarrassed at left
    show sis neutral_talk at right
    sis "Good!"
    show pov neutral at left
    show sis smirk_talk at right
    sis "Now let's bounce before [missus] comes over and finds us."

    #Mom: (from upstairs and out of frame)
    show pov shocked at left
    show sis shocked at right
    mum "Kids? Is that you talking downstairs?"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Uhh- Yeah!"
    show pov shocked at left
    sis "Just asking [povname] to go get some ice cream!"
    show pov shocked_talk at left
    show sis shocked at right
    pov "What?"
    show pov angry at left
    show sis embarrassed at right
    mum "Tell him to get me some creamy white filling flavour!"
    show pov bored at left
    show sis embarrassed_talk at right
    sis "You heard the woman, off you go!"
    show pov bored_talk at left
    show sis smirk at right
    pov "Y-Yeah, later!"

    $ principallashley_path = 12

    $ inventory.add(Items.cookingwine)

    jump lbl_mykitchen_night_setup

    #=SCENE END=

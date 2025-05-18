## Three Staged Breakfast
label lbl_three_staged_breakfast:
    if mowed_lawn == 1:
        scene bg mydiningroom_day
    else:
        scene bg mydiningroom_day_grassy

    ## Sprites start
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right zorder 50
    with dissolve
    #"You are coming down the stairs rather earlier than usual to the smell of a delicious Mom made breakfast"

    pov "{i}*Sniff sniff*{/i} Is that…?"
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, good morning, honey!"
    mum "Sit down, I made breakfast."
    show pov neutral_talk at left
    show mum neutral at right
    pov "What’s the occasion?"
    pov "I mean, I appreciate it, but this is quite unusual for you."
    pov "I can’t remember the last made one of your famous three-stage breakfasts."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Well, I figured that the two of you have been through a lot lately, so I wanted to give you a good start to your morning."
    ## hide mum's sprite without any effect
    ## sister sprite enters
    show sis neutral_talk at Position(xpos=1300) zorder 1
    with dissolve
    ## show mum again withou any effect
    show mum neutral at right
    ## this is so that mum is layered in front of sister's sprite

    sis "Well, as long as you cooked my favorite breakfast -sausage omelette- then I can’t complain! "
    sis "It tastes WAY better when YOU cook them!"
    show pov neutral at left
    show sis neutral at Position(xpos=1300)
    show mum smirk_talk at right
    mum "The secret is love, baby. Love."
    show pov neutral at left
    show sis neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Come on, mini-mes, sit down before it gets cold."

    ## CG Starts
    ## bg threestagedbreakfasts_x
    scene bg threestagedbreakfast_1
    with fade
    mum "I hope this helps at making you feel better."
    show bg threestagedbreakfast_2
    if winc == 0:
        pov "It really does, [missus], thank you."
    else:
        pov "It really does, mom, thank you."
    show bg threestagedbreakfast_3
    mum "So, any big plans for the weekend, you two?"
    show bg threestagedbreakfast_4
    sis "Nothing on my end, just another boring weekend home."
    show bg threestagedbreakfast_7
    mum "What about you, [povname]?"
    show bg threestagedbreakfast_5
    pov "I’m free so far, haven’t really made plans with anyone other than working on my project."
    show bg threestagedbreakfast_6
    sis "Nerd."
    show bg threestagedbreakfast_8
    mum "Oh, leave him alone, [sister]."
    show bg threestagedbreakfast_9
    mum "That’s wonderful!"
    mum "I am glad you are taking such a serious look at your studies, [povname]."
    show bg threestagedbreakfast_10
    mum "But if you have some time free after working on the project, I figured we could all do something together."
    if winc == 0:
        show bg threestagedbreakfast_11
        sis "What about [dadname]?"
        show bg threestagedbreakfast_12
        mum "Your [dadrole] is busy with work, I already asked him earlier this morning."
        show bg threestagedbreakfast_13
        mum "To be honest, it’s not a huge loss."
        show bg threestagedbreakfast_14
        mum "I was hoping it would only be the three of us anyway."
        show bg threestagedbreakfast_15
        sis "Damn, [missus]."
    else:
        show bg threestagedbreakfast_11
        sis "What about dad?"
        show bg threestagedbreakfast_12
        mum "Your father is busy with work, I already asked him earlier this morning."
        show bg threestagedbreakfast_13
        mum "To be honest, it’s not a huge loss."
        show bg threestagedbreakfast_14
        mum "I was hoping it would only be the three of us anyway."
        show bg threestagedbreakfast_15
        sis "Damn, Mom."
    sis "Kind of cold against him, isn’t it?"
    show bg threestagedbreakfast_16
    mum "Well, he has been quite the party pooper lately."
    show bg threestagedbreakfast_17
    mum "And I wanted to spend some time with my two favorite people in the world."
    show bg threestagedbreakfast_18
    if winc == 0:
        mum "So if your [dadname] has a problem, well then he can sleep outside for all I care."
    else:
        mum "So if your dad has a problem, well then he can sleep outside for all I care."
    show bg threestagedbreakfast_19
    pov "Sounds good to me!"
    show bg threestagedbreakfast_20
    sis "Yeah!"
    if winc == 0:
        show bg threestagedbreakfast_21
        sis "What do you want to do, [missus]?"
        show bg threestagedbreakfast_22
        mum "Well, I was thinking maybe have some take out, watch a movie or two and maybe play some board games, perhaps some puzzles."
        show bg threestagedbreakfast_23
        mum "Like we used to do when you two were little."
        show bg threestagedbreakfast_24
        pov "That sounds really nice, [missus]."
    else:
        show bg threestagedbreakfast_21
        sis "What do you want to do, Mom?"
        show bg threestagedbreakfast_22
        mum "Well, I was thinking maybe have some take out, watch a movie or two and maybe play some board games, perhaps some puzzles."
        show bg threestagedbreakfast_23
        mum "Like we used to do when you two were little."
        show bg threestagedbreakfast_24
        pov "That sounds really nice, Mom."
    show bg threestagedbreakfast_25
    sis "Beats anything I’ve been doing lately."

    if sister_path >= 10:
        show bg threestagedbreakfast_26
        sis "Besides, we already have a fort on our basement, so it will totally be like back then!"
    show bg threestagedbreakfast_27
    sis "Sure, Let’s do it!"
    show bg threestagedbreakfast_28
    mum "I am so glad you kids are on board!"
    show bg threestagedbreakfast_29
    mum "I’ve been dying to have a day off like this with you two for a long time now."
    show bg threestagedbreakfast_30
    if winc == 0:
        sis "You could have asked earlier, [missus]."
    else:
        sis "You could have asked earlier, Mom."
    show bg threestagedbreakfast_31
    pov "Yeah, It’s not like we are going to say ‘No’. We loved doing this."
    show bg threestagedbreakfast_32
    pov "It’s actually a shocker that it’s taken us this long to get back into it."
    show bg threestagedbreakfast_33
    pov "I guess lots have been going on lately between all of us."
    show bg threestagedbreakfast_34
    sis "Here here."
    show bg threestagedbreakfast_35
    pov "And as long as you make sure ‘Cheaty McCheat Cheatington’ over here doesn’t sit anywhere near the bank, I am down for a few games of Monopoly."
    show bg threestagedbreakfast_36
    sis "Oh, you are such a crybaby!"
    show bg threestagedbreakfast_37
    sis "I didn’t cheat, you bought the freakin railroads!"
    show bg threestagedbreakfast_38
    sis "What kind of moron does that?!"
    show bg threestagedbreakfast_39
    pov "Shut up!"
    show bg threestagedbreakfast_40
    pov "It’s a valid strategy that pays up in the long run!"
    show bg threestagedbreakfast_41
    sis "Yet you somehow managed to keep losing?"
    show bg threestagedbreakfast_42
    mum "Ok, Monopoly is definitely off the table in this house."
    if winc == 0:
        show bg threestagedbreakfast_43
        sis "Don’t feel bad, [missus]."
        show bg threestagedbreakfast_44
        sis "That game was made to break households apart."
        show bg threestagedbreakfast_45
        pov "It’s the curse of greed, [missus]."
    else:
        show bg threestagedbreakfast_43
        sis "Don’t feel bad, Mom."
        show bg threestagedbreakfast_44
        sis "That game was made to break families apart."
        show bg threestagedbreakfast_45
        pov "It’s the curse of greed, Mom."
    show bg threestagedbreakfast_46
    mum "I’ll have something else ready by then."
    show bg threestagedbreakfast_47
    mum "Now hurry up and eat, [povname]."
    show bg threestagedbreakfast_48
    mum "You are going to be late."
    show bg threestagedbreakfast_49
    pov "Sure thing!"

    $ main_story = 51

    jump lbl_mykitchen_day_setup

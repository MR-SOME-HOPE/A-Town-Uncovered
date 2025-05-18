default failed_strike_a_pose = False

label lbl_strike_a_pose:
    #[Comic Book Store Backroom, Afternoon - “Strike a Pose”  - hitomi_path = 8

    #[Scene takes place automatically after the first one with Mc traveling into
    # the backroom of the comic book store which has been repurposed as an impromptu
    # art studio for Hitomi

    ## SPRITEWORK

    if not failed_strike_a_pose:
        scene bg comicbookbackroom_day
        show pov neutral at left
        show hit shocked_talk at right
        with fade
        hit "Ah, [povname]!"
        show hit embarrassed_talk at right
        hit "I was starting to think you weren’t going to come."

        show pov embarrassed_talk
        show hit bored
        pov "Yeah, sorry about the delay, I got a bit caught up with Lord Kev and the guys in the front of the store."

        show pov smirk
        show hit confused_talk
        hit "Yeah, they weren’t happy when I asked to use the back room for today."
        hit "Especially when I added the note on the curtain to keep everyone else out."

        show pov confused_talk
        show hit confused
        pov "Were they having a tournament or playing a game today or something?"
        show hit bored
        pov "They were quite upset!"

        show pov embarrassed
        show hit bored_talk
        hit "No, I just don’t think they have anywhere else to hang out, and they’ve made this place kind of their second home."
        show pov neutral
        show hit neutral_talk
        hit "A lot of the furniture and decor was actually donated by them and other regulars, to make this whole space more comfy for everybody."

        show pov neutral_talk
        show hit neutral
        pov "Well, that’s nice of them."

        show pov embarrassed
        show hit bored_talk
        hit "Yeah, but they do hoard the place to themselves far too much."
        hit "And I have to reign them in sometimes when new clients are coming in to play some board games or something."
        show pov neutral
        show hit neutral_talk
        hit "But enough of all that - I’m really happy you actually came!"

        show pov smirk_talk
        show hit embarrassed
        pov "You certainly look excited. And here I was, thinking you were going to back out at the last second or something."

        show pov smirk
        show hit embarrassed_talk
        hit "Well, after you left, I saw some exercises that people usually use models for and went down the rabbit hole of the whole practice."
        show hit shocked_talk
        hit "I’m definitely really excited at the potential benefits this will have for my art!"
        show hit embarrassed_talk
        hit "I really can’t thank you enough for doing this for me."

        show pov neutral_talk
        show hit embarrassed
        pov "Don’t sweat it. I’m happy to help!"
        pov "Besides, it’s just modeling, it’s not that difficult of a thing to do."

        show pov neutral
        show hit embarrassed_talk
        hit "I’m really glad you see it that way."
        show pov confused
        show hit neutral_talk
        hit "Alright, I marked the position for you to stand in."

        show pov confused_talk
        show hit neutral
        pov "Right over there, right?"

        show pov neutral
        show hit neutral_talk
        hit "Right!"
        hit "I also set a place for your clothes, so stand on the mark as soon as you strip and we can begin!"

        show pov neutral_talk
        show hit neutral
        pov "Yeah, no proble-"
        show pov shocked_talk
        show hit shocked
        with hpunch
        pov "Wait, did you say 'Strip'?"

        show pov shocked
        show hit confused_talk
        hit "Yes, naturally."
        show hit embarrassed_talk
        hit "The best kind of modeling is Nude Modeling, after all."

        show pov shocked_talk
        show hit confused
        pov "We never said anything about nude modeling!"

        show pov shocked
        show hit confused_talk
        hit "I thought it was implied?"
        show hit embarrassed_talk
        hit "I mean, you were sounding so confident about it, that I figured that’s what you meant by it!"

        show pov shocked_talk
        show hit confused
        pov "I thought you just wanted me in different poses for you to trace over!"

        show pov shocked
        show hit bored_talk
        hit "First of all, it’s not tracing, it’s using Reference. Very different things."
        show hit embarrassed_talk
        hit "And second of all, I’m trying to learn raw anatomy right now."
        hit "It won’t be helping my sketches much if I’m also sketching the volume of your clothes when making a body, right?"
        show pov embarrassed
        show hit sad_talk
        hit "Please don’t tell me you are getting cold feet NOW. I’ve worked really hard to prepare for all this!"

        show pov embarrassed_talk
        show hit sad
        pov "I-I’m not getting cold feet, here!"
        show hit shocked
        pov "If anything, I’m just really surprised you are so okay with this."
        pov "I thought you would be all embarrassed over the whole thing."

        show pov embarrassed
        show hit embarrassed_talk
        hit "Well… truth be told, I was quite nervous when I was preparing all of this, but once I saw the benefits of the exercise-"
        hit "-I got really excited for what I can potentially learn!"
        hit "Besides, I’ve seen you go to the beach all the time, anyway. And you gotta strip in order to get in and mess around, right?"
        hit "We are literally across the street from it, so there’s no big deal about you doing it in a private room, right?"

        show pov embarrassed_talk
        show hit embarrassed
        pov "Well, yeah. But it’s that street of distance that separates welcomed nudity to a felony, in my experience…"

        show pov sad
        show hit sad_talk
        hit "I won’t hold it against you if you wanna back out…"

        show pov shocked_talk
        show hit shocked
        pov "No, no! I’ll do it."
        show pov embarrassed_talk
        show hit embarrassed
        pov "You just surprised me, is all."
        pov "Let me strip down and we can begin."

        hide pov
        with dissolve

        #-Mc fades from the scene to indicate him changing but he is still talking
        #to Hitomi as she turns around in the meantime to give him some privacy as
        #he gets ready-

        show hit embarrassed_talk
        hit "Thank you so much for this, [povname]. I really don’t know where to begin to thank you for all you’ve done for me!"

        show hit embarrassed
        pov "Don’t sweat it. I’m honestly happy to help out and get you out of that sour mood."
        pov "How’s your first webcomic coming along, by the way?"

        show hit embarrassed_talk
        hit "It’s doing okay!"
        hit "Getting steady views and nicer comments as I tell some of my life stories working as the cashier of a comic book shop."
        hit "I actually announced my new webcomic yesterday and had a whole small chapter where you come in to lend me help with modeling and all!"

        show hit embarrassed
        pov "Really? Hope you drew me in a flattering way, then!"

        show hit embarrassed_talk
        hit "I kept your features overall hidden, since I figured you didn’t want any of my readers in town to figure out it’s you who is helping me out with this."

        show hit embarrassed
        pov "I appreciate that."

        #-MC reappears on the scene now naked-

        show povn embarrassed_talk at left
        with dissolve
        show hit shocked
        pov "Alright, so, what, do I just stand in the spot and strike a pose?"

        #-Hitomi turns around with a cheerful expression-

        show povn embarrassed
        show hit shocked_talk
        hit "Yeah! Let’s start off with-"

        #-Hitomi’s expression changes to that of shock upon seeing the MC-

        hit "With…"
        hit "…"
        show povn confused
        hit "Woah…"

        show povn confused_talk
        show hit shocked
        pov "Uhhh… Hitomi?"

        show povn confused
        hit "Hmm?"

        show povn embarrassed_talk
        pov "I don’t mind you staring, considering you are going to be drawing and all, but shouldn’t I get on a pose first?"

        show povn embarrassed
        show hit shocked_talk
        hit "What?"
        show hit embarrassed_talk
        hit "Oh! Um, right!"
        hit "Sorry about that, It’s just… It kind of dawned on me that I have you actually naked in front of me - and all alone in a room…"

        show povn smirk_talk
        show hit shocked
        pov "It just dawned on you now?!"

        show povn embarrassed
        show hit embarrassed_talk
        hit "I-I’m sorry! I kept looking at it in a cold analytical manner, and didn’t realize you would… you know… really BE naked until now!"

        show povn embarrassed_talk
        show hit shocked
        pov "Should I put my clothes back on, or…?"

        show povn shocked
        show hit shocked_talk
        hit "N-No!" with hpunch
        show hit embarrassed_talk
        hit "No, it’s fine!"
        hit "I do see how having you naked will help with me getting used to drawing silhouettes."
        show povn embarrassed
        hit "And help me with some other things…"

        show povn confused_talk
        show hit shocked
        pov "What was that?"

        show povn smirk
        show hit shocked_talk
        hit "N-Nothing! Nothing at all, just thinking out loud!"
        show hit embarrassed_talk
        hit "L-Let’s just start, OK?"
        show povn neutral
        hit "Get on the spot and I’ll guide you on which positions to get on."
        hit "I need to focus, so… can you try not to get… you know…"
        hit "Hard…?"

        show povn embarrassed_talk
        show hit embarrassed
        pov "Alright, I’ll try my best, then…"

label skip_strike_a_pose:
    scene bg strikeapose_1
    show img strikeapose_pov_1
    with fade

    #-Fade to black to indicate the MC and Hitomi getting ready. Mc is posing on
    # a small pedestal while Hitomi is sitting at a distance with her drawing tablet
    # on hand and sketching him away. Have the curtains of the backroom visible
    # for when Jacob pops in-
    #[The following minigame comes in order to check whether or not the MC gets a
    #boner upon modeling for Hitomi. Each round it will take 2 stamina points off
    #the Mc for 3 rounds for a total of 6 stamina points. The Mc must avoid thinking
    #of Hitomi while also enduring for long enough for the session to end]
    #-The following dialogue comes up within the MC’s head-

    ## CG

    pov "{i}Alright… Just gotta focus on keeping Mini-Me down and hang on until Hitomi’s satisfied. Come on, [povname]. Focus!{/i}"

    menu menu_strike_a_pose_1:
        "Think about Hitomi's Ass":
            pov "{i}Oh no- don't- don't- don't think-!{/i}"
            scene bg strikeapose_7
            with dissolve
            pov "{i}Fuck!{/i}"
            pov "{i}What an ass though...{/i}"
            pov "{i}Man, what I'd do to have her sit on my face.{/i}"
            pov "{i}I wonder what they look like bouncing on my-{/i}"
            scene bg strikeapose_10
            show img strikeapose_pov_1
            with hpunch
            jump skip_pov_strike_a_pose_erection

        "Think about the nature of one’s existence" if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2

    show bg strikeapose_1
    show img strikeapose_pov_1

    hit "Hmmmm~"
    show bg strikeapose_6
    hit "Alright-"
    show bg strikeapose_1
    hit "..."
    show bg strikeapose_6
    hit "Okaaaaay-"
    show bg strikeapose_5
    hit "Don't move, [povname]. Keep that position."
    show bg strikeapose_3
    hit "Mhmm..."
    show bg strikeapose_5
    hit "Hmm- I never noticed that part of the body."
    show bg strikeapose_6
    hit "Okie dokie..."
    show bg strikeapose_1
    hit "..."
    show bg strikeapose_2
    hit "...."
    show bg strikeapose_6
    hit "Alright!"
    hit "Next pose please."

    show bg strikeapose_1
    show img strikeapose_pov_2
    with dissolve

    menu menu_strike_a_pose_2:
        "Think about Hitomi’s Breasts":
            pov "{i}Oh no- don't- don't- don't think-!{/i}"
            scene bg strikeapose_7
            with dissolve
            pov "{i}Fuck!{/i}"
            pov "{i}What a cute set though...{/i}"
            pov "{i}Man, what I'd do to suck on them.{/i}"
            pov "{i}I wonder how hard her nip-{/i}"
            scene bg strikeapose_10
            show img strikeapose_pov_1
            with hpunch
            jump skip_pov_strike_a_pose_erection

        "Think about the mortality of a crab" if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2

    show bg strikeapose_6
    hit "Awesome- That's great."
    show bg strikeapose_5
    hit "Woops- okie, I'm just gonna ignore that line."
    show bg strikeapose_3
    hit "Hmmmmm..."
    show bg strikeapose_5
    hit "Is that- okay, got it."
    show bg strikeapose_1
    hit "Mhmm~"
    show bg strikeapose_6
    hit "Ah-huh~"
    show bg strikeapose_5
    hit "Wait- is that attached-"
    show bg strikeapose_3
    hit "..."
    show bg strikeapose_6
    hit "ahh okay!"
    show bg strikeapose_5
    hit "So that's that muscle..."
    show bg strikeapose_6
    hit "There!"
    hit "Next pose please, [povname]."

    show bg strikeapose_1
    show img strikeapose_pov_3
    with dissolve

    menu menu_strike_a_pose_3:
        "Think about Hitomi’s Lips":
            pov "{i}Oh no- don't- don't- don't think-!{/i}"
            scene bg strikeapose_7
            with dissolve
            pov "{i}Fuck!{/i}"
            pov "{i}What a tight looking pussy though...{/i}"
            pov "{i}Man, what I'd do to slip my cock in between them.{/i}"
            pov "{i}I wonder how tight she really is-{/i}"
            scene bg strikeapose_10
            show img strikeapose_pov_1
            with hpunch
            jump skip_pov_strike_a_pose_erection

        "Think about the fact the player doesn’t know we are watching them" if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2

            show bg strikeapose_6
            hit "Awesome- That's great."
            show bg strikeapose_5
            hit "Woops- okie, I'm just gonna ignore that line."
            show bg strikeapose_3
            hit "Hmmmmm..."
            show bg strikeapose_5
            hit "Is that- okay, got it."
            show bg strikeapose_4
            hit "Mhmm~"
            show bg strikeapose_5
            hit "Ah-huh~"
            show bg strikeapose_6
            hit "Wait- is that attached- ahh okay!"
            show bg strikeapose_5
            hit "So that's that muscle..."
            show bg strikeapose_1
            hit "..."
            show bg strikeapose_6
            hit "There!"
            hit "I think that should be it!"

            jump skip_pov_strike_a_pose_success

    #-If at any point the player chooses one of the options involving Hitomi or
    # runs out of Stamina-

    #-The Mc gets a boner-

label skip_pov_strike_a_pose_erection:
    hit "Kyaaah!"
    hit "[povname]! Do you have a-"
    hit "-A boner?!"

    show bg strikeapose_11
    show img strikeapose_pov_1
    pov "Oh God! I’m so sorry!"

    show bg strikeapose_12
    hit "No, no, no! It’s fine, it’s fine, it’s fine!"
    hit "I’m the one putting you in this position to begin with."
    show bg strikeapose_13
    hit "Um… I’m going to let you deal with that, and we can continue another day…"

    show bg strikeapose_14
    pov "I’m so sorry about this, Hitomi."

    show bg strikeapose_12
    hit "I-It’s fine, really! I don’t mind. And I understand it’s natural and all…"
    hit "Plus it’s not like I mind seeing it and-"
    show bg strikeapose_10
    hit "GAH, WHAT AM I SAYING?!"
    hit "I’M SORRY, I HAVE TO GO!"

    scene black with fade

    $ failed_strike_a_pose = True
    $ hitomi_path = 7.1

    jump lbl_comicbookstore_day

# label skip_pov_strike_a_pose_exhausted:
#     pov "…"
#     pov "{i}Damnit…{/i}"
#     pov "{i}I really need to focus here!{/i}"
#     pov "{i}I should also work on my Stamina for next time…{/i}"
#     pov "{i}For now, let’s put my clothes back on and get out of here…{/i}"
#
#     #-Fade to black as the MC changes-
#
#     scene black with fade
#
#     $ failed_strike_a_pose = True
#     $ hitomi_path = 7.1
#
#     jump lbl_comicbookstore_day

label skip_pov_strike_a_pose_success:
    #-If the player chooses all options that don’t involve Hitomi and doesn’t run
    # out of Stamina-

    show bg strikeapose_15
    show img strikeapose_pov_1
    with dissolve

    hit "Alright, [povname]. We are almost done here for today."
    hit "I got the preliminary poses I wanted, for now. And I think we can stop for now once I finish this one."
    hit "How are you feeling?"

    show bg strikeapose_16
    pov "A bit stiff on the shoulders but nothing too bad."

    show bg strikeapose_15
    hit "This has been a wonderful exercise, [povname]. I really can’t thank you enough for all of this."
    hit "I doubt I would have managed to get these poses as easily online and I really wasn't able to pay for an actual model."

    show bg strikeapose_16
    pov "I keep telling you, Hitomi. Don’t mention it."
    show bg strikeapose_14
    pov "It really wasn’t a problem and I’m happy to help. You don’t have to make it up to me."

    show bg strikeapose_12
    hit "I-I know, but I still feel like I should do something, since you’ve been so nice and supportive of me."
    hit "A-Actually, while I was sketching your silhouette, I was thinking…"

    show bg strikeapose_14
    pov "Yeah?"

    show bg strikeapose_13
    hit "M-Maybe I shouldn’t really be asking this now, considering the circumstances…"
    show bg strikeapose_12
    hit "B-But would you like to go out and grab something to eat sometime or-"

    #-Hitomi is interrupted by the sound of Jacob’s voice from beyond the curtain-

    scene bg comicbookstore_day
    show povn shocked flip
    show hit shocked at right
    with dissolve
    jac "Yo, [povname]. You in here, bro?" with hpunch

    show povn shocked_talk flip
    show hit shocked
    pov "J-Jacob?!"

    #-Jacob opens the curtains and gets in-
    show jac smirk_talk flip at left
    show povn shocked flip
    show hit shocked
    jac "Dude, you gotta come quick! They released the new volume of-"
    show jac shocked_talk flip
    show povn shocked flip
    show hit shocked
    jac "SWEET MOTHER OF NAKED JESUS!"

    show jac shocked flip
    show povn angry_talk flip
    show hit shocked
    pov "JACOB, WHAT THE HELL?!!"

    show povn angry flip
    show hit angry_talk
    hit "DIDN’T YOU READ THE 'DO NOT DISTURB' SIGN?!!"

    show jac shocked_talk flip
    show povn shocked flip
    show hit angry
    jac "THERE’S NOTHING ON THE CURTAIN! IT MUST HAVE FALLEN OFF!"
    show jac embarrassed_talk flip
    show povn sad flip
    show hit sad
    jac "I’M SO SORRY FOR INTERRUPTING! I’LL LET YOU GUYS GET BACK ON IT! I WAS NEVER HERE!"

    #-Jacob leaves the room red in the face closing the curtain behind him-
    hide jac
    hide povn
    with dissolve

    hit "..."

    show povn sad at left
    with dissolve
    show hit sad_talk
    hit "JACOB WAIT, DON’T MISUNDERSTAND THINGS!"

    show povn sad_talk
    show hit sad
    pov "No use, he is gone…"

    show povn sad
    show hit sad_talk
    hit "Oh God. What am I gonna do?!"
    hit "I don’t want any weird rumors to spread - and Jacob is literally incapable of keeping his mouth shut!"

    show povn embarrassed_talk
    show hit sad
    pov "Don’t worry, I’ll stop him next time I see him and explain things to him."

    show povn embarrassed
    show hit shocked_talk
    hit "Please do!"
    show hit sad_talk
    hit "Gosh, I’m not going to be able to look him in the eye again after this!"

    show povn embarrassed
    show hit embarrassed_talk
    pov "I think you’ll be fine. I mean, I’m the one that’s naked, you know?"

    show povn shocked
    show hit embarrassed_talk
    hit "F-Fair point… Could you please put some clothes on before anyone else tries to drop in?"
    hit "I’ll get out there and make sure the curtain is closed. And figure out a way to keep the sign from falling, for next time…"

    show povn embarrassed_talk
    show hit embarrassed
    pov "Sounds good. I’ll be right out."

    show povn embarrassed
    show hit embarrassed_talk
    hit "T-Thank you again, [povname]."
    hit "A-And please talk to Jacob as soon as you can."

    show povn embarrassed_talk
    show hit embarrassed
    pov "Will do. Don’t worry."

    #-Hitomi leaves the room as the MC gets dressed and the scene fades to black-

    scene black
    with fade
    $ hitomi_path = 8

    jump lbl_comicbookstore_day

    #-In order to repeat the minigame if the Player failed, the Player will need
    # to approach hitomi in a different day and try again until they succeed and
    # go through the other ending of the scene in order to continue the storyline-

    #-If the player succeded then the scene continues as normal-

    #=SCENE END=

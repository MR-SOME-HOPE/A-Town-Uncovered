## A Sacrifice for Vi
default a_sacrifice_for_vi = "pov"

label lbl_a_sacrifice_for_vi:
    #-Scene starts with Mc and Effie bursting out the door to the storage garage
    # and starting to run as fast as they can away from Vi, who is gonna start
    # counting before giving chase. Jacob is already in front of them as he had
    # been waiting for them to get out so they could escape together, he takes
    # the Front point of the group with Mc on the Middle and Effie on the back
    # while holding onto the MC's hand-

    scene bg asacrificeforvi_1
    with hpunch

    jac "Dudes!"
    jac "You guys aren't gonna believe it, Edward and I crafted this quick MacGyver style trap with the crowbar so I wouldn't have to be near the short circuit and-"

    pov "Jacob, not the time! Run faster!"

    jac "W-What? Why?!"

    edw "Guys, what's wrong!"

    eff "It's her! The woman of the lake!"
    eff "She was on the Storage unit and knows we are here!"

    "Jacob & Edward" "WAIT, WHAT?!"

    # -Vi is gonna start a countdown off screen as the group tries to run away-

    scene bg asacrificeforvi_2

    vi "I'm gonna start counting now, [povname]! I hope you can get away on time~"
    vi "10~"

    scene bg asacrificeforvi_3

    pov "Edward, what's the fastest way out of here?!"

    edw "J-Just head forward towards the exit point!"
    edw "All the guards around the area seemed to have headed somewhere else so you guys are in the clear!"

    eff "Wait, all of the guards are gone as soon as the power goes out?!"

    scene bg asacrificeforvi_2

    vi "9~"

    scene bg asacrificeforvi_3

    jac "Dude! This is Not the time to look at a gift horse in the mouth!"
    jac "Not when we have a ghost chick with the hots for [povname] after us!"

    eff "But what if this is a trap?!"

    jac "I'm pretty sure SHE IS THE TRAP!"

    scene bg asacrificeforvi_2

    vi "8~"

    scene bg asacrificeforvi_3

    pov "Edward, pack everything right now and run!"
    pov "You have all our evidence, head to the safe house and make sure you aren't followed!"

    edw "I-I'm on it! "
    edw "I'll see you guys there!"

    scene bg asacrificeforvi_2

    vi "7~"

    scene bg asacrificeforvi_3

    jac "Just what the hell did you guys find in there?!"

    eff "Not enough time to explain, not the right place to do so either!"
    eff "Just keep running!"

    jac "But what does she even want?!"

    scene bg asacrificeforvi_2

    vi "6~"

    scene bg asacrificeforvi_3

    pov "Me, Jacob! She wants me, one way or another!"
    pov "She wants to take me back to her Mistress. The woman that tried to kill me!"

    jac "Wait, so the Sex World and all that happened to you was actually real?!"

    eff "Can we discuss this later?!"

    scene bg asacrificeforvi_2

    vi "5~"

    scene bg asacrificeforvi_3

    jac "Wait, but where do we go from here?!"
    jac "Do we even have another lead to keep investigating?!"

    pov "Let's lose the crazy lake psycho and live enough to worry about that!"

    eff "We are almost at the turning point for our exit!"

    scene bg asacrificeforvi_2

    vi "4~"

    scene bg asacrificeforvi_3

    jac "We are gonna make it, we are actually going to make it!"

    eff "We still need to jump the fence and then head to our safe house so don't go calling victory yet!"

    pov "We might be able to lose her if we get out of here by the time she finishes counting!"

    scene bg asacrificeforvi_2

    vi "3, 2, 1, GO!"

    scene bg asacrificeforvi_3

    pov "Son of a bitch-!"

    # -the group looks back and watches as from the open gate of the Storage Garage,
    # where Vi is standing menacingly, she jumps into the air like a bat out of
    # hell, bouncing and running over the rooftops of the storage units and quickly
    # gaining on them before doing a final big jump into the air before dropping
    # like a ton of bricks and creating a crater on the ground just behind them-

    #-from the ground, she then reaches forward and manages to grab Effie's ankle
    # hard, making her fall to the ground only to be stopped by the MC who is
    # still holding her hand, with Jacob too far forward to do anything about it-

    scene bg asacrificeforvi_4
    $ renpy.pause(1,hard=True)
    scene bg asacrificeforvi_5
    $ renpy.pause(0.4,hard=True)
    scene bg asacrificeforvi_6_0
    $ renpy.pause(0.8,hard=True)
    scene bg asacrificeforvi_6_1
    $ renpy.pause(0.3,hard=True)
    scene bg asacrificeforvi_6_2
    $ renpy.pause(0.7,hard=True)
    scene bg asacrificeforvi_7

    eff "AHHHHHH!"

    scene bg asacrificeforvi_8
    $ renpy.pause(1,hard=True)
    scene bg asacrificeforvi_9
    with vpunch

    pov "EFFIE!"

    vi "You are coming back to my Mistress' side, [povname]... Whether it is right now by your own accord or when you come looking for her!"

    pov "Let her go, you crazy bitch!"

    vi "We can do this the easy way or the hard way, [povname]!"
    vi "You know exactly what I want and if you won't give it to me, then I'll take it the hard way and take something you care about in the process!"

    scene bg asacrificeforvi_10

    eff "[povname], let me go!"

    pov "W-What are you-?!"

    eff "If she gets you it's all over!"
    eff "Let me go and run!"

    jac "Effie, Don't-"

    eff "Don't get any closer, Jacob!"
    eff "Just take [povname] and get out of here!"

    pov "Effie, No… Y-You can't-"

    eff "It's ok…"
    eff "I know you'll come get me. Just let go…"

    pov "I- I..."

    #-This is a major choice where the ending of it will change some of the events in the future scenes-

    menu:
        "Let Effie go":
            jump lbl_a_sacrifice_for_vi_effie
        "Sacrifice yourself":
            jump lbl_a_sacrifice_for_vi_yourself


label lbl_a_sacrifice_for_vi_effie:
    $ a_sacrifice_for_vi = "eff"

    eff "It's ok-"
    eff "I wasn't really gonna leave you the opportunity to choose anyway."

    pov "Wha-"
    #-Effie proceeds to free herself from the MC's grip before pushing him back
    # into the floor-

    scene bg asacrificeforvi_11

    pov "Effie, don't!"

    #-Vi takes the opportunity to jump towards Effie once again, Wrapping her
    # arms around her in a suggestive way-

    scene bg asacrificeforvi_12

    vi "Ahhh, so it's gonna be the hard way then, [povname]?"
    vi "That's more than okay, but I hope you can live with the consequences~"

    scene bg asacrificeforvi_13

    pov "No, let her go!"
    pov "Let her go right now!"

    #-Vi jumps with her mechanical strength once again, this time taking Effie
    # with her before reappearing in the roof of the storage unit with Effie on her arms-

    scene bg asacrificeforvi_12

    vi "Nope~"
    vi "You don't want to come with me on your own volition so I'll take her instead. I'm sure we can find a really nice place for her~"

    pov "Just let her go and I'll go with you!"

    vi "Awww, if only you had agreed to that when you had the chance!"
    vi "I'm afraid that you have been shown an unacceptable level of disobedience and as your future owner, I need to make sure you understand the consequences that come with disobedience~"

    scene bg asacrificeforvi_13

    pov "You crazy fucking bitch, just let her go!"

    vi "If you want her, you'll have to come get her yourself. You know where to find us, darling~"
    vi "And I hope for her sake that you are more willing to obey the orders of our Mistress by then…"

    scene bg asacrificeforvi_12

    eff "It's fine, you guys!"
    eff "Just get out of here!"

    vi "Ooooooooh, she is a feisty one!"
    vi "I love that type of woman, you and I are gonna have a lot of fun~"

    eff "What did you do to my Mom you crazy whore?!"

    vi "Your mom?"
    vi "Wait a second, you are…"
    vi "My my, I thought I made it clear when you were a kid that you shouldn't be poking your nose where it doesn't concern you, yet here you are again~"
    vi "And you became quite the woman too!"
    vi "Nice plump butt, cute breasts and lips I can't wait to make use of~"

    eff "Answer me!"
    eff "{i}*Gasp*{/i}"

    vi "Everything in due time honey!"

    eff "{i}*Struggled breaths*{/i}"

    vi "Don't worry, I'm gonna show you exactly what happened to her, but just to make sure you don't try anything funny before I put the strap on-"

    #-Vi chokes her out and she passes out-

    scene bg asacrificeforvi_13

    pov "EFFIE!"

    vi "Don't worry you two, she'll live."
    vi "But I'm afraid our time is up~"

    jac "You aren't gonna get away with this, you heard me?!"

    pov "Just you wait you crazy bitch,"
    pov "I'll come get her and make you pay for all of this!"

    scene bg asacrificeforvi_12

    vi "Oh my sweet, sexy and stupid [povname]..."
    vi "You coming to get her is exactly what I want you to do~"
    vi "Bye-Bye now~"

    #-Vi zips away as if glitched out of existence-

    scene bg asacrificeforvi_13

    pov "EFFIE!!!"

    #=CHOICE END=

    $ main_story = 122

    jump lbl_letting_effie_go


label lbl_a_sacrifice_for_vi_yourself:
    $ a_sacrifice_for_vi = "pov"

    pov "I'm sorry, Effie…"

    eff "It's okay-"
    eff "I wasn't really gonna leave you the opportunity to-"

    pov "Forgive me for this!"

    scene bg asacrificeforvi_10
    $ renpy.pause(0.5,hard=True)
    scene bg asacrificeforvi_16
    $ renpy.pause(0.5,hard=True)
    scene bg asacrificeforvi_14

    #-The Mc interrupts Effie by pulling her with all of his strength from Vi's
    # grasp and pushing her into safety only for him to fall back as Vi jumps at
    # him, wrapping her arms around him in a dominant way-

    vi "Good, you picked the easy way!"
    vi "Now I won't have to punish you as harshly~"

    scene bg asacrificeforvi_15

    eff "WAIT, DON'T!"

    jac "[povname]!"
    jac "Let her go you crazy bitch!"

    scene bg asacrificeforvi_14

    pov "I'm sorry guys… This is my mess and I won't get you caught up in the crossfire."

    vi "Look at him trying to play the hero~"
    vi "Goddess, the things I want to do to you!"

    # -Vi jumps with her mechanical strength once again, this time taking Mc with
    # her before reappearing in the roof of the storage unit with him on her arms-

    eff "Give him back you whore, you already had me!"

    vi "Oh, I'm sorry honey. Trust me, I would love to take you with us but I'm afraid he is the priority and I can't go wasting an opportunity like this where he jumps right into my loving arms!"

    pov "You already have me, don't get them involved with this!"

    vi "Oh, [povname]. That's not for you to decide silly!"

    scene bg asacrificeforvi_15

    eff "You are not taking him! You are not taking someone else precious to me, you hear me?!"

    vi "My~ You certainly got yourself a feisty girlfriend, didn't you? I like that~"

    pov "Leave her out of this!"

    scene bg asacrificeforvi_14

    pov "{i}*Gasp*{/i}"
    pov "{i}*Struggled breaths*{/i}"

    vi "Don't worry, she'll join us eventually. But for now though~"

    #-Vi chokes out the MC-

    jac "[povname]!"

    vi "The way I see it, you two have only two choices."
    vi "You either forget what you saw today and get yourselves safe for a couple more weeks."
    vi "Or you can try and come get him if you care about him so much~"
    vi "I'll warn you though, you may be stumbling into something you are definitely not ready for."

    scene bg asacrificeforvi_15

    eff "Just you wait! I'll make you pay for this, you hear me?!"
    eff "I'm going to make you regret all of this!"

    vi "Oh you can try, honey!"
    vi "I love it when they fight back!"

    scene bg asacrificeforvi_14

    vi "Say good-bye now~"
    vi "And we'll be waiting for you, at the bottom of the lake~"

    #-Vi zips away as if glitched out of existence-

    scene bg asacrificeforvi_15

    eff "[povname]!!!"

    #=SCENE END=

    $ main_story = 127
    $ insexworld = 1

    $ gtime = 0

    call lbl_next_date

    jump lbl_a_sacrifice_for_vi_checkdate

label lbl_a_sacrifice_for_vi_checkdate:
    if day >= 5:
        call lbl_next_date
    else:
        pass

    jump lbl_did_my_friends_save_me

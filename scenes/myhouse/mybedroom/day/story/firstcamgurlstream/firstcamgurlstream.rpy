## First Camgurl Stream ##
label lbl_first_camgurl_stream:
    define usn = Character("[usname]", color="#5e8fb4")
    if winc == 0:
        jump lbl_first_camgurl_stream_winc0

    scene bg firstcamgurlstream_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_2
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_1
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_3
    sis "Yesterday I only managed to get six inches deep..."
    sis "Do you think I can take more today?"
    show bg firstcamgurlstream_1
    pov "..."
    show bg firstcamgurlstream_2
    pov "... Holy shi-"
    show bg firstcamgurlstream_1
    sis "Hehehehe... Mmm. It's so tasty."
    show bg firstcamgurlstream_3
    sis "Later on I'm going to unwrap a brand new toy. Do you want to see it?"
    show bg firstcamgurlstream_4
    sis "Mmm..."
    show bg firstcamgurlstream_3
    sis "I can see some of you are on trial accounts. You better sign up for realsies or you'll miss our party."
    show bg firstcamgurlstream_1
    pov "{i}This cannot really be [sister].{/i}"
    show bg firstcamgurlstream_3
    sis "Hehehe!"
    show bg firstcamgurlstream_2
    pov "{i}...Looks like her. Sort of sounds like her. But those clothes... That look...{/i}"
    show bg firstcamgurlstream_1
    pov "{i}Fuck..{/i}"
    show bg firstcamgurlstream_3
    pov "{i}I've seen her naked. How can this be affecting me so much more than that?{/i}"
    sis "Ooh, I'm just too excited. I've got to open my present!"
    show bg firstcamgurlstream_0
    $ renpy.pause()

    menu:
        "Register an account and pay for viewtime" if inventory.money >= 40:
            $ inventory.money -= 40
            $ renpy.notify("You paid $40")

            jump lbl_first_camgurl_stream_1
        "I don't have enough money":
            pov "{i}Fuck, I don't have any money on me right now.{/i}"
            pov "{i}It's not like I can come back here at a later date.{/i}"
            pov "..."
            pov "{i}No wonder she doesn't want me to know what she does for a job...{/i}"
            pov "..."
            pov "Wow..."
            pov "This is a lot to process right now."
            pov "I need a shower, I can't get that image out of my mind."

            jump lbl_first_camgurl_stream_end
        "Quit out" if inventory.money >= 40:
            jump lbl_first_camgurl_stream_2

label lbl_first_camgurl_stream_1:
    scene bg firstcamgurlstream_0_4

    python:
        usname = renpy.input("")
        usname = usname.strip()
        if not usname:
            usname = "Hugh_GeeCock"

    show bg firstcamgurlstream_3
    sis "So, since you have all given me so many lovely gifts, I had to take a poll to decide what you might most like me to get myself."
    show bg firstcamgurlstream_5
    sis "But I finally settled on this guy."
    show bg firstcamgurlstream_6
    $ renpy.pause(1.5,hard=True)
    show bg firstcamgurlstream_7
    sis "Captain Cuddles."
    sis "Isn't he so cute?"
    show bg firstcamgurlstream_8
    sis "He's very naughty, too. Aren't you, Captain Cuddles?"
    show bg firstcamgurlstream_9
    sis "Yes, I know you are..."
    show bg firstcamgurlstream_10
    sis "And I know you're eager..."
    show bg firstcamgurlstream_11
    sis "Oh, you bad little bear. You're already getting me wet... Can you see?"
    show bg firstcamgurlstream_12
    sis "I always feel somewhat uncomfortable when they get like this..."
    show bg firstcamgurlstream_11
    sis "Do you mind, Captain Cuddles? Of course not, naughty bear."
    show bg firstcamgurlstream_13
    "{i}Bzzzzz{/i}"
    show bg firstcamgurlstream_14
    sis "He says that he'd rather snack on me instead of cake..."
    sis "Captain Cuddles is very insistent that I let him celebrate my unbirthday."
    pov "{i}...Wow.. the bear's actually vibrating pretty violently.{/i}"
    show bg firstcamgurlstream_13
    sis "Oooh, Captain Cuddles... You're a naughty, naughty bear."
    sis "But so soft... Mmmm..."
    show bg firstcamgurlstream_15
    $ renpy.pause()
    show bg firstcamgurlstream_16
    $ renpy.pause()
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)

    menu:
        "Try to enter her room":
            jump lbl_first_camgurl_stream_3
        "Keep watching":
            jump lbl_first_camgurl_stream_4

label lbl_first_camgurl_stream_2:
    pov "{i}No, I can't just watch her. She's my sister.{/i}"
    pov "{i}How the hell am I supposed to look her in the eye after this.{/i}"
    pov "..."

    menu:
        "I've got too see this." if inventory.money >= 40:
            pov "{i}Fuck it, I've got to see this.{/i}"

            jump lbl_first_camgurl_stream_1
        "No wonder she doesn't want me to find out what she does.":
            pov "{i}No wonder she doesn't want me to know what she does for a job...{/i}"
            pov "..."
            pov "Wow..."
            pov "This is a lot to process right now."
            pov "I need a shower, I can't get that image out of my mind."

            jump lbl_first_camgurl_stream_end

label lbl_first_camgurl_stream_3:
    show bg firstcamgurlstream_18
    pov "{i}I wonder if I can get into her room.{/i}"
    show bg firstcamgurlstream_17
    pov "..."
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    sis "Oh, Cuddles--You're going too far. I'm not going to be able to hold myself bac-"
    "{i}*Knock knock*{/i}"
    show bg firstcamgurlstream_19
    sis "..."
    show bg firstcamgurlstream_20
    sis "What?"
    show bg firstcamgurlstream_19

    menu:
        "What are you doing?":
            pov "Hey, what are you doing?"
            show bg firstcamgurlstream_20
            sis "I'm busy, go away!"
        "Are you in there?":
            pov "Hey, are you in there?"
            show bg firstcamgurlstream_20
            sis "Yeah, but I'm kinda busy! Go away!"
        "I need something.":
            pov "Hey, I need something in your room!"
            show bg firstcamgurlstream_20
            sis "I'm busy! Get it later!"
        "Mom's calling you.":
            pov "Hey, Mom's calling for you."
            show bg firstcamgurlstream_20
            sis "Tell her I'm busy at the moment!"
    show bg firstcamgurlstream_21
    sis "{i}That's my brother...{/i}"
    show bg firstcamgurlstream_19
    pov "Can I come i-"
    show bg firstcamgurlstream_20
    sis "I said I'm busy! Go away!"
    show bg firstcamgurlstream_19
    pov "With what?"
    show bg firstcamgurlstream_20
    sis "None of your business!"
    show bg firstcamgurlstream_19
    pov "..."
    sis "..."
    show bg firstcamgurlstream_21
    sis "I think he's gone."
    show bg firstcamgurlstream_18
    pov "{i}No, I'm not 'LittleBowPeep'. I'm still here on my laptop.{/i}"
    show bg firstcamgurlstream_22
    sis "Sorry, honeys. I had some- erm.. technical difficulties."
    show bg firstcamgurlstream_23
    sis "But I guess I should really be apologizing to Captain Cuddles, shouldn't I?"
    show bg firstcamgurlstream_22
    sis "Sorry, about that little hiccup guys but it's time I take this public stream to my VIP stream."
    show bg firstcamgurlstream_18
    pov "What?!"
    show bg firstcamgurlstream_17
    sis "Nawww, don't be sad, guys. I'll be on again soon."
    show bg firstcamgurlstream_18
    pov "But I just..."
    show bg firstcamgurlstream_22
    sis "As for my special subscribers, I'll see you in our private tea party stream."
    sis "Byee~!"
    show bg firstcamgurlstream_0_2
    pov "Damnit. She blue balled me. I think I need a shower."
    pov "That got me a little more worked up than I thought."

    jump lbl_first_camgurl_stream_end

label lbl_first_camgurl_stream_4:
    show bg firstcamgurlstream_18
    sis "Yes... Oh... Oh..."
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    pov "{i}I think she might be having an actual orgasm.{/i}"
    show bg firstcamgurlstream_24
    sis "Mmmm. Ah.. I- I feel all tingly inside, guys."
    show bg firstcamgurlstream_17
    pov "{i}You're not the only one.{/i}"
    show bg firstcamgurlstream_24
    sis "Mmmmffmm... I'm gonna... I- I'm.."
    show bg firstcamgurlstream_25
    sis "Ahhh... fuu--mmff. C-Captain Cuddles, you n-naughty bear."
    show bg firstcamgurlstream_17
    sis "{i}*Huff huff*{/i}"
    show bg firstcamgurlstream_22
    sis "This was a wonderful Unbirthday gift."
    show bg firstcamgurlstream_26
    sis "{i}You're welcome, Babykins... You taste like cupcakes and rainbows.{/i}"
    show bg firstcamgurlstream_27
    sis "Hehehehe, silly Cuddles."
    sis "But we can't leave the rest of our guests out of the fun, can we?"
    sis "I think it's time for a cuddle party with everyone..."
    show bg firstcamgurlstream_28
    $ renpy.pause(1.5,hard=True)
    show bg firstcamgurlstream_29
    $ renpy.pause(5,hard=True)
    show bg firstcamgurlstream_30
    $ renpy.pause(0.4,hard=True)
    show bg firstcamgurlstream_31
    $ renpy.pause()
    show bg firstcamgurlstream_32
    sis "Mmm, that was fun. But now I'm going to have some extra special fun with those of you who want to have a private tea party..."
    sis "I'll catch the rest of you later, okay?"
    pov "..."
    show bg firstcamgurlstream_0_3
    pov "That's enough for me right now anyway.. I think I need a shower."
    pov "That got me a little more worked up than I thought."

    jump lbl_first_camgurl_stream_end

label lbl_first_camgurl_stream_end:
    $ sister_path = 5

    jump lbl_peeking_sister

### NO WINC ###
label lbl_first_camgurl_stream_winc0:

    scene bg firstcamgurlstream_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_2
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_1
    $ renpy.pause(1,hard=True)
    show bg firstcamgurlstream_3
    sis "Yesterday I only managed to get six inches deep..."
    sis "Do you think I can take more today?"
    show bg firstcamgurlstream_1
    pov "..."
    show bg firstcamgurlstream_2
    pov "... Holy shi-"
    show bg firstcamgurlstream_1
    sis "Hehehehe... Mmm. It's so tasty."
    show bg firstcamgurlstream_3
    sis "Later on I'm going to unwrap a brand new toy. Do you want to see it?"
    show bg firstcamgurlstream_4
    sis "Mmm..."
    show bg firstcamgurlstream_3
    sis "I can see some of you are on trial accounts. You better sign up for realsies or you'll miss our party."
    show bg firstcamgurlstream_1
    pov "{i}This cannot really be [sister].{/i}"
    show bg firstcamgurlstream_3
    sis "Hehehe!"
    show bg firstcamgurlstream_2
    pov "{i}...Looks like her. Sort of sounds like her. But those clothes... That look...{/i}"
    show bg firstcamgurlstream_1
    pov "{i}Fuck..{/i}"
    show bg firstcamgurlstream_3
    pov "{i}I've seen her naked. How can this be affecting me so much more than that?{/i}"
    sis "Ooh, I'm just too excited. I've got to open my present!"
    show bg firstcamgurlstream_0
    $ renpy.pause()

    menu:
        "Register an account and pay for viewtime" if inventory.money >= 40:
            $ inventory.money -= 40
            $ renpy.notify("You paid $40")

            jump lbl_first_camgurl_stream_1_winc0
        "I don't have enough money":
            pov "{i}Fuck, I don't have any money on me right now.{/i}"
            pov "{i}It's not like I can come back here at a later date.{/i}"
            pov "..."
            pov "{i}No wonder she doesn't want me to know what she does for a job...{/i}"
            pov "..."
            pov "Wow..."
            pov "This is a lot to process right now."
            pov "I need a shower, I can't get that image out of my mind."

            jump lbl_first_camgurl_stream_end_winc0
        "Quit out" if inventory.money >= 40:
            jump lbl_first_camgurl_stream_2_winc0

label lbl_first_camgurl_stream_1_winc0:
    scene bg firstcamgurlstream_0_4

    python:
        usname = renpy.input("")
        usname = usname.strip()
        if not usname:
            usname = "Hugh_GeeCock"
            
    show bg firstcamgurlstream_3
    sis "So, since you have all given me so many lovely gifts, I had to take a poll to decide what you might most like me to get myself."
    show bg firstcamgurlstream_5
    sis "But I finally settled on this guy."
    show bg firstcamgurlstream_6
    $ renpy.pause(1.5,hard=True)
    show bg firstcamgurlstream_7
    sis "Captain Cuddles."
    sis "Isn't he so cute?"
    show bg firstcamgurlstream_8
    sis "He's very naughty, too. Aren't you, Captain Cuddles?"
    show bg firstcamgurlstream_9
    sis "Yes, I know you are..."
    show bg firstcamgurlstream_10
    sis "And I know you're eager..."
    show bg firstcamgurlstream_11
    sis "Oh, you bad little bear. You're already getting me wet... Can you see?"
    show bg firstcamgurlstream_12
    sis "I always feel somewhat uncomfortable when they get like this..."
    show bg firstcamgurlstream_11
    sis "Do you mind, Captain Cuddles? Of course not, naughty bear."
    show bg firstcamgurlstream_13
    "{i}Bzzzzz{/i}"
    show bg firstcamgurlstream_14
    sis "He says that he'd rather snack on me instead of cake..."
    sis "Captain Cuddles is very insistent that I let him celebrate my unbirthday."
    pov "{i}...Wow.. the bear's actually vibrating pretty violently.{/i}"
    show bg firstcamgurlstream_13
    sis "Oooh, Captain Cuddles... You're a naughty, naughty bear."
    sis "But so soft... Mmmm..."
    show bg firstcamgurlstream_15
    $ renpy.pause()
    show bg firstcamgurlstream_16
    $ renpy.pause()
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)

    menu:
        "Try to enter her room":
            jump lbl_first_camgurl_stream_3_winc0
        "Keep watching":
            jump lbl_first_camgurl_stream_4_winc0

label lbl_first_camgurl_stream_2_winc0:
    pov "{i}No, I can't just watch her. She's my [sisrole].{/i}"
    pov "{i}How the hell am I supposed to look her in the eye after this.{/i}"
    pov "..."

    menu:
        "I've got too see this." if inventory.money >= 40:
            pov "{i}Fuck it, I've got to see this.{/i}"

            jump lbl_first_camgurl_stream_1_winc0
        "No wonder she doesn't want me to find out what she does.":
            pov "{i}No wonder she doesn't want me to know what she does for a job...{/i}"
            pov "..."
            pov "Wow..."
            pov "This is a lot to process right now."
            pov "I need a shower, I can't get that image out of my mind."

            jump lbl_first_camgurl_stream_end_winc0

label lbl_first_camgurl_stream_3_winc0:
    show bg firstcamgurlstream_18
    pov "{i}I wonder if I can get into her room.{/i}"
    show bg firstcamgurlstream_17
    pov "..."
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    sis "Oh, Cuddles--You're going too far. I'm not going to be able to hold myself bac-"
    "{i}*Knock knock*{/i}"
    show bg firstcamgurlstream_19
    sis "..."
    show bg firstcamgurlstream_20
    sis "What?"
    show bg firstcamgurlstream_19

    menu:
        "What are you doing?":
            pov "Hey, what are you doing?"
            show bg firstcamgurlstream_20
            sis "I'm busy, go away!"
        "Are you in there?":
            pov "Hey, are you in there?"
            show bg firstcamgurlstream_20
            sis "Yeah, but I'm kinda busy! Go away!"
        "I need something.":
            pov "Hey, I need something in your room!"
            show bg firstcamgurlstream_20
            sis "I'm busy! Get it later!"
        "Mom's calling you." if winc == 1:
            pov "Hey, Mom's calling for you."
            show bg firstcamgurlstream_20
            sis "Tell her I'm busy at the moment!"
        "[missus]'s calling you." if winc == 1:
            pov "Hey, [missus]'s calling for you."
            show bg firstcamgurlstream_20
            sis "Tell her I'm busy at the moment!"
    show bg firstcamgurlstream_21
    sis "{i}That's my [povsisrole]...{/i}"
    show bg firstcamgurlstream_19
    pov "Can I come i-"
    show bg firstcamgurlstream_20
    sis "I said I'm busy! Go away!"
    show bg firstcamgurlstream_19
    pov "With what?"
    show bg firstcamgurlstream_20
    sis "None of your business!"
    show bg firstcamgurlstream_19
    pov "..."
    sis "..."
    show bg firstcamgurlstream_21
    sis "I think he's gone."
    show bg firstcamgurlstream_18
    pov "{i}No, I'm not 'LittleBowPeep'. I'm still here on my laptop.{/i}"
    show bg firstcamgurlstream_22
    sis "Sorry, honeys. I had some- erm.. technical difficulties."
    show bg firstcamgurlstream_23
    sis "But I guess I should really be apologizing to Captain Cuddles, shouldn't I?"
    show bg firstcamgurlstream_22
    sis "Sorry, about that little hiccup guys but it's time I take this public stream to my VIP stream."
    show bg firstcamgurlstream_18
    pov "What?!"
    show bg firstcamgurlstream_17
    sis "Nawww, don't be sad, guys. I'll be on again soon."
    show bg firstcamgurlstream_18
    pov "But I just..."
    show bg firstcamgurlstream_22
    sis "As for my special subscribers, I'll see you in our private tea party stream."
    sis "Byee~!"
    show bg firstcamgurlstream_0_2
    pov "Damnit. She blue balled me. I think I need a shower."
    pov "That got me a little more worked up than I thought."

    jump lbl_first_camgurl_stream_end_winc0

label lbl_first_camgurl_stream_4_winc0:
    show bg firstcamgurlstream_18
    sis "Yes... Oh... Oh..."
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg firstcamgurlstream_17
    pov "{i}I think she might be having an actual orgasm.{/i}"
    show bg firstcamgurlstream_24
    sis "Mmmm. Ah.. I- I feel all tingly inside, guys."
    show bg firstcamgurlstream_17
    pov "{i}You're not the only one.{/i}"
    show bg firstcamgurlstream_24
    sis "Mmmmffmm... I'm gonna... I- I'm.."
    show bg firstcamgurlstream_25
    sis "Ahhh... fuu--mmff. C-Captain Cuddles, you n-naughty bear."
    show bg firstcamgurlstream_17
    sis "{i}*Huff huff*{/i}"
    show bg firstcamgurlstream_22
    sis "This was a wonderful Unbirthday gift."
    show bg firstcamgurlstream_26
    sis "{i}You're welcome, Babykins... You taste like cupcakes and rainbows.{/i}"
    show bg firstcamgurlstream_27
    sis "Hehehehe, silly Cuddles."
    sis "But we can't leave the rest of our guests out of the fun, can we?"
    sis "I think it's time for a cuddle party with everyone..."
    show bg firstcamgurlstream_28
    $ renpy.pause(1.5,hard=True)
    show bg firstcamgurlstream_29
    $ renpy.pause(5,hard=True)
    show bg firstcamgurlstream_30
    $ renpy.pause(0.4,hard=True)
    show bg firstcamgurlstream_31
    $ renpy.pause()
    show bg firstcamgurlstream_32
    sis "Mmm, that was fun. But now I'm going to have some extra special fun with those of you who want to have a private tea party..."
    sis "I'll catch the rest of you later, okay?"
    pov "..."
    show bg firstcamgurlstream_0_3
    pov "That's enough for me right now anyway.. I think I need a shower."
    pov "That got me a little more worked up than I thought."

    jump lbl_first_camgurl_stream_end_winc0

label lbl_first_camgurl_stream_end_winc0:
    $ sister_path = 5

    jump lbl_peeking_sister

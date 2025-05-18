## VIP ROOM
label lbl_zariahs_party_vip:
    #-Scene starts once the MC approaches the VIP only to hear the sounds of moaning coming from the inside-
    if zariahs_party_talking_vip == 0:
        pov "What the…?"

        #-The Mc gets closer to the VIP room and the moans get louder-

        "Sultry Voice" "{i}*Moan*{/i} God, I love the way you run your tongue down my abs~"

        "Seductive Voice" "And I love the way your fat tits jiggle every time you moan~"

        "Sultry Voice" "H-Hey, that’s not fair!"
        "Sultry Voice" "Your tits are bigger than mine and- *Moan*!"

        "Seductive Voice" "True, and I know you like them from how hard you were sucking on them just a moment ago."
        "Seductive Voice" "But now it’s my turn to taste something of yours~"
        "Seductive Voice" "And I Think you know where I’m going with this, Violette~"

        "Sultry Voice" "Oh god Hazel, yes~"

        #-The moans grow louder and more frequent now-

        #-Back with the Mc outside-

        pov "Wow, Hazel and Violette are really going at it."
        pov "I suppose they want to get it out of their system before the actual party starts and people flood the place."
        pov "Perhaps I should…"

        menu:
            "Take a closer look?":
                #-If “Take a Closer Look” was picked-

                pov "I mean, they are doing this here because of the added risk, right?"
                pov "No harm in just being curious…"

                #-The Mc leans further in to peek into the VIP room-

                #(In here we can either add a graphic of Hazel eating out Violette as she plays with her breasts or leave it to the imagination as regardless, Hazel will notice someone peeking and joke around with Violette about not being onboard about having an audience without pay and that perhaps she should stop, which will make Violette aggressive and will promise to bury whoever is peeking in the beach and wait for the high tide to take them away if they ruin this for her)

                haz "That’s a good girl, moan for mama~"

                vio "H-How are you so good at this?!"

                haz "When you work at a sex shop as long as I have, you get to know a few tricks and rules~"
                haz "Rules such as how Mama isn’t about to give someone a show without proper compensation."

                vio "W-What, someone is trying to peek at us?!"

                pov "Crap, she saw me!"

                haz "Hmmm, I love the rush of getting caught, but not so much the idea of fooling around while someone’s watching, especially for free~"
                haz "Perhaps I should stop and let you take care of yourself, Violette, I do have to save some face, you know?"

                vio "W-What?! No!"
                vio "I’m so close to-!"
                vio "Alright, whoever is out there trying to get a show, better piss off and pray I don’t find out who you are!"
                vio "I swear, if you ruin this for me, I’ll bury you up to your freakin neck on the beach and let you get washed away in high tide!"
                vio "Don’t you freaking test me!"

                pov "And, that’s my cue to leave!"

                #-Mc hurriedly leaves before he gets spotted-

                haz "That’s a good girl~"

                vio "Can we carry on then… please?"

                haz "Of course, sweetie, but from now on…"
                haz "You get to call me “Mommy”~"
                $ has_been_caught_peeping_at_zariahs_party_vip_room = 1

                #=RESULT END=
            "Give them some privacy?":

                #-If “Give them some privacy” was picked-

                pov "As interesting as it may be, I’m pretty sure Violette would kill me if she found out I was peeking on her."
                pov "Better not risk it, right?"
                pov "Let’s see who else is around, I’m sure I can talk to them later."

                #=RESULT END=

        $ zariahs_party_talking_vip = 1

        #=RESULT END=
    else:
        pov "It's too risky to go back there again."
    jump lbl_nightclub_zariahs_party_setup

## Lashley's Strange Noise
label lbl_lashleys_strange_noise:
    #-You arrive on Lashley’s office door-
    scene bg lashleystrangenoises_background_and_body
    show eyes lashleystrangenoises_eyesup
    show charexpression lashleystrangenoises_neutral
    with fade
    $ renpy.pause(1.0)
    show charexpression lashleystrangenoises_confused
    pri "Mmmmnn…"

    #-You stop when you hear a strange noise coming from within Lashley’s office-
    show charexpression lashleystrangenoises_shocked
    pri "Ooohhhhh…"
    show charexpression lashleystrangenoises_shocked_talk
    pov "What the-?"
    #show eyes lashleystrangenoises_eyesdown
    show charexpression lashleystrangenoises_shocked
    pri "Ohhh yessss…"

    #-You listen in to Lashley moaning on the other side of the door-
    show charexpression lashleystrangenoises_embarrassed
    pri "More… More~"
    show charexpression lashleystrangenoises_embarrassed_talk
    pov "Someone’s having fun."
    show charexpression lashleystrangenoises_bored_talk
    pov "Should I…?"
    show charexpression lashleystrangenoises_bored

    default random_lashley_strange_noise = 0
    menu lashley_strange_noise_options:
        "Keep listening":
            show charexpression lashleystrangenoises_shocked
            #(Picking this option will return you to the previous menu, you can pick this option multiple times, each time showing randomly one of the following variants)
            $ random_lashley_strange_noise = renpy.random.randint(1, 6)
            #-Variant 1-
            if random_lashley_strange_noise == 1:
                pri "Ohhh Lord~"
            #-Variant 2-
            elif random_lashley_strange_noise == 2:
                pri "Harder… Harder~"
            #-Variant 3-
            elif random_lashley_strange_noise == 3:
                pri "Forgive me, Father… But I can’t stop…"
            #-Variant 4-
            elif random_lashley_strange_noise == 4:
                pri "Oh God… Oh God~!"
            #-Variant 5-
            elif random_lashley_strange_noise == 5:
                pri "Yes, yes, yes, yes, yes~"
            #-Variant 6-
            elif random_lashley_strange_noise == 6:
                pri "Oh God… Harder, [povname]. Harder~!"
                show charexpression lashleystrangenoises_confused_talk
                pov "Is… Is she calling my name?"
                pov "She masturbates to me?"
                show charexpression lashleystrangenoises_confused
            jump lashley_strange_noise_options
        "Knock":
            #-You knock on her door-
            show bodypart lashleystrangenoises_knocking
            show eyes lashleystrangenoises_eyesdown
            show charexpression lashleystrangenoises_confused_talk
            pov "Director Lashley?"
            show charexpression lashleystrangenoises_shocked
            show eyes lashleystrangenoises_eyesup
            pri "Eeep!"

            #-You hear a loud ruckus coming from the inside of the office-

            pri "J-Just a moment, [povname]!"
            hide bodypart
            show charexpression lashleystrangenoises_shocked_talk
            pov "Are you okay?"
            show charexpression lashleystrangenoises_confused
            pri "Y-Yes! Just a moment, please!"

            #-The ruckus continues for a few more moments before being replaced with silence-
            show charexpression lashleystrangenoises_sad
            pri "..."
            pov "...."
            show charexpression lashleystrangenoises_sad_talk
            pov "Director Lashley?"
            pri "Y-Yes, come in. [povname]."
            pri "Thank you for knocking…"

            if principallashley_points <= 9:
                $ principallashley_points += 1
                $ renpy.notify("Relationship with Director Lashley Increased")
            else:
                $ principallashley_points = 10


        "Enter without warning":
            #-The mc goes for the door handle, however it rattles fruitlessly as the door is tightly locked-
            show charexpression lashleystrangenoises_neutral
            show eyes lashleystrangenoises_eyesdown
            pri "Eeep!"
            show charexpression lashleystrangenoises_confused
            #-You hear a loud ruckus coming from the inside of the office-

            pri "J-Just a moment, please!"
            show charexpression lashleystrangenoises_sad_talk
            show eyes lashleystrangenoises_eyesup
            pov "Director Lashley?"
            show charexpression lashleystrangenoises_sad
            pri "W-What, [povname]?!"
            pri "Why aren’t you in class?!"
            show charexpression lashleystrangenoises_embarrassed_talk
            pov "Uhh… Miss Allaway told me you were requesting to see me?"
            show charexpression lashleystrangenoises_embarrassed
            pri "R-Right!"
            pri "Right, um… Give me a moment!"

            menu:
                "Keep talking":
                    show charexpression lashleystrangenoises_sad_talk
                    pov "Are you alright in there?"
                    show charexpression lashleystrangenoises_sad
                    pri "Y-Yes! J-Just a little bit busy!"
                    show charexpression lashleystrangenoises_confused_talk
                    pov "Busy with what?"
                    show charexpression lashleystrangenoises_confused
                    pri "I-I’m um… Doing some research!"
                    pri "Y-Yeah, some research!"
                    show charexpression lashleystrangenoises_sad_talk
                    pov "I heard some strange noises. Is everything okay in there?"
                    pov "Do you need me to come in?"
                    show charexpression lashleystrangenoises_shocked
                    pri "N-No!"
                    pri "I um… I pulled a muscle!"
                    pri "Yeah, Ow! Ow ow ow."
                    pri "I’m okay, however!"
                    show charexpression lashleystrangenoises_confused
                    pri "I massaged the area and I am better now!"
                    show charexpression lashleystrangenoises_confused_talk
                    pov "You pulled the muscle doing research."
                    show charexpression lashleystrangenoises_sad
                    pri "It’s um, some new exercise regimen for PE class!"
                    pri "Some safe and God-approved activities for you kids to do!"
                    pri "I just wanted to try them to make sure they are safe for you before I have Coach Fistem implement it on the curriculum!"
                    pri "T-Turns out it’s not safe at all!"
                    pri "So I won’t be introducing it!"
                    show charexpression lashleystrangenoises_confused_talk
                    pov "You are doing PE exercises in your office?"
                    show charexpression lashleystrangenoises_sad
                    pri "Y-Yes?"
                    pri "Anyway, Give me a moment [povname]!"
                    pri "I’ll be with you shortly."

                    #-The ruckus goes on for a few moments again before going quiet-
                    show charexpression lashleystrangenoises_neutral
                    pri "O-Okay, [povname]."
                    pri "You can come in now."

                "Keep silent and wait":
                    if principallashley_points <= 9:
                        $ principallashley_points += 1
                        $ renpy.notify("Relationship with Director Lashley Increased")
                    else:
                        $ principallashley_points = 10
                    show charexpression lashleystrangenoises_confused
                    show black with fade
                    #-The ruckus goes on for a few moments again before going quiet-
                    hide black with fade
                    show charexpression lashleystrangenoises_neutral
                    pri "O-Okay, [povname]."
                    pri "You can come in now."
                    show charexpression lashleystrangenoises_bored_talk
                    pov "Are you sure?"
                    show charexpression lashleystrangenoises_bored
                    pri "Y-Yeah."
                    pri "I think i’ve got everything off the desk…"
                    show charexpression lashleystrangenoises_confused_talk
                    pov "What was that?"
                    show charexpression lashleystrangenoises_confused
                    pri "N-Nothing!"
                    pri "Come in, let’s not waste daylight given to us by the kindness of our lord!"

    $ main_story = 74
    scene black with fade
    jump lbl_a_talk_with_lashley

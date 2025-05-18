## Effie Text Invitation
label lbl_effie_text_invitation:
    #-As a prelude to the next scene, The player will receive a text message from Effie as soon as they wake up-

    scene bg effietextinvitation_1
    with fade
    $ renpy.pause()
    # eff "Hey dude."
    # eff "Are you doing anything right now?"

    show bg effietextinvitation_2
    $ renpy.pause()
    # pov "Just got up why?"

    show bg effietextinvitation_3
    $ renpy.pause(1,hard=True)
    # eff "Art students making an exhibition in the uni gym."
    show bg effietextinvitation_4
    $ renpy.pause()
    # eff "Wanna go check it out?"

    show bg effietextinvitation_5
    $ renpy.pause()
    # pov "Aight sounds dope!"

    show bg effietextinvitation_6
    $ renpy.pause()
    # eff "Cool meet you in the gym then!"

    pov "{i}Well, guess I have plans now.{/i}"
    pov "{i}Gotta meet with Effie at the gym.{/i}"

    $ effie_path = 7

    scene bg mybedroom_day
    with fade

    jump lbl_mybedroom_day_setup

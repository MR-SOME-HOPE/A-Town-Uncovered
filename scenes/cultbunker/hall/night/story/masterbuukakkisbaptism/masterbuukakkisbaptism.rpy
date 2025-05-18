## Master Buukakki's Baptism
label lbl_master_buukakkis_baptism:
    ## The team joins MB and a few other people through into a side room that houses a big giant tub with water in it.\

    scene bg masterbuukakkisbaptism_1
    with fade

    mas "Alright, everyone gather in here."
    mas "There’s a couple of cameras in each corner  of the room but that’s simply to allow the congregation outside to watch it on the projected screen out there."
    mas "As you can tell, it’s quite small and intimate here so we make do with what we can."
    mas "Now, everyone just gather round and we’ll start the baptism."

    show bg masterbuukakkisbaptism_2

    mas "Who’s first?"
    mas "…"
    mas "My dear?"
    mas "Don’t be timid, step on up."

    ## A random girl comes on up with Master Buukakki and they both get into the giant tub.
    show bg masterbuukakkisbaptism_3_1
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_3_2
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_3_3
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_3_4
    $ renpy.pause(1,hard=True)

    mas "{i}*Mumbles a chant*{/i}"

    ## MB says under his breath as he holds the girl in a manner as to let her fall on her back as safely as possible*
    show bg masterbuukakkisbaptism_4_1
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_4_2
    $ renpy.pause(0.6,hard=True)
    show bg masterbuukakkisbaptism_4_3
    $ renpy.pause(0.6,hard=True)
    show bg masterbuukakkisbaptism_4_4
    $ renpy.pause(0.6,hard=True)

    mas "…"

    ## MB Drops the girl underwater and holds her there for a looooong time.
    ## There’s some splashing going on to signify the girl gasping for air
    ## Then… silence.

    show bg masterbuukakkisbaptism_5_1
    $ renpy.pause(5,hard=True)
    show bg masterbuukakkisbaptism_5_2
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_5_3
    with hpunch
    $ renpy.pause(1,hard=True)
    show bg masterbuukakkisbaptism_4_4
    $ renpy.pause(4,hard=True)
    show bg masterbuukakkisbaptism_5_4
    $ renpy.pause(2,hard=True)

    mas "It’s done."
    mas "..."

    show bg masterbuukakkisbaptism_4_4
    $ renpy.pause(5,hard=True)


    ## MB stands up and faces the new members without a word
    ## Just then, the girl shoots straight out of the water gasping for air.
    ## They give her a second to catch her breath.
    show bg masterbuukakkisbaptism_4_5
    with hpunch

    "Girl" "{i}*Gasping for air*{/i}"

    mas "Have you converted, my child?"

    "Girl" "Y-yes."
    "Girl" "I-"
    "Girl" "I’ve converted."

    mas "Praise be!"

    "Everyone" "{i}*Applauses and cheers*{/i}"

    mas "Praise be!"

    "Everyone" "PRAISE BE!"

    mas "Come my dear."
    mas "Let’s get you covered in cum."

    scene black
    with fade
    $ renpy.pause()
    "Master Buukakki leads her back out into the main hall..."

    ## SCENE ENDS

    $ main_story = 161

    jump lbl_escape_master_buukakki

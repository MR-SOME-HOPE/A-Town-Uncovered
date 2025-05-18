## Violette's Punishment
default violettespunishment_reversecowgirl = 0
default violettespunishment_archeddoggy = 0
default violettespunishment_matingpress = 0

label lbl_violettes_punishment:
    scene black

    menu:
        "Reverse Cowgirl":
            jump lbl_violettes_punishment_reversecowgirl
        "Arched Doggy":
            jump lbl_violettes_punishment_archeddoggy
        "Mating Press":
            jump lbl_violettes_punishment_matingpress

label lbl_violettes_punishment_end:
    $ violette_path = 15
    $ gtime = 3

    jump lbl_townmap_setup

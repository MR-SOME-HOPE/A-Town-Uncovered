## Truck Burning ##
label lbl_truck_burning:

    scene black
    with fade
    $ renpy.pause()
    "After driving out of town for a couple of miles..."

    scene bg truckburning_1
    with fade
    $ renpy.pause()
    mis "..."

    scene bg truckburning_2
    pov "..."

    scene bg truckburning_1
    mis "..."

    scene bg truckburning_2
    pov "We are free now, Miss."

    scene bg truckburning_1
    pov "We are free..."

    scene bg truckburning_2
    $ renpy.pause()

    scene bg truckburning_1
    mis "I love you, [povname]."

    scene bg truckburning_2
    mis "I love you so much..."

    scene bg truckburning_1
    pov "I love you too."

    scene bg truckburning_2
    $ renpy.pause(1,hard=True)

    scene bg truckburning_1
    $ renpy.pause(1,hard=True)

    scene bg truckburning_2
    $ renpy.pause(1,hard=True)

    scene bg truckburning_3
    with dissolve
    $ renpy.pause(1,hard=True)

    scene bg truckburning_4
    $ renpy.pause(1,hard=True)

    scene bg truckburning_3
    $ renpy.pause(1,hard=True)

    scene bg truckburning_4
    $ renpy.pause(1.5,hard=True)

    scene bg truckburning_3
    $ renpy.pause()
    mis "It's over..."
    mis "It's finally over..."

    scene bg truckburning_4
    pov "I told you, we would get out of this together."
    pov "Never again..."

    scene bg truckburning_3
    mis "Ahem- {i}I{/i} told you we'd get out of this together."
    mis "..."

    scene bg truckburning_4
    mis "It's a little cold out here, don't you think?"
    pov "Well, we have a beautiful bonfire to keep warm with."

    scene bg truckburning_3
    mis "..."

    jump lbl_sex_by_the_fire_truck

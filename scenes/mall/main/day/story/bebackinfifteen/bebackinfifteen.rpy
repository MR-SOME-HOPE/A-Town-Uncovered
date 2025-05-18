## Be Back In Fifteen

label lbl_be_back_in_fifteen:
    scene black
    scene bg bebackinfifteen_1
    with fade
    $ renpy.pause()
    pov "{i}Hmmm, that girl must be on break. I'll look elsewhere for a job.{/i}"

    scene bg mall_day
    show btn mall_day_icecreamstorebeback_idle
    with fade

    jump lbl_mall_day

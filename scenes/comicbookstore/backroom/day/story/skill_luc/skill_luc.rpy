## Increase LUC ##
label lbl_comicbookbackroom_day_table:
    show btn_comicbookbackroom_day_crugeon_idle2
    show btn_comicbookbackroom_day_davendithas_idle2
    show btn_comicbookbackroom_day_lordkev_idle2
    if sister_path == 17.5:
        pov "{i}I shouldn't spend my time playing cards.{/i}"
        pov "{i}I still have to look for [sister] next door.{/i}"

        jump lbl_comicbookbackroom_day_setup
    elif main_story == 20:
        pov "{i}I shouldn't spend my time playing cards.{/i}"
        if winc == 0:
            pov "{i}Missus told me to get a job. I'll check the mall.{/i}"
        else:
            pov "{i}Mom told me to get a job. I'll check the mall.{/i}"

        jump lbl_comicbookbackroom_day_setup
    elif skill_luc_times == 0:

        "Who do you want to play against?"

        menu:

            "Crugeon - Low Level Deck":
                jump lbl_skills_luc_1
            "Davendithas - Standard Deck":
                jump lbl_skills_luc_2
            "Lord Kevlamin - High Level Deck":
                jump lbl_skills_luc_3
            "I don't want to play.":
                jump lbl_comicbookbackroom_day_setup
    elif skill_luc_times == 1:
        pov "{i}I don't think I should play again for today, I might become a gambling addict.{/i}"

        jump lbl_comicbookbackroom_day_setup

## LUCK
label lbl_skills_luc_1:

    scene bg skills_luc_1
    with fade
    $ renpy.pause ()
    if skill_lucmax >= 11:
        scene bg skills_luc_4
        with fade
        "Crugeon's Deck is too low for you and didn't challenge your LUC enough."
        "Your LUC Max Limit stays the same."
    elif not (day == 0 or day == 1 or day == 2 or day == 3 or day == 4 or day == 5):
        scene bg skills_luc_5
        with fade
        "You dealt a bad hand today thus, losing your the game."
        if not day == 0 or day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            "Today was one of those unlucky days, better luck next time."

        jump lbl_skills_luc_end
    else:
        scene bg skills_luc_4
        with fade
        "You successfully increased your LUC Max Limit."
        $ skill_lucmax += 1
        if skill_lucmax >= 20:
            $ skill_lucmax == 20

    jump lbl_skills_luc_end

label lbl_skills_luc_2:

    scene bg skills_luc_2
    with fade
    $ renpy.pause ()
    if skill_lucmax >= 16:
        scene bg skills_luc_4
        with fade
        "Davendithas' Deck is too low for you and didn't challenge your LUC enough."
        "Your LUC Max Limit stays the same."
    elif not (day == 0 or day == 1 or day == 2 or day == 3):
        scene bg skills_luc_5
        with fade
        "You dealt a bad hand today thus, losing you the game."
        if not day == 0 or day == 1 or day == 2 or day == 3:
            "Today was one of those unlucky days, better luck next time."

        jump lbl_skills_luc_end
    else:
        scene bg skills_luc_4
        with fade
        "You successfully increased your LUC Max Limit."
        $ skill_lucmax += 1
        if skill_lucmax >= 20:
            $ skill_lucmax == 20

    jump lbl_skills_luc_end

label lbl_skills_luc_3:

    scene bg skills_luc_3
    with fade
    $ renpy.pause ()
    if skill_lucmax >= 20:
        scene bg skills_luc_4
        with fade
        "You've already reached your LUC Max Limit."
    elif skill_lucmax <= 15 or not (day == 2 or day == 6):
        scene bg skills_luc_5
        with fade
        "You dealt a bad hand today thus, losing you the game."
        if skill_lucmax <= 15:
            "Your LUC Max Limit is too low too perform at this level."
        elif not day == 2 or day == 6:
            "Today was one of those unlucky days, better luck next time."
    else:
        scene bg skills_luc_4
        with fade
        "You successfully increased your LUC Max Limit."
        $ skill_lucmax += 1
        if skill_lucmax >= 20:
            $ skill_lucmax == 20

    jump lbl_skills_luc_end

label lbl_skills_luc_end:
    $ gtime += 1
    $ skill_luc_times = 1
    $ renpy.notify("You can currently hold [skill_lucmax] LUC points")
    if gtime == 1:
        scene bg comicbookbackroom_day
        with fade

        jump lbl_comicbookbackroom_day_setup
    elif gtime == 2:
        scene bg street_night
        with fade

        jump lbl_street_night_setup

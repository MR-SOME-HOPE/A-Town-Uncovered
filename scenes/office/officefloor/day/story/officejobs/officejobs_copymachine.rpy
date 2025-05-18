#########################################################################################
## COPY MACHINE
label lbl_office_jobs_tutorial_copy_machine:
    default toggle_copier_desk_files_collected_left = False#FOR_RESET
    default toggle_copier_desk_files_collected_right = False#FOR_RESET
    default ctr_copier_originals_placed = 0
    default is_copier_scanner_opened = False
    default is_original_in_scanner = False
    default is_original_ready_to_scan = False
    default ctr_originals_removed_from_scanner = 0
    default ctr_copies_of_originals_printed = 0
    default ctr_copies_of_originals_delivered = 0
    default copymachine_leftstack = 3
    #$ style.default.hyperlink_functions = (hyperlink_styler, hyperlink_callback, None)

    jump lbl_copier_tutorial

##########################################
## INSTRUCTIONS
label lbl_copier_tutorial:
    mrf "This task requires you to scan old, degraded documents to digital and print physical copies for filing."
    mrf "When you're done with a stack, put them on my desk."
    mrf "Simple, right?"
    scene black with fade
    scene bg copymachine
    show leftstack1
    show leftstack2
    show copymachine lidclosed
    with fade

    call screen scr_copier_tutorial

##########################################
## OFFICE JOBS
label lbl_officejobs_copymachine:
    $ toggle_copier_desk_files_collected_left = False#FOR_RESET
    $ toggle_copier_desk_files_collected_right = False#FOR_RESET
    $ ctr_copier_originals_placed = 0
    $ is_copier_scanner_opened = False
    $ is_original_in_scanner = False
    $ is_original_ready_to_scan = False
    $ ctr_originals_removed_from_scanner = 0
    $ ctr_copies_of_originals_printed = 0
    $ ctr_copies_of_originals_delivered = 0
    $ copymachine_leftstack = 3
    scene black with fade
    scene bg copymachine
    show leftstack1
    show leftstack2
    show copymachine lidclosed
    with fade

    call screen scr_copier_tutorial

##########################################
## ASSET LAYERS
label lbl_copier_tutorial_foreground:
    if is_copier_scanner_opened:
        show copymachine lidopen
    elif not is_copier_scanner_opened:
        show copymachine lidclosed

    if ctr_copier_originals_placed > 0:
        if ctr_copier_originals_placed == 1:
            show stack1 1
        elif ctr_copier_originals_placed == 2:
            show stack1 2
        elif ctr_copier_originals_placed == 3:
            show stack1 3
        elif ctr_copier_originals_placed == 4:
            show stack1 4
        elif ctr_copier_originals_placed == 5:
            show stack1 5
    else:
        hide stack1

    if ctr_copies_of_originals_printed > 0:
        if ctr_copies_of_originals_printed == 1:
            show stack2 1
        elif ctr_copies_of_originals_printed == 2:
            show stack2 2
        elif ctr_copies_of_originals_printed == 3:
            show stack2 3
        elif ctr_copies_of_originals_printed == 4:
            show stack2 4
        elif ctr_copies_of_originals_printed == 5:
            show stack2 5
    else:
        hide stack2

    if ctr_copies_of_originals_delivered > 0:
        show rightstack1
        if ctr_copies_of_originals_delivered > 1:
            show rightstack2

    call screen scr_copier_tutorial

##########################################
## SCREENS
screen scr_copier_tutorial():
    ## Left Stack
    if not toggle_copier_desk_files_collected_right:
        imagebutton auto "btn copymachine_leftstack1_%s" xpos 0 ypos 0 focus_mask True:
            if ctr_copier_originals_placed == 0:
                action Jump("lbl_copier_desk_files_collected_right")
    if not toggle_copier_desk_files_collected_left:
        imagebutton auto "btn copymachine_leftstack2_%s" xpos 0 ypos 0 focus_mask True:
            if ctr_copier_originals_placed == 0:
                action Jump("lbl_copier_desk_files_collected_left")

    ## Copy Machine Lid
    if is_copier_scanner_opened and is_original_in_scanner:
        imagebutton:
            focus_mask True
            idle "btn copymachine_lidopen_idle"
            hover "btn copymachine_lidopen_hover"
            # imagebutton auto "btn copymachine_lidopen_%s" xpos 0 ypos 0 focus_mask True action If(is_original_in_scanner==True, Jump("lbl_close_scanner"))
            if is_original_in_scanner:
                action Jump("lbl_close_scanner")
    elif not is_copier_scanner_opened:
        imagebutton:
            focus_mask True
            idle "btn copymachine_lidclosed_idle"
            hover "btn copymachine_lidclosed_hover"
            #imagebutton auto "btn copymachine_lidclosed_%s" xpos 0 ypos 0 focus_mask True action If(is_original_in_scanner==False, Jump("lbl_open_scanner"))
                # imagebutton auto "btn copymachine_lidclosed_%s"
            if not is_original_ready_to_scan:
                action Jump("lbl_open_scanner")

    ## Stack1
    if ctr_copier_originals_placed > 0:
        imagebutton:
            focus_mask True
            idle "btn copymachine_stack1_[ctr_copier_originals_placed]_idle"
            hover "btn copymachine_stack1_[ctr_copier_originals_placed]_hover"
            if is_copier_scanner_opened and not is_original_in_scanner:
                action Jump("lbl_place_original_in_scanner")
    ## Stack2
    if ctr_copies_of_originals_printed > 0:
        if ctr_copies_of_originals_printed != 5:
            add "stack2 [ctr_copies_of_originals_printed]"
        if ctr_copies_of_originals_printed == 5:
            imagebutton:
                focus_mask True
                idle "btn copymachine_stack2_5_idle"
                hover "btn copymachine_stack2_5_hover"
                action Jump("lbl_deliver_duplicates_to_colleague")


    if is_original_ready_to_scan:
        imagebutton:
            focus_mask True
            if ctr_copies_of_originals_printed != 5:
                idle "btn print_idle"
                hover "btn print_hover"
                if not is_copier_scanner_opened:
                    action Jump("lbl_make_copy_of_original")
            else:
                idle "hazard"

    #use hud_overlay

label lbl_close_scanner:
    $ is_copier_scanner_opened = False
    if is_original_in_scanner:
        $ is_original_ready_to_scan = True
    jump lbl_copier_tutorial_foreground

label lbl_open_scanner:
    $ is_copier_scanner_opened = True
    if is_original_in_scanner:
        $ is_original_in_scanner = False
        $ ctr_originals_removed_from_scanner += 1
    jump lbl_copier_tutorial_foreground

label lbl_deliver_duplicates_to_colleague:
    $ ctr_copies_of_originals_printed = 0
    hide stack2
    $ ctr_copies_of_originals_delivered += 1
    if ctr_copies_of_originals_delivered > 0:
        show rightstack1
        if ctr_copies_of_originals_delivered > 1:
            show rightstack2

##############################################################################
        ## COMPLETE TASK
    if ctr_copies_of_originals_delivered == 2:
        $ renpy.pause(2.0,hard=True)

        ## FIRST SHIFT / TUTORIAL
        if main_story <= 100:
            $ internship_job_tutorial_completed_copy_machine = True
            hide screen scr_copier_tutorial
            scene black with fade
            scene bg officefloor_day with fade
            if internship_job_tutorial_completed_coffee_runs:
                jump lbl_completed_all_office_training
            else:
                jump lbl_office_jobs_tutorials
        ## DAILY GRIND
        else:
            $ officejobs_complete += 1
            $ officejobs_copymachine = 1

            if main_story == 101:
                if officejobs_complete == 1:
                    jump lbl_daily_grind_part1_jobs_midscene
                else:
                    jump lbl_daily_grind_part1_jobs_end
            elif main_story == 102:
                if officejobs_complete == 1:
                    jump lbl_daily_grind_part2_jobs_midscene
                else:
                    jump lbl_daily_grind_part2_jobs_end
            elif main_story == 103:
                if officejobs_complete == 1:
                    jump lbl_daily_grind_part3_jobs_menu
                else:
                    jump lbl_daily_grind_part3_jobs_end
            ## NON-MAIN STORY
            else:
                jump lbl_officefloor_day_setup

    ## INCOMPLETE TASK
    else:
        jump lbl_copier_tutorial_foreground

##############################################################################
label lbl_make_copy_of_original:
    hide paperon
    $ ctr_copies_of_originals_printed += 1
    $ is_original_in_scanner = False
    $ is_original_ready_to_scan = False
    jump lbl_copier_tutorial_foreground

label lbl_place_original_in_scanner:
    $ ctr_copier_originals_placed -= 1
    show copymachine lidopen
    show paperon
    if ctr_copier_originals_placed == 1:
        show stack1 1
    elif ctr_copier_originals_placed == 2:
        show stack1 2
    elif ctr_copier_originals_placed == 3:
        show stack1 3
    elif ctr_copier_originals_placed == 4:
        show stack1 4
    elif ctr_copier_originals_placed == 5:
        show stack1 5
    else:
        hide stack1
    $ is_copier_scanner_opened = True
    $ is_original_in_scanner = True
    $ is_original_ready_to_scan = False
    jump lbl_copier_tutorial_foreground

    # $ renpy.pause()
    # hide paperon
    # show copymachine lidclosed

    # jump lbl_copier_tutorial_foreground


label lbl_copier_desk_files_collected_left:
    $ toggle_copier_desk_files_collected_left = True
    $ copymachine_leftstack = 1
    jump lbl_copier_desk_files_collected

label lbl_copier_desk_files_collected_right:
    $ toggle_copier_desk_files_collected_right = True
    $ copymachine_leftstack = 2
    jump lbl_copier_desk_files_collected

label lbl_copier_desk_files_collected:
    if copymachine_leftstack == 2:
        hide leftstack1
    elif copymachine_leftstack == 1:
        hide leftstack2
    $ ctr_copier_originals_placed = 5
    jump lbl_copier_tutorial_foreground

##########################################
## Images

## Left Stack
image btn copymachine_leftstack1_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/leftstack1.png"

image btn copymachine_leftstack1_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/leftstack1.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_leftstack2_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/leftstack2.png"

image btn copymachine_leftstack2_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/leftstack2.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

## Copy Machine Lid
image btn copymachine_lidopen_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/copymachine_lidopen.png"

image btn copymachine_lidopen_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/copymachine_lidopen.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_lidclosed_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/copymachine_lidclosed.png"

image btn copymachine_lidclosed_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/copymachine_lidclosed.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

## Stack1
image btn copymachine_stack1_1_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_1.png"

image btn copymachine_stack1_1_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_1.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack1_2_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_2.png"

image btn copymachine_stack1_2_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_2.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack1_3_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_3.png"

image btn copymachine_stack1_3_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_3.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack1_4_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_4.png"

image btn copymachine_stack1_4_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_4.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack1_5_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_5.png"

image btn copymachine_stack1_5_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack1_5.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack2_1_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_1.png"

image btn copymachine_stack2_1_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_1.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack2_2_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_2.png"

image btn copymachine_stack2_2_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_2.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack2_3_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_3.png"

image btn copymachine_stack2_3_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_3.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack2_4_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_4.png"

image btn copymachine_stack2_4_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_4.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

image btn copymachine_stack2_5_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_5.png"

image btn copymachine_stack2_5_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/stack2_5.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

## Print
image btn print_idle:
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/print.png"

image btn print_hover = im.MatrixColor(
    "//scenes/office/officefloor/day/story/officejobs/assets/copymachine/print.png",
    im.matrix.brightness(0.15)*
    im.matrix.opacity(1))

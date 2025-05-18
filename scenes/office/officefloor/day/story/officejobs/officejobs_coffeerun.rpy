#########################################################################################
## COFFEE RUN
label lbl_office_jobs_tutorial_coffee_runs:
    scene bg officefloor_day
    default coffeerun_firsttime = 1
    default coffee_runs_stage = 2
    default dad_stage_2 = ["Dad",("Espresso Triple Shot", "No Cream"), ("Pour Over Medium", "No Milk")]
    default howie_stage_2 = ["Howie",("Decaf Mocha Medium", "Whole Milk"), ("Iced Tea Large", "Extra Sugar")]
    default manager_stage_2 = ["Manager",("Decaf Cappuccino Large", "Skimmed Milk"), ("Chai Tea Medium", "No Sugar")]

    default kanako_stage_3 = ["Kanako",("Cappuccino Medium", "Almond Milk", "Regular Cream"), ("Frappe Large", "Caramel Syrup", "Extra Whip Cream")]
    default isaac_stage_3 = ["Isaac", ("Cappuccino Medium", "Whole Milk", "Chocolate Sprinkles"), ("Americano Large", "Almond Milk", "Hazelnut Cream")]
    default corrine_stage_3 = ["Corrine", ("Macchiato Small", "Caramel Syrup", "Milk Chocolate Sprinkles"), ("Chai Tea Large", "Honey", "25%% Ice")]

    default bradley_stage_4 = ["Bradley", ("Mocha Grande", "Soy Milk", "Extra Cream", "No Ice"), ("Espresso Triple Shot", "Almond Milk", "No Cream", "No Sugar")]
    default gloria_stage_4 = ["Gloria", ("Vanilla Latte Large", "Soy Milk", "No Sugar", "Extra Whipped Cream"), ("Mocha Latte Large", "Chocolate Syrup", "Dark Chocolate Sprinkles", "Sugar Free Cookie")]

    default dad_order = None
    default howie_order = None
    default manager_order = None
    default kanako_order = None
    default isaac_order = None
    default corrine_order = None
    default bradley_order = None
    default gloria_order = None
    default current_chosen_drink = None
    default current_chosen_milk = None
    default current_chosen_cream = None
    default current_chosen_topping = None

    default dad_order_brought = None
    default howie_order_brought = None
    default manager_order_brought = None
    default kanako_order_brought = None
    default isaac_order_brought = None
    default corrine_order_brought = None
    default bradley_order_brought = None
    default gloria_order_brought = None

    default bought_coffee_run_drinks = False
    default on_coffee_run_blocking = False

##########################################
## INSTRUCTIONS
    mrf "Memorize the coffee orders of 3 of your coworkers and correctly order them at the cafe."
    mrf "The orders range from simple and easy to absurdly complicated depending on the person."
    mrf "Bring them back here when they're ready."
    mrf "Pretty simple and straight-forward."

    jump lbl_take_coffee_orders

##########################################
## OFFICE JOBS
label lbl_officejobs_coffeerun:
    $ coffee_runs_stage += 1
    jump lbl_take_coffee_orders

##########################################
## Taking Orders
label lbl_take_coffee_orders:
    show pov neutral_talk at left
    with dissolve
    pov "I'm taking coffee orders!"
    show pov neutral at left
    if coffee_runs_stage == 2:
        $ dad_order = dad_stage_2[random.randint(1,2)]
        $ howie_order = howie_stage_2[random.randint(1,2)]
        $ manager_order = manager_stage_2[random.randint(1,2)]

        $ on_coffee_run_blocking = True


        show dad neutral_talk at right with dissolve
        dad "[dad_order[0]]. [dad_order[1]]."
        hide dad with dissolve
        $ renpy.pause(2.0)

        show how embarrassed_talk at right with dissolve
        how "[howie_order[0]]. [howie_order[1]]."
        hide how with dissolve
        $ renpy.pause(2.0)

        show mrf bored_talk at right with dissolve
        mrf "[manager_order[0]]. [manager_order[1]]."
        hide mrf with dissolve
        $ renpy.pause(2.0)
    elif coffee_runs_stage == 3:
        $ kanako_order = kanako_stage_3[random.randint(1,2)]
        $ isaac_order = isaac_stage_3[random.randint(1,2)]
        $ corrine_order = corrine_stage_3[random.randint(1,2)]

        show kan neutral_talk at right with dissolve
        kan "[kanako_order[0]]. [kanako_order[1]]. [kanako_order[2]]."
        hide kan with dissolve
        $ renpy.pause(2.0)

        show jacdad neutral_talk at right with dissolve
        jacdad "[isaac_order[0]]. [isaac_order[1]]. [isaac_order[2]]."
        hide jacdad with dissolve
        $ renpy.pause(2.0)

        show cor neutral_talk at right with dissolve
        cor "[corrine_order[0]]. [corrine_order[1]]. [corrine_order[2]]."
        hide cor with dissolve
        $ renpy.pause(2.0)
    elif coffee_runs_stage >= 4:#==
        $ bradley_order = bradley_stage_4[random.randint(1,2)]
        $ gloria_order = gloria_stage_4[random.randint(1,2)]

        show bra neutral_talk at right with dissolve
        bra "[bradley_order[0]]. [bradley_order[1]]. [bradley_order[2]]. [bradley_order[3]]."
        hide bra with dissolve
        $ renpy.pause(2.0)

        show glo neutral_talk at right with dissolve
        glo "[gloria_order[0]]. [gloria_order[1]]. [gloria_order[2]]. [gloria_order[3]]."
        hide glo with dissolve
        $ renpy.pause(2.0)

    pov "I hope I remember right. I'll have to take a trip to the cafe."
    if coffeerun_firsttime == 1:
        show mrf shocked_talk at right
        with dissolve
        mrf "Oh- and tell them it's for TRC, they'll put it on the tab."
        show pov neutral_talk at left
        show mrf neutral at right
        pov "Will do."
        $ coffeerun_firsttime = 0
    else:
        pass

    $ on_coffee_run_blocking = True
    jump lbl_officefloor_day_setup

##########################################
## GET COFFEE FROM CAFE
label lbl_get_coffee_from_cafe:
    show pov neutral_talk at left
    if gtime == 0:
        pov "Hey, I'm on a coffee run for TRC."
        show brow neutral at right
        call lbl_cafeinside_counter_check
        show pov neutral at left
        show brow neutral_talk at right
        bro "Gotcha, what'll be today?"
        show brow neutral at right
    else:
        pov "Hey, I'm on a coffee run for TRC."
        show effw neutral at right
        call lbl_cafeinside_counter_check
        show pov neutral at left
        show effw neutral_talk at right
        eff "Gotcha, what'll be today?"
        show effw neutral at right
        show pov confused at left
    if coffee_runs_stage == 2:
        ## DAD ORDER
        pov "{i}What did [dad] want to drink?{/i}"
        if dad_order[0] == "Espresso Triple Shot":
            menu:
                "Espresso Triple Shot":
                    $ current_chosen_drink = "Espresso Triple Shot"
                "Americano Large":
                    $ current_chosen_drink = "Americano Large"
            menu:
                "No Cream":
                    $ current_chosen_milk = "No Cream"
                "Whole Milk":
                    $ current_chosen_milk = "Whole Milk"

        elif dad_order[0] == "Pour Over Medium":
            menu:
                "Pour Over Medium":
                    $ current_chosen_drink = "Pour Over Medium"
                "Americano Medium":
                    $ current_chosen_drink = "Americano Medium"
            menu:
                "No Milk":
                    $ current_chosen_milk = "No Milk"
                "Whole Milk":
                    $ current_chosen_milk = "Whole Milk"

        $ dad_order_brought = (current_chosen_drink,current_chosen_milk)

        ## HOWIE ORDER
        pov "What did [how] want to drink?"
        if howie_order[0] == "Decaf Mocha Medium":
            menu:
                "Decaf Mocha Medium":
                    $ current_chosen_drink = "Decaf Mocha Medium"
                "Decaf Macchiato Medium":
                    $ current_chosen_drink = "Decaf Macchiato Medium"
            menu:
                "Soy Milk":
                    $ current_chosen_milk = "Soy Milk"
                "Whole Milk":
                    $ current_chosen_milk = "Whole Milk"

        elif howie_order[0] == "Iced Tea Large":
            menu:
                "Chai Tea Large":
                    $ current_chosen_drink = "Chai Tea Large"
                "Iced Tea Large":
                    $ current_chosen_drink = "Iced Tea Large"
            menu:
                "Extra Sugar":
                    $ current_chosen_milk = "Extra Sugar"
                "Brown Sugar":
                    $ current_chosen_milk = "Brown Sugar"

        $ howie_order_brought = (current_chosen_drink,current_chosen_milk)

        ## MANAGER ORDER
        pov "What did [mrf] want to drink?"
        if manager_order[0] == "Decaf Cappuccino Large":
            menu:
                "Decaf Café au Lait":
                    $ current_chosen_drink = "Decaf Café au Lait"
                "Decaf Cappuccino Large":
                    $ current_chosen_drink = "Decaf Cappuccino Large"
            menu:
                "2%% Milk":
                    $ current_chosen_milk = "2%% Milk"
                "Skimmed Milk":
                    $ current_chosen_milk = "Skimmed Milk"

        elif manager_order[0] == "Chai Tea Medium":
            menu:
                "Iced Tea Large":
                    $ current_chosen_drink = "Iced Tea Large"
                "Chai Tea Medium":
                    $ current_chosen_drink = "Chai Tea Medium"
            menu:
                "No Sugar":
                    $ current_chosen_milk = "No Sugar"
                "Extra Sugar":
                    $ current_chosen_milk = "Extra Sugar"

        $ manager_order_brought = (current_chosen_drink,current_chosen_milk)
    elif coffee_runs_stage == 3:
        ## KANAKO ORDER
        pov "{i}What did [kan] want to drink?{/i}"
        if kanako_order[0] == "Cappuccino Medium":
            menu:
                "Matcha Latte Large":
                    $ current_chosen_drink = "Matcha Latte Large"
                "Cappuccino Medium":
                    $ current_chosen_drink = "Cappuccino Medium"
                "Pour Over Small":
                    $ current_chosen_drink = "Pour Over Small"
            menu:
                "Almond Milk":
                    $ current_chosen_milk = "Almond Milk"
                "Chocolate Milk":
                    $ current_chosen_milk = "Chocolate Milk"
                "Skim Milk":
                    $ current_chosen_milk = "Skim Milk"
            menu:
                "Heavy Cream":
                    $ current_chosen_cream = "Heavy Cream"
                "No Cream":
                    $ current_chosen_cream = "No Cream"
                "Regular Cream":
                    $ current_chosen_cream = "Regular Cream"

        elif kanako_order[0] == "Frappe Large":
            menu:
                "Decaf Large":
                    $ current_chosen_drink = "Decaf Large"
                "Iced Coffee Medium":
                    $ current_chosen_drink = "Iced Coffee Medium"
                "Frappe Large":
                    $ current_chosen_drink = "Frappe Large"
            menu:
                "Caramel Syrup":
                    $ current_chosen_milk = "Caramel Syrup"
                "Vanilla Extract":
                    $ current_chosen_milk = "Vanilla Extract"
                "Hazelnut Syrup":
                    $ current_chosen_milk = "Hazelnut Syrup"
            menu:
                "Extra Heavy Cream":
                    $ current_chosen_cream = "Extra Heavy Cream"
                "Extra Whip Cream":
                    $ current_chosen_cream = "Extra Whip Cream"
                "Extra Vanilla Cream":
                    $ current_chosen_cream = "Extra Vanilla Cream"

        $ kanako_order_brought = (current_chosen_drink,current_chosen_milk,current_chosen_cream)

        ## ISAAC ORDER
        pov "What did [jacdad] want to drink?"
        if isaac_order[0] == "Cappuccino Medium":
            menu:
                "Café au Lait Medium":
                    $ current_chosen_drink = "Café au Lait Medium"
                "Cappuccino Medium":
                    $ current_chosen_drink = "Cappuccino Medium"
                "Macchiato Medium":
                    $ current_chosen_drink = "Macchiato Medium"
            menu:
                "Caramel Syrup":
                    $ current_chosen_milk = "Caramel Syrup"
                "Vanilla Extract":
                    $ current_chosen_milk = "Vanilla Extract"
                "Whole Milk":
                    $ current_chosen_milk = "Whole Milk"
            menu:
                "White Chocolate Sprinkles":
                    $ current_chosen_cream = "White Chocolate Sprinkles"
                "Rainbow Sprinkles":
                    $ current_chosen_cream = "Rainbow Sprinkles"
                "Chocolate Sprinkles":
                    $ current_chosen_cream = "Chocolate Sprinkles"

        elif isaac_order[0] == "Americano Large":
            menu:
                "Americano Large":
                    $ current_chosen_drink = "Americano Large"
                "Espresso Double":
                    $ current_chosen_drink = "Espresso Double"
                "Frappe Large":
                    $ current_chosen_drink = "Frappe Large"
            menu:
                "Almond Milk":
                    $ current_chosen_milk = "Almond Milk"
                "Soy Milk":
                    $ current_chosen_milk = "Soy Milk"
                "2%% Milk":
                    $ current_chosen_milk = "2%% Milk"
            menu:
                "Hazelnut Cream":
                    $ current_chosen_cream = "Hazelnut Cream"
                "Vanilla Cream":
                    $ current_chosen_cream = "Vanilla Cream"
                "Caramel Cream":
                    $ current_chosen_cream = "Caramel Cream"

        $ isaac_order_brought = (current_chosen_drink,current_chosen_milk,current_chosen_cream)

        ## CORRINE ORDER
        pov "What did [cor] want to drink?"
        if corrine_order[0] == "Macchiato Small":
            menu:
                "Macchiato Small":
                    $ current_chosen_drink = "Macchiato Small"
                "Café au Lait Small":
                    $ current_chosen_drink = "Café au Lait Small"
                "Mocha Latte Small":
                    $ current_chosen_drink = "Mocha Latte Small"
            menu:
                "Vanilla Syrup":
                    $ current_chosen_milk = "Vanilla Syrup"
                "Chocolate Syrup":
                    $ current_chosen_milk = "Chocolate Syrup"
                "Caramel Syrup":
                    $ current_chosen_milk = "Caramel Syrup"
            menu:
                "Dark Chocolate Sprinkles":
                    $ current_chosen_cream = "Dark Chocolate Sprinkles"
                "Milk Chocolate Sprinkles":
                    $ current_chosen_cream = "Milk Chocolate Sprinkles"
                "White Chocolate Sprinkles":
                    $ current_chosen_cream = "White Chocolate Sprinkles"

        elif corrine_order[0] == "Chai Tea Large":
            menu:
                "Chai Tea Large":
                    $ current_chosen_drink = "Chai Tea Large"
                "Iced Tea Large":
                    $ current_chosen_drink = "Iced Tea Large"
                "Boba Tea Large":
                    $ current_chosen_drink = "Boba Tea Large"
            menu:
                "Lemon":
                    $ current_chosen_milk = "Lemon"
                "Honey":
                    $ current_chosen_milk = "Honey"
                "Sugar":
                    $ current_chosen_milk = "Sugar"
            menu:
                "No Ice":
                    $ current_chosen_cream = "No Ice"
                "50%% Ice":
                    $ current_chosen_cream = "50%% Ice"
                "25%% Ice":
                    $ current_chosen_cream = "25%% Ice"
        $ corrine_order_brought = (current_chosen_drink,current_chosen_milk,current_chosen_cream)

    elif coffee_runs_stage >= 4:#==
        ## BRADLEY ORDER
        pov "{i}What did [bra] want to drink?{/i}"
        if bradley_order[0] == "Mocha Grande":
            menu:
                "Mocha Grande":
                    $ current_chosen_drink = "Mocha Grande"
                "Cappuccino Double Shot":
                    $ current_chosen_drink = "Cappuccino Double Shot"
                "Small Hot Chocolate":
                    $ current_chosen_drink = "Small Hot Chocolate"
                "Medium Decaf":
                    $ current_chosen_drink = "Medium Decaf"
            menu:
                "Soy Milk":
                    $ current_chosen_milk = "Soy Milk"
                "Almond Milk":
                    $ current_chosen_milk = "Almond Milk"
                "Full Cream Milk":
                    $ current_chosen_milk = "Full Cream Milk"
                "2%% Milk":
                    $ current_chosen_milk = "2%% Milk"

            menu:
                "No Cream":
                    $ current_chosen_cream = "No Cream"
                "Extra Cream":
                    $ current_chosen_cream = "Extra Cream"
                "Regular Cream":
                    $ current_chosen_cream = "Regular Cream"
                "Chocolate Sprinkles":
                    $ current_chosen_cream = "Chocolate Sprinkles"
            menu:
                "No Ice":
                    $ current_chosen_topping = "Heavy Cream"
                "25%% Ice":
                    $ current_chosen_topping = "25%% Ice"
                "50%% Ice":
                    $ current_chosen_topping = "50%% Ice"
                "80%% Ice":
                    $ current_chosen_topping = "80%% Ice"

        elif bradley_order[0] == "Espresso Triple Shot":
            menu:
                "Americano Medium":
                    $ current_chosen_drink = "Americano Medium"
                "Macchiato Small":
                    $ current_chosen_drink = "Macchiato Small"
                "Pour Over Large":
                    $ current_chosen_drink = "Pour Over Large"
                "Espresso Triple Shot":
                    $ current_chosen_drink = "Espresso Triple Shot"
            menu:
                "Vanilla Syrup":
                    $ current_chosen_milk = "Vanilla Syrup"
                "Almond Milk":
                    $ current_chosen_milk = "Almond Milk"
                "Full Cream Milk":
                    $ current_chosen_milk = "Full Cream Milk"
                "2%% Milk":
                    $ current_chosen_milk = "2%% Milk"
            menu:
                "No Cream":
                    $ current_chosen_cream = "No Cream"
                "Vanilla Cream":
                    $ current_chosen_cream = "Vanilla Cream"
                "Cinnamon Cream":
                    $ current_chosen_cream = "Cinnamon Cream"
                "Cocoa Powder":
                    $ current_chosen_cream = "Cocoa Powder"
            menu:
                "No Calorie Sugar":
                    $ current_chosen_topping = "No Calorie Sugar"
                "Brown sugar":
                    $ current_chosen_topping = "Brown sugar"
                "No Sugar":
                    $ current_chosen_topping = "No Sugar"
                "Honey":
                    $ current_chosen_topping = "Honey"

        $ bradley_order_brought = (current_chosen_drink,current_chosen_milk,current_chosen_cream,current_chosen_topping)

        ## GLORIA ORDER
        pov "What did [glo] want to drink?"
        if gloria_order[0] == "Vanilla Latte Large":
            menu:
                "Chocolate Latte Large":
                    $ current_chosen_drink = "Chocolate Latte Large"
                "Hazelnut Latte Large":
                    $ current_chosen_drink = "Hazelnut Latte Large"
                "Caramel Latte Large":
                    $ current_chosen_drink = "Caramel Latte Large"
                "Vanilla Latte Large":
                    $ current_chosen_drink = "Vanilla Latte Large"
            menu:
                "Whole Milk":
                    $ current_chosen_milk = "Whole Milk"
                "Skim Milk":
                    $ current_chosen_milk = "Skim Milk"
                "Almond Milk":
                    $ current_chosen_milk = "Almond Milk"
                "Soy Milk":
                    $ current_chosen_milk = "Soy Milk"
            menu:
                "No Sugar":
                    $ current_chosen_cream = "No Sugar"
                "Honey":
                    $ current_chosen_cream = "Honey"
                "Brown Sugar":
                    $ current_chosen_cream = "Brown Sugar"
                "Extra Sugar":
                    $ current_chosen_cream = "Extra Sugar"
            menu:
                "Extra Whipped Cream":
                    $ current_chosen_topping = "Extra Whipped Cream"
                "Extra Whole Milk":
                    $ current_chosen_topping = "Extra Whole Milk"
                "Extra Heavy Cream":
                    $ current_chosen_topping = "Extra Heavy Cream"
                "Extra Chocolate Milk":
                    $ current_chosen_topping = "Extra Chocolate Milk"

        elif gloria_order[0] == "Mocha Latte Large":
            menu:
                "Macchiato Large":
                    $ current_chosen_drink = "Macchiato Large"
                "Mocha Latte Large":
                    $ current_chosen_drink = "Mocha Latte Large"
                "Matcha Latte Large":
                    $ current_chosen_drink = "Matcha Latte Large"
                "Cappuccino Latte Large":
                    $ current_chosen_drink = "Cappuccino Latte Large"
            menu:
                "Hazelnut Syrup":
                    $ current_chosen_milk = "Hazelnut Syrup"
                "Vanilla Syrup":
                    $ current_chosen_milk = "Vanilla Syrup"
                "Chocolate Syrup":
                    $ current_chosen_milk = "Chocolate Syrup"
                "Caramel Syrup":
                    $ current_chosen_milk = "Caramel Syrup"
            menu:
                "White Chocolate Sprinkles":
                    $ current_chosen_cream = "White Chocolate Sprinkles"
                "Dark Chocolate Sprinkles":
                    $ current_chosen_cream = "Dark Chocolate Sprinkles"
                "Rainbow Color Sprinkles":
                    $ current_chosen_cream = "Rainbow Color Sprinkles"
                "Milk Chocolate Sprinkles":
                    $ current_chosen_cream = "Milk Chocolate Sprinkles"
            menu:
                "Jam Stuffed Cookie":
                    $ current_chosen_topping = "Jam Stuffed Cookie"
                "Rice Cake Cookie":
                    $ current_chosen_topping = "Rice Cake Cookie"
                "Sugar Free Cookie":
                    $ current_chosen_topping = "Sugar Free Cookie"
                "Chocolate Chip Cookie":
                    $ current_chosen_topping = "Chocolate Chip Cookie"

        $ gloria_order_brought = (current_chosen_drink,current_chosen_milk,current_chosen_cream,current_chosen_topping)


    show black with dissolve
    $ renpy.pause()
    "When the orders are ready..."
    show pov neutral at left
    hide black with dissolve

    if gtime == 0:
        show brow neutral_talk at right
        bro "Here you go, thanks for the wait, my man."
    else:
        show effw neutral_talk at right
        eff "Here you go, [povname]. See ya at school."
    show pov neutral_talk at left
    pov "Thank you!"
    show pov embarrassed at left
    pov "{i}I'd better get these drinks back to the office. I hope they're right...{/i}"

    $ inventory.add(Items.coffeetray)
    $ renpy.notify("New Item Obtained: Tray of Coffee")

    $ bought_coffee_run_drinks = True

    jump lbl_cafeinside_day_setup

##########################################
## Returning with Coffee
label lbl_returning_with_coffee_order:
    scene bg officefloor_day with fade
    show pov neutral_talk at left with dissolve
    pov "Coffee's here!"
    show pov neutral at left
    if coffee_runs_stage == 2:
        show dad neutral_talk at right with dissolve
        if dad_order == dad_order_brought:
            dad "I'm surprised. You got it right."
        else:
            dad "You didn't get the right thing."
        hide dad with dissolve
        $ renpy.pause(2.0)

        show how embarrassed_talk at right with dissolve
        if howie_order == howie_order_brought:
            how "That's right."
        else:
            how "That's wrong."
        hide how with dissolve
        $ renpy.pause(2.0)

        show mrf bored_talk at right with dissolve
        if manager_order == manager_order_brought:
            mrf "That's right."
        else:
            mrf "That's wrong."
        hide mrf with dissolve

    elif coffee_runs_stage == 3:
        show kan neutral_talk at right with dissolve
        if kanako_order == kanako_order_brought:
            kan "That's right."
        else:
            kan "That's wrong."
        hide kan with dissolve
        $ renpy.pause(2.0)

        show jacdad embarrassed_talk at right with dissolve
        if isaac_order == isaac_order_brought:
            jacdad "That's right."
        else:
            jacdad "That's wrong."
        hide jacdad with dissolve
        $ renpy.pause(2.0)

        show cor bored_talk at right with dissolve
        if corrine_order == corrine_order_brought:
            cor "That's right."
        else:
            cor "That's wrong."# [corrine_order[2]] [corrine_order_brought[2]]
        hide cor with dissolve
    elif coffee_runs_stage >= 4:#==
        show bra neutral_talk at right with dissolve
        if bradley_order == bradley_order_brought:
            bra "That's right."
        else:
            bra "That's wrong."
        hide bra with dissolve
        $ renpy.pause(2.0)

        show glo embarrassed_talk at right with dissolve
        if gloria_order == gloria_order_brought:
            glo "That's right."
        else:
            glo "That's wrong."
        hide glo with dissolve
        $ renpy.pause(2.0)

    $ inventory.drop(Items.coffeetray)
    $ bought_coffee_run_drinks = False
    $ on_coffee_run_blocking = False

    ## FIRST SHIFT / TUTORIAL
    if main_story <= 100:
        $ renpy.pause(2.0)
        $ renpy.pause()

        $ internship_job_tutorial_completed_coffee_runs = True
        if internship_job_tutorial_completed_copy_machine:

            jump lbl_completed_all_office_training
        else:
            jump lbl_office_jobs_tutorials
    ## DAILY GRIND
    else:
        $ officejobs_complete += 1
        $ officejobs_coffeerun = 1

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

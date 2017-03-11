# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

define gui.text_font = "CARERRA-Jones.otf"
define gui.what_font = "CARERRA-Jones.otf"
define gui.interface_text_font = "CARERRA-Jones.otf"
define gui.glyph_font = "CARERRA-Jones.otf"


#define gui.interface_text_font = "The Black Pearl.ttf"
#define gui.glyph_font = "The Black Pearl.ttf"

#define gui.text_size = 40

init:
    $ frank = Character("Frank", image = "frank", color="#009900", what_color="#009900", what_font = "CARERRA-Jones.otf")
    $ claire = Character("Claire",image = "claire", color="#33ccff", what_color="#33ccff", what_font = "CARERRA-Jones.otf")
    $ bartender = Character("Bartender", color = "#dddcc5", what_color = "#dddcc5")

    $ ScaleClaire = 350
    $ ScaleFrank = 400

    $ PortraitScale = 1.1

    $ charles = Character("Charles", image = "charles", color="#FFA500", what_color="#FFA500", what_font = "CARERRA-Jones.otf")

    $ disFactor = 0.1

# The game starts here.

label start:

    image bgBar = "bgSectionsEdit1080.png"
    image bgBarDay = "Bar-BG-Daytime.png"
    #image bgBarDay = im.Scale("Bar-BG-Daytime.png", 1280 , 720)
    #image bgBarNight = im.Scale("Bar-BG-Nighttime.png", 1280 , 720)
    
    #image bgCounterTop = "bgBarTop1080.png"
    image bgCounterTop = "tempBarCounter.png"

    #image claire sit = 'ClaireLook1.png'
    image claire sit = im.Scale("ClaireLook1.png", ScaleClaire, ScaleClaire)
    image side claire = im.Scale("tempClairePortrait.png", ScaleClaire * PortraitScale, ScaleClaire* PortraitScale)

    image ClaireAngryUp = im.Scale("ClaireAngry1.png", ScaleClaire, ScaleClaire)
    #image ClaireAngryUp = 'ClaireAngry1.png'

    image claire look left = im.Scale("ClaireLook2.png", ScaleClaire, ScaleClaire)
    #image claire look left = 'ClaireLook2.png'

    image claire look player = im.Scale("ClaireLook-Player.png", ScaleClaire, ScaleClaire)

    image claire happy = im.Scale("ClaireHappy.png", ScaleClaire, ScaleClaire)

    image claire happy player= im.Scale("ClaireHappy2.png", ScaleClaire, ScaleClaire)

    #image frank sit = "TruckerSmall.png"
    image frank sit = im.Scale("RegularFrank.png", ScaleFrank, ScaleFrank)

    image side frank sit = im.Scale("tempFrankPortrait.png", ScaleFrank * PortraitScale, ScaleFrank * PortraitScale)

    image frank sit beer lookPlayer= im.Scale("TruckerSmallDrink.png", ScaleFrank, ScaleFrank)

    image frank sit beer lookRight = im.Scale("Frank-BeerLook1.png", ScaleFrank, ScaleFrank)
    image frank sit beer lookLeft = im.Scale("Frank-BeerLook2.png", ScaleFrank, ScaleFrank)

    image frank angry lookLeft = im.Scale("Frank-Angry2.png", ScaleFrank, ScaleFrank)
    image frank angry lookRight = im.Scale("Frank-Angry1.png", ScaleFrank, ScaleFrank)

    image frank smile = im.Scale("Frank-Smile1.png", ScaleFrank, ScaleFrank)

    image frank smile beer = im.Scale("Frank-Smile2.png", ScaleFrank, ScaleFrank)

    image frank drunk = im.Scale("Frank-BeerDrunk1.png", ScaleFrank, ScaleFrank)

    image frank drunk angry lookLeft = im.Scale("Frank-AngryDrunk2.png", ScaleFrank, ScaleFrank)
    image frank drunk angry lookRight = im.Scale("Frank-AngryDrunk1.png", ScaleFrank, ScaleFrank)

    image frank looking anim:
        #"Frank-BeerLook1.png"
        im.Scale("Frank-BeerLook1.png", ScaleFrank, ScaleFrank)
        pause 1.0
        #"Frank-BeerLook2.png"
        im.Scale("Frank-BeerLook2.png", ScaleFrank, ScaleFrank)
        pause 1.0
        repeat

    image frank drink anim:
        "TruckerSmallDrink.png"
        pause 1.0
        "TruckerSmall.png"
        pause 1.0
        repeat

    $ factorSeat = (0.1) * 0.85
    $ factorSeatOffset = 0.1
    $ factorSeatHeightOffset = -0.03

    transform Seat1:
        xcenter ((1 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    transform Seat2:
        xcenter ((3 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    transform Seat3:
        xcenter ((5 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset
        
    transform Seat4:
        xcenter ((7 * factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset
        
    transform Seat5:
        xcenter ((9 *factorSeat) + factorSeatOffset)
        yalign 0.25 + factorSeatHeightOffset

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    with dissolve
    
    jump Day1Block
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #"Hello, world."

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

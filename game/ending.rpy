label EndingBlock:
    scene black
    with dissolve
    transform epos1:
        xcenter 0.2
        ycenter 0.25
    transform epos2:
        xcenter 0.35
        ycenter 0.375
    transform epos3:
        xcenter 0.5
        ycenter 0.5
    transform epos3a:
        xcenter 0.2
        ycenter 0.8
    transform epos3b:
        xcenter 0.5
        ycenter 0.8
    transform etext1:
        xcenter 0.5
        ycenter 0.2
    transform etext2:
        xcenter 0.5
        ycenter 0.3
    transform etext3:
        xcenter 0.5
        ycenter 0.4
    transform etext4:
        xcenter 0.5
        ycenter 0.5
    transform etext5:
        xcenter 0.5
        ycenter 0.6
        
    
    show text "Isn't it interesting..." at epos1 as endingtext1
    with dissolve
    pause 3
    hide endingtext1
    with dissolve
    pause 1
    show text "sometimes the only choices you see" at epos2 as endingtext2
    with dissolve
    pause 3
    hide endingtext2
    with dissolve
    pause 1
    show text "are ones of little consequence." at epos3 as endingtext3
    with dissolve
    pause 3
    hide endingtext3
    with dissolve
    pause 1
    show frank drunk at epos3a
    with dissolve
    show text "Rude...It mattered to me" at epos3b as endingtext4
    with dissolve
    pause 3
    hide endingtext4
    hide frank drunk
    show text "My bad Frank... trying to be all deep and philosophical here." at epos3b as sorryfrank1
    with dissolve
    pause 3
    hide sorryfrank1
    pause 1
    show text "How much must you learn about someone, before you {bhave them figured out?}b" at etext1 as deeptext1
    with dissolve
    pause 3
    hide deeptext1
    
    
    

return
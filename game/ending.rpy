label EndingBlock:
    
    scene black
    with dissolve

    # play music "noir_v002_lpf_LOOPedit.wav" fadein 1.0 fadeout 1.0
    
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
        xalign 0.1
        ycenter 0.8
    transform epos3b:
        xalign 0.35
        ycenter 0.8
    transform etext1:
        xalign 0.3
        ycenter 0.2
    transform etext2:
        xalign 0.3
        ycenter 0.3
    transform etext3:
        xalign 0.3
        ycenter 0.4
    transform etext4:
        xalign 0.3
        ycenter 0.5
    transform etext5:
        xalign 0.3
        ycenter 0.6
    transform piccoord:
        xcenter 0.75
        ycenter 0.5
    transform quotespot1:
        xcenter 0.17
        ycenter 0.3
    transform quotespot2:
        xcenter 0.54
        ycenter 0.3
    transform quotespot3:
        xcenter 0.14
        ycenter 0.24
    transform piccoord2:
        xcenter 0.72
        ycenter 0.65
    

    show text "Isn't it interesting..." at epos1 as endingtext1
    with dissolve
    pause 3
    hide endingtext1
    with dissolve
  
    show text "sometimes the only choices you see" at epos2 as endingtext2
    with dissolve
    pause 3
    hide endingtext2
    with dissolve
    
    show choicepic at piccoord as sweetchoices
    with dissolve
    
    show text "are ones of little consequence." at epos3 as endingtext3
    with dissolve
    pause 3
    hide endingtext3
    with dissolve
    pause 0.5
    
    show text "That is what tends to happen... when you play someone else's game." at epos3b as profound1
    with dissolve
    pause 4
    hide profound1
    with dissolve
    show text "When you stick by the rules, the game stays the same, no matter how many times you play it." at epos3b as profound2
    with dissolve
    pause 4
    hide profound2
    with dissolve
    show text "Sometimes, a small change in the code... can unlock many possibilities." at epos3b as profound3
    with dissolve
    pause 4   
    hide profound3
    with dissolve
    
    show frank drunk at epos3a
    with dissolve
    pause 0.5 
    
    show text "       Rude...It mattered to me!" at epos3b as endingtext4
    with dissolve
    pause 3
    hide endingtext4
    hide frank drunk
    hide sweetchoices
    
    show text "My bad, Frank... trying to be all deep and philosophical here." at epos3b as sorryfrank1
    with dissolve
    pause 5
    hide sorryfrank1
    pause 0.5
               
    show text "How much must you learn about someone before you have them..." at etext2 as deeptext1
    with dissolve
    pause 3
    show text "{size=+10}Figured out?{/size}" at epos2 as deeptext2
    with dissolve
    pause 3
    
    hide deeptext1 
    hide deeptext2    
        
    show grouppic at piccoord2
    with dissolve
    show text "    Claire" at quotespot1 as clairequote
    with dissolve
    show text "stayed home instead of marching against dangerous deregulations." at quotespot2 as quotebasic
    with dissolve
    pause 2
    hide clairequote
    show text "  Charles" at quotespot1 as charlesquote
    with dissolve
    pause 4
    hide charlesquote
    pause 2
    
    show text "What if:" at quotespot3 as quoteadv
    with dissolve
    show text "   Frank" at quotespot1 as franksquote
    with dissolve
    pause 2
    hide franksquote
    show text "   Elysia" at quotespot1 as elysiasquote
    with dissolve
    pause 2
    hide elysiasquote
    show text " Braxton" at quotespot1 as braxtonsquote
    with dissolve
    pause 2
    hide braxtonsquote
    hide quoteadv
    hide quotebasic
    hide grouppic
    
   
    show text "{size=+10}How often do we judge people by a single decision,\nand make assumptions about their motivations?{/size}" at epos3 as datquote
    with dissolve
    pause 8
    hide datquote
    
    show text "{size=+10}Thank you for playing!{/size}" at epos3 as finalthanks
    with dissolve
    pause 4
    hide finalthanks
    
    show text "{size=-10}BTW: We know the earlier line about changing the \ncode STRONGLY hints at the fact that we might\nhave hidden secret content behind a few code\nchanges. We acknowledge it would be super \nclever but we didn't have time to get fancy with it\n so...it's just a metaphor :P{/size}" at epos3 as luls 
    with dissolve
    pause 10
    
    jump CreditsBlock
    

return
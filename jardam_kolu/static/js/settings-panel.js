function thisIsMadness() {

    // First, determine which scheme should be displayed. Priority: 1. URL, 2:Cookie. Same for welcome screen

    sColorScheme = "";
    bShowWelcome = false;

    if(location.hash.length > 0) {
        //remove # from hash string
        var sStrippedHash= location.hash.replace('#', '');
        if(location.hash.indexOf("styles-") > -1) {
            //Cookies.set('ht-hideWelcome', true);
            sColorScheme = sStrippedHash;
        }   

        if (location.hash.indexOf("welcome") > -1) {
            bShowWelcome = true;
        }
    }
    if(!sColorScheme) {
        sColorScheme = Cookies.get('ht-colorscheme');
    }

    // Secondly, write some temporary styles that will prevent flickering on Windows Chrome
    
    if (sColorScheme != null) {
        var sCssLink = "css/" + sColorScheme + '.css';
        $("link#theme-styles").attr("href", sCssLink);
        // Adding temporary style to make the current scheme look "active"
    }
    else {
        sColorScheme = "styles-bluegreen";
    }
    history.replaceState(undefined, undefined, "#" + sColorScheme);

    document.write('<style class="tempStyle">#' + sColorScheme + ' {background:#646464;}</style>');

    bHideSwitcher = Cookies.get('ht-hideSwitcher');
    if(!bHideSwitcher){
        // Show the switcher. By default it's off so add some temporary styles that make it on
        document.write('<style class="tempStyle">#settings-panel {display: block}</style>');
        document.write('<style class="tempStyle">.settings-toggle {background-color:#e9e9e9;}</style>');
        document.write('<style class="tempStyle">.settings-toggle a {color:#37424c}</style>');
    }
}

function refreshAfterHashChange(){
    //remove # from hash string
    var sStrippedHash= location.hash.replace('#', '');
    //update isFirstPick
    isFirstPick = !Cookies.get('ht-firstPickMade');
    if(location.hash.length > 0) {
        if(sStrippedHash.indexOf("styles-") > -1) {
            var sCssLink = 'css/' + sStrippedHash + '.css';
            $("link#theme-styles").attr("href", sCssLink);

            // Change the highlight to the active scheme
            $(".settings-panel").children('.theme').each(function() {
                $(this).removeClass('active');
            });
            $('#' + sStrippedHash).addClass('active');

            Cookies.set('ht-colorscheme', sStrippedHash);
        }
        if (location.hash.indexOf("welcome") > -1) {
            $("#welcomeScreen").show();
        } else {
            $("#welcomeScreen").hide({duration:400});
        } 
    }
}

/**
 * Randomize array element order in-place.
 * Using Durstenfeld shuffle algorithm.
 */
function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

$(function() {
    // Main function after document load completes
    
    window.onhashchange = function() {
        refreshAfterHashChange();
    };

    // Remove the temporary stylesheets introduced by thisIsMadness
    $("style.tempStyle").remove();

    isFirstPick = !Cookies.get('ht-firstPickMade');

    if(isFirstPick) {
        //Randomizer
        var aSchemes = [];
        $(".schemeShowcase").each(function(){
            aSchemes.push($(this).html());
            $(this).html("");
        });
        // This actually shuffles very poorly as Steve has discovered
        //aSchemes.sort(function() { return 0.5 - Math.random() });
        
        shuffleArray(aSchemes);

        $(".schemeShowcase").each(function(){
            $(this).html(aSchemes.pop());
        });
    }

    if(bShowWelcome){
        window.location.hash = "welcome";
    }
    
    $("#welcomeScreen .schemeSelect .scheme").each(function() {
        $(this).click(function(){
            $(window).scrollTop(0);

            if(isFirstPick) {
                var sStrippedHash= $(this).attr("href").replace('#', '');

                //alert("logging " + sStrippedHash + " as first pick");

                ga('send', {
                    hitType: 'event',
                eventCategory: 'Initial Scheme Selection',
                eventAction: sStrippedHash
                });

                Cookies.set('ht-firstPickMade', true, {expires:30});
            }
            return true;
        });
    });
        
    if(Cookies.get('ht-hideSwitcher') == null){
        $(".settings-panel").addClass("toggled");
        $(".settings-toggle").addClass("toggled");
    }

    $(".settings-toggle .toggle").click(function(){
        $(".settings-panel").fadeToggle({duration:400});
        if ($(".settings-toggle").hasClass('toggled') === false) {
            $(".settings-toggle").addClass("toggled");
            $(".settings-panel").addClass("toggled");
            Cookies.remove('ht-hideSwitcher');
        } else {
            $(".settings-panel").removeClass("toggled");
            $(".settings-toggle").removeClass("toggled");
            Cookies.set('ht-hideSwitcher', true);
        }
        return false;
    });


    refreshAfterHashChange();

    setTimeout(function() {
        $(".settings-panel").height($(document).height()-70);
        $("#welcomeScreen").height($(document).height());
    }, 500);
});



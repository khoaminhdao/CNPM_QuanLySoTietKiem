$(document).ready(function() {


      if($("#notification").text() != "")
            if($("#notification").text() == "Account or password is wrong!!" || $("#notification").text() == "You must login!!")
                $("#overlay").fadeToggle("fast");
            else
                $("#overlayPass").fadeToggle("fast");


    $("#changePass").click(function( event ){

        event.preventDefault();

        $("#overlayPass").fadeToggle("fast");

    });


    $("#loginLink").click(function( event ){

        event.preventDefault();

        $("#overlay").fadeToggle("fast");

    });


    $(".close").click(function(){

       if($("#overlay").css("display") != "none" ) {

            $("#overlay").fadeToggle("fast");
       }

       else if($("#overlayPass").css("display") != "none" ) {

            $("#overlayPass").fadeToggle("fast");
       }

    });



    $(document).keyup(function(e) {

        if(e.keyCode == 27)
            /* if($("#overlay").css("display") != "none" ) {

                event.preventDefault();

                $("#overlay").fadeToggle("fast");

            }

            else */ if($("#overlayPass").css("display") != "none" ){

                event.preventDefault();

                $("#overlayPass").fadeToggle("fast");
            }


    });

});
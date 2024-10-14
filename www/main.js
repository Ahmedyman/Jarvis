$(document).ready(function () {
    // Textillate on .text with adjusted delay
    $(".text").textillate({
      loop: true,
      sync: true,
      in: {
        effect: "bounceIn",
        delayScale: 1.5,  // Adjusted for smoother animations
        delay: 50,        // Increased delay for better effect timing
      },
      out: {
        effect: "bounceOut",
        delayScale: 1.5,
        delay: 50,
      },
    });
  
    // SiriWave configuration
    var siriWave = new SiriWave({
      container: document.getElementById("siri-container"),
      width: 800,
      height: 200,
      style: "ios9",
      amplitude: 1,
      speed: 0.3,
      autostart: true,
    });
  
    // Siri message animation
    $(".siri-message").textillate({
      loop: true,
      sync: true,
      in: {
        effect: "fadeInUp",
        delayScale: 1.5,  // Same delay scale for consistency
        delay: 50,
      },
      out: {
        effect: "fadeOutUp",
        delayScale: 1.5,
        delay: 50,
      },
    });
  
    // Click event for MicBtn
    $("#MicBtn").click(function () {
        eel.playAssistantSound();  // This should now work correctly
    
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommand()();
    });

    function doc_keyUp(e) {
      // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time 
      if (e.key === 'j' && e.metakey){
          eel.playAssistantSound()
          $("#oval").attr("hidden", true);
          $("#SiriWave").attr("hidden", false);
          eel.allCommand()();
      }
    }
    document.addEventListener('keyup',doc_keyUp,false);

    
  });



  //   function playAssistant(message){
  //     if (message != ""){
  //       $('#oval').attr("hidden", true);
  //       $('#SiriWave').attr("hidden", false);
  //       eel.allCommand(message);
  //       $("#chatbox").val("")
  //       $("#MicBtn").attr('hidden',false)
  //       $("#SendBtn").attr('hidden',true)
  //     }
  //   }
  //   function showHideButton(message){
  //     if (message.length == 0){
  //       $("#MicBtn").attr('hidden',false)
  //       $("#SendBtn").attr('hidden',true)
  //     }
  //     else{
  //       $("#MicBtn").attr('hidden',true)
  //       $("#SendBtn").attr('hidden',false)
  //     }
  //   }

  //   $("#chatbox").keyup(function (){
  //     let message = $("#chatbox").val();
  //     showHideButton(message)

  //   });
  //   $("#SendBtn").click(function () {
  //     let message = $("#chatbox").val();  // Get the message from the chatbox
  //     playAssistant(message);             // Pass the message to playAssistant
  //   });
    
  //   // enter press event handler on chat box
  //   $("#chatbox").keypress(function (e) {
  //     key = e.which;
  //     if (key == 13) {
  //         let message = $("#chatbox").val()
  //         playAssistant(message)
  //     }
  // });






  
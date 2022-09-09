function sendCommand(curDir, command) {
  finalCommand = curDir + command.replace(/\\n/g, '')
  console.log('sending.. ' + finalCommand)
  $.ajax({
    type: "POST",
    url: "/runCommand",
    data: JSON.stringify({ "command": finalCommand }),
    contentType: "application/json",
    dataType: 'json',
    success: function (data) {
      console.log(data)

      if ('currentDir' in data) {
        output = data['currentDir']
        console.log(output)
        $("#commandPalette").empty()
        $("#currentDir").empty().append(output + " --->>")
        $(".output").append("\n\rDirectory Changed to " + output+"\n\r")
        $(".output").append("\n\r----------------------------------------------------------------------------------------\n\r")
        $(".output").scrollTop($(".output")[0].scrollHeight);
        $("#commandHistory").append(finalCommand+"\n")
      }
      else {
        $("#commandPalette").empty()
        output = data['output']
        $(".output").append("\n" + output)
        $("#commandHistory").append(finalCommand+"\n")
        $(".output").append("\n\r------------------------------------------------------------------------------------------\n\r")
        $(".output").scrollTop($(".output")[0].scrollHeight);
        
      }

    }
  });
}

function setCurrentDir() {
  $.ajax({
    type: "POST",
    url: "/setCurrentDir",
    // data: JSON.stringify({ "command": command.replace(/\\n/g, '') }),
    contentType: "application/json",
    dataType: 'json',
    success: function (data) {
      //console.log(data)
      output = data['currentDir']
      $("#currentDir").empty().append(output + " --->>")
    }
  });
};

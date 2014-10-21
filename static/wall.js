function getMessage (){
    $.get(
        "/api/wall/list",
         function (data) {
            console.log(data);
        $("#message-container").empty();
        $(data.messages).each(function (msg) {
            var message_text = data.messages[msg].message;
            $('#message-container').append('<li class="list-group-item">' +
                message_text + '</li>');
        });
        }
    );
}

getMessage();

function updateMessage(){

}



// $(".list-group-item").empty();
// $(".list-group-item").load("/api/wall/list", function() {
//   for (dict in session['messages']) {
//     message = dict['message'];
//   }
// }); 
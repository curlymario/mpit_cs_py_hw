function update() {
    $.get('log', function(data) {
        $('#chat').html(data);
    });
}

$(function() {
    $('#send').click(function() {
        $.post('/send', {'msg': $('#msg').val()}, update);
    })

    setInterval(update, 1000);
})
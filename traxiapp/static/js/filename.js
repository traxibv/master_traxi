$(document).ready(function () {
    $('#profile_pic').change(function () {
        var filename = $('input[type=file]').val().split('\\').pop();
        console.log(filename, $('#filename'));
        var lastIndex = filename.lastIndexOf("\\");
        $('#filename').val(filename);
    });
});

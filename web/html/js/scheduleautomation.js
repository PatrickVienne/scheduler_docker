$(function() {
    console.log('jquery loaded');
    $.ajax({
        url: 'http://localhost:8081'
    })
    .done(function( data ) {
        console.log('Data: ' + data);
    });

    $("#employee_form").submit(function(e){
        console.log("Submitting Form");
        console.log("Serialized data" +  $("#employee_form").serialize());
        console.log("Serialized data" +  $(this).serialize());
        $.ajax({
            url: 'http://localhost:8081/employee/add',
            method: 'POST',
            data: $("#employee_form").serialize()
            }).done(function(data) {
                console.log('Done Adding, Data: ' + data);
            });
        e.preventDefault();
    });

});

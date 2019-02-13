$(document).ready(function(){
    $( "#dialog_add_student" ).dialog({ autoOpen: false, width:500 });

    $("#add_student").click(function(){
        $( "#dialog_add_student" ).dialog( "open" );
        $(this).hide();
    });

    $("#form_add_student").submit(function(e){
        e.preventDefault();
         $.ajax({
            url:'/ajax_add_student/',
            type:"post",
            data: $(this).serialize(),
            success:function(data){
                console.log(data);
            },
            error:function(){
                alert("Ошибка");
            }
        })
    });

});
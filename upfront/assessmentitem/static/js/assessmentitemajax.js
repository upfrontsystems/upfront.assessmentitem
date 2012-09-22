$(document).ready(function() {

    var answercount = 0;

    $("#add_answer").click(function() {

        answercount += 1;
        answerid = 'answer' + answercount;

        $.ajax({
            url: '@@upfront.assessmentitem.answerform',
            data: {'answerid': answerid},
            success: function(data) {
                $("#answer_listing").append(data);
                tinymceid = 'form.widgets.' + answerid + '.answer';
                var config = new TinyMCEConfig(tinymceid);
                config.init();
                $('#' + answerid + " .delete").click(function() {
                    $(this).parent().remove();    
                });
            }
        });

    });

});


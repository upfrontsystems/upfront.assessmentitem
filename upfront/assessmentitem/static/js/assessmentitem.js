$(document).ready(function() {

    var url = location.href;

    $('.assessmentitem-edit-link').prepOverlay({
        subtype: 'ajax',
        filter: '#content>*',
        formselector: '#form',
        noform: 'reload',
        redirect: url,
        closeselector: '[name=form.buttons.cancel]',
        config: {
            onLoad: function() {
                $("#add_answer").click(add_answer);
                tinymceid = 'form.widgets.question';
                delete InitializedTinyMCEInstances[tinymceid];
                var config = new TinyMCEConfig(tinymceid);
                config.init();
            }
        }
    });


    var answercount = 0;

    function add_answer() {
        answercount += 1;
        answerid = 'answer' + answercount;

        $.ajax({
            url: '@@upfront.assessmentitem.answerform',
            data: {'answerid': answerid},
            success: function(data) {
                $("#answer_listing").append(data);
                tinymceid = 'form.widgets.' + answerid + '-answer';
                var config = new TinyMCEConfig(tinymceid);
                config.init();
                $('#' + answerid + " .delete").click(function() {
                    $(this).parent().remove();    
                });
            }
        });
    }

    $('#add_answer').click(add_answer);

    $('#answer_listing .delete').click(function() {
        $(this).parent().remove();    
    });
});


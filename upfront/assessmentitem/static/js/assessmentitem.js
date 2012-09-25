$(document).ready(function() {

    var url = location.href;

    var answercount = 0;

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
                var tinymceid = 'form.widgets.question';
                delete InitializedTinyMCEInstances[tinymceid];
                var config = new TinyMCEConfig(tinymceid);
                config.init();
                answercount = 0;

                $("#answer_listing textarea.mce_editable").each(
                    function(index) {
                        answercount += answercount;
                        config = new TinyMCEConfig($(this).attr('id'));
                        config.init();
                    }
                );
            }
        }
    });


    function add_answer() {
        answercount += 1;
        answerid = 'answer' + answercount;

        $.ajax({
            url: '@@upfront.assessmentitem.answerform',
            data: {'answerid': answerid},
            success: function(data) {
                $("#answer_listing").append(data);
                var tinymceid = 'form.widgets.' + answerid + '-answer';
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


$(document).ready(function() {

    var url = location.href;

    var answercount = 0;

    $('a.showintro').click(function() {
        $('#introduction').toggle();
        return false;
    });

    $('a.add-intro-link').prepOverlay({
        subtype: 'ajax',
        filter: '#content>*',
        formselector: '#form',
        noform: 'close',
        closeselector: '[name=form.buttons.cancel]',
        config: {
            onLoad: function() {
                var tinymceid = 'form.widgets.introduction';
                delete InitializedTinyMCEInstances[tinymceid];
                var config = new TinyMCEConfig(tinymceid);
                config.init();
            }
        },
        afterpost: function(resp, data) {
            console.log(resp);
            console.log(data);
        }
    });

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
        answerid = answercount;

        $.ajax({
            url: '@@upfront.assessmentitem.answerform',
            data: {'answerid': answerid},
            success: function(data) {
                $("#answer_listing").append(data);
                $("input[name='form.widgets.answers.count']").attr('value', answercount);
                answercount += 1;
                $("input[name='form.widgets.answers.count']").attr('originalvalue', answercount);
                var tinymceid = 'form.widgets.answers.' + answerid + '.widgets.answer';
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


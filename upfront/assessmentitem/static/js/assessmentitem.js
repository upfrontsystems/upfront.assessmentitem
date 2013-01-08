$(document).ready(function() {

    var url = location.href;

    $('a.delete_confirmation').prepOverlay({
        subtype: 'ajax',
        filter: common_content_filter,
        formselector: '#delete_confirmation',
        noform: function(el) {return $.plonepopups.noformerrorshow(el, 'redirect');},
        redirect: $.plonepopups.redirectbasehref,
        closeselector: '[name="form.button.Cancel"]',
        width:'50%'
    });

    var answercount = 0;

    $('input.remove-intro-button').click(function() {
        $('#intro-selected').hide();
        $('#intro-actions').show();
        return false;
    });

    var selectintro = function(resp, data) {
            var div = $(resp),
                path = $('#path', div).attr('data-path'),
                href = $('#url', div).attr('data-url');
            $('#introtext').html(
                $('#form-widgets-introduction', div).html()
            );
            $('#form-widgets-introduction').attr('value', path);
            $('#intro-actions').hide();
            $('#intro-selected').show();
            $('#intro-selected input.edit-intro-button').attr('href', href + '/edit');
            $('input.edit-intro-button').prepOverlay(config);
    };

    var config = {
        subtype: 'ajax',
        filter: '#content>*',
        formselector: '#form',
        noform: 'close',
        closeselector: '[name="form.button.Cancel"]',
        config: {
            onLoad: function() {
                var tinymceid = 'form.widgets.introduction';
                delete InitializedTinyMCEInstances[tinymceid];
                var config = new TinyMCEConfig(tinymceid);
                config.init();
            }
        },
        afterpost: selectintro
    }

    $('input.add-intro-button').prepOverlay(config);
    $('input.edit-intro-button').prepOverlay(config);

    $('input.select-intro-button').prepOverlay({
        subtype: 'ajax',
        filter: '#content>*',
        formselector: 'form',
        noform: 'close',        
        closeselector: '[name="form.button.Cancel"]',
        afterpost: selectintro
    });

    function add_answer() {
        var answercount = $('input[name="form.widgets.answers.count"]')
            .attr('value');

        $.ajax({
            url: '++add++upfront.assessmentitem.content.assessmentitem',
            data: {'form.widgets.answers.buttons.add': 'Add Answer',
                   'form.widgets.answers.count': answercount},
            success: function(data) {
                var el = $(data),
                    answers = $('#formfield-form-widgets-answers', el),
                    answercount = $('input[name="form.widgets.answers.count"]',
                        answers).attr('value');;
                var newanswer = $('div.answers-widget-field', answers).last();
                var removebtn_id = $('div.answers-widget-remove-button input',
                    newanswer).attr('id');

                /* update answercount */
                $('input[name="form.widgets.answers.count"]').attr('value',
                    answercount);
                /* hack to get answer's outerhtml */
                var html = $('<div />').append(newanswer.clone()).html()
                $("#formfield-form-widgets-answers").append(html);

                var tinymceid = $('textarea.mce_editable', newanswer)
                    .attr('id');
                var config = new TinyMCEConfig(tinymceid);
                config.init();
                $('#'+removebtn_id).click(function() {
                    $(this).parents('div.answers-widget-field').remove();
                    return false;
                });
            }
        });
        return false;
    }

    $('#form-widgets-answers-buttons-add').addClass('allowMultiSubmit');
    $('#form-widgets-answers-buttons-add').click(add_answer);

    $('#answer_listing .delete').click(function() {
        $(this).parent().remove();    
    });
});


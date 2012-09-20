$(document).ready(function() {

    var answercount = 0;

    jq("#add_answer").click(function() {

        // Extract URL from HTML page
        var answerhtml = jq("#add_answer_ajaxlink a").attr("href");
        if (answerhtml) {
            // create the divs where ajax call with reside
            jq("#answer_template").append('<li><div id="result_answer"></div><div id="result_choice"></div></li>');
    
            answercount += 1;
            answerid = 'form.widgets.answer' + answercount;
            jq("#result_answer").load(
                '@@tinymce',
                {'fieldname': answerid},
                function() {
                    var config = new TinyMCEConfig(answerid);
                    config.init();

                });
            jq("#result_choice").load('++add++upfront.assessmentitem.content.answer #formfield-form-widgets-iscorrect');

            // place formatted ajax result in appropriate place
            jq("#answer_listing ul").append(jq('#answer_template li'));

            //remove result_answer and result_choice id from placed ajax results. (to not confuse next ajax request)
            jq("#answer_listing #result_answer").removeAttr('id');
            jq("#answer_listing #result_choice").removeAttr('id');

            // show the delete answer button
            jq("#delete_last_answer").removeClass('hidden');
            
        }
    });

    jq("#delete_last_answer").click(function() {

        jq("#answer_listing li:last").detach();

        //hide delete answer button if no answers exist
        if (jq("#answer_listing li").length == 0) {
            jq("#delete_last_answer").addClass('hidden');
        }

    });

});


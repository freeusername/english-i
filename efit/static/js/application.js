$(function () {

    $("input[placeholder], textarea[placeholder]").placeholder();

    $(function () {
        $('#registration_form, #reset_form_pasword').on('submit', function (e) {
            e.preventDefault();
            var $form = $(this);
            $('*', $form).removeClass('errors');
            $form.ajaxSubmit({
                success: function (data) {
                    if (data.errors) {
                        var error_list = new Array();
                        $.each(data['errors'], function (k, v) {
                            $('*[name=' + k + '][type!=submit]', $form).addClass('errors');
                            error_list.push(v);
                        });
                        $('div.error_notice', $form).html(error_list.join(' '));
                    } else {
                        if (data['location']) {
                            window.location = data['location'];
                        } else {
                            window.location = $form.action
                        }
                    }
                }
            });
        });
        $('#profile-edit_form').on('submit', function (e) {
            e.preventDefault();
            var $form = $(this);
            $('*', $form).removeClass('errors');
            $('#success').hide();
            $form.ajaxSubmit({
                success: function (data) {
                    if (data.errors) {
                        var error_list = new Array();
                        $.each(data['errors'], function (k, v) {
                            $('*[name=' + k + '][type!=submit]', $form).addClass('errors');
                            error_list.push(v);
                        });
                        $('div.error_notice', $form).html(error_list.join(' '));
                    } else {
                        if (data['success']) {
                            $('#success').show(true)
                        }
                    }
                }
            });
        });
        $('#login_form').on('submit', function (e) {
            e.preventDefault();
            var $form = $(this);
            $('*', $form).removeClass('errors');
            $form.ajaxSubmit({
                success: function (data) {
                    if (data.errors) {
                        var error_list = new Array();
                        $.each(data['errors'], function (k, v) {
                            $('*[name=' + k + '][type!=submit]', $form).addClass('errors');
                            error_list.push(v);
                        });
                        $('div.error_notice', $form).html(error_list.join(' '));
                    } else {
                        window.location = data['location'];
                    }
                }
            });
        });
    });
});

/* slider */
$(window).load(function() {
  var slider_block = $('.slider_block');
  var slides = $('.slides');
  var slide = $('.slide');

  var current_height = $(window).innerHeight() - $('.header').innerHeight();

  slider_block.css({'height' : ((current_height * 85) / 100) + 'px'});
  slides.css({'height' : ((current_height * 85) / 100) + 'px'});
  slide.css({'height' : ((current_height * 85) / 100) + 'px'});
});

$(window).resize(function() {
  var slider_block = $('.slider_block');
  var slides = $('.slides');
  var slide = $('.slide');

  var current_height = $(window).innerHeight() - $('.header').innerHeight();

  slider_block.css({'height' : ((current_height * 85) / 100) + 'px'});
  slides.css({'height' : ((current_height * 85) / 100) + 'px'});
  slide.css({'height' : ((current_height * 85) / 100) + 'px'});
});
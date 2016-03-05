(function($) {
    $(document).ready(function(){
        $(document).on("change", "select#id_value_type", function(evt) {
            var vt = $(this).val();
            $("fieldset.value_fields").hide();
            $("fieldset.cls-"+vt).show();
        });
        $("select#id_value_type").trigger('change');
    })
})(jQuery || django.jQuery);


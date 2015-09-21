(function($) {
    $.fn.scrollbox = function() {


        return this.each(function() {
            var container = $(this),
                containerUL,
                nextScrollId = null,
                forward,
                move_on,
                scrollForward,
                move = 1,

                containerUL = container.children('ul:first-child');
            scrollForward = function() {


                $('.boll1, .boll2, .boll3, .boll4, .boll5, .boll6, .boll7, .boll8').show();
                containerUL.children('li').removeClass('boll1 boll2 boll3 boll4 boll5 boll6 boll7 boll8');

                containerUL.children('li:nth-child(1)').addClass('boll1');
                containerUL.children('li:nth-child(2)').addClass('boll2');
                containerUL.children('li:nth-child(3)').addClass('boll3');
                containerUL.children('li:nth-child(4)').addClass('boll4');
                containerUL.children('li:nth-child(5)').addClass('boll5');
                containerUL.children('li:nth-child(6)').addClass('boll6');
                containerUL.children('li:nth-child(7)').addClass('boll7');
                containerUL.children('li:nth-child(8)').addClass('boll8');
            };
            forward = function() {
                if(move==1){
                    scrollForward();
                    return false;
                }
            };
            move_off = function() {
                    move=0;

            };
            move_on = function() {
                move=1;

            };
            // bind events for container
            container.bind('forward', function() { clearTimeout(nextScrollId);containerUL.append(containerUL.children('li:nth-child(1)')) ; forward();});
            container.bind('move_on', function() {move_on();});
            container.bind('move_off', function() {move_off();});

            return false;
        });
        return false;
    };return false;
}(jQuery));

$(function () {
    $('.mainNav a').each(function () {
        var location = window.location.href;
        var link = this.href;
        if(location == link)
        {
            $(this).parent().addClass('active');
        }
    });return false;
});
var Frontend = (function() {

    var animateJuryText = function() {
        var typed = new Typed('.juryTextValue', {
            strings: ['HABEL'],
            typeSpeed: 20
        });
    };

    var initClock = function() {
        setInterval('Frontend.updateClock()', 1000);
        $('.typed-cursor').show();
    };

    return {
        init: function() {
            initClock();
            animateJuryText();
        },

        updateClock: function() {
            $('.clock').html(moment().locale('de').format('LLLL'));
        }
    };
})();

$(document).ready( function() {
	Frontend.init();
});

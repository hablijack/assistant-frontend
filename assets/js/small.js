var Frontend = (function() {
    var initClock = function() {
        Frontend.updateClock()
        setInterval('Frontend.updateClock()', 50000);
    };
    return {
        init: function() {
            initClock();
        },
        updateClock: function() {
            $('.clock').html(moment().locale('de').format('LT'));
        }
    };
})();

$(document).ready( function() {
    Frontend.init();
    Frontend.updateClock();
});

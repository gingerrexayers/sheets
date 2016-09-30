$(document).ready(function(){
  $('.rollable').click(function(){
    var result = 0;
    var mod = 0;
    for (var x = 0; x < $(this).find('.die_count').val(); x++) {
      result += Math.ceil(Math.random() * $(this).find('.die_size').val());
    }
    var str = $(this).children('input').val();
    if (str > 17) {
      mod = 3;
    } else if (str > 15) {
      mod = 2;
    } else if (str > 12) {
      mod = 1;
    } else if (str > 8) {
      mod = 0;
    } else if (str > 5) {
      mod = -1;
    } else if (str > 3) {
      mod = -2;
    } else {
      mod = -3;
    }
    var roll = result+mod;
    $('#result').text(result + ' + ' + mod + ' = ' + roll);
  });
});

$(function(){
	loadEvents();
});


function loadEvents(){
	$('#tabled').hide();
	$('#submit-nag').click(function(){
		var data = $('#data-numbers').val()
		$.ajax({
            url: '/tendencia-central/calcular_tendencia_no_agrupada',
            data: {data: data},
            type: 'POST',
            success: function(response) {

                var k = 0;
                $.each(response, function(i,v){
					console.log([i,v]);
//					$('#tabledbody').empty().append("<tr><td>"+ m['intervalo'] +"</td><td>"+ m['marca de clase'] +"</td><td>"+ m['frecuencia relativa'] +"</td><td>"+ m['frecuencia relativa acumulada'] +"</td></tr>");
					k += 1;
                });
                $('#tabled').show();
            },
            error: function(error) {
                console.log(error);
            }
        });
	});
}

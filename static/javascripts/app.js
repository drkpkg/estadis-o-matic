$(function(){
	loadEvents();
});


function loadEvents(){
	$('#tabled').hide();
	$('#tc').hide();

	$('#submit-nag').click(function(){
		var data = $('#data-numbers').val()
		$('#submit-nag').hide();

		$.ajax({
            url: '/tendencia-central/calcular_tendencia_no_agrupada',
            data: {data: data},
            sync: true,
            type: 'POST',
            success: function(response) {
                $('#tabledbody').empty();
                $('#tc').empty();

                $.each(response.tabla,function(i,data){
			        $('#tabledbody').append("<tr><td>" + data['intervalo'][0] + "-" + data['intervalo'][1] + "</td><td>" + data['marca de clase']
					                        + "</td><td>" + data['frecuencia relativa'] + "</td><td>" + data['frecuencia relativa acummulada']
					                        +"</td></tr>");
				});

                $('#tc').append("<div class='form-group'><label>Media: " + response.tc.media + "</label></div>");
                $('#tc').append("<div class='form-group'><label>Mediana: " + response.tc.mediana + "</label></div>");
                $('#tc').append("<div class='form-group'><label>Moda: " + response.tc.moda + "</label></div>");
                $('#tc').append("<div class='form-group'><label>Media Armónica: " + response.tc.armonica + "</label></div>");
                $('#tc').append("<div class='form-group'><label>Media Geométrica: " + response.tc.geometrica + "</label></div>");

                $('#tabled').show();
                $('#tc').show();
            },
            error: function(error) {
                console.log(error);
            }
        });
        $('#submit-nag').show();
	});
}

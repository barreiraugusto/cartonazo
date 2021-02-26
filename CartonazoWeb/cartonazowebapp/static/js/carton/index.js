/**
     * Permite obtener el token de django
     * 
     */
    function getCookie(name) {

        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        //RETORNANDO EL TOKEN
        return cookieValue;
  
      }//end function getCookie
  
  /*EJEMPLO AJAX HACIA DJANGO*/
          //token
        setInterval(function chequeo_carton(){
          var csrftoken = getCookie('csrftoken');
          $.ajax({
              type: "POST",
              url: "/control/",
              data:{
                  csrfmiddlewaretoken : csrftoken, 
              },
              dataType: "json",
              success: function(data) {
                //location.reload(true);
                //$('#carton').load("{% url 'controlar' %}");
                $('#carton tbody').html("");
                
                for (let f = 0; f < 3; f++){
                    let fila1 ="<tr>";
                    for (let i = 0; i < 9; i++){
                        let celda = "celda" + i + f
                        if (data[celda]){
                            if (data[celda][1]){
                                fila1 += "<td style='background-color:green; text-align: center;'><h1>" + data[celda][0] + "</td>"
                            }else{
                                fila1 += "<td style='background-color:orange; text-align: center;'><h1>" + data[celda][0] + "</td>"
                            }
                        }else{
                            fila1 += "<td style='background-color:lightslategray;'></td>"
                        }
                    }               
                    fila1 += '</tr>';
                    $('#carton tbody').append(fila1);
                //document.getElementById("carton").innerHTML = data;
                }
              },
              error: function( jqXHR, textStatus, errorThrown ) {
  
                  if (jqXHR.status === 0) {
  
                      alert('Error al intentar Conectarse: Verifique su conexion a Internet.');
  
                  } else if (jqXHR.status == 404) {
  
                      alert('La Pagina solicitada no fue encontrada [404]');
  
                  } else if (jqXHR.status == 500) {
  
                      alert('Erro Interno [500]');
  
                  } else if (textStatus === 'parsererror') {
  
                      alert('Error en el retorno de Datos. [parseJson]');
  
                  } else if (textStatus === 'timeout') {
  
                      alert('Tiempo de Espera agotado');
  
                  } else if (textStatus === 'abort') {
                      alert('Solicitud Abortada. [Ajax Request]');
  
                  } else {
                      alert('Error desconocido: ' + jqXHR.responseText);
  
                  }//end if 
  
              }//end error
          }); 
        },2000)

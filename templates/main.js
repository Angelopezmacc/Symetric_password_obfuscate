// function cifrar(elem){
// 	// var plaintext = document.getElementsByTagName('input')[0].value;
// 	var plaintext = "Hola"
// 	var aes256 = require('aes256');
// 	var key = 'my passphrase';

// 	var buffer = Buffer.from(plaintext);

// 	var cipher = aes256.createCipher(key);

// 	var encryptedPlainText = cipher.encrypt(plaintext);
// 	var decryptedPlainText = cipher.decrypt(encryptedPlainText);
// 	// plaintext === decryptedPlainText

// 	var encryptedBuffer = cipher.encrypt(buffer);
// 	var decryptedBuffer = cipher.decrypt(encryptedBuffer);

// 	console.log(encryptedBuffer);
// 	console.log(encryptedPlainText);
// 	alert(encryptedBuffer);
// }
// function fun() {  

//     var plaintext = document.getElementsByTagName("input")[0].value;
//     //var plaintext = "Hola";
//     //const aes256 = require('aes256');
//     var key = 'my passphrase';
//     var palabra_codificada = btoa(plaintext);
//     // var buffer = Buffer.from(plaintext);

//     // var cipher = aes256.createCipher(key);

//     // var encryptedPlainText = cipher.encrypt(plaintext);
//     // var decryptedPlainText = cipher.decrypt(encryptedPlainText);
//     // // plaintext === decryptedPlainText

//     // var encryptedBuffer = cipher.encrypt(buffer);
//     // var decryptedBuffer = cipher.decrypt(encryptedBuffer);

//     console.log(palabra_codificada);
//     alert(palabra_codificada);  
//     }

var plaintext1 = document.getElementsByTagName("input")[0].value;
var plaintext2 = document.getElementsByTagName("input")[1].value;

var palabra_codificada1 = btoa(plaintext1);
var palabra_codificada2 = btoa(plaintext2);

$(document).ready(function () {
    $("#formulario").bind("submit",function(){
        // Capturamnos el boton de envío
        var btnEnviar = $("#btnEnviar");
        //event.preventDefault();
    //     $.ajax({
    //         type: $(this).attr("method"),
    //         url: $(this).attr("action"),
    //         data:$(palabra_codificada1,palabra_codificada2).serialize(),
        	$.ajax({
			    type:"POST", // la variable type guarda el tipo de la peticion GET,POST,..
			    $(this).attr("action")
			    //url:"/login", //url guarda la ruta hacia donde se hace la peticion
			    data:{username:palabra_codificada1,password:palabra_codificada2}, // data recive un objeto con la informacion que se enviara al servidor
			    success:function(datos){ //success es una funcion que se utiliza si el servidor retorna informacion
			         console.log(datos.promedio)
			     },
			    dataType: dataType // El tipo de datos esperados del servidor. Valor predeterminado: Intelligent Guess (xml, json, script, text, html).
				})
            beforeSend: function(){
                /*
                * Esta función se ejecuta durante el envió de la petición al
                * servidor.
                * */
				users = jQuery.parseJSON(response.d);

                user = data[0].password;
                pass = data[1].username;
                console.log(user);
                console.log(pass);

                // btnEnviar.text("Enviando"); Para button 
                btnEnviar.val("Enviando"); // Para input de tipo button
                btnEnviar.attr("disabled","disabled");
                alert("paso1");
            },
            complete:function(data){
                /*
                * Se ejecuta al termino de la petición
                * */
                users = jQuery.parseJSON(response.d);

                user = data[0].password;
                pass = data[1].username;
                console.log(user);
                console.log(pass);
                btnEnviar.val("Enviar formulario");
                btnEnviar.removeAttr("disabled");
                alert("paso2");
            },
            success: function(data){
                /*
                * Se ejecuta cuando termina la petición y esta ha sido
                * correcta
                * */
                users = jQuery.parseJSON(response.d);

                user = data[0].password;
                pass = data[1].username;
                console.log(user);
                console.log(pass);
                $(".respuesta").html(data);
                alert("paso3");
            },
            error: function(data){
                /*
                * Se ejecuta si la peticón ha sido erronea
                * */
                alert("Problemas al tratar de enviar el formulario");
            }
        });

        // Nos permite cancelar el envio del formulario
        return false;
    });
});
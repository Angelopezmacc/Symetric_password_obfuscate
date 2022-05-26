// $("#funciona").ready(function() {
//     $('funciona').on('submit', function(event) {
//         $.ajax({
//             data : {
//                 username : $(hash1).val(),
//                 password: $(hash2).val()
//             },
//             type : 'POST',
//             url : '/process'
//         })
//         .done(function(data) {
//             if (data.error) {
//                 $('#errorAlert').text(data.error).show();
//                 $('#successAlert').hide();
//             }
//             else {
//                 $('#successAlert').text(data.name).show();
//                 $('#errorAlert').hide();
//             }
//         });
//         event.preventDefault();
//     });
// });

var user = document.getElementById("username");
var password = document.getElementById("password");

var hash1 = CryptoJS.SHA256(user);
var hash2 = CryptoJS.SHA256(password);

console.log(hash1);

// Primero es necesario deshabilitar el envío automático de la acción del formulario
$("#funciona").submit(function(e){
    e.preventDefault();
    var user = document.getElementsByTagName('input')[0].value;
    var password = document.getElementsByTagName('input')[1].value;

    var hash1 = CryptoJS.SHA256(user);
    var hash2 = CryptoJS.SHA256(password);
    e.preventDefault();
    console.log(hash1);
    $.ajax({
    type:"POST", // la variable type guarda el tipo de la peticion GET,POST,..
    url:"/process", //url guarda la ruta hacia donde se hace la peticion
    //data:{nombre:"pepe",edad:10}, // data recive un objeto con la informacion que se enviara al servidor
    // data : {
    //             username : $(hash1).val(),
    //             password: $(hash2).val()
    // },
    data : {
                username : has1,
                password: hash2
    }, 
    success:function(datos){ //success es una funcion que se utiliza si el servidor retorna informacion
         console.log(datos.promedio)
     },

    //dataType: dataType // El tipo de datos esperados del servidor. Valor predeterminado: Intelligent Guess (xml, json, script, text, html).
})
         $.ajaxSetup({
      data:{
        isAjax:true
      }
    });

    // $.ajax({
    //     type : 'POST',
    //     url : '/process',
        // data : {
        //         "username" : $(hash1).val(),
        //         "password": $(hash2).val()
        //     },   // Este pase de serialización es importante
    //     // headers:{
    //     //     "X-CSRF-Token": getCookie('csrf_token')
    //     // },
    //     // success:function (resp) {
    //     //     // window.location.href = "/admin/page";
    //     //     if(resp.error){
    //     //         console.log(resp.errmsg);
    //     //     }
    //     // }
    // })
    // .done(function(data) {
    //         if (data.error) {
    //             $('#errorAlert').text(data.error).show();
    //             $('#successAlert').hide();
    //             console.log(hash1);
    //         }
    //         else {
    //             $('#successAlert').text(data.name).show();
    //             $('#errorAlert').hide();
    //         }
    //     });
    //     //event.preventDefault();
    e.preventDefault();
});

// $(document).ready(function(){
//   function ajax_login(){
//     $.ajax({
//          url:'/process',
//         data : {
//                 username : $(hash1).val(),
//                 password: $(hash2).val()
//             },
//          type:'POST',
//          success:function(response){
//            console.log(response);
//          },
//          error:function(error){
//            console.log(error);
//          }
//     });
//   }
//   $("#funciona").submit(function(event){
//        event.preventDefault();
//        ajax_login();
//   });
// });
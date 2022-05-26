// alert(atob("hola"))
var user = document.getElementById("username");
var password = document.getElementById("password");

var hash1 = atob(user.value);
var hash2 = atob(password.value);

alert(hash2);

$("#funciona").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: actionUrl,
        //data: form.serialize(), // serializes the form's elements.
        data : {
          username : hash1,
          password: hash1
        },
        success: function(data)
        {
          str = JSON.stringify(obj)
          alert("xxxxxcmzxclz"); // show response from the php script.
        }
    });
    
});

// var formData = new FormData(document.getElementsById('username'));// yourForm: form selector        
// $.ajax({
//     type: "POST",
//     url: "yourURL",// where you wanna post
//     data: formData,
//     processData: false,
//     contentType: false,
//     error: function(jqXHR, textStatus, errorMessage) {
//         console.log(errorMessage); // Optional
//     },
//     success: function(data) {console.log(data)} 
// });

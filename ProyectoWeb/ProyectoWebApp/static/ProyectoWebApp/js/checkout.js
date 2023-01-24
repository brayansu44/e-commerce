$(document).ready(function (){

    $('.payWithRazor').click(function (e) {

        var fname = $("[name='nombre']").val();
        var lname = $("[name='apellido']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='telefono']").val();
        var address = $("[name='direccion']").val();
        var city = $("[name='ciudad']").val();
        var state = $("[name='estado']").val();
        var country = $("[name='pais']").val();
        var pinCode = $("[name='codigo_pin']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if(fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || country == "" || pinCode == ""){
            swal("Alerta!", "Todos los campos son obligatorios", "error");
            return false;
        }else{
            $.ajax({
                method: "GET",
                url: "../pedidosproceder-a-pagar",
                success: function (response) {
                    //console.log(response)
                    var options = {
                        "key": "rzp_test_z7nyUPJfR7WgGs", // Enter the Key ID generated from the Dashboard
                        "amount": 1*100,//response.precio_total * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Brayan Suarez",
                        "description": "Gracias por comprar",
                        "image": "https://example.com/your_logo",
                        //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                "nombre":fname,
                                "apellido":lname,
                                "email":email,
                                "telefono":phone,
                                "direccion":address,
                                "ciudad":city,
                                "estado":state,
                                "pais":country,
                                "codigo_pin":pinCode,
                                "modo_pago":"Pagado por Razorpay",
                                "id_pago":responseb.razorpay_payment_id,
                                csrfmiddlewaretoken : token
                            }
                            $.ajax({
                                method: "POST",
                                url: "../pedidosrealizar_pedido",
                                data: data,
                                success: function (responsec) {
                                    swal("Felicitaciones", responsec.estado, "success").then((vale) =>{
                                        window.location.href='../pedidosmis-pedidos'
                                    });
                                    /*swal("Felicitaciones", responsec.estado, "success")
                                    console.log(responsec.estado)*/
                                }
                            });
                            //alert(response.razorpay_order_id);
                            //alert(response.razorpay_signature)
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone
                        },
                        /*"notes": {
                            "address": "Razorpay Corporate Office"
                        },*/
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                } 
            });
        }
    });

});
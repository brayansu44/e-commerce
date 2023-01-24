
$(document).ready(function () {
    
    $('.increment-btn').click(function (e) {
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var limite_producto = $(this).closest('.product_data').find('.prod_cantidad').val();
        var value = parseInt(inc_value,limite_producto);
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) {

        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if(value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addToCartBtn').click(function (e) {
        var product_id= $(this).closest('.product_data').find('.prod_id').val();
        var producto_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "carro",
            data: {
                'product_id' : product_id,
                'product_qty' : producto_qty,
                csrfmiddlewaretoken : token
            },
            success: function (response) {
                console.log(response)
                var contador = document.getElementById("contadorCarrito").innerHTML = response.contador;
                console.log(contador)
                alertify.success(response.estado)
            }
        });

    });

    $('.changeQuantity').click(function (e) {
        var product_id= $(this).closest('.product_data').find('.prod_id').val();
        var producto_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "actualizar-carro",
            data: {
                'product_id' : product_id,
                'product_qty' : producto_qty,
                csrfmiddlewaretoken : token
            },
            success: function (response) {
                console.log(response)
                //alertify.success(response.estado)
            }
        });

    });

    

    $(document).on('click','.delete-cart-item', function (e) {

        var product_id= $(this).closest('.product_data').find('.prod_id').val();
        var product_nombre= $(this).closest('.product_data').find('.prod_nombre').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log(product_nombre);
        
        $.ajax({
            method: "POST",
            url: "eliminar-carro-articulo",
            data: {
                'product_id' : product_id,
                csrfmiddlewaretoken : token
            },
            success: function (response) {
                console.log(response)
                alertify.success(response.estado)
                $('.cartdata').load(location.href + " .cartdata")
            }
        });

    });
});

 

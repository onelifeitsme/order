        $("#id_type").change(function () {
        const url = $("#OrderForm").attr("data-products-url");  // get the url of the `load_cities` view
        const typeId = $(this).val();  // get the selected country ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'type_id': typeId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_product").html(data);  // replace the contents of the city input with the data that came from the server
                /*
                let html_data = '<option value="">---------</option>';
                data.forEach(function (city) {
                    html_data += `<option value="${city.id}">${city.name}</option>`
                });
                console.log(html_data);
                $("#id_city").html(html_data);
                */
            }
        });

    });
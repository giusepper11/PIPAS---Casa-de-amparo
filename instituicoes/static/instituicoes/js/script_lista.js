var $filtersCheckboxes = $('.filter');
var instlist = $('#inst_table_content');

$filtersCheckboxes.on('change', function () {

    instlist.hide();

    var selectedFilters = {};

    $filtersCheckboxes.filter(':checked').each(function () {

        if (!selectedFilters.hasOwnProperty(this.name)) {
            selectedFilters[this.name] = [];
        }


        selectedFilters[this.name].push(this.value);

    });
    // console.log(selectedFilters);
    $.ajax({
        type: "POST",
        url: "/instituicoes/inst_filter/",
        method: "POST",
        data: JSON.stringify(selectedFilters),
        contentType: "application/json; charset=utf-8",
        success: function (r) {
            instlist.empty();
            JSON.parse(r).forEach(function (x,y,z) {
                instlist.append(
                    '<tr class="tr" id="tr_inst">' +
                    '<td class="text-left">' + x.instituicao + '</td>' +
                    '<td class="text-left">' + x.endereco + '</td>' +
                    '<td class="text-left">' + x.bairro + '</td>' + '</tr>'
                )
            })
        },
        error: function () {
            alert("Error")

        }
    });
    instlist.show('slow')
});

                    //
                    // '<tr class="tr" id="tr_inst">' +
                    // '<td class="text-left">' + value.instituicao + '</td>' +
                    // '<td class="text-left">' + value.endereco + '</td>' +
                    // '<td class="text-left">' + value.bairro + '</td>' + '</tr>'

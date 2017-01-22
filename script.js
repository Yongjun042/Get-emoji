function createTable(tableData)
 {
    var table = document.createElement('table');
    var tableBody = document.createElement('tbody');
    //div create
    var objTo = document.getElementsByClassName('searcharea')
    var divtest = document.createElement("div");

    tableData.forEach(function (rowData) {
        var row = document.createElement('tr');

        rowData.forEach(function (cellData) {
            var cell = document.createElement('td');
            cell.appendChild(document.createTextNode(cellData));
            row.appendChild(cell);
        });

        tableBody.appendChild(row);
    });

    table.appendChild(tableBody);
    divtest.appendChild(table);
    objTo[0].appendChild(divtest);
    document.body.appendChild(ojbTo[0]);
}

createTable([["row 1, cell 1", "row 1, cell 2"], ["row 2, cell 1", "row 2, cell 2"]]);

//클릭시 이벤트 받기
Document.getElementByKey("sth").onclick = function() {};
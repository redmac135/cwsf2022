function make_matrix(rows, cols){
    let wrapper = document.getElementById("matrix-wrapper");

    let table = document.createElement("table");
    table.className = "matrix";

    for (let i = 0; i < rows; i++){
        let row = document.createElement("tr");
        row.id = "row-" + i;
        for (let j = 0; j < cols; j++){
            let cell = document.createElement("td");
            cell.id = "cell-" + i + "-" + j;

            let color = document.createElement("div");
            color.style.backgroundColor = "rgb(" + Math.floor(Math.random() * 256) + "," + Math.floor(Math.random() * 256) + "," + Math.floor(Math.random() * 256) + ")";
            color.style.height = "10px";
            color.style.width = "10px";
            color.title = "Cell " + i + "-" + j;

            cell.appendChild(color);

            row.appendChild(cell);
        }
        table.appendChild(row);
    }

    wrapper.appendChild(table);
}

make_matrix(45, 57);
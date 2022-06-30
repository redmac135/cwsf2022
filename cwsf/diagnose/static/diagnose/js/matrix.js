function make_matrix(rows, cols, matrix_data){
    matrix_data = matrix_data.replaceAll("&quot;", "\"");
    matrix_data = JSON.parse(matrix_data);

    gene_names = matrix_data.gene_names;
    matrix_colors = matrix_data.matrix_colors;
    console.log(matrix_colors);

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
            color.style.backgroundColor = "rgb(" + matrix_colors[i * 45 + j] + "," +(255-matrix_colors[i * 45 + j])+ ", 0)";
            color.title = gene_names[i * 45 + j];

            cell.appendChild(color);

            row.appendChild(cell);
        }
        table.appendChild(row);
    }

    wrapper.appendChild(table);
}
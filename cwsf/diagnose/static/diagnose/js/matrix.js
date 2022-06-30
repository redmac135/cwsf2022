function get_RBG_matrix(x) {
    let g = x >= 128 ? 255 - 2 * (x-128) : 255;
    let r = x >= 128 ? 255 : 2 * x;
    let color = "rgb(" + r + "," + g + ", 0)";
    return color
}

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
            color.style.backgroundColor = get_RBG_matrix(matrix_colors[i * 45 + j]);
            color.title = gene_names[i * 45 + j];

            cell.appendChild(color);

            row.appendChild(cell);
        }
        table.appendChild(row);
    }

    wrapper.appendChild(table);
}
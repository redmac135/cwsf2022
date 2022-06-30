function make_matrix(rows, cols, gene_names){
    gene_names = gene_names.replaceAll("&quot;", "\"");
    gene_names = JSON.parse(gene_names).gene_names;

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
            color.title = gene_names[i * 45 + j];

            cell.appendChild(color);

            row.appendChild(cell);
        }
        table.appendChild(row);
    }

    wrapper.appendChild(table);
}
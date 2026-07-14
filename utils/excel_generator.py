import os
import pandas as pd
from flask import send_file


def generate_excel(data, columns, filename):

    os.makedirs("exports", exist_ok=True)

    file_path = os.path.join("exports", filename)

    df = pd.DataFrame(data, columns=columns)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:

        df.to_excel(
            writer,
            sheet_name="Report",
            index=False
        )

        worksheet = writer.sheets["Report"]

        # Auto-fit column widths
        for column_cells in worksheet.columns:
            length = max(len(str(cell.value)) if cell.value else 0 for cell in column_cells)
            worksheet.column_dimensions[column_cells[0].column_letter].width = length + 5

    return send_file(
        file_path,
        as_attachment=True,
        download_name=filename
    )
from pathlib import Path
from typing import List, Union

from pypdf import PdfReader, PdfWriter, Transformation


def stamp(
    content_pdf: Union[Path, str],
    pdf_result: Union[Path, str],
    page_indices: Union[None, List[int]] = None,
):
    stamp_page = PdfReader('opticgardInvoiceHeader.pdf').pages[0]

    writer = PdfWriter()
    # page_indices can be a List(array) of page, tuples are for range definition
    reader = PdfReader(content_pdf)
    writer.append(reader, pages=page_indices)

    for content_page in writer.pages:
        # translation values
        #sales order values x = 170, y = 700, scale = .6

        translate_x = (150)
        translate_y = (690)

        # Apply the transformation
        content_page.merge_transformed_page(
            stamp_page,
            Transformation().scale(0.7).translate(tx=translate_x, ty=translate_y)
        )

    writer.write(pdf_result)

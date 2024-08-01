from pathlib import Path
from typing import List, Union

from pypdf import PdfReader, PdfWriter, Transformation


def stamp(
    content_pdf: Union[Path, str],
    pdf_result: Union[Path, str],
    sales: bool,
    page_indices: Union[None, List[int]] = None,
):
    stamp_page = PdfReader('./invoiceOrderPDFStamp/opticgardInvoiceHeader.pdf').pages[0]
    whiteSpace = PdfReader('./invoiceOrderPDFStamp/whiteSpace.pdf').pages[0]

    writer = PdfWriter()
    # page_indices can be a List(array) of page, tuples are for range definition
    reader = PdfReader(content_pdf)
    writer.append(reader, pages=page_indices)

    #defines the transformation and scale variables then assigns the correct one based on the option the user selected
    x, y, scale = (170, 700, 0.6) if sales else (150, 690, 0.7)


    for content_page in writer.pages:
        translate_x = x
        translate_y = y

        # Apply the transformation
        content_page.merge_transformed_page(
            stamp_page,
            Transformation().scale(scale).translate(tx=translate_x, ty=translate_y)
        )

        if not sales:
            content_page.merge_transformed_page(
                whiteSpace,
                Transformation().scale(1.5).translate(tx=25, ty=-115)

            )


    writer.write(pdf_result)
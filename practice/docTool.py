from docx2pdf import convert

# 将docs文件转成pdf
def docs_to_pdf():
    convert("D://test.docx", "D://test.pdf")


if __name__ == "__main__":
    docs_to_pdf()

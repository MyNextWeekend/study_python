from markitdown import MarkItDown

# 初始化转换器
markitdown = MarkItDown()

# 转换不同类型的文件
# PDF文档
pdf_result = markitdown.convert("annual_report.pdf")
print(pdf_result.text_content)

# Word文档
docx_result = markitdown.convert("meeting_notes.docx")
print(docx_result.text_content)

# Excel表格
xlsx_result = markitdown.convert("sales_data.xlsx")
print(xlsx_result.text_content)

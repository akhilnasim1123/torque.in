# from io import BytesIO
# from unittest import result
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def html2pdf(template_source,context_dict={}):
#     template=get_template(template_source)
#     html=template.render(context_dict)
#     result=BytesIO()
#     pdf=pisa.pisaDocument(BytesIO(html.encode('utf8')),result)
#     if not pdf.error:
#         return HttpResponse(result.getvalue(),content_type="application/pdf")
#     return None 
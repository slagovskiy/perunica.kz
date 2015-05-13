from .models import Global


class GlobalsMiddleware:

    def process_request(self, request):
        g = Global.objects.filter(active=True)
        if len(g) > 0:
            g = g[0]
        else:
            g = Global.objects.create()
        request.session['meta_title'] = g.meta_title
        request.session['meta_description'] = g.meta_description
        request.session['meta_keywords'] = g.meta_keywords
        request.session['first_page_text'] = g.first_page_text


    def process_response(self, request, response):
        return response

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import locale
from urllib.parse import urlparse, parse_qs

class Accesare:
    _id_cnt = 1
    
    def __init__(self, ip_client, url, data_acces):
        self.id = Accesare._id_cnt
        Accesare._id_cnt += 1
        self.ip_client = ip_client
        self.url_acc = url
        self.data = data_acces
    
    def lista_parametri(self):
        if self.url_acc:
            parsed = urlparse(self.url_acc)
            qs = parse_qs(parsed)
            return [(k, v[0] if v else None) for k, v in qs.items()]
        return []
    
    def url(self):
        return self.url_acc
    
    def data(self, format_str="%A, %d %B %Y %H:%M:%S"):
        return self.data_access.strftime(format_str)
    
    def pagina(self):
        if self.url_acc:
            parsed = urlparse(self.url_acc)
            return parsed.path
        return None

def afis_data(param=""):
    locale.setlocale(locale.LC_TIME, 'ro_RO.UTF-8')
    now = datetime.now()
    html = "<h2>Data si Ora</h2>"
    if param == "zi":
        html += f"<p>{now.strftime('%A, %d %B %Y')}</p>"
    elif param == "timp":
        html += f"<p>{now.strftime('%H:%M:%S')}</p>"
    else:
        html += f"<p>{now.strftime('%A, %d %B %Y, %H:%M:%S')}</p>"
    return html

def afis_template(request):
    param = {
        'nume' : "albert"
    }
    return render(request, "app_exemplu/exemplu.html", param)

def afis_ex(request):
    param = {
        'titlu_tab' : "exemplu tab",
        'titlu_articol' : "articol titlu",
        'continut_articol' : "continut"
    }
    return render(request, "app_exemplu/exemplu1.html", param)
        
def index(request):
	return HttpResponse("""
                    <html>
                    <p><b>
                    Site-ul comercial va oferi produse pentru intretinerea 
                    si ingrijirea animalelor de companie precum hrana, accesorii, jucarii si diverse produse de ingrijire pentru animale. Printre functionalitatile site-ului se numara: gestionarea eficienta a stocurilor produselor, sesiuni de logare pentru clienti si simularea activitatilor comerciale pe platforma site-ului
                    </b></p>
                    </html>
                    """)
                    
def pag1(request):
    return HttpResponse(2+3)

l=[]
def pag2(request):
    global l
    a=request.GET.get("a",10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit</b>: {l}")

def info(request):
    data = request.GET.get("data", "")
    p_data = afis_data(data)
    context  = {"title" : "Informatii despre server",
                "paragraf" : p_data 
                }
    return render(request, "app_exemplu/info.html", context)
    

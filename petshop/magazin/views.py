from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.template.loader import render_to_string
import locale
from urllib.parse import urlparse, parse_qs, urlsplit
from collections import Counter
from .forms import ContactForm, ProdusFilterForm
from django.core.paginator import Paginator
from .models import Produs, Categorie, Brand

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

accesari = []
    
def get_ip(request):
    req_headers = request.META
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR')

def logare_acces(request):
    ip = get_ip(request)
    url = request.get_full_path()
    acc = Accesare(ip, url, datetime.now())
    accesari.append(acc)

def get_base_context():
    return {
        'toate_categoriile': Categorie.objects.all().order_by('denumire')
    }

def afis_data(param):
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
    logare_acces(request)
    param = {
        'nume' : "albert"
    }
    return render(request, "magazin/exemplu.html", param)

def afis_ex(request):
    logare_acces(request)
    param = {
        'titlu_tab' : "exemplu tab",
        'titlu_articol' : "articol titlu",
        'continut_articol' : "continut"
    }
    return render(request, "magazin/exemplu1.html", param)
        
def index(request):
    logare_acces(request)
    context = get_base_context()
    text = """Site-ul comercial va oferi produse pentru intretinerea 
                    si ingrijirea animalelor de companie precum hrana, accesorii, jucarii si diverse 
                    produse de ingrijire pentru animale. Printre functionalitatile site-ului se numara: 
                    gestionarea eficienta a stocurilor produselor, sesiuni de logare pentru clienti si simularea activitatilor comerciale pe platforma site-ului"""
    ip_user = get_ip(request)
    context.update({"text" : text,
               "ip_user" : ip_user})
    return render(request, "magazin/pag_principala.html", context)
 
def info(request):
    context = get_base_context()
    logare_acces(request)
    data = request.GET.get("data", "")
    lista_param = request.GET.keys()
    n = len(lista_param)
    p_data = afis_data(data)
    context.update({"title" : "Informatii despre server",
                "paragraf" : p_data, 
                "l_p": lista_param,
                "n": n
                })
    return render(request, "magazin/info.html", context)

def log(request):
    logare_acces(request)
    context = get_base_context()
    ip_user = get_ip(request)
    total = len(accesari)
    n_accesari = request.GET.get("ultimele")
    id_accesari =[]
    
    nr_acc = request.GET.get("accesari")
    
    ids = request.GET.getlist("iduri")
    dupl = request.GET.get("dubluri", False)
    if (ids):
        try:
            ids = [int(x)-1 for elem in ids for x in elem.split(',')]
            if not dupl:
                ids = set(ids)
        except ValueError:
            return HttpResponse("<p><b>Eroare:</b> valoare invaida pentru parametrul iduri</p>")
        if total > max(ids):
            id_accesari = [accesari[i] for i in ids]
        else:
            return HttpResponse("<p><b>Eroare:</b> id idex out of range</p>")
        
    if nr_acc and nr_acc not in ["nr", "detalii"] :
        return HttpResponse("<p><b>Eroare:</b> valoare invaida pentru parametrul accesari</p>")
    
    mesaj = ""
    if (n_accesari is None):
        n = total
    else: 
        try:
            n = int(n_accesari)
        except ValueError:
            return HttpResponse("<p><b>Eroare:</b> parametrul 'ultimele' trebuie să fie un număr întreg!</p>")
    if n > total:
        return HttpResponse(f"<p>Exista doar {total} accesari fata de {n} accesari cerute</p>")
    ult_n = accesari[-n:]
    
    tab_val = []    
    tab_col = []
    tabel = request.GET.get("tabel")
    if tabel:
        col_valide = ["id", "ip_client", "url_acc", "data"]
        if tabel == "tot":
            col = col_valide 
        else:
            col = [x.strip() for x in tabel.split(',') if x.strip()]
        tab_col = [x.capitalize() for x in col]
        for acces in accesari:
            l = []
            for c in col:
                l.append(getattr(acces, c, "N/A"))
            tab_val.append(l)
                
    lista_cai = [urlsplit(acc.url_acc).path for acc in accesari]
    frecv_cai = Counter(lista_cai).most_common()
    extreme = (frecv_cai[0], frecv_cai[-1])
        
    context.update({
        "ip_user" : ip_user,
        "tab_col": tab_col,
        "tab_val": tab_val,
        "ids": ids,
        "nr": total,
        "accesari": accesari,
        "id_accesari": id_accesari,
        "u_accesari": ult_n,
        "mesaj": mesaj,
        "extreme": extreme
    })
    return render(request, "magazin/log.html", context)

def despre(request):
    logare_acces(request)
    context = get_base_context()
    ip_user = get_ip(request)
    context.update({"ip_user" : ip_user})
    return render(request, "magazin/despre.html", context)

def in_lucru(request):
    logare_acces(request)
    context = get_base_context()
    ip_user = get_ip(request)
    context.update({"ip_user" : ip_user})
    return render(request, "magazin/in_lucru.html", context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  
            nume = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            mesaj = form.cleaned_data['mesaj']
            return redirect('mesaj_trimis')
    else:
        form = ContactForm()
    return render(request, 'aplicatie_exemplu/contact.html', {'form': form})

def pag_produse(request):
    """Afișează pagina inițială (cochilia) pentru TOATE produsele."""
    logare_acces(request) # Am păstrat funcția ta de logare
    context = get_base_context()
    
    # Inițializăm formularul GOL cu valoarea implicită pentru paginare
    form = ProdusFilterForm(initial={'items_per_page': 5}) 
    
    # Afișăm primele 5 produse (fără filtre)
    lista_produse = Produs.objects.all().order_by('nume')
    paginator = Paginator(lista_produse, 5) 
    pag_produse = paginator.get_page(1) # Folosim 'pagina_produse'

    context.update({
        'pag_produse': pag_produse,
        'form': form,
        'sort_by': None, # Fără sortare inițială
        'ip_user': get_ip(request) 
    })
    return render(request, 'magazin/produse.html', context)

def pag_categorie(request, slug_categorie):
    """Afișează pagina inițială (cochilia) pentru O CATEGORIE."""
    logare_acces(request) # Am păstrat funcția ta de logare
    context = get_base_context() 
    categorie_curenta = get_object_or_404(Categorie, slug__iexact=slug_categorie)
    
    # Inițializăm formularul cu categoria blocată (Req 8)
    form = ProdusFilterForm(
        initial={'categorie': categorie_curenta, 'items_per_page': 5},
        categorie_blocata=categorie_curenta
    ) 
    
    # Afișăm primele 5 produse din categorie
    lista_produse = Produs.objects.filter(categorie=categorie_curenta).order_by('nume')
    paginator = Paginator(lista_produse, 5) 
    pag_produse = paginator.get_page(1)
    
    context.update({
        'pag_produse': pag_produse,
        'categorie_curenta': categorie_curenta,
        'form': form,
        'sort_by': None,
    })
    return render(request, 'magazin/produse.html', context)


# --- B) FUNCȚIA NOUĂ PENTRU FETCH ---
# Acesta este "motorul" tău AJAX.

def ajax_filtru(request):
    categorie_curenta = None
    cat_slug = request.GET.get('cat_slug') # Nume scurt pentru slug
    if cat_slug:
        categorie_curenta = get_object_or_404(Categorie, slug__iexact=cat_slug)
    form = ProdusFilterForm(request.GET or None, categorie_blocata=categorie_curenta)
    if not form.is_valid():
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    cd = form.cleaned_data
    # Req 9: Verificare de securitate
    if categorie_curenta:
        if cd.get('categorie') and cd.get('categorie') != categorie_curenta:
            return JsonResponse({'status': 'error', 'message': 'Eroare: Categorie invalidă.'}, status=403)
    # Filtrarea
    if categorie_curenta:
        lista_produse = Produs.objects.filter(categorie=categorie_curenta)
    else:
        lista_produse = Produs.objects.all()

    # Metoda eficientă (DRY) de a construi filtrele
    filtre = {}
    if cd.get('nume'): filtre['nume__icontains'] = cd['nume']
    if cd.get('pret_min'): filtre['pret__gte'] = cd['pret_min']
    if cd.get('pret_max'): filtre['pret__lte'] = cd['pret_max']
    if cd.get('brand'): filtre['brand'] = cd['brand']
    if cd.get('in_stoc'): filtre['stoc__gt'] = 0
    if cd.get('data_adaugare_dupa'): filtre['data_adaugarii__gte'] = cd['data_adaugare_dupa']
    if cd.get('greutate_min'): filtre['greutate__gte'] = cd['greutate_min']
    if cd.get('greutate_max'): filtre['greutate__lte'] = cd['greutate_max']
    
    if not categorie_curenta and cd.get('categorie'):
         filtre['categorie'] = cd['categorie']

    lista_produse = lista_produse.filter(**filtre)

    # Sortarea (Req 3)
    sort_by = request.GET.get('sort')
    if sort_by == 'a':
        lista_produse = lista_produse.order_by('pret')
    elif sort_by == 'd':
        lista_produse = lista_produse.order_by('-pret')
    else:
        lista_produse = lista_produse.order_by('nume')

    # Paginarea (Req 7)
    items_per_page = cd.get('items_per_page') or 5
    repaginare_mesaj = None
    items_per_page_old = request.GET.get('items_per_page_old')
    if items_per_page_old and str(items_per_page) != items_per_page_old:
         repaginare_mesaj = "Ați schimbat numărul de elemente pe pagină."

    paginator = Paginator(lista_produse, items_per_page)
    page_number = request.GET.get('page', 1)
    pag_produse = paginator.get_page(page_number) # Folosim 'pagina_produse'
    
    context = {
        'pag_produse': pag_produse, # Trimitem cu același nume
        'sort_by': sort_by,
        'categorie_curenta': categorie_curenta,
    }
    
    # Randăm HTML-ul ca string-uri
    html_produse = render_to_string('magazin/snippets/_lista_produse.html', context, request=request)
    html_paginare = render_to_string('magazin/snippets/_paginare.html', context, request=request)

    return JsonResponse({
        'status': 'success',
        'html_produse': html_produse,
        'html_paginare': html_paginare,
        'repaginare_mesaj': repaginare_mesaj,
    })

# def pag_produse(request):
#     lista_produse = Produs.objects.all()
#     context = get_base_context()
#     sort_by = request.GET.get('sort')
#     if sort_by == 'a':
#         lista_produse = lista_produse.order_by('pret')
#     elif sort_by == 'd':
#         lista_produse = lista_produse.order_by('-pret')
#     else:
#         lista_produse = lista_produse.order_by('nume')
#     paginator = Paginator(lista_produse, 5) 
#     page_number = request.GET.get('page')
#     pagina_produse = paginator.get_page(page_number)
#     ip_user = get_ip(request)
#     context.update({
#         'sort_by': sort_by,
#         'pag_produse': pagina_produse,
#         'ip_user': ip_user
#     })
#     return render(request, 'magazin/produse.html', context)

def pag_prod(request, pk): # <-- Numele funcției este acum 'pag_prod'
    context = get_base_context()
    produs = get_object_or_404(Produs, pk=pk)
    context.update({
        'produs': produs
    })
    
    return render(request, 'magazin/produs_detaliu.html', context)

# def pag_categorie(request, slug_categorie):
#     context = get_base_context() 
    
#     categorie_curenta = get_object_or_404(
#         Categorie, 
#         slug__iexact=slug_categorie
#     )
#     lista_produse = Produs.objects.filter(categorie=categorie_curenta).order_by('nume')
#     paginator = Paginator(lista_produse, 5) 
#     page_number = request.GET.get('page')
#     pagina_produse = paginator.get_page(page_number)
    
#     context.update({
#         'pag_produse': pagina_produse,
#         'categorie_curenta': categorie_curenta,
#     })
    
#     return render(request, 'magazin/produse.html', context)

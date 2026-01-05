from django.shortcuts import render, get_object_or_404
from .models import RecursoEducativo, Post
from django.db.models import Q

# =============================================================================
# VISTAS DE BLOG IA (Recursos Educativos)
# =============================================================================

def blog_index_ia(request):
    """
    Vista optimizada: RecursoEducativo.
    """
    all_resources = RecursoEducativo.objects.all().order_by('-created_at')

    # Filtrado en memoria
    capsulas_list = [r for r in all_resources if r.type == 'CAPSULA']
    noticias_list = [r for r in all_resources if r.type == 'NOTICIA']
    infografias_list = [r for r in all_resources if r.type == 'INFOGRAFIA']

    context = {
        'capsulas': capsulas_list,
        'noticias': noticias_list,
        'infografias': infografias_list,
    }
    # Nota: Ajustaremos los paths de los templates en el siguiente paso
    return render(request, 'blog/ia/blog_index-aldo.html', context)

def resource_detail(request, pk):
    recurso = get_object_or_404(RecursoEducativo, pk=pk)
    context = {
        'recurso': recurso
    }
    return render(request, 'blog/ia/resource_detail-aldo.html', context)


# =============================================================================
# VISTAS DE BLOG GENERAL (Posts)
# =============================================================================

def blog_general_index(request):
    # Base query
    queryset = Post.objects.filter(is_active=True)

    # Search
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

    # Filter by Category
    category = request.GET.get('category')
    if category and category != 'ALL':
        queryset = queryset.filter(category=category)

    # Get Featured Post
    featured = queryset.filter(is_featured=True).first()
    if not featured:
        featured = queryset.first()

    # Get List (Exclude featured)
    if featured:
        posts = queryset.exclude(id=featured.id).order_by('-created_at')
    else:
        posts = queryset.order_by('-created_at')

    # Categories
    categories = [
        {'code': 'ALL', 'label': 'Todos'},
        {'code': 'FISCALIDAD', 'label': 'Fiscalidad'},
        {'code': 'ADMINISTRACION', 'label': 'Administración'},
        {'code': 'IA', 'label': 'Inteligencia Artificial'},
        {'code': 'NOTICIAS', 'label': 'Noticias'},
        {'code': 'CASOS', 'label': 'Casos de Éxito'},
    ]

    context = {
        'featured': featured,
        'posts': posts,
        'categories': categories,
        'active_category': category or 'ALL',
        'search_query': query,
    }
    return render(request, 'blog/general/blog_general_index.html', context)


def blog_general_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_active=True)
    return render(request, 'blog/general/blog_general_detail.html', {'post': post})

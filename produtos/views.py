from django.shortcuts import redirect, render
from .models import Produto
from usuario.models import Usuario
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_user')
def index(request):

    produtos = Produto.objects.all()

    usuario_perfil = Usuario.objects.get(user=request.user)

    paginator = Paginator(produtos, 3)
    page = request.GET.get('page', 1)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        "produtos": result,
        "user": usuario_perfil,
    }


    return render(request, 'dashboard.html', context)

@login_required(login_url='login_user')
def registrar_produto(request):

    usuario = Usuario.objects.all()
    
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco_produto = request.POST.get('preco_produto')
        imagem_produto = request.FILES.get('imagem_produto')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')

        produto = Produto(
            nome=nome_produto,
            email=email,
            preco=preco_produto,
            foto_produto=imagem_produto,
            descricao=descricao,
            categoria=categoria,
            usuario=Usuario.objects.get(user__username=request.user)
        )

        produto.save()

    return render(request, 'registrar-produtos.html')

@login_required(login_url='login_user')
def editar_produto(request, id):

    produto = Produto.objects.get(id=id)
    print(produto.get_categoria_display)

    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco_produto = request.POST.get('preco_produto')
        imagem_produto = request.FILES.get('imagem_produto')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')

        produto.nome = nome_produto
        produto.email = email
        produto.preco = preco_produto
        produto.foto_produto = imagem_produto
        produto.descricao = descricao
        produto.categoria = categoria
        produto.save()


    context = {
        'produto': produto
    }
    
    return render(request, 'editar-produto.html', context)

@login_required(login_url='login_user')
def detalhar(request):

    produtos = Produto.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        "produtos": result,
    }

    return render(request, 'meus-produtos.html', context)

@login_required(login_url='login_user')
def deletar(request, id):

    produto = Produto.objects.get(id=id)
    produto.delete()

    return redirect('detalhar_produto')

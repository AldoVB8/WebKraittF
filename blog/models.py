from django.db import models
from django.urls import reverse

# ---------------------------------------------------------
# MODELO 1: RECURSO EDUCATIVO (De blog_ia)
# ---------------------------------------------------------
class RecursoEducativo(models.Model):
    TIPO_CHOICES = [
        ('CAPSULA', 'Cápsula IA (Video)'),
        ('NOTICIA', 'Noticia IA'),
        ('INFOGRAFIA', 'Infografía IA'),
    ]

    type = models.CharField(max_length=20, choices=TIPO_CHOICES, default='NOTICIA', verbose_name="Tipo de Recurso")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción Corta")
    content = models.TextField(blank=True, null=True, verbose_name="Contenido (Solo Noticias)")
    video_url = models.URLField(blank=True, null=True, verbose_name="URL Video (Solo Cápsulas)")
    image = models.ImageField(upload_to='resources/', blank=True, null=True, verbose_name="Imagen Principal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def get_embed_url(self):
        """Helper para convertir URLs de YouTube a formato embed."""
        if not self.video_url: return ""
        url = self.video_url
        video_id = ""
        if "youtu.be" in url:
            video_id = url.split("/")[-1]
        elif "youtube.com" in url and "v=" in url:
            video_id = url.split("v=")[1].split("&")[0]
        elif "youtube.com/embed/" in url:
            return url
        
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return url

    def __str__(self):
        return f"[{self.get_type_display()}] {self.title}"

    class Meta:
        verbose_name = "Recurso Educativo"
        verbose_name_plural = "Recursos Educativos"


# ---------------------------------------------------------
# MODELO 2: POST (De blog_general)
# ---------------------------------------------------------
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('FISCALIDAD', 'Fiscalidad'),
        ('ADMINISTRACION', 'Administración'),
        ('IA', 'Inteligencia Artificial'),
        ('NOTICIAS', 'Noticias'),
        ('CASOS', 'Casos de Éxito'),
        ('OTROS', 'Otros'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="Slug")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='NOTICIAS', verbose_name="Categoría")
    image = models.ImageField(upload_to='blog_general/', verbose_name="Imagen Principal", blank=True, null=True)
    excerpt = models.TextField(verbose_name="Extracto", blank=True, help_text="Breve descripción para la tarjeta")
    content = models.TextField(verbose_name="Contenido")
    reading_time = models.PositiveIntegerField(default=5, verbose_name="Tiempo de lectura (min)")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_general_detail', kwargs={'slug': self.slug})

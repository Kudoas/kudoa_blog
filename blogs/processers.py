from .models import Category


def common(self):
    context = {
        'category_list': Category.objects.all()
    }
    return context

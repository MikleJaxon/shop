from .models import Category


def categories(request):
    """
    Function to retrieve categories from the database based on the provided request.

    Parameters:
    - request: the request object containing information needed to retrieve the categories

    Returns:
    - A dictionary containing the retrieved categories
    """
    categories = Category.objects.filter(parent = None)
    return {'categories': categories}
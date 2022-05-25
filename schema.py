import graphene

from serializers import (
    ProductModel,
    ProductGrapheneModel,
    ProductGrapheneInputModel
)

from models.product import Product


class Query(graphene.ObjectType):
    say_name = graphene.String(name=graphene.String(default_value='Test Driven'))
    list_product = graphene.List(ProductGrapheneModel)
    get_single_product = graphene.Field(ProductGrapheneModel, product_id=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_name(parent, info, name):
        return f'Hello {name}'

    @staticmethod
    def resolve_list_product(parent, info):
        return Product.all()

    @staticmethod
    def resolve_get_single_product(parent, info, product_id):
        return Product.find_or_fail(product_id)


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_details = ProductGrapheneInputModel()

    Output = ProductGrapheneModel

    @staticmethod
    def mutate(parent, info, product_details):
        product = Product()
        product.id = product_details.id
        product.name = product_details.name
        product.price = product_details.price
        product.category = product_details.category

        product.save()

        return product

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
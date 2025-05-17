from flask import Flask
from flask_cors import CORS
from graphql_server.flask import GraphQLView
import graphene

ELECTRONICS = [
    {'id': '1', 'nombre': 'Laptop', 'precio': 1500, 'stock': 5, 'disponible': True},
    {'id': '2', 'nombre': 'Auriculares', 'precio': 200, 'stock': 3, 'disponible': True},
    {'id': '3', 'nombre': 'Mouse', 'precio': 50, 'stock': 10, 'disponible': True},
]

class ElectronicType(graphene.ObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

class UpdateStock(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        amount = graphene.Int(required=True)

    electronic = graphene.Field(ElectronicType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id, amount):
        electronic = next((e for e in ELECTRONICS if e['id'] == id), None)
        if not electronic:
            return UpdateStock(success=False, message="Producto no encontrado")

        electronic['stock'] += amount

        if electronic['stock'] < 0:
            electronic['stock'] = 0

        electronic['disponible'] = electronic['stock'] > 0

        return UpdateStock(
            electronic=electronic,
            success=True,
            message="Stock actualizado correctamente"
        )

#class AddElectronic(graphene.Mutation):
    #class Arguments:
     #   nombre = graphene.String(required=True)
      #  precio = graphene.Float(required=True)
       # stock = graphene.Int(required=True)

#    electronic = graphene.Field(ElectronicType)

 #   def mutate(self, info, nombre, precio, stock):
        new_id = str(len(ELECTRONICS) + 1)
        disponible = stock > 0
        new_electronic = {
            'id': new_id,
            'nombre': nombre,
            'precio': precio,
            'stock': stock,
            'disponible': disponible
        }
        ELECTRONICS.append(new_electronic)
        return AddElectronic(electronic=new_electronic)

class Mutation(graphene.ObjectType):
    update_stock = UpdateStock.Field()
    #add_electronic = AddElectronic.Field() 

class Query(graphene.ObjectType):
    electronics = graphene.List(ElectronicType)

    def resolve_electronics(parent, info):
        return ELECTRONICS

schema = graphene.Schema(query=Query, mutation=Mutation)


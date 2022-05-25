from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('products') as table:
            table.increments('id')
            table.string('name')
            table.integer('price')
            table.integer('category')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('products')

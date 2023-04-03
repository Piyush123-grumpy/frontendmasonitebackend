"""CreateBlog Migration."""

from masoniteorm.migrations import Migration


class CreateBlog(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")
            table.string('author').nullable()
            table.string('title').nullable()
            table.string('text').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")

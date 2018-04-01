from django.db import models
import uuid

class Inventory(models.Model):
    """
    Model representing a the inventory.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    inventory_name = models.CharField("INVENTORY NAME" ,max_length=200, help_text="This contains the Inventory name:")
    short_name = models.CharField(max_length=20, help_text="This contains an abbreviation:")
    inventory_code = models.IntegerField("INVENTORY CODE" ,default = '0', help_text="This contains the Inventory code:")
    price = models.IntegerField(default = '0')
    stocks_left = models.IntegerField("STOCKS LEFT",default = '0')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '{0} ({1}) ({2})'.format(self.inventory_name,self.inventory_code,self.stocks_left)

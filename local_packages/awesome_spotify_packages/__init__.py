import importlib
import pkgutil

# Dynamically import all modules and their classes in this package
for module_info in pkgutil.iter_modules(__path__):
    module_name = module_info.name
    module = importlib.import_module(f".{module_name}", package=__name__)
    
    # Import all classes from the module
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isinstance(attribute, type):  # Check if the attribute is a class
            globals()[attribute_name] = attribute
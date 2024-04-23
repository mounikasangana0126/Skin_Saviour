import os

def facewash_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/facewash"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def serum_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/serum"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def moisturizer_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/moisturizer"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def sunscreen_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "suggestions/sunscreen"
    ext = filename.split(".")[-1]
    if instance.skin_type.skin_type:
        filename = f"{instance.skin_type.skin_type}.{ext}"
    return os.path.join(upload_to, filename)

def facewash_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "NaturalProducts/facewash"
    ext = filename.split(".")[-1]
    if instance.treatment.treatment:
        filename = f"{instance.treatment.treatment}.{ext}"
    return os.path.join(upload_to, filename)

def serum_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "NaturalProducts/serum"
    ext = filename.split(".")[-1]
    if instance.treatment.treatment:
        filename = f"{instance.treatment.treatment}.{ext}"
    return os.path.join(upload_to, filename)

def moisturizer_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "NaturalProducts/moisturizer"
    ext = filename.split(".")[-1]
    if instance.treatment.treatment:
        filename = f"{instance.treatment.treatment}.{ext}"
    return os.path.join(upload_to, filename)

def scrub_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "NaturalProducts/scrub"
    ext = filename.split(".")[-1]
    if instance.treatment.treatment:
        filename = f"{instance.treatment.treatment}.{ext}"
    return os.path.join(upload_to, filename)

def facemask_image(instance, filename):
    """
    Generate a filename for a  image and returns the path for the uploaded image.

    Args:
        instance: The instance of the  image.
        filename: The original filename of the image.

    Returns:
        str: The path for the uploaded image.
    """
    upload_to = "NaturalProducts/facemask"
    ext = filename.split(".")[-1]
    if instance.treatment.treatment:
        filename = f"{instance.treatment.treatment}.{ext}"
    return os.path.join(upload_to, filename)


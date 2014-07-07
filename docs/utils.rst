Documenting the utilities available in this repo

Potential Cases:
----------------

1. Developer has a concept but doesn't know its source
2. Developer has a collection but doesn't know its owner type
3. Developer has a source but doesn't know its owner type

Open Questions:
---------------

1. Do the collection and source objects know their owner type?
 
    If so, this will probably be easier, and the utils below might not be necessary.

2. Do the concept objects know about their source?

``utils.ocl_reverse``

This is a (future) utility to reverse a collection or source when you don't know the type of owner.

.. code-block:: python

    from ocl_web.utils import ocl_reverse
    from ocl import Collection

    # Get data from API
    a_collection = Collection.get(name="bennyBHealth")

    # Get a URL from ocl_web.
    ocl_reverse(obj_type="collection", obj_name=a_collection.name)

If the Collection object doesn't have a ownerType, then we'll have to hit the
API to figure that out, I think.  Not ideal.

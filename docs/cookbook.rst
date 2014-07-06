Collection of stuff you can use from various parts of ocl_web.

Reversing URLs
--------------
A collections or source can be owned by either a user or a organization.  Reversing_ a URL for either is very similar.

.. _Reversing: djangoproject.com/reversing-urls/

TODO: Fill in the proper URL to Django docs.

Example: Reversing a URL for a collection owned by an org
`````````````````````````````````````````````````````````

In a template::

    {% url 'orgs:collection-detail', org=<org_name>, collection=<collection_name> %}

In a Django view::

    from django.core.urlresolvers import reverse

    reverse('orgs:collection-detail', org=<org_name>, collection=<collection_name>)

If the above calls had "WHO" as an `<org>`, and "dabombcollection" as the `<collection_name>`, the resulting path would look like this::

    /orgs/WHO/collections/dabombcollection/

Example: Reversing a URL for a collection owned by an user
``````````````````````````````````````````````````````````

In a template::

    {% url 'users:collection-detail', org=<org_name>, collection=<collection_name> %}

In a Django view::

    from django.core.urlresolvers import reverse

    reverse('users:collection-detail', org=<org_name>, collection=<collection_name>)

If the above calls had "phyllisd" as a `<user>`, and "deltaphiepsilon" as the `<collection_name>`, the resulting path would look like this::

    /users/phyllisd/collections/deltaphiepsilon/

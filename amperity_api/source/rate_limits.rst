.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        A rate limit is the number of requests that may be made to the Amperity API in a given time period.

.. meta::
    :content class=swiftype name=body data-type=text:
        A rate limit is the number of requests that may be made to the Amperity API in a given time period.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity API rate limits

==================================================
Rate limits
==================================================

.. rate-limits-start

A rate limit is the number of requests that may be made to the Amperity API in a given time period.

.. rate-limits-end


.. _rate-limits-amperity:

Amperity API
==================================================

.. rate-limits-amperity-start

The Amperity API supports requests to endpoints that do not exceed a rate of 10 requests per second. Response times will vary by endpoint and the complexity of data that is returned by the response. Some requests may take seconds to return.

Requests to the Amperity API that exceed 10 requests per second may return an error response with an HTTP 429 status code.

.. rate-limits-amperity-end


.. _rate-limits-profile:

Profile API
==================================================

.. rate-limits-profile-start

The Amperity Profile API enforces a rate limit of 2000 requests per second across the entire tenant, including sandboxes.

Rate limit increases are supported and requests for increased rate limits will be reviewed on a case-by-case basis. Reach out to Amperity Support or your Customer Success Manager for details.

.. rate-limits-profile-end
.. https://docs.amperity.com/realtime/


.. meta::
    :description lang=en:
        A rate limit is the number of requests that may be made to the Amperity Real-time API in a given time period.

.. meta::
    :content class=swiftype name=body data-type=text:
        A rate limit is the number of requests that may be made to the Amperity Real-time API in a given time period.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity Real-time API rate limits

==================================================
Rate limits
==================================================

.. rate-limits-start

A rate limit is the number of requests that may be made to the Amperity Real-time API in a given time period.

.. rate-limits-end


.. _rate-limits-events:

Events API
==================================================

.. rate-limits-events-start

The Amperity Events API enforces a rate limit of 2000 requests per second across the entire tenant, including sandboxes.

Requests to the Events API that exceed 2000 requests per second may return an error response with an HTTP 429 status code.

.. rate-limits-events-end


.. _rate-limits-profile:

Profile API
==================================================

.. rate-limits-profile-start

The Amperity Profile API enforces a rate limit of 2000 requests per second across the entire tenant, including sandboxes.

Requests to the Profile API that exceed 2000 requests per second may return an error response with an HTTP 429 status code.

Rate limit increases are supported and requests for increased rate limits will be reviewed on a case-by-case basis. Reach out to Amperity Support or your Customer Success Manager for details.

.. rate-limits-profile-end

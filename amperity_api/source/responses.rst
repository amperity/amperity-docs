.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Amperity API endpoints use conventional HTTP response status codes to indicate success or failure for any API request.

.. meta::
    :content class=swiftype name=body data-type=text:
        Amperity API endpoints use conventional HTTP response status codes to indicate success or failure for any API request.

.. meta::
    :content class=swiftype name=title data-type=string:
        Responses


==================================================
Amperity API response codes
==================================================

.. status_codes-start

Amperity API endpoints use conventional HTTP response status codes---3-digit numbers where the first digit of the code defines the class of response---to indicate success or failure for any API request. Response status codes fall into three categories:

#. 2xx - Success
#. 4xx - Error

   A 4xx error occurs when information in a request is invalid, such as requesting access to an endpoint that does not exist or by including the wrong value for a query parameter.

#. 5xx - Error

   A 5xx error is caused when the API or endpoint is unavailable.

.. status_codes-end


.. _status_codes-2xx:

2xx status codes
==================================================

.. status_codes-2xx-start

The 2xx class of status codes indicate that your request was successfully received, understood, and accepted by your Amperity tenant.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Status code
     - Description

   * - **200 OK**
     - A request completed successfully.

.. status_codes-2xx-end


.. _status_codes-4xx:

4xx status codes
==================================================

.. status_codes-4xx-start

The 4xx class of status codes indicate that your request experienced a fatal client error. 

When a request returns a fatal client error, the standard error response will include the following:

* **status** The status code for the error.
* **message** A human readable error message.
* **request_id** Optional. An Amperity request ID.
* **trace_id** Optional. An Amperity tracing ID.

For example:

.. code-block:: json

   {
     "status": 400,
     "message": "Error updating database: Can't find campaign named \
                 'CampaignName'",
     "request_id":"1ab23456-c78d-9012-3456-78efg9hi01j2",
     "trace_id":"1a2b3456789cd0ef1g234hijklm5nopq"
   }


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Status code
     - Description

   * - **400 Bad Request**
     - A request did not contain a required parameter or has an invalid parameter.

   * - **401 Authentication Required**
     - A request contains invalid authentication, an invalid version identifier, or an expired token.

   * - **403 Not Authorized**
     - A request contains valid authentication, but does have permission to perform the requested action.

   * - **404 Not Found**
     - A request was made to a resource that does not exist.

   * - **405 Method not Allowed**
     - A request used an unsupported HTTP method.

   * - **409 Conflict**
     - A request conflicts with the current state.

   * - **429 Too Many Requests**
     - A rate limit has been exceeded.

       .. note:: Amperity does not currenctly enforce a rate limit.

       .. tip:: Watch for 429 error codes and build a retry mechanism into the integrations or applications that interact with the Amperity API. Use an exponential backoff schedule with some randomness built in to reduce request volume.

.. status_codes-4xx-end


.. _status_codes-5xx:

5xx status codes
==================================================

.. status_codes-5xx-start

The 5xx class of status codes indicate a fatal server error. When your integration or application experiences a 5xx error, use an exponential backoff schedule with some randomness built in to reduce request volume.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Status code
     - Description

   * - **500 Server Error**
     - An internal error occurred. Simplify the request or retry with exponential backoff.

   * - **503 Service Unavailable**
     - The server is currently unavailable.

       .. tip:: Watch for 503 error codes and build a retry mechanism into the integrations or applications that interact with the Amperity API.

.. status_codes-5xx-end

.. https://docs.amperity.com/reference/


.. meta::
    :description lang=en:
        Recognize a returning customer at request time and read their real-time profile to personalize the experience.

.. meta::
    :content class=swiftype name=body data-type=text:
        Recognize a returning customer at request time and read their real-time profile to personalize the experience.

.. meta::
    :content class=swiftype name=title data-type=string:
        Personalize experiences for recognized customers

==================================================
Personalize experiences for recognized customers
==================================================

.. real-time-personalization-overview-start

Recognize a returning customer the moment they arrive, and tailor what they see to what Amperity already knows about them. This article shows how to personalize an on-site or in-app experience at request time by reading a customer's real-time profile through the Real-time API.

.. real-time-personalization-overview-end


.. _real-time-personalization-problem:

The problem
==================================================

.. real-time-personalization-problem-start

A known customer returns to your site or app. To personalize their experience--the products you feature, the offers you show, the message you lead with--you need to know who they are and what they care about at the moment the page renders, not hours later after a batch job.

This is a **read** problem: given an identifier for the visitor, retrieve what Amperity knows about that customer fast enough to shape the response.

.. real-time-personalization-problem-end


.. _real-time-personalization-solution:

Look up the profile at request time
==================================================

.. real-time-personalization-solution-start

At request time, personalize from the customer's :doc:`real-time profile <real_time_profiles>`:

#. **Identify the visitor.** Resolve an identifier for the visitor--an email address, a loyalty ID, a known device identifier.
#. **Read the profile.** Call the Real-time API to look up the profile for that identifier: ``GET /prof/profiles/{collection-id}/{profile-id}``. The response carries the customer's attributes--the aggregate and computed values the collection maintains.
#. **Read segment membership.** Where personalization depends on an audience, read the customer's :doc:`real-time segment <real_time_segments>` memberships from the segment-membership endpoint.
#. **Personalize the response.** Use the attributes and memberships to shape what the customer sees.

For request and response details, and for the full set of endpoints, see the `Real-time API endpoint reference <../api/endpoints_realtime.html>`__.

.. real-time-personalization-solution-end


.. _real-time-personalization-recognition:

Personalization depends on recognition
==================================================

.. real-time-personalization-recognition-start

This pattern works only for customers Amperity has **recognized**. A lookup succeeds when the visitor's identifier resolves to a profile; if it does not resolve, there is no profile to personalize from, and you fall back to a default experience.

Recognition is a lookup against a keychain built from Stitch output, not live re-stitching (see :doc:`real-time identity recognition <real_time_identity>`). A customer whose identity Stitch has only just resolved may not yet be recognized in real time, so a very recent first-time customer can still see the default experience until their identifier is reflected in the keychain.

.. real-time-personalization-recognition-end

.. TODO: verify with <eng> -- state the recognition latency plainly once NC1 lands (the keychain refresh cadence between a newly stitched identity and real-time recognition). Until then, describe the dependency qualitatively without a latency figure.


.. _real-time-personalization-related:

Related
==================================================

.. real-time-personalization-related-start

* :doc:`About real-time identity recognition <real_time_identity>` -- how a visitor's identifier resolves to a stitched customer.
* :doc:`About profile collections and real-time profiles <real_time_profiles>` -- what a profile contains and how to inspect it.
* :doc:`Recognize and re-engage abandoning customers <real_time_abandonment>` -- a journey-based real-time use case, in contrast to this request-time lookup.
* :doc:`About real-time <real_time>` -- an orientation to the real-time objects.

.. real-time-personalization-related-end

.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Configure Amazon Quick to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=body data-type=text:
        Configure Amazon Quick to connect to the Amperity MCP server.

.. meta::
    :content class=swiftype name=title data-type=string:
        Set up Amazon Quick


==================================================
Set up Amazon Quick
==================================================

.. mcp-setup-amazon-quick-start

Connect Amazon Quick to the Amperity MCP server by adding a team MCP integration. Amazon Quick discovers Amperity tools and registers them as actions that the assistant can use in conversations.

For more information about Amazon Quick MCP integrations, see the `Amazon Quick documentation <https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html>`__.

.. mcp-setup-amazon-quick-end


.. _mcp-setup-amazon-quick-requirements:

Requirements
==================================================

.. mcp-setup-amazon-quick-requirements-start

Connecting Amazon Quick to the MCP server requires:

* An active Amperity account with access to at least one tenant.
* An Amazon Quick Enterprise subscription.
* Permission to create a team connector in Amazon Quick.

.. mcp-setup-amazon-quick-requirements-end


.. _mcp-setup-amazon-quick-add:

Add the Amperity MCP server
==================================================

.. mcp-setup-amazon-quick-add-start

To add the Amperity MCP server to Amazon Quick:

#. In the Amazon Quick console, choose **Connectors**.
#. Choose **Create for your team**, and then choose **Model Context Protocol (MCP)**.
#. Enter a name and, optionally, a description for the integration.
#. For **MCP server endpoint**, enter:

   .. code-block:: none

      https://mcp.amperity.com

#. For **Connection type**, choose **Public network**, and then choose **Next**.
#. Choose **User authentication (OAuth)**.

   .. important:: Amazon Quick discovers Amperity's OAuth metadata and automatically registers itself as a public client secured with PKCE. You do not need to enter manual OAuth credentials or a client secret.

#. Choose **Create and continue**.
#. Review the actions that Amazon Quick discovered and turn on the actions you want to make available.

   Amperity provides Amazon Quick with a compatible curated tool set that stays below Amazon Quick's 100-tool limit.

#. Choose **Next**, and then share the integration with other users if needed.

.. mcp-setup-amazon-quick-add-end


.. _mcp-setup-amazon-quick-authorize:

Authorize the connection
==================================================

.. mcp-setup-amazon-quick-authorize-start

Each person who uses the integration must complete their own OAuth sign-in when Amazon Quick prompts them. Sign in with your Amperity credentials and select your tenant.

.. mcp-setup-amazon-quick-authorize-end


.. _mcp-setup-amazon-quick-verify:

Verify the connection
==================================================

.. mcp-setup-amazon-quick-verify-start

In an Amazon Quick conversation with the Amperity integration enabled, ask:

.. code-block:: none

   "Tell me about my Amperity tenant."

A successful response includes details about your current Amperity tenant.

.. mcp-setup-amazon-quick-verify-end

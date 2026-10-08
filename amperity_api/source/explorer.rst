:layout: landing

.. https://docs.amperity.com/api/


.. meta::
    :description lang=en:
        Browse and try every Amperity API from its OpenAPI specification.

.. meta::
    :content class=swiftype name=body data-type=text:
        Browse and try every Amperity API from its OpenAPI specification.

.. meta::
    :content class=swiftype name=title data-type=string:
        Amperity APIs

==================================================
Amperity APIs
==================================================

.. api-explorer-start

Browse the endpoints for each Amperity API, read their request and response schemas, and send requests from this page. Choose an API from the **API Family** list. To send a request, click **Authorize**, enter an access token, and then use **Try it out** on any endpoint. To get an access token, see :doc:`How to authenticate with Amperity APIs <authentication>`.

.. api-explorer-end

.. raw:: html

   <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui.css">
   <link rel="stylesheet" href="_static/swagger-amperity.css?v=3">
   <div id="swagger-ui" class="amperity-swagger"></div>
   <script src="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-bundle.js"></script>
   <script src="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-standalone-preset.js"></script>
   <script>
     // Replace Swagger's plain spec URL under the title with a download button.
     // CSS places it in the same row as the API name and its version tags.
     function SpecDownloadButton() {
       return {
         wrapComponents: {
           InfoUrl: function (Original, system) {
             return function (props) {
               return system.React.createElement(
                 "a",
                 { className: "amperity-spec-download", href: props.url, download: "" },
                 "Download OpenAPI spec"
               );
             };
           }
         }
       };
     }

     window.addEventListener("load", function () {
       // Only the API family is read from the address. Swagger UI's own
       // queryConfigEnabled would also accept ?url= and ?configUrl=, which would let
       // a link load any spec on this domain, including one whose servers send the
       // token entered under Authorize somewhere else.
       var primaryName = new URLSearchParams(window.location.search).get("urls.primaryName");
       window.ui = SwaggerUIBundle({
         urls: [
           { name: "Tenant API (2024-04-01)", url: "../downloads/openapi/control-plane-2024-04-01-openapi.json" },
           { name: "Tenant API (unstable)", url: "../downloads/openapi/control-plane-unstable-openapi.json" },
           { name: "Database Profile API (2025-07-31)", url: "../downloads/openapi/profile-2025-07-31-openapi.json" },
           { name: "Real-time API (2026-09-03)", url: "../downloads/openapi/real-time-2026-09-03-openapi.json" },
           { name: "Streaming API (v0)", url: "../downloads/openapi/streaming-v0-openapi.json" }
         ],
         dom_id: "#swagger-ui",
         presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
         plugins: [SpecDownloadButton],
         layout: "StandaloneLayout",
         "urls.primaryName": primaryName || undefined,
         deepLinking: true,
         docExpansion: "list",
         defaultModelsExpandDepth: 0,
         displayRequestDuration: true,
         filter: true,
         persistAuthorization: false
       });
     });
   </script>

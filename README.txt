=== Custom Alert Action webhook_plus ===

   Author: my2ndhead

   Version/Date: 1.0 / 20160707

   Description: Custom Alert Action, that sends all results via HTTP(S) POST request to recipient. Supports Basic Authentication.

   Usage: Setup Custom Alert Action through the Setup Page. Enter the HTTP Endpoint URL, User/PW for Basic Authentication

   Limitations: - Password is stored in cleartext
                - Using the alert action without user/password is possible, but not configurable through the UI 

   License: - This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. [1]
            - Commercial Use, Excerpt from CC BY-NC-SA 4.0:
              "A commercial use is one primarily intended for commercial advantage or monetary compensation."
            - In case of Custom Alert Action Webhook Plus this translates to:
              - You may use Custom Alert Action Webhook Plus in commercial environments for handling in-house Splunk alerts
              - You may use Custom Alert Action Webhook Plus as part of your consulting or integration work, 
                if you're considered to be working on behalf of your customer. 
                The customer will be the licensee of Support Add-on for Hypercrypto and must comply according to the license terms
              - You are not allowed to sell Custom Alert Action Webhook Plus as a standalone product or within an application bundle
              - If you want to use Custom Alert Action Webhook Plus outside of these license terms, please contact us and we will find a solution


=== Example Payload:

{
   "owner": "admin",
   "session_key": "e3zGNz5X5a^OWq_X1HvGulywPNpnGnvRBRRDDFmEVoPOnPVKXkDk2h_8^jxaRbnl5YvEpxfZGfGIkVNUWjS0fsKGlN^9O3FZtD3uvLxhDC7eQsSCd_E7e7W8ntP2yPtxjX1TQKWg",
   "sid": "scheduler__admin__search__test_at_1467139140_2714",
   "search_name": "demosearch",
   "server_host": "linux",
   "results_link": "https://linux:8000/app/search/@go?sid=scheduler__admin__search__demosearch_at_1467139140_2714",
   "server_uri": "https://127.0.0.1:8089",
   "results": {
      "field_list": [
         "sourcetype",
         "count"
      ],
      "fields": [
         {
            "count": "10",
            "sourcetype": "splunkd"
         },
         {
            "count": "30",
            "sourcetype": "scheduler"
         }
      ]
   },
   "results_file": "/opt/splunk/var/run/splunk/dispatch/scheduler__admin__search__demosearch_at_1467139140_2714/results.csv.gz",
   "app": "search"
}


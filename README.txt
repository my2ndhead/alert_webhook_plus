=== Custom Alert Action webhook_plus ===

   Author: my2ndhead

   Version/Date: 0.1 / 20160629


Custom Alert Action, that sends all results via HTTP(S) POST request to recipient. Supports Basic Authentication.

=== Example Payload:

{
   "owner": "admin",
   "session_key": "e3zGNz5X5a^OWq_X1HvGulywPNpnGnvRBRRDDFmEVoPOnPVKXkDk2h_8^jxaRbnl5YvEpxfZGfGIkVNUWjS0fsKGlN^9O3FZtD3uvLxhDC7eQsSCd_E7e7W8ntP2yPtxjX1TQKWg",
   "sid": "scheduler__admin__search__test_at_1467139140_2714",
   "search_name": "test",
   "server_host": "linux",
   "results_link": "https://linux:8000/app/search/@go?sid=scheduler__admin__search__test_at_1467139140_2714",
   "server_uri": "https://127.0.0.1:8089",
   "results": {
      "field_list": [
         "sourcetype",
         "count"
      ],
      "fields": [
         {
            "count": "10",
            "sourcetype": "alert_manager_suppression_helper-2"
         },
         {
            "count": "30",
            "sourcetype": "app_permissions_manager"
         }
      ]
   },
   "results_file": "/opt/splunk/var/run/splunk/dispatch/scheduler__admin__search__test_at_1467139140_2714/results.csv.gz",
   "app": "search"
}

